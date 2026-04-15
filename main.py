"""
SMC Trading Bot — BTC/USDT Futures на MEXC
Main loop: скан → анализ → торговля → уведомление
Дневные лимиты: +$250 profit / -$100 loss → стоп
Breakeven: при 70% пути к TP → SL на вход + $5
"""
import asyncio
import traceback
import time
import sdnotify
from config import config
from exchange.mexc import MexcFutures
from exchange.models import Side
from strategy.mtf import analyze_mtf
from strategy.risk import calculate_position_size, validate_rr, max_positions_reached
from notify.telegram import send_tg, tg_poll
from control import is_paused, set_paused, clear_paused, pause_reason
from db.storage import (
    init_db, log_signal, is_duplicate_signal, log_trade_open, log_trade_close,
    get_open_trades, update_trade_entry,
    init_daily_pnl, update_daily_pnl, set_daily_stopped, is_daily_stopped,
    clear_daily_stopped,
    get_today_start_balance, get_today_trade_count, get_last_close_ts,
)

_breakeven_done = set()
_partial_tp_done = set()
# Per-symbol state для analyze_mtf (mitigated OBs и т.д.)
_btc_state: dict = {}
_sol_state: dict = {}
_sol_last_tg_ts: float = 0.0
# Защита от вводов/выводов: запоминаем последний баланс между тиками
_last_tick_balance: float = 0.0
# Резкий скачок > этой суммы между тиками → не торговый PnL, а ввод/вывод
BALANCE_JUMP_THRESHOLD: float = 30.0


async def main():
    init_db()
    notifier = sdnotify.SystemdNotifier()
    mexc = MexcFutures()

    balance = await mexc.get_balance()
    price = await mexc.get_ticker(config.SYMBOL)

    init_daily_pnl(balance)

    daily_pnl_at_start = update_daily_pnl(balance)
    start_bal_today = get_today_start_balance() or balance
    daily_loss_limit = start_bal_today * config.DAILY_LOSS_PCT
    daily_profit_limit = start_bal_today * config.DAILY_PROFIT_PCT
    if daily_pnl_at_start <= -daily_loss_limit or daily_pnl_at_start >= daily_profit_limit:
        if not is_daily_stopped():
            set_daily_stopped()
        warn = (
            "⏸ <b>Bot started — daily limit already reached</b>\n"
            f"Today PnL: <b>${daily_pnl_at_start:+.2f}</b>\n"
            f"Limits: +${daily_profit_limit:.2f} / -${daily_loss_limit:.2f}\n"
            "Trading paused until tomorrow."
        )
        print(warn)
        await send_tg(warn)

    paused_state = "⏸ PAUSED" if is_paused() else "▶️ ACTIVE"
    start_msg = (
        f"🤖 <b>SMC Bot Started</b> — {paused_state}\n"
        f"Balance: <b>${balance:.2f}</b>\n"
        f"BTC Price: <b>${price:,.2f}</b>\n"
        f"Leverage: <b>x{config.LEVERAGE}</b>\n"
        f"Risk: <b>{config.RISK_PCT*100:.1f}%</b> (${balance*config.RISK_PCT:.2f})\n"
        f"R:R min: <b>{config.MIN_RR}</b>\n"
        f"Max positions: <b>{config.MAX_POSITIONS}</b>\n"
        f"Daily limits: <b>+${daily_profit_limit:.2f}</b> / <b>-${daily_loss_limit:.2f}</b>\n"
        f"Max trades/day: <b>{config.MAX_DAILY_TRADES}</b>\n"
        f"Breakeven: at <b>{config.BREAKEVEN_PCT*100:.0f}%</b> to TP\n"
        f"Commands: /start /stop /status /help"
    )
    print(start_msg)
    await send_tg(start_msg)

    for pos_type in [1, 2]:
        await mexc.set_leverage(config.SYMBOL, config.LEVERAGE, pos_type)

    print(f"[*] Scanning every {config.SCAN_INTERVAL}s...")
    notifier.notify("READY=1")

    async def handle_tg_command(text: str):
        cmd = text.strip().lower().split()[0].lstrip("/")
        if cmd in ("start", "resume"):
            if is_paused():
                clear_paused()
                await send_tg("✅ <b>Trading resumed</b>")
                print("[tg] resume", flush=True)
            else:
                await send_tg("ℹ️ Already trading (not paused)")
        elif cmd in ("stop", "pause"):
            if not is_paused():
                set_paused(f"manual /stop at {time.strftime('%H:%M:%S')}")
                await send_tg("⏸ <b>Trading paused</b>. Send /resume to continue")
                print("[tg] pause", flush=True)
            else:
                await send_tg(f"ℹ️ Already paused: {pause_reason()}")
        elif cmd == "status":
            try:
                bal = await mexc.get_balance()
                avail = await mexc.get_available_balance()
                positions_now = await mexc.get_positions(config.SYMBOL)
                pnl_today = update_daily_pnl(bal)
                if is_paused():
                    state = "⏸ paused"
                elif is_daily_stopped():
                    state = "🛑 daily stop"
                else:
                    state = "▶️ trading"
                msg = (
                    f"📊 <b>Status</b>\n"
                    f"State: {state}\n"
                    f"Balance: <b>${bal:.2f}</b> (avail ${avail:.2f})\n"
                    f"Today PnL: <b>${pnl_today:+.2f}</b>\n"
                    f"Open positions: <b>{len(positions_now or [])}</b>\n"
                )
                if is_paused():
                    msg += f"Reason: {pause_reason() or 'n/a'}\n"
                await send_tg(msg)
            except Exception as e:
                await send_tg(f"❌ status err: {e}")
        elif cmd == "help":
            await send_tg(
                "<b>Commands</b>\n"
                "/start, /resume — resume trading\n"
                "/stop, /pause — pause trading\n"
                "/status — current state\n"
                "/help — this message"
            )

    async def trade_loop():
        """Главный цикл бота. Порядок внутри тика (2026-04-14 рефакторинг):
        1. ВСЕГДА: fetch (balance/price/positions), watchdog, sync_closed_trades, protection (partial_tp+breakeven).
           Эти шаги работают независимо от daily_stopped/paused, чтобы открытая позиция всегда
           была под защитой и БД всегда в синхроне с MEXC.
        2. Переоценка лимитов: auto-clear daily_stopped если PnL вернулся под лимит.
        3. Гейты торговли: daily_stopped, paused, trade_cap, daily_pnl limits — выставляют should_scan=False.
        4. scan_and_trade и watch_sol — только если should_scan остался True.
        Никаких ранних `continue` — всё проходит через один общий путь и заканчивается sleep'ом.
        """
        while True:
            try:
                notifier.notify("WATCHDOG=1")

                # === ВСЕГДА RUN: sync + protection =================================
                try:
                    current_balance = await mexc.get_balance()
                    price_now = await mexc.get_ticker(config.SYMBOL)
                    positions = await mexc.get_positions(config.SYMBOL)
                except Exception as e:
                    print(f"[tick] fetch err: {e}", flush=True)
                    await asyncio.sleep(config.SCAN_INTERVAL)
                    continue

                print("[" + time.strftime("%H:%M:%S") + f"] tick balance=${current_balance:.2f}", flush=True)
                init_daily_pnl(current_balance)

                # Защита от ввода/вывода: если баланс резко изменился > BALANCE_JUMP_THRESHOLD
                # за один тик, это движение средств, а не торговый PnL.
                global _last_tick_balance
                if _last_tick_balance > 0:
                    jump = abs(current_balance - _last_tick_balance)
                    if jump > BALANCE_JUMP_THRESHOLD:
                        msg = (
                            f"💰 <b>Balance jump detected: ${jump:.2f}</b>\n"
                            f"Old: ${_last_tick_balance:.2f} → New: ${current_balance:.2f}\n"
                            f"Treating as deposit/withdrawal, resetting daily baseline."
                        )
                        print(msg, flush=True)
                        await send_tg(msg)
                        import sqlite3
                        conn = sqlite3.connect("/root/smc-bot/smc_bot.db")
                        cur = conn.cursor()
                        from db.storage import get_today as _gt
                        cur.execute("DELETE FROM daily_pnl WHERE date=?", (_gt(),))
                        conn.commit()
                        conn.close()
                        init_daily_pnl(current_balance)
                _last_tick_balance = current_balance

                # Синк БД с состоянием MEXC (работает ВСЕГДА, даже в daily stop).
                # Без этого закрытые на бирже сделки остаются в БД как "open" →
                # дашборд показывает призраков, check_partial_tp пытается работать на мертвых.
                close_events = sync_closed_trades(positions, price_now or 0.0)
                for ev in close_events:
                    if ev["reason"] == "manual":
                        set_paused(
                            f"manual close of {ev['side']} @ {ev['entry']} at {time.strftime('%H:%M:%S')}"
                        )
                        await send_tg(
                            f"⛔ <b>Manual close detected</b>\n"
                            f"{ev['side']} entry ${ev['entry']:.1f} closed by hand.\n"
                            f"Trading <b>paused</b>. Send /resume to continue."
                        )
                    elif ev["reason"] == "sl":
                        await send_tg(
                            f"🛑 <b>SL hit</b> {ev['side']} entry ${ev['entry']:.1f}"
                        )
                    elif ev["reason"] == "tp":
                        await send_tg(
                            f"🎯 <b>TP hit</b> {ev['side']} entry ${ev['entry']:.1f}"
                        )

                # Защита открытых позиций (работает ВСЕГДА, даже в daily stop / pause).
                # Это критично: если бот на паузе, а позиция ещё жива — partial TP и breakeven
                # продолжают следить за ней. Без этого бот бы смотрел как winning trade
                # разворачивается в SL без защиты.
                if positions and price_now:
                    await check_partial_tp(mexc, positions, price_now)
                    await check_breakeven(mexc, positions, price_now)

                # === ОЦЕНКА ЛИМИТОВ =================================================
                daily_pnl = update_daily_pnl(current_balance)
                start_bal = get_today_start_balance() or current_balance
                loss_lim = start_bal * config.DAILY_LOSS_PCT
                profit_lim = start_bal * config.DAILY_PROFIT_PCT

                # Auto-clear daily_stopped если PnL снова в пределах лимитов.
                # Триггеры: user поднял DAILY_LOSS_PCT, или закрытая сделка вернула капитал,
                # или unrealised профит снова в границах. Без этого флаг залипает в БД после рестарта.
                if is_daily_stopped() and -loss_lim < daily_pnl < profit_lim:
                    clear_daily_stopped()
                    msg = (
                        f"▶️ <b>Daily stop auto-cleared</b>\n"
                        f"PnL: <b>${daily_pnl:+.2f}</b> back within limits\n"
                        f"Range: +${profit_lim:.2f} / -${loss_lim:.2f}"
                    )
                    print(msg, flush=True)
                    await send_tg(msg)

                # === ГЕЙТЫ ТОРГОВЛИ =================================================
                should_scan = True

                if daily_pnl >= profit_lim:
                    if not is_daily_stopped():
                        set_daily_stopped()
                        msg = (
                            f"🎯 <b>Daily PROFIT limit reached!</b>\n"
                            f"PnL: <b>+${daily_pnl:.2f}</b>\n"
                            f"Limit: +${profit_lim:.2f} ({config.DAILY_PROFIT_PCT*100:.0f}% of ${start_bal:.2f})\n"
                            f"Bot stopped for today. Resumes tomorrow."
                        )
                        print(msg)
                        await send_tg(msg)
                    should_scan = False

                if daily_pnl <= -loss_lim:
                    if not is_daily_stopped():
                        set_daily_stopped()
                        msg = (
                            f"🛑 <b>Daily LOSS limit reached!</b>\n"
                            f"PnL: <b>-${abs(daily_pnl):.2f}</b>\n"
                            f"Limit: -${loss_lim:.2f} ({config.DAILY_LOSS_PCT*100:.0f}% of ${start_bal:.2f})\n"
                            f"Bot stopped for today. Resumes tomorrow."
                        )
                        print(msg)
                        await send_tg(msg)
                    should_scan = False

                # Кап на число сделок в сутки
                trades_today = get_today_trade_count()
                if trades_today >= config.MAX_DAILY_TRADES:
                    if not is_daily_stopped():
                        set_daily_stopped()
                        msg = (
                            f"🚫 <b>Daily trade cap reached</b>\n"
                            f"Trades today: <b>{trades_today}</b> / {config.MAX_DAILY_TRADES}\n"
                            f"Bot stopped for today."
                        )
                        print(msg)
                        await send_tg(msg)
                    should_scan = False

                if is_daily_stopped():
                    should_scan = False

                if is_paused():
                    print(f"  ⏸ paused: {pause_reason()}", flush=True)
                    should_scan = False

                # === НОРМАЛЬНАЯ ТОРГОВЛЯ ============================================
                if should_scan:
                    diag = await scan_and_trade(mexc, daily_pnl) or {}
                    if diag:
                        print("  diag: " + " ".join(f"{k}={v}" for k, v in diag.items()), flush=True)
                    await watch_sol(mexc)

            except Exception as e:
                err = f"[ERROR] {e}\n{traceback.format_exc()}"
                print(err)
                await send_tg(f"⚠️ Error: {e}")

            await asyncio.sleep(config.SCAN_INTERVAL)

    await asyncio.gather(
        trade_loop(),
        tg_poll(handle_tg_command),
    )


def sync_closed_trades(positions: list, current_price: float = 0.0) -> list:
    """Закрывает БД-записи когда на бирже нет позиции этой стороны.
    MEXC объединяет одинаково-направленные ордера в одну позицию со средней
    ценой, поэтому матчить по entry нельзя — только по side."""
    events = []
    open_trades = get_open_trades()
    if not open_trades:
        return events
    sides_with_pos = set()
    for pos in positions or []:
        side = "BUY" if pos.get("positionType") == 1 else "SELL"
        sides_with_pos.add(side)
    for row in open_trades:
        trade_id = row[0]
        side = row[3]
        entry = round(float(row[4]), 1)
        sl = float(row[5])
        tp = float(row[6])
        if side in sides_with_pos:
            continue
        log_trade_close(trade_id, 0.0)

        reason = "manual"
        if current_price and sl and tp:
            risk = abs(entry - sl)
            reward = abs(tp - entry)
            # Направленная проверка с буфером 30% от расстояния:
            # цена должна быть на "своей" стороне TP/SL ИЛИ в пределах буфера.
            if side == "SELL":
                # SHORT: SL > entry > TP
                if current_price <= tp + reward * 0.30:
                    reason = "tp"
                elif current_price >= sl - risk * 0.30:
                    reason = "sl"
            else:
                # LONG: SL < entry < TP
                if current_price >= tp - reward * 0.30:
                    reason = "tp"
                elif current_price <= sl + risk * 0.30:
                    reason = "sl"

        print(
            f"[sync] trade #{trade_id} {side} entry={entry} closed ({reason}) at price={current_price}",
            flush=True,
        )
        events.append({
            "id": trade_id, "side": side, "entry": entry,
            "sl": sl, "tp": tp, "reason": reason,
        })
    return events


async def check_partial_tp(mexc: MexcFutures, positions: list, current_price: float):
    """Partial TP на 1R: закрывает PARTIAL_TP_FRACTION позиции когда цена достигла
    entry ± risk_distance × PARTIAL_TP_R, и двигает SL на остатке в breakeven.
    Главная защитная механика бота: превращает 'почти-winner' SMC-ретесты из полных SL
    в +0.5R прибыли + безрисковую остальную часть.
    """
    if not config.PARTIAL_TP_ENABLED or not positions:
        return

    try:
        stop_orders = await mexc.get_stop_orders(config.SYMBOL)
    except Exception as e:
        print(f"[partial_tp] failed to fetch stop orders: {e}", flush=True)
        return

    so_by_pos = {}
    for so in stop_orders:
        pid = so.get("positionId")
        try:
            so_by_pos[int(pid)] = so
        except (TypeError, ValueError):
            continue

    for pos in positions:
        try:
            pos_id = int(pos.get("positionId", 0))
        except (TypeError, ValueError):
            continue
        if str(pos_id) in _partial_tp_done:
            continue

        so = so_by_pos.get(pos_id)
        if not so:
            continue

        entry = float(pos.get("openAvgPrice") or pos.get("holdAvgPrice") or 0)
        hold_vol = int(pos.get("holdVol") or 0)
        sl = float(so.get("stopLossPrice") or 0)
        pos_type = pos.get("positionType", 1)

        if not entry or not sl or hold_vol <= 0:
            continue

        if pos_type == 1:
            risk_dist = entry - sl
            trigger_price = entry + risk_dist * config.PARTIAL_TP_R
            reached = current_price >= trigger_price
        else:
            risk_dist = sl - entry
            trigger_price = entry - risk_dist * config.PARTIAL_TP_R
            reached = current_price <= trigger_price

        if risk_dist <= 0 or not reached:
            continue

        close_vol = int(hold_vol * config.PARTIAL_TP_FRACTION)
        remaining_vol = hold_vol - close_vol
        if close_vol < 1 or remaining_vol < 1:
            continue

        if pos_type == 1:
            be_sl = round(entry + config.BREAKEVEN_OFFSET, 1)
        else:
            be_sl = round(entry - config.BREAKEVEN_OFFSET, 1)

        stop_plan_order_id = so.get("id")
        if not stop_plan_order_id:
            continue

        # Step 1: двигаем SL в BE пока позиция ещё полная (zero no-SL window)
        try:
            sl_result = await mexc.change_stop_loss(int(stop_plan_order_id), be_sl)
        except Exception as e:
            print(f"[partial_tp] SL move exc pos={pos_id}: {e}", flush=True)
            await send_tg(f"⚠️ Partial TP SL move failed pos {pos_id}: {e}")
            continue

        sl_ok = bool(sl_result.get("success")) or sl_result.get("code") == 0
        if not sl_ok:
            print(f"[partial_tp] SL move rejected: {sl_result}", flush=True)
            await send_tg(f"⚠️ Partial TP SL move rejected pos {pos_id}: {sl_result}")
            continue

        # Step 2: partial close остатка через market
        try:
            close_result = await mexc.partial_close(config.SYMBOL, pos_type, close_vol)
        except Exception as e:
            print(f"[partial_tp] partial_close exc: {e}", flush=True)
            await send_tg(f"⚠️ Partial close failed pos {pos_id}: {e}")
            continue

        close_ok = bool(close_result.get("success")) or close_result.get("code") == 0
        if not close_ok:
            print(f"[partial_tp] partial_close rejected: {close_result}", flush=True)
            await send_tg(f"⚠️ Partial close rejected pos {pos_id}: {close_result}")
            continue

        _partial_tp_done.add(str(pos_id))
        _breakeven_done.add(str(pos_id))

        direction = "LONG" if pos_type == 1 else "SHORT"
        locked_profit = risk_dist * close_vol * 0.0001 * config.PARTIAL_TP_R
        msg = (
            f"💰 <b>Partial TP {direction}</b>\n"
            f"Entry: <b>${entry:,.1f}</b>\n"
            f"Trigger: <b>${trigger_price:,.1f}</b> ({config.PARTIAL_TP_R:.1f}R)\n"
            f"Closed: <b>{close_vol}</b> / {hold_vol} contracts\n"
            f"Remaining: <b>{remaining_vol}</b>\n"
            f"Locked: <b>+${locked_profit:.2f}</b>\n"
            f"New SL: <b>${be_sl:,.1f}</b> (breakeven)\n"
            f"Price: <b>${current_price:,.1f}</b>"
        )
        print(msg)
        await send_tg(msg)


async def check_breakeven(mexc: MexcFutures, positions: list, current_price: float):
    """Переносит SL на breakeven+offset при BREAKEVEN_PCT пути к TP.
    Fix 2026-04-14: читает SL/TP из stoporder/list/orders (в position data их нет),
    матчит по positionId, вызывает change_stop_loss (атомарный update plan price).
    """
    if not positions:
        return

    try:
        stop_orders = await mexc.get_stop_orders(config.SYMBOL)
    except Exception as e:
        print(f"[breakeven] failed to fetch stop orders: {e}", flush=True)
        return

    so_by_pos = {}
    for so in stop_orders:
        pid = so.get("positionId")
        try:
            so_by_pos[int(pid)] = so
        except (TypeError, ValueError):
            continue

    for pos in positions:
        try:
            pos_id_int = int(pos.get("positionId", 0))
        except (TypeError, ValueError):
            continue
        pos_id = str(pos_id_int)
        if pos_id in _breakeven_done:
            continue

        so = so_by_pos.get(pos_id_int)
        if not so:
            continue

        entry = float(pos.get("openAvgPrice") or pos.get("holdAvgPrice") or 0)
        tp = float(so.get("takeProfitPrice") or 0)
        sl = float(so.get("stopLossPrice") or 0)
        pos_type = pos.get("positionType", 1)

        if not entry or not tp:
            continue

        if pos_type == 1 and sl >= entry:
            _breakeven_done.add(pos_id)
            continue
        if pos_type == 2 and 0 < sl <= entry:
            _breakeven_done.add(pos_id)
            continue

        if pos_type == 1:
            total_distance = tp - entry
            current_progress = current_price - entry
        else:
            total_distance = entry - tp
            current_progress = entry - current_price

        if total_distance <= 0:
            continue

        progress_pct = current_progress / total_distance

        if progress_pct >= config.BREAKEVEN_PCT:
            if pos_type == 1:
                new_sl = round(entry + config.BREAKEVEN_OFFSET, 1)
            else:
                new_sl = round(entry - config.BREAKEVEN_OFFSET, 1)

            stop_plan_order_id = so.get("id")
            if not stop_plan_order_id:
                print(f"[breakeven] pos {pos_id} has stop order without id, skip", flush=True)
                continue

            try:
                result = await mexc.change_stop_loss(int(stop_plan_order_id), new_sl)
            except Exception as e:
                print(f"[breakeven] change_stop_loss exc pos={pos_id}: {e}", flush=True)
                await send_tg(f"⚠️ Breakeven API error pos {pos_id}: {e}")
                continue

            ok = bool(result.get("success")) or result.get("code") == 0
            if ok:
                _breakeven_done.add(pos_id)
                direction = "LONG" if pos_type == 1 else "SHORT"
                msg = (
                    f"🔄 <b>Breakeven {direction}</b>\n"
                    f"Entry: <b>${entry:,.1f}</b>\n"
                    f"New SL: <b>${new_sl:,.1f}</b>\n"
                    f"TP: <b>${tp:,.1f}</b>\n"
                    f"Progress: <b>{progress_pct*100:.0f}%</b> to TP\n"
                    f"Price: <b>${current_price:,.1f}</b>"
                )
                print(msg)
                await send_tg(msg)
            else:
                err_msg = f"⚠️ Breakeven rejected pos={pos_id}: {result}"
                print(err_msg, flush=True)
                await send_tg(err_msg)


async def watch_sol(mexc: MexcFutures) -> None:
    """Shadow watcher: считает что бы открылось по SOL_USDT, но НЕ торгует.
    Логирует в /root/smc-bot/sol_shadow.log, шлёт TG не чаще 1 раза в час."""
    global _sol_last_tg_ts
    if not config.WATCH_ENABLED:
        return
    try:
        sym = config.WATCH_SYMBOL
        c4h, c1h, c15, c5, price = await asyncio.gather(
            mexc.get_candles(sym, config.TF_HTF),
            mexc.get_candles(sym, config.TF_TREND),
            mexc.get_candles(sym, config.TF_ZONES),
            mexc.get_candles(sym, config.TF_ENTRY),
            mexc.get_ticker(sym),
        )
        if not all([c4h, c1h, c15, c5, price]):
            return
        signals, diag = analyze_mtf(c4h, c1h, c15, c5, price, state=_sol_state)
        ts = time.strftime("%Y-%m-%d %H:%M:%S")
        with open("/root/smc-bot/sol_shadow.log", "a") as f:
            f.write(f"[{ts}] {sym} price={price} diag={diag}\n")
            for s in signals:
                f.write(
                    f"  WOULD: {s.side.value} entry={s.entry:.3f} "
                    f"sl={s.sl:.3f} tp={s.tp:.3f} reason={s.reason}\n"
                )
        if signals and (time.time() - _sol_last_tg_ts > 3600):
            _sol_last_tg_ts = time.time()
            s = signals[0]
            await send_tg(
                f"👁 <b>SOL shadow signal</b>\n"
                f"Side: <b>{s.side.value}</b>\n"
                f"Entry: <b>${s.entry:.2f}</b>\n"
                f"SL: ${s.sl:.2f}\n"
                f"TP: ${s.tp:.2f}\n"
                f"<i>(только наблюдение, реальной сделки нет)</i>"
            )
    except Exception as e:
        print(f"[sol watch err] {e}", flush=True)


async def scan_and_trade(mexc: MexcFutures, daily_pnl: float) -> dict:
    candles_4h, candles_1h, candles_15m, candles_5m, price, positions = await asyncio.gather(
        mexc.get_candles(config.SYMBOL, config.TF_HTF),
        mexc.get_candles(config.SYMBOL, config.TF_TREND),
        mexc.get_candles(config.SYMBOL, config.TF_ZONES),
        mexc.get_candles(config.SYMBOL, config.TF_ENTRY),
        mexc.get_ticker(config.SYMBOL),
        mexc.get_positions(config.SYMBOL),
    )

    if not candles_4h or not candles_1h or not candles_15m or not candles_5m or not price:
        print("[!] No data, skipping...")
        return {"err": "no_data"}

    # Post-close cooldown 30 мин после ЛЮБОГО закрытия
    last_close = get_last_close_ts()
    if last_close:
        elapsed = time.time() - last_close
        if elapsed < config.POST_CLOSE_COOLDOWN:
            wait = int(config.POST_CLOSE_COOLDOWN - elapsed)
            return {"skip": "post_close_cooldown", "wait_s": wait}

    open_db = get_open_trades()
    if len(open_db) >= config.MAX_POSITIONS:
        return {"skip": "max_pos", "open": len(open_db)}

    signals, diag = analyze_mtf(candles_4h, candles_1h, candles_15m, candles_5m, price, state=_btc_state)

    if not signals:
        return diag

    open_sides = {t[3] for t in open_db}
    signals.sort(key=lambda s: s.score, reverse=True)
    # MEXC объединяет одинаково-направленные ордера, поэтому пропускаем сигнал
    # если у нас уже есть открытая сделка в этом направлении
    signal = next((s for s in signals if s.side.value not in open_sides), None)
    if signal is None:
        return {**diag, "skip": "side_busy", "open_sides": list(open_sides)}

    if not validate_rr(signal):
        print(f"[!] R:R too low, skipping: {signal.reason}")
        return diag

    if is_duplicate_signal(signal.side.value, signal.reason, config.SIGNAL_COOLDOWN):
        return diag

    balance = await mexc.get_available_balance()
    vol = calculate_position_size(balance, signal, price)

    if vol <= 0:
        return diag

    log_signal(signal.side.value, signal.entry, signal.sl, signal.tp, signal.reason)

    result = await mexc.place_order(
        symbol=config.SYMBOL,
        side=signal.side,
        vol=vol,
        sl=round(signal.sl, 1),
        tp=round(signal.tp, 1),
    )

    success = result.get("success", False)
    order_id = str(result.get("data", ""))

    if success:
        trade_id = log_trade_open(signal.side.value, signal.entry, signal.sl, signal.tp, vol, order_id, signal.reason)

        # Подтянуть реальную цену исполнения с биржи (slippage против signal.entry)
        try:
            await asyncio.sleep(0.5)  # короткая пауза чтобы позиция успела появиться
            fresh_positions = await mexc.get_positions(config.SYMBOL)
            target_pos_type = 1 if signal.side == Side.BUY else 2
            for pos in fresh_positions or []:
                if pos.get("positionType") == target_pos_type:
                    real_entry = float(pos.get("openAvgPrice", 0))
                    if real_entry > 0:
                        update_trade_entry(trade_id, real_entry)
                        signal.entry = real_entry
                    break
        except Exception as e:
            print(f"[entry update err] {e}", flush=True)

        risk_usd = balance * config.RISK_PCT
        msg = (
            f"✅ <b>{'LONG' if signal.side == Side.BUY else 'SHORT'} Opened</b>\n"
            f"Entry: <b>${signal.entry:,.1f}</b>\n"
            f"SL: <b>${signal.sl:,.1f}</b>\n"
            f"TP: <b>${signal.tp:,.1f}</b>\n"
            f"Vol: <b>{vol}</b> contracts\n"
            f"Risk: <b>${risk_usd:.2f}</b>\n"
            f"Daily PnL: <b>${daily_pnl:+.2f}</b>\n"
            f"Reason: {signal.reason}"
        )
        print(msg)
        await send_tg(msg)
    else:
        err_msg = f"❌ Order failed: {result}"
        print(err_msg)
        await send_tg(err_msg)

    return diag


if __name__ == "__main__":
    asyncio.run(main())
