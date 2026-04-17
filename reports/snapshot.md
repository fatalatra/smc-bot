# Bot Snapshot — 2026-04-17 18:55 UTC

## Service: active
balance=$311.88

## Config
POST_CLOSE_COOLDOWN: int = 180 # 3 мин техническая пауза после закрытия
RISK_PCT: float = 0.05 # 5% от баланса на сделку
ADX_MIN: float = 20.0 # ADX < 20 → choppy market, skip entry

## Trades (last 20)
```
22|BUY|77789.0|-16.14|closed|2026-04-17 15:56:44|2026-04-17 17:13:11
21|BUY|77434.2|-1.57|closed|2026-04-17 14:22:26|2026-04-17 14:30:46
20|BUY|76000.0|36.88|closed|2026-04-17 12:47:27|2026-04-17 13:51:25
19|BUY|75720.1|-19.66|closed|2026-04-17 09:47:35|2026-04-17 10:29:29
18|BUY|76272.4|-16.61|closed|2026-04-17 09:28:51|2026-04-17 09:35:09
17|SELL|74090.0|-19.57|closed|2026-04-16 17:05:43|2026-04-16 17:43:32
16|SELL|73884.1|-18.54|closed|2026-04-16 14:56:12|2026-04-16 15:09:47
15|SELL|74394.2|-2.15|closed|2026-04-16 10:37:10|2026-04-16 11:34:20
14|BUY|74983.1|-19.34|closed|2026-04-15 22:32:25|2026-04-16 10:07:17
13|BUY|74275.5|-20.71|closed|2026-04-15 13:30:37|2026-04-15 15:30:56
12|SELL|73899.1|39.1|closed|2026-04-15 06:09:07|2026-04-15 07:46:09
11|BUY|74056.1|-3.16|closed|2026-04-14 19:38:54|2026-04-14 21:21:29
10|BUY|74270.7|-18.86|closed|2026-04-14 19:08:32|2026-04-14 19:33:51
9|BUY|74842.7|-22.95|closed|2026-04-14 15:24:35|2026-04-14 17:34:53
8|BUY|75630.3|-3.46|closed|2026-04-14 14:22:42|2026-04-14 15:00:43
7|SELL|70843.3|-11.35|closed|2026-04-12 15:59:14|2026-04-12 17:51:45
6|SELL|70977.6|16.89|closed|2026-04-12 13:15:20|2026-04-12 14:43:04
5|SELL|71364.3|13.27|closed|2026-04-12 10:57:04|2026-04-12 13:01:46
4|SELL|71492.1|13.27|closed|2026-04-12 10:41:17|2026-04-12 10:42:19
3|SELL|71597.7|13.27|closed|2026-04-12 10:25:37|2026-04-12 10:42:19
```

## Daily PnL
```
2026-04-17|328.7|-16.81|0
2026-04-16|381.29|-52.59|0
2026-04-15|363.1|17.9|0
2026-04-14|413.74|-50.64|0
2026-04-13|413.74|0.0|0
2026-04-12|423.86|-10.12|0
2026-04-11|457.33|-130.15|0
```

## Open Positions
```
none
```

## Diag Summary (last ~4h)
```
     13 trend=bullish skip=atr_low ratio=0.78 min=0.8
     10 trend=bullish skip=atr_low ratio=0.79 min=0.8
      8 trend=bullish skip=atr_low ratio=0.76 min=0.8
      6 trend=bullish skip=atr_low ratio=0.8 min=0.8
      5 trend=bullish skip=atr_low ratio=0.77 min=0.8
      4 trend=bullish skip=atr_low ratio=0.75 min=0.8
      3 trend=bullish skip=atr_low ratio=0.74 min=0.8
      3 trend=bullish skip=atr_low ratio=0.72 min=0.8
      3 trend=bullish skip=atr_low ratio=0.71 min=0.8
      3 trend=bullish atr_ratio=0.85 obs=10 obs_fresh=5 fvgs=14 bos=28 sigs=0 wrong_side=5 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=0
      3 trend=bullish atr_ratio=0.83 obs=9 obs_fresh=5 fvgs=14 bos=28 sigs=0 wrong_side=5 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=0
      2 trend=bullish skip=atr_low ratio=0.7 min=0.8
      2 trend=bullish atr_ratio=0.85 obs=12 obs_fresh=7 fvgs=14 bos=26 sigs=0 wrong_side=7 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=0
      2 trend=bullish atr_ratio=0.85 obs=11 obs_fresh=6 fvgs=14 bos=27 sigs=0 wrong_side=6 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=0
      2 trend=bullish atr_ratio=0.83 obs=10 obs_fresh=3 fvgs=12 bos=31 sigs=0 wrong_side=3 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=0
      2 trend=bullish atr_ratio=0.82 obs=11 obs_fresh=6 fvgs=13 bos=27 sigs=0 wrong_side=6 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=0
      2 trend=bullish atr_ratio=0.82 obs=10 obs_fresh=4 fvgs=11 bos=28 sigs=0 wrong_side=4 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=0
      2 trend=bullish atr_ratio=0.81 obs=10 obs_fresh=3 fvgs=12 bos=29 sigs=0 wrong_side=3 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=0
      1 trend=bullish skip=trend_immature trend_age_s=61 need_s=900
      1 trend=bullish skip=trend_immature trend_age_s=186 need_s=900
```

## Errors
```
httpcore.ConnectError: [Errno -2] Name or service not known
The above exception was the direct cause of the following exception:
Traceback (most recent call last):
    with map_httpcore_exceptions():
    self.gen.throw(typ, value, traceback)
  File "/root/smc-bot/venv/lib/python3.11/site-packages/httpx/_transports/default.py", line 118, in map_httpcore_exceptions
httpx.ConnectError: [Errno -2] Name or service not known
[ERROR] [Errno -2] Name or service not known
Traceback (most recent call last):
  File "/root/smc-bot/venv/lib/python3.11/site-packages/httpx/_transports/default.py", line 101, in map_httpcore_exceptions
    with map_exceptions(exc_map):
    self.gen.throw(typ, value, traceback)
  File "/root/smc-bot/venv/lib/python3.11/site-packages/httpcore/_exceptions.py", line 14, in map_exceptions
httpcore.ConnectError: [Errno -2] Name or service not known
The above exception was the direct cause of the following exception:
Traceback (most recent call last):
    with map_httpcore_exceptions():
    self.gen.throw(typ, value, traceback)
  File "/root/smc-bot/venv/lib/python3.11/site-packages/httpx/_transports/default.py", line 118, in map_httpcore_exceptions
httpx.ConnectError: [Errno -2] Name or service not known
```

## Last 100 Log Lines
```
[20:12:00] tick balance=$311.88
  ⏸ paused: manual /stop at 20:10:04
[20:13:02] tick balance=$311.88
  ⏸ paused: manual /stop at 20:10:04
[20:14:04] tick balance=$311.88
  ⏸ paused: manual /stop at 20:10:04
[20:15:05] tick balance=$311.88
  ⏸ paused: manual /stop at 20:10:04
[20:16:06] tick balance=$311.88
  ⏸ paused: manual /stop at 20:10:04
[20:17:08] tick balance=$311.88
  ⏸ paused: manual /stop at 20:10:04
[20:18:09] tick balance=$311.88
  ⏸ paused: manual /stop at 20:10:04
[20:19:11] tick balance=$311.88
  ⏸ paused: manual /stop at 20:10:04
[20:20:12] tick balance=$311.88
  ⏸ paused: manual /stop at 20:10:04
[20:21:14] tick balance=$311.88
  ⏸ paused: manual /stop at 20:10:04
[20:22:15] tick balance=$311.88
  ⏸ paused: manual /stop at 20:10:04
[20:23:17] tick balance=$311.88
  ⏸ paused: manual /stop at 20:10:04
[20:24:18] tick balance=$311.88
  ⏸ paused: manual /stop at 20:10:04
[20:25:19] tick balance=$311.88
  ⏸ paused: manual /stop at 20:10:04
[20:26:20] tick balance=$311.88
  ⏸ paused: manual /stop at 20:10:04
[20:27:22] tick balance=$311.88
  ⏸ paused: manual /stop at 20:10:04
[20:28:23] tick balance=$311.88
  ⏸ paused: manual /stop at 20:10:04
[20:29:24] tick balance=$311.88
  ⏸ paused: manual /stop at 20:10:04
[20:30:25] tick balance=$311.88
  ⏸ paused: manual /stop at 20:10:04
[20:31:27] tick balance=$311.88
  ⏸ paused: manual /stop at 20:10:04
[20:32:28] tick balance=$311.88
  ⏸ paused: manual /stop at 20:10:04
[20:33:29] tick balance=$311.88
  ⏸ paused: manual /stop at 20:10:04
[20:34:30] tick balance=$311.88
  ⏸ paused: manual /stop at 20:10:04
[20:35:31] tick balance=$311.88
  ⏸ paused: manual /stop at 20:10:04
[20:36:33] tick balance=$311.88
  ⏸ paused: manual /stop at 20:10:04
[20:37:34] tick balance=$311.88
  ⏸ paused: manual /stop at 20:10:04
[20:38:35] tick balance=$311.88
  ⏸ paused: manual /stop at 20:10:04
[20:39:36] tick balance=$311.88
  ⏸ paused: manual /stop at 20:10:04
[20:40:37] tick balance=$311.88
  ⏸ paused: manual /stop at 20:10:04
[20:41:39] tick balance=$311.88
  ⏸ paused: manual /stop at 20:10:04
[20:42:40] tick balance=$311.88
  ⏸ paused: manual /stop at 20:10:04
[20:43:41] tick balance=$311.88
  ⏸ paused: manual /stop at 20:10:04
[20:44:42] tick balance=$311.88
  ⏸ paused: manual /stop at 20:10:04
[20:45:44] tick balance=$311.88
  ⏸ paused: manual /stop at 20:10:04
[20:46:45] tick balance=$311.88
  ⏸ paused: manual /stop at 20:10:04
[20:47:46] tick balance=$311.88
  ⏸ paused: manual /stop at 20:10:04
[20:48:47] tick balance=$311.88
  ⏸ paused: manual /stop at 20:10:04
🤖 <b>SMC Bot Started</b> — ⏸ PAUSED
Balance: <b>$311.88</b>
BTC Price: <b>$77,302.40</b>
Leverage: <b>x30</b>
Risk: <b>5.0%</b> ($15.59)
R:R min: <b>2.5</b>
Max positions: <b>2</b>
Daily limits: <b>+$82.17</b> / <b>-$65.74</b>
Max trades/day: <b>10</b>
Breakeven: at <b>50%</b> to TP
Commands: /start /stop /status /help
[*] Scanning every 60s...
[TG poll] drained backlog, starting offset=0
[20:48:58] tick balance=$311.88
  ⏸ paused: manual /stop at 20:10:04
[20:50:00] tick balance=$311.88
  ⏸ paused: manual /stop at 20:10:04
[tg] resume
[20:51:01] tick balance=$311.88
  diag: trend=bullish skip=trend_immature trend_age_s=0 need_s=900
[20:52:03] tick balance=$311.88
  diag: trend=bullish skip=trend_immature trend_age_s=61 need_s=900
[20:53:05] tick balance=$311.88
  diag: trend=bullish skip=trend_immature trend_age_s=124 need_s=900
[20:54:08] tick balance=$311.88
  diag: trend=bullish skip=trend_immature trend_age_s=186 need_s=900
```
