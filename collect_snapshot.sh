#!/bin/bash
set -e
cd /root/smc-bot
SNAP="reports/snapshot.md"
TS=$(date -u +"%Y-%m-%d %H:%M UTC")
SVC=$(systemctl is-active smc-bot 2>/dev/null || echo unknown)
BAL=$(tail -5 bot.log | grep -oP "balance=.{1,15}" | tail -1)
COOLDOWN=$(grep POST_CLOSE_COOLDOWN config.py | head -1 | xargs)
RISK=$(grep RISK_PCT config.py | head -1 | xargs)
ADX=$(grep ADX_MIN config.py | head -1 | xargs)
TRADES=$(sqlite3 smc_bot.db "SELECT id, side, round(entry,1), round(pnl,2), status, datetime(open_ts,unixepoch), datetime(close_ts,unixepoch) FROM trades ORDER BY id DESC LIMIT 20;" 2>/dev/null || echo "err")
DAILY=$(sqlite3 smc_bot.db "SELECT date, round(start_balance,2), round(pnl,2), stopped FROM daily_pnl ORDER BY date DESC LIMIT 7;" 2>/dev/null || echo "err")
OPENPOS=$(sqlite3 smc_bot.db "SELECT id,side,round(entry,1),status FROM trades WHERE status=open;" 2>/dev/null || echo "none")
DIAG=$(grep "diag:" bot.log | tail -240 | sed "s/.*diag: //" | sort | uniq -c | sort -rn | head -20)
ERRS=$(grep -iE "ERROR|exception|traceback" bot.log | tail -20 || echo "none")
LOGS=$(tail -100 bot.log)

cat > "$SNAP" << MDEOF
# Bot Snapshot — $TS

## Service: $SVC
$BAL

## Config
$COOLDOWN
$RISK
$ADX

## Trades (last 20)
\`\`\`
$TRADES
\`\`\`

## Daily PnL
\`\`\`
$DAILY
\`\`\`

## Open Positions
\`\`\`
${OPENPOS:-none}
\`\`\`

## Diag Summary (last ~4h)
\`\`\`
$DIAG
\`\`\`

## Errors
\`\`\`
${ERRS:-none}
\`\`\`

## Last 100 Log Lines
\`\`\`
$LOGS
\`\`\`
MDEOF

git add reports/snapshot.md
git diff --cached --quiet || (git commit -m "snapshot $(date -u +%Y-%m-%d_%H%M)" && git push)
echo "OK: $TS"
