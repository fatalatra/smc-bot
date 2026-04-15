#!/usr/bin/env python3
"""Local analyst — generates reports from DB every 4 hours via cron."""
import sqlite3
import time
import re
import subprocess
from datetime import datetime, timezone
from pathlib import Path

DB = "/root/smc-bot/smc_bot.db"
LOG = "/root/smc-bot/bot.log"
REPORTS = Path("/root/smc-bot/reports")
REPO = Path("/root/smc-bot")


def db():
    c = sqlite3.connect(DB)
    c.row_factory = sqlite3.Row
    return c


def tail(path, n=32768):
    try:
        with open(path, "rb") as f:
            f.seek(0, 2)
            f.seek(max(0, f.tell() - n))
            return f.read().decode("utf-8", errors="ignore")
    except Exception:
        return ""


def run():
    now = datetime.now(timezone.utc)
    conn = db()

    trades = [dict(r) for r in conn.execute(
        "SELECT * FROM trades ORDER BY open_ts DESC"
    ).fetchall()]

    daily = [dict(r) for r in conn.execute(
        "SELECT * FROM daily_pnl ORDER BY date DESC LIMIT 7"
    ).fetchall()]

    cutoff = time.time() - 4 * 3600
    recent = [t for t in trades if t["status"] == "closed" and (t.get("close_ts") or 0) > cutoff]
    open_pos = [t for t in trades if t["status"] == "open"]

    closed = [t for t in trades if t["status"] == "closed" and t.get("pnl") is not None]
    wins = [t for t in closed if t["pnl"] > 0]
    losses = [t for t in closed if t["pnl"] <= 0]
    win_rate = len(wins) / len(closed) * 100 if closed else 0
    avg_win = sum(t["pnl"] for t in wins) / len(wins) if wins else 0
    avg_loss = sum(t["pnl"] for t in losses) / len(losses) if losses else 0
    total_pnl = sum(t["pnl"] for t in closed)
    best = max(closed, key=lambda t: t["pnl"]) if closed else None
    worst = min(closed, key=lambda t: t["pnl"]) if closed else None

    if len(daily) >= 2:
        d0 = daily[0].get("start_balance", 0) + daily[0].get("pnl", 0)
        d1 = daily[1].get("start_balance", 0)
        bal_trend = "up" if d0 > d1 else "down"
    else:
        bal_trend = "n/a"

    log_tail = tail(LOG)
    diag_lines = [ln for ln in log_tail.splitlines() if "diag:" in ln]
    skip_counts = {}
    total_diag = len(diag_lines)
    for ln in diag_lines:
        m = re.search(r"skip=(\w+)", ln)
        if m:
            skip_counts[m.group(1)] = skip_counts.get(m.group(1), 0) + 1

    err_lines = [ln.strip() for ln in log_tail.splitlines()
                 if re.search(r"ERROR|exception|Traceback", ln, re.I)]
    unique_errs = list(set(err_lines))[:5]

    ts_str = now.strftime("%Y-%m-%d %H:%M UTC")
    fname = now.strftime("%Y-%m-%d_%H%M") + ".md"

    lines = [f"# Analyst Report — {ts_str}", ""]

    cur_bal = daily[0].get("start_balance", 0) + daily[0].get("pnl", 0) if daily else 0
    lines += [
        "## Status",
        f"- Balance: ~${cur_bal:.2f}",
        f"- Trend: {bal_trend}",
        f"- Closed trades: {len(closed)}",
        f"- Win rate: {win_rate:.1f}% ({len(wins)}W / {len(losses)}L)",
        f"- Total PnL: ${total_pnl:.2f}",
        f"- Avg win: ${avg_win:.2f} | Avg loss: ${avg_loss:.2f}",
        "",
    ]
    if best:
        lines.append(f"- Best: #{best['id']} {best['side']} ${best['pnl']:.2f}")
    if worst:
        lines.append(f"- Worst: #{worst['id']} {worst['side']} ${worst['pnl']:.2f}")
    lines.append("")

    if open_pos:
        lines += ["## Open Positions"]
        for p in open_pos:
            sl = p.get("sl") or 0
            tp = p.get("tp") or 0
            lines.append(f"- #{p['id']} {p['side']} entry ${p['entry']:.1f} SL ${sl:.1f} TP ${tp:.1f}")
        lines.append("")

    lines += ["## Trades (last 4h)"]
    if recent:
        for t in recent:
            result = "WIN" if t["pnl"] > 0 else "LOSS"
            ct = datetime.fromtimestamp(t["close_ts"], tz=timezone.utc).strftime("%H:%M") if t.get("close_ts") else "?"
            lines.append(f"- #{t['id']} {t['side']} ${t['pnl']:.2f} ({result}) closed {ct} | {t.get('reason', '?')}")
    else:
        lines.append("- No closed trades in period")
    lines.append("")

    lines += ["## Filters (diag)"]
    if skip_counts:
        for sk, cnt in sorted(skip_counts.items(), key=lambda x: -x[1]):
            pct = cnt / total_diag * 100 if total_diag else 0
            lines.append(f"- {sk}: {cnt}x ({pct:.0f}%)")
    else:
        lines.append("- No skips in recent logs")
    lines.append("")

    lines += ["## Errors"]
    if unique_errs:
        for e in unique_errs:
            lines.append(f"- `{e[:120]}`")
    else:
        lines.append("- None")
    lines.append("")

    lines += ["## Recommendations"]
    recs = []
    if win_rate < 50:
        recs.append(f"Win rate {win_rate:.0f}% below 50% — consider tightening entry filters")
    if avg_loss and avg_win and abs(avg_loss) > avg_win:
        recs.append(f"Avg loss (${avg_loss:.2f}) > avg win (${avg_win:.2f}) — R:R not holding")
    if skip_counts.get("trend_mismatch", 0) > total_diag * 0.8:
        recs.append("trend_mismatch blocking >80% ticks — market ranging, bot correctly waiting")
    if "SSL" in " ".join(unique_errs):
        recs.append("SSL errors detected — monitor MEXC API connectivity")
    if not recs:
        recs.append("All within normal parameters")
    for r in recs:
        lines.append(f"- {r}")

    conn.close()

    report_path = REPORTS / fname
    report_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"Report: {report_path}")

    # Git commit & push
    subprocess.run(["git", "add", "reports/"], cwd=REPO)
    res = subprocess.run(
        ["git", "diff", "--cached", "--quiet"], cwd=REPO
    )
    if res.returncode != 0:
        subprocess.run(
            ["git", "commit", "-m", f"analyst report {now.strftime('%Y-%m-%d_%H%M')}"],
            cwd=REPO,
        )
        subprocess.run(["git", "push"], cwd=REPO)
        print("Pushed")
    else:
        print("No changes")


if __name__ == "__main__":
    run()
