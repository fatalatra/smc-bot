import sqlite3
import time
from datetime import datetime, timezone

DB_PATH = "/root/smc-bot/smc_bot.db"


def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS signals (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ts REAL, side TEXT, entry REAL, sl REAL, tp REAL,
        reason TEXT, acted INTEGER DEFAULT 0
    )""")
    c.execute("""CREATE TABLE IF NOT EXISTS trades (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        open_ts REAL, close_ts REAL,
        side TEXT, entry REAL, sl REAL, tp REAL,
        vol INTEGER, pnl REAL,
        status TEXT DEFAULT 'open',
        order_id TEXT, reason TEXT
    )""")
    c.execute("""CREATE TABLE IF NOT EXISTS daily_pnl (
        date TEXT PRIMARY KEY,
        start_balance REAL,
        pnl REAL DEFAULT 0.0,
        stopped INTEGER DEFAULT 0
    )""")
    conn.commit()
    conn.close()


def get_today() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%d")


def init_daily_pnl(balance: float):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    today = get_today()
    c.execute("SELECT date FROM daily_pnl WHERE date=?", (today,))
    if not c.fetchone():
        c.execute("INSERT INTO daily_pnl (date, start_balance, pnl, stopped) VALUES (?,?,0.0,0)",
                  (today, balance))
        conn.commit()
    conn.close()


def update_daily_pnl(current_balance: float) -> float:
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    today = get_today()
    c.execute("SELECT start_balance FROM daily_pnl WHERE date=?", (today,))
    row = c.fetchone()
    if not row:
        conn.close()
        return 0.0
    pnl = current_balance - row[0]
    c.execute("UPDATE daily_pnl SET pnl=? WHERE date=?", (pnl, today))
    conn.commit()
    conn.close()
    return pnl


def set_daily_stopped():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("UPDATE daily_pnl SET stopped=1 WHERE date=?", (get_today(),))
    conn.commit()
    conn.close()


def is_daily_stopped() -> bool:
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT stopped FROM daily_pnl WHERE date=?", (get_today(),))
    row = c.fetchone()
    conn.close()
    return bool(row and row[0])


def clear_daily_stopped():
    """Снимает флаг stopped для сегодняшнего дня. Используется авто-healing'ом
    когда PnL возвращается под лимит (например, пользователь поднял DAILY_LOSS_PCT
    или прилетел положительный PnL который вернул нас в зелёную зону).
    """
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("UPDATE daily_pnl SET stopped=0 WHERE date=?", (get_today(),))
    conn.commit()
    conn.close()


def log_signal(side: str, entry: float, sl: float, tp: float, reason: str) -> int:
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("INSERT INTO signals (ts, side, entry, sl, tp, reason) VALUES (?,?,?,?,?,?)",
              (time.time(), side, entry, sl, tp, reason))
    conn.commit()
    sid = c.lastrowid
    conn.close()
    return sid


def is_duplicate_signal(side: str, reason: str, cooldown: int = 900) -> bool:
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT ts FROM signals WHERE side=? AND reason=? ORDER BY ts DESC LIMIT 1", (side, reason))
    row = c.fetchone()
    conn.close()
    if row and (time.time() - row[0]) < cooldown:
        return True
    return False


def log_trade_open(side: str, entry: float, sl: float, tp: float, vol: int, order_id: str, reason: str) -> int:
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("INSERT INTO trades (open_ts, side, entry, sl, tp, vol, status, order_id, reason) VALUES (?,?,?,?,?,?,?,?,?)",
              (time.time(), side, entry, sl, tp, vol, "open", order_id, reason))
    conn.commit()
    tid = c.lastrowid
    conn.close()
    return tid


def log_trade_close(trade_id: int, pnl: float):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("UPDATE trades SET close_ts=?, pnl=?, status='closed' WHERE id=?",
              (time.time(), pnl, trade_id))
    conn.commit()
    conn.close()


def get_open_trades() -> list:
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT * FROM trades WHERE status='open'")
    rows = c.fetchall()
    conn.close()
    return rows


def update_trade_entry(trade_id: int, real_entry: float):
    """Обновить entry на реальную цену исполнения (openAvgPrice с биржи)."""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("UPDATE trades SET entry=? WHERE id=?", (real_entry, trade_id))
    conn.commit()
    conn.close()


def get_today_start_balance() -> float:
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT start_balance FROM daily_pnl WHERE date=?", (get_today(),))
    row = c.fetchone()
    conn.close()
    return float(row[0]) if row else 0.0


def get_last_close_ts() -> float:
    """Timestamp последнего закрытого трейда (для post-close cooldown)."""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT MAX(close_ts) FROM trades WHERE close_ts IS NOT NULL")
    row = c.fetchone()
    conn.close()
    return float(row[0]) if row and row[0] else 0.0


def get_today_trade_count() -> int:
    """Сколько сделок открыто сегодня (UTC). Считает по open_ts."""
    today = get_today()  # YYYY-MM-DD UTC
    # Convert to unix timestamp for midnight UTC
    midnight = datetime.strptime(today, "%Y-%m-%d").replace(tzinfo=timezone.utc).timestamp()
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT COUNT(*) FROM trades WHERE open_ts >= ?", (midnight,))
    n = c.fetchone()[0]
    conn.close()
    return int(n)


def update_trade_pnl(trade_id: int, pnl: float, profit: float = 0.0, fees: float = 0.0):
    """Update real PnL for a closed trade (fetched from MEXC order history)."""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("UPDATE trades SET pnl=? WHERE id=?", (pnl, trade_id))
    conn.commit()
    conn.close()


def get_trades_needing_pnl() -> list:
    """Closed trades with pnl=0 that need real PnL from MEXC."""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT id, order_id, side FROM trades WHERE status=? AND pnl=0.0",
              ("closed",))
    rows = c.fetchall()
    conn.close()
    return rows
