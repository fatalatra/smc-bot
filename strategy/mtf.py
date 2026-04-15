"""
Multi-Timeframe Logic с фильтрами качества:
- 4H + 1H тренды должны совпасть (HTF фильтр)
- Относительный ATR-фильтр (текущая волатильность не сильно ниже средней)
- Сессия Лондон/NY (07-21 UTC)
- Confluence: только OB+FVG перекрытия
- SL = OB-граница ± ATR × mult (адаптивный буфер)
- OB mitigation: каждый OB торгуется один раз (state dict)
"""
import datetime
import time
from exchange.models import Candle, Signal, Side, OrderBlock, FVG
from strategy.smc import (
    find_swings, detect_trend_combined, find_order_blocks, find_fvg,
    detect_bos, compute_atr, compute_adx,
)
from config import config


def _in_session() -> bool:
    h = datetime.datetime.now(datetime.timezone.utc).hour
    return config.SESSION_START_UTC <= h < config.SESSION_END_UTC


def _zones_overlap(a_low: float, a_high: float, b_low: float, b_high: float) -> bool:
    return a_low <= b_high and b_low <= a_high


def _ob_key(ob: OrderBlock) -> tuple:
    """Стабильный идентификатор OB между перерасчётами."""
    return (ob.tf, ob.ts, ob.side.value)


def _find_liquidity_trap_long(sl_price: float, price: float, h1_lows: list,
                               threshold_pct: float, lookback: int) -> float | None:
    """Для LONG: ищет недавний 1h swing low который сидит чуть НИЖЕ планируемого SL.
    Если такой есть — цена придёт его снять, и по дороге снимет наш SL. Возвращает price
    найденной ловушки (или None если чисто).

    Trap condition: swing_low < sl AND (sl - swing_low) < price * threshold_pct.
    """
    if not h1_lows:
        return None
    threshold_abs = price * threshold_pct
    recent_lows = h1_lows[-lookback:]
    for tup in recent_lows:
        low_price = tup[1]  # find_swings returns (idx, price, ts)
        if low_price >= sl_price:
            continue
        gap = sl_price - low_price
        if gap < threshold_abs:
            return low_price
    return None


def _find_liquidity_trap_short(sl_price: float, price: float, h1_highs: list,
                                threshold_pct: float, lookback: int) -> float | None:
    """Для SHORT: зеркально — ищет недавний 1h swing high чуть ВЫШЕ планируемого SL."""
    if not h1_highs:
        return None
    threshold_abs = price * threshold_pct
    recent_highs = h1_highs[-lookback:]
    for tup in recent_highs:
        high_price = tup[1]
        if high_price <= sl_price:
            continue
        gap = high_price - sl_price
        if gap < threshold_abs:
            return high_price
    return None


def analyze_mtf(candles_4h: list[Candle],
                candles_1h: list[Candle],
                candles_15m: list[Candle],
                candles_5m: list[Candle],
                current_price: float,
                state: dict | None = None) -> tuple[list[Signal], dict]:
    """MTF анализ с фильтрами и OB mitigation tracking.
    state: dict с ключом 'mitigated_obs' (set) — переживает между вызовами.
    """
    if state is None:
        state = {}
    mitigated = state.setdefault("mitigated_obs", set())

    # 1) Сессионный фильтр
    if not _in_session():
        return [], {"skip": "off_session", "hour_utc": datetime.datetime.now(datetime.timezone.utc).hour}

    # 2) HTF (4H) + 1H тренды должны совпадать
    h4_highs, h4_lows = find_swings(candles_4h)
    trend_4h = detect_trend_combined(candles_4h, h4_highs, h4_lows)

    h1_highs, h1_lows = find_swings(candles_1h)
    trend_1h = detect_trend_combined(candles_1h, h1_highs, h1_lows)

    # Смягчённый фильтр v2: блокируем только (а) оба ranging — нет направления,
    # или (б) явный конфликт bull vs bear. Если направление есть хотя бы у одного —
    # торгуем, приоритет у HTF.
    if trend_4h == "ranging" and trend_1h == "ranging":
        return [], {"trend_htf": trend_4h, "trend_mid": trend_1h, "skip": "trend_mismatch"}
    if trend_4h != "ranging" and trend_1h != "ranging" and trend_4h != trend_1h:
        return [], {"trend_htf": trend_4h, "trend_mid": trend_1h, "skip": "trend_mismatch"}

    trend = trend_4h if trend_4h != "ranging" else trend_1h

    # 2b) Trend stability: не входить пока тренд не простоял TREND_MIN_STABLE сек
    prev_trend = state.get('_trend_dir')
    now_ts = time.time()
    if trend != prev_trend:
        state['_trend_dir'] = trend
        state['_trend_since'] = now_ts
    trend_age = now_ts - state.get('_trend_since', 0)
    if trend_age < config.TREND_MIN_STABLE:
        return [], {
            'trend': trend, 'skip': 'trend_immature',
            'trend_age_s': int(trend_age),
            'need_s': config.TREND_MIN_STABLE,
        }

    # 3) Относительный ATR фильтр (15M)
    atr_short = compute_atr(candles_15m, config.ATR_PERIOD)
    atr_long = compute_atr(candles_15m, config.ATR_LONG_PERIOD)
    atr_ratio = atr_short / atr_long if atr_long else 0.0
    if atr_ratio < config.ATR_RATIO_MIN:
        return [], {
            "trend": trend, "skip": "atr_low",
            "ratio": round(atr_ratio, 2), "min": config.ATR_RATIO_MIN,
        }

    # 4) Зоны 15M
    obs_15m = find_order_blocks(candles_15m, "Min15")
    fvgs_15m = find_fvg(candles_15m, "Min15")

    # Отсечь уже использованные OB
    obs_fresh = [ob for ob in obs_15m if _ob_key(ob) not in mitigated]

    # 5) BOS подтверждение на 5M
    m5_highs, m5_lows = find_swings(candles_5m, left=2, right=2)
    bos_events = detect_bos(m5_highs, m5_lows)

    # 6) Confluence + ATR-based SL + liquidity-aware filter
    if trend == "bullish":
        signals, sub = _check_long_signals(obs_fresh, fvgs_15m, bos_events, current_price, atr_short, mitigated, h1_lows)
    else:
        signals, sub = _check_short_signals(obs_fresh, fvgs_15m, bos_events, current_price, atr_short, mitigated, h1_highs)

    diag = {
        "trend": trend,
        "atr_ratio": round(atr_ratio, 2),
        "obs": len(obs_15m),
        "obs_fresh": len(obs_fresh),
        "fvgs": len(fvgs_15m),
        "bos": len(bos_events),
        "sigs": len(signals),
        **sub,
    }
    return signals, diag


def _check_long_signals(obs: list[OrderBlock], fvgs: list[FVG],
                        bos: list[dict], price: float, atr: float,
                        mitigated: set, h1_lows: list) -> tuple[list[Signal], dict]:
    signals = []
    counts = {"wrong_side": 0, "price_out": 0, "bos_miss": 0, "risk_neg": 0, "liquidity_trap": 0}
    bull_fvgs = [f for f in fvgs if f.side == Side.BUY and not f.filled]
    bullish_obs = [ob for ob in obs if ob.side == Side.BUY and not ob.mitigated]
    if bullish_obs:
        nearest = min(bullish_obs, key=lambda o: abs(price - (o.low + o.high) / 2))
        counts["near_gap_pct"] = round((price - nearest.high) / price * 100, 3)

    for ob in obs:
        if ob.side != Side.BUY or ob.mitigated:
            counts["wrong_side"] += 1
            continue
        if not (ob.low <= price <= ob.high * 1.007):
            counts["price_out"] += 1
            continue
        if not any(e["side"] == "bullish" for e in bos[-15:]):
            counts["bos_miss"] += 1
            continue
        confluent = any(_zones_overlap(ob.low, ob.high, f.low, f.high) for f in bull_fvgs)

        sl = ob.low - atr * config.SL_ATR_MULT
        risk = price - sl
        if risk <= 0:
            counts["risk_neg"] += 1
            continue
        # Liquidity-aware SL: skip if our SL sits just above a recent 1h swing low
        # (stop-hunt trap). Threshold 0.3% of price by default.
        if config.LIQUIDITY_CHECK_ENABLED:
            trap = _find_liquidity_trap_long(
                sl, price, h1_lows,
                config.LIQUIDITY_THRESHOLD_PCT,
                config.LIQUIDITY_SWINGS_LOOKBACK,
            )
            if trap is not None:
                counts["liquidity_trap"] += 1
                continue
        tp = price + risk * config.MIN_RR
        signals.append(Signal(
            side=Side.BUY, entry=price, sl=sl, tp=tp,
            ob=ob,
            score=0.9 if confluent else 0.7,
            reason="Long: OB+FVG confluence + BOS" if confluent else "Long: Pure OB + BOS",
        ))
        mitigated.add(_ob_key(ob))
        break  # один сигнал за тик

    return signals, counts


def _check_short_signals(obs: list[OrderBlock], fvgs: list[FVG],
                         bos: list[dict], price: float, atr: float,
                         mitigated: set, h1_highs: list) -> tuple[list[Signal], dict]:
    signals = []
    counts = {"wrong_side": 0, "price_out": 0, "bos_miss": 0, "risk_neg": 0, "liquidity_trap": 0}
    bear_fvgs = [f for f in fvgs if f.side == Side.SELL and not f.filled]
    bearish_obs = [ob for ob in obs if ob.side == Side.SELL and not ob.mitigated]
    if bearish_obs:
        nearest = min(bearish_obs, key=lambda o: abs(price - (o.low + o.high) / 2))
        counts["near_gap_pct"] = round((nearest.low - price) / price * 100, 3)

    for ob in obs:
        if ob.side != Side.SELL or ob.mitigated:
            counts["wrong_side"] += 1
            continue
        if not (ob.low * 0.993 <= price <= ob.high):
            counts["price_out"] += 1
            continue
        if not any(e["side"] == "bearish" for e in bos[-15:]):
            counts["bos_miss"] += 1
            continue
        confluent = any(_zones_overlap(ob.low, ob.high, f.low, f.high) for f in bear_fvgs)

        sl = ob.high + atr * config.SL_ATR_MULT
        risk = sl - price
        if risk <= 0:
            counts["risk_neg"] += 1
            continue
        # Liquidity-aware SL: skip if our SL sits just below a recent 1h swing high
        if config.LIQUIDITY_CHECK_ENABLED:
            trap = _find_liquidity_trap_short(
                sl, price, h1_highs,
                config.LIQUIDITY_THRESHOLD_PCT,
                config.LIQUIDITY_SWINGS_LOOKBACK,
            )
            if trap is not None:
                counts["liquidity_trap"] += 1
                continue
        tp = price - risk * config.MIN_RR
        signals.append(Signal(
            side=Side.SELL, entry=price, sl=sl, tp=tp,
            ob=ob,
            score=0.9 if confluent else 0.7,
            reason="Short: OB+FVG confluence + BOS" if confluent else "Short: Pure OB + BOS",
        ))
        mitigated.add(_ob_key(ob))
        break

    return signals, counts
