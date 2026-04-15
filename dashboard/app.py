import os
import re
import sys
import sqlite3
import asyncio
from pathlib import Path
from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, JSONResponse

sys.path.insert(0, "/root/smc-bot")

from exchange.mexc import MexcFutures
from config import config
import control

DB_PATH = "/root/smc-bot/smc_bot.db"
BOT_LOG = "/root/smc-bot/bot.log"
STATIC_DIR = Path("/root/smc-bot/dashboard/static")


def _tail_bytes(path: str, n: int = 16384) -> str:
    try:
        with open(path, "rb") as f:
            f.seek(0, 2)
            size = f.tell()
            f.seek(max(0, size - n))
            return f.read().decode("utf-8", errors="ignore")
    except Exception:
        return ""


def _parse_latest_diag() -> dict | None:
    tail = _tail_bytes(BOT_LOG, 16384)
    lines = [ln.strip() for ln in tail.splitlines() if "diag:" in ln]
    if not lines:
        return None
    last = lines[-1]
    body = last.split("diag:", 1)[1].strip()
    out: dict[str, str | float | int] = {}
    for m in re.finditer(r"(\w+)=([^\s]+)", body):
        k, v = m.group(1), m.group(2)
        try:
            out[k] = float(v) if "." in v else int(v)
        except ValueError:
            out[k] = v
    return out or None

app = FastAPI(title="SMC Bot Dashboard")
mexc = MexcFutures()


def _db():
    c = sqlite3.connect(DB_PATH)
    c.row_factory = sqlite3.Row
    return c


@app.get("/api/candles")
async def api_candles(interval: str = "Min5", count: int = 300):
    allowed = {"Min1", "Min5", "Min15", "Min30", "Min60", "Hour4", "Day1"}
    if interval not in allowed:
        raise HTTPException(400, f"interval must be one of {allowed}")
    count = max(50, min(count, 1000))
    candles = await mexc.get_candles(config.SYMBOL, interval, count)
    return [
        {"time": int(c.ts), "open": c.open, "high": c.high,
         "low": c.low, "close": c.close, "volume": c.volume}
        for c in candles
    ]


@app.get("/api/position")
async def api_position():
    conn = _db()
    rows = conn.execute(
        "SELECT id, open_ts, side, entry, sl, tp, vol, status "
        "FROM trades WHERE status='open' ORDER BY open_ts DESC"
    ).fetchall()
    conn.close()
    try:
        price = await mexc.get_ticker(config.SYMBOL)
    except Exception:
        price = None

    # Fetch live SL/TP from MEXC stop-orders (overrides stale DB values)
    live_sl = None
    live_tp = None
    try:
        stop_orders = await mexc.get_stop_orders(config.SYMBOL)
        for so in stop_orders:
            sl_val = so.get("stopLossPrice")
            tp_val = so.get("takeProfitPrice")
            if sl_val and float(sl_val) > 0:
                live_sl = float(sl_val)
            if tp_val and float(tp_val) > 0:
                live_tp = float(tp_val)
    except Exception:
        pass  # fall back to DB values

    positions = []
    for r in rows:
        entry = r["entry"]
        sl = live_sl if live_sl is not None else r["sl"]
        tp = live_tp if live_tp is not None else r["tp"]
        side = r["side"]
        pnl_pct = None
        if price and entry:
            if side in ("BUY", "long", "LONG"):
                pnl_pct = (price - entry) / entry * 100 * config.LEVERAGE
            else:
                pnl_pct = (entry - price) / entry * 100 * config.LEVERAGE
        positions.append({
            "id": r["id"], "open_ts": r["open_ts"], "side": side,
            "entry": entry, "sl": sl, "tp": tp, "vol": r["vol"],
            "pnl_pct": round(pnl_pct, 2) if pnl_pct is not None else None,
        })
    return {"price": price, "positions": positions}


@app.get("/api/trades")
async def api_trades(limit: int = 20):
    limit = max(1, min(limit, 200))
    conn = _db()
    rows = conn.execute(
        "SELECT id, open_ts, close_ts, side, entry, sl, tp, vol, pnl, status, reason "
        "FROM trades ORDER BY open_ts DESC LIMIT ?", (limit,)
    ).fetchall()
    conn.close()
    return [dict(r) for r in rows]


@app.get("/api/status")
async def api_status():
    conn = _db()
    row = conn.execute(
        "SELECT date, start_balance, pnl, stopped FROM daily_pnl "
        "ORDER BY date DESC LIMIT 1"
    ).fetchone()
    conn.close()
    try:
        balance = await mexc.get_balance()
    except Exception:
        balance = None
    paused = control.is_paused()
    reason = control.pause_reason() if paused else None
    return {
        "balance": balance,
        "paused": paused,
        "pause_reason": reason,
        "symbol": config.SYMBOL,
        "leverage": config.LEVERAGE,
        "risk_pct": config.RISK_PCT,
        "min_rr": config.MIN_RR,
        "atr_ratio_min": config.ATR_RATIO_MIN,
        "daily": dict(row) if row else None,
        "diag": _parse_latest_diag(),
    }


@app.get("/")
async def index():
    return FileResponse(STATIC_DIR / "index.html")


app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")
