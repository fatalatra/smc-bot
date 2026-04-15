#!/usr/bin/env bash
# One-shot report: how did SMC bot do 2h after TF shift (Hour4→Min60...).
# Collects state, sends to Telegram.
set -u

source /root/smc-bot/.env

STATE=$(systemctl is-active smc-bot)
SINCE_TS=1776097500  # 2026-04-13 18:05 CEST (16:05 UTC), the shift moment — epoch

cd /root/smc-bot
source venv/bin/activate

REPORT=$(python3 << 'PY'
import sqlite3, time, datetime
db = sqlite3.connect('smc_bot.db')
c = db.cursor()

# new trades after the TF shift (id > 7)
rows = c.execute("SELECT id, side, entry, open_ts, close_ts, pnl, reason FROM trades WHERE id > 7 ORDER BY id").fetchall()
lines = []
lines.append(f"<b>SMC TF-shift report</b> (2h after)")
lines.append(f"Trades since shift: <b>{len(rows)}</b>")
total_pnl = 0.0
for r in rows:
    tid, side, entry, open_ts, close_ts, pnl, reason = r
    dur = ""
    if close_ts and open_ts:
        dur = f" dur={int((close_ts-open_ts)/60)}m"
    total_pnl += (pnl or 0)
    closed = "open" if not close_ts else "closed"
    lines.append(f"#{tid} {side} @{entry:.1f} {closed}{dur} pnl=${pnl or 0:.2f}")

# open trades
opn = c.execute("SELECT id, side, entry FROM trades WHERE close_ts IS NULL").fetchall()
lines.append(f"\nOpen: {len(opn)}")

# daily_pnl today
today = datetime.date.today().isoformat()
dp = c.execute("SELECT * FROM daily_pnl WHERE date=?", (today,)).fetchone()
if dp:
    lines.append(f"daily_pnl: start=${dp[1]:.2f} realized=${dp[2]:.2f} trades={dp[3]}")

print("\n".join(lines))
PY
)

# Use file size marker to scan only lines added since shift (18:05 CEST 2026-04-13).
# Marker file stores line count at that moment. If absent, fall back to last 300 lines.
MARKER=/root/smc-bot/.tf-shift-line-marker
if [ -f "$MARKER" ]; then
    START_LINE=$(cat "$MARKER")
    RECENT=$(tail -n +"$START_LINE" /root/smc-bot/bot.log)
else
    RECENT=$(tail -n 300 /root/smc-bot/bot.log)
fi

SKIPS=$(echo "$RECENT" | grep -oE 'skip=\w+' | sort | uniq -c | sort -rn | head -6 | sed 's/^/  /')
TICK_COUNT=$(echo "$RECENT" | grep -c 'tick balance')

MSG="<b>SMC TF-shift 2h report</b>
systemd: <code>$STATE</code>
ticks since shift: <b>$TICK_COUNT</b>

$REPORT

<b>Skip reasons since 18:05:</b>
<pre>$SKIPS</pre>"

# send to TG
curl -s -X POST "https://api.telegram.org/bot${TG_TOKEN}/sendMessage" \
  -d "chat_id=${TG_CHAT_ID}" \
  -d "parse_mode=HTML" \
  --data-urlencode "text=${MSG}" > /tmp/smc-tf-report.tg.log

echo "[$(date -Iseconds)] report sent" >> /var/log/smc-tf-report.log
