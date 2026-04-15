"""
SMC (Smart Money Concepts) анализ
- Swing Points (HH, HL, LH, LL)
- Order Blocks (OB)
- Fair Value Gaps (FVG)
- Break of Structure (BOS) / Change of Character (CHoCH)
"""
from exchange.models import Candle, OrderBlock, FVG, Side


def find_swings(candles: list[Candle], left: int = 3, right: int = 3) -> tuple[list, list]:
    """Находит свинг-хай и свинг-лоу"""
    highs, lows = [], []
    for i in range(left, len(candles) - right):
        is_high = all(candles[i].high >= candles[i - j].high for j in range(1, left + 1)) and \
                  all(candles[i].high >= candles[i + j].high for j in range(1, right + 1))
        is_low = all(candles[i].low <= candles[i - j].low for j in range(1, left + 1)) and \
                 all(candles[i].low <= candles[i + j].low for j in range(1, right + 1))
        if is_high:
            highs.append((i, candles[i].high, candles[i].ts))
        if is_low:
            lows.append((i, candles[i].low, candles[i].ts))
    return highs, lows


def detect_trend(highs: list, lows: list) -> str:
    """Определяет тренд по последним 3 свингам (2 сравнения с каждой стороны).
    Голосование: из 4 сравнений (2 high + 2 low) минимум 3 в одну сторону +
    хотя бы один из лоу/хай должен подтверждать структуру (LL для bearish, HL для bullish).
    """
    if len(highs) < 3 or len(lows) < 3:
        # Fallback на старую 2-свинговую логику
        if len(highs) < 2 or len(lows) < 2:
            return "ranging"
        hh = highs[-1][1] > highs[-2][1]
        hl = lows[-1][1] > lows[-2][1]
        lh = highs[-1][1] < highs[-2][1]
        ll = lows[-1][1] < lows[-2][1]
        if hh and hl:
            return "bullish"
        if lh and ll:
            return "bearish"
        return "ranging"

    def _cmp(seq):
        rising = sum(1 for i in (-1, -2) if seq[i][1] > seq[i - 1][1])
        falling = sum(1 for i in (-1, -2) if seq[i][1] < seq[i - 1][1])
        return rising, falling

    hh_c, lh_c = _cmp(highs)
    hl_c, ll_c = _cmp(lows)

    bull_score = hh_c + hl_c
    bear_score = lh_c + ll_c

    if bear_score >= 3 and ll_c >= 1:
        return "bearish"
    if bull_score >= 3 and hl_c >= 1:
        return "bullish"
    return "ranging"


def _ema(values: list[float], period: int) -> list[float]:
    if not values:
        return []
    k = 2.0 / (period + 1)
    result = [values[0]]
    for v in values[1:]:
        result.append(v * k + result[-1] * (1 - k))
    return result


def detect_trend_ema(candles: list[Candle]) -> str:
    """EMA-based тренд: EMA20 vs EMA50, позиция цены, наклон EMA20."""
    if len(candles) < 50:
        return "ranging"
    closes = [c.close for c in candles]
    ema20 = _ema(closes, 20)
    ema50 = _ema(closes, 50)

    e20 = ema20[-1]
    e50 = ema50[-1]
    e20_back = ema20[-5]  # наклон за 5 баров
    price = closes[-1]

    bull = e20 > e50 and price > e20 and e20 > e20_back
    bear = e20 < e50 and price < e20 and e20 < e20_back

    if bull:
        return "bullish"
    if bear:
        return "bearish"
    return "ranging"


def compute_atr(candles: list[Candle], period: int = 14) -> float:
    """Average True Range — мера волатильности по последним N свечам."""
    if len(candles) < period + 1:
        return 0.0
    trs = []
    for i in range(1, len(candles)):
        c = candles[i]
        prev = candles[i - 1]
        tr = max(
            c.high - c.low,
            abs(c.high - prev.close),
            abs(c.low - prev.close),
        )
        trs.append(tr)
    return sum(trs[-period:]) / period


def detect_trend_combined(candles: list[Candle], highs: list, lows: list) -> str:
    """Объединяет swing-голосование и EMA-фильтр.
    Оба метода должны дать одинаковый направленный тренд, иначе ranging.
    Это снижает ложные сигналы на флэте и при противоречивых импульсах.
    """
    swing = detect_trend(highs, lows)
    ema = detect_trend_ema(candles)
    if swing == ema and swing in ("bullish", "bearish"):
        return swing
    return "ranging"


def find_order_blocks(candles: list[Candle], tf: str, lookback: int = 50) -> list[OrderBlock]:
    """
    Order Block — последняя противоположная свеча перед импульсом.
    Bullish OB: последняя медвежья свеча перед бычьим импульсом
    Bearish OB: последняя бычья свеча перед медвежьим импульсом
    """
    obs = []
    start = max(0, len(candles) - lookback)
    for i in range(start + 2, len(candles)):
        c0, c1, c2 = candles[i - 2], candles[i - 1], candles[i]
        body0 = c0.close - c0.open
        body2 = c2.close - c2.open
        # Bullish OB: медвежья свеча → рост с перекрытием
        if body0 < 0 and body2 > 0 and c2.close > c0.high:
            obs.append(OrderBlock(side=Side.BUY, high=c0.high, low=c0.low, tf=tf, ts=c0.ts))
        # Bearish OB: бычья свеча → падение с перекрытием
        if body0 > 0 and body2 < 0 and c2.close < c0.low:
            obs.append(OrderBlock(side=Side.SELL, high=c0.high, low=c0.low, tf=tf, ts=c0.ts))
    return obs


def find_fvg(candles: list[Candle], tf: str, lookback: int = 50) -> list[FVG]:
    """
    Fair Value Gap — разрыв между свечами 1 и 3 (свеча 2 — импульс).
    Bullish FVG: candle[0].high < candle[2].low
    Bearish FVG: candle[0].low > candle[2].high
    """
    fvgs = []
    start = max(0, len(candles) - lookback)
    for i in range(start + 2, len(candles)):
        c0, c1, c2 = candles[i - 2], candles[i - 1], candles[i]
        # Bullish FVG
        if c0.high < c2.low:
            fvgs.append(FVG(side=Side.BUY, high=c2.low, low=c0.high, tf=tf, ts=c1.ts))
        # Bearish FVG
        if c0.low > c2.high:
            fvgs.append(FVG(side=Side.SELL, high=c0.low, low=c2.high, tf=tf, ts=c1.ts))
    return fvgs


def detect_bos(highs: list, lows: list) -> list[dict]:
    """
    Break of Structure — пробой предыдущего свинг-хай/лоу.
    Возвращает список событий: {'type': 'BOS'|'CHoCH', 'side': 'bullish'|'bearish', ...}
    """
    events = []
    for i in range(1, len(highs)):
        if highs[i][1] > highs[i - 1][1]:
            events.append({"type": "BOS", "side": "bullish", "level": highs[i - 1][1], "ts": highs[i][2]})
    for i in range(1, len(lows)):
        if lows[i][1] < lows[i - 1][1]:
            events.append({"type": "BOS", "side": "bearish", "level": lows[i - 1][1], "ts": lows[i][2]})
    return events
