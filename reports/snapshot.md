# Bot Snapshot — 2026-04-19 10:55 UTC

## Service: active
balance=$345.17

## Config
POST_CLOSE_COOLDOWN: int = 180 # 3 мин техническая пауза после закрытия
RISK_PCT: float = 0.05 # 5% от баланса на сделку
ADX_MIN: float = 20.0 # ADX < 20 → choppy market, skip entry

## Trades (last 20)
```
26|SELL|75081.6||open|2026-04-19 09:30:34|
25|SELL|75705.5|0.3|closed|2026-04-18 19:15:28|2026-04-19 04:18:16
24|SELL|76093.0|0.2|closed|2026-04-18 15:10:50|2026-04-18 16:27:41
23|SELL|76513.3|39.13|closed|2026-04-18 09:55:19|2026-04-18 11:06:57
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
```

## Daily PnL
```
2026-04-19|354.45|-9.28|0
2026-04-18|311.88|42.12|0
2026-04-17|328.7|-16.81|0
2026-04-16|381.29|-52.59|0
2026-04-15|363.1|17.9|0
2026-04-14|413.74|-50.64|0
2026-04-13|413.74|0.0|0
```

## Open Positions
```
26|SELL|75081.6|open
```

## Diag Summary (last ~4h)
```
     28 trend_htf=ranging trend_mid=ranging skip=trend_mismatch
      5 trend=bearish atr_ratio=1.06 obs=3 obs_fresh=2 fvgs=14 bos=24 sigs=0 wrong_side=2 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=0
      5 trend=bearish atr_ratio=1.03 obs=4 obs_fresh=3 fvgs=14 bos=25 sigs=0 wrong_side=3 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=0
      3 trend=bearish atr_ratio=1.08 obs=3 obs_fresh=2 fvgs=15 bos=25 sigs=0 wrong_side=2 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=0
      3 trend=bearish atr_ratio=1.02 obs=3 obs_fresh=2 fvgs=17 bos=25 sigs=0 wrong_side=2 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=0
      3 trend=bearish atr_ratio=1.01 obs=3 obs_fresh=2 fvgs=16 bos=25 sigs=0 wrong_side=2 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=0
      2 trend=bearish atr_ratio=1.09 obs=4 obs_fresh=3 fvgs=14 bos=25 sigs=0 wrong_side=3 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=0
      2 trend=bearish atr_ratio=1.09 obs=3 obs_fresh=2 fvgs=14 bos=24 sigs=0 wrong_side=2 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=0
      2 trend=bearish atr_ratio=1.07 obs=4 obs_fresh=3 fvgs=14 bos=25 sigs=0 wrong_side=3 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=0
      2 trend=bearish atr_ratio=1.03 obs=3 obs_fresh=2 fvgs=18 bos=27 sigs=0 wrong_side=2 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=0
      2 trend=bearish atr_ratio=1.03 obs=3 obs_fresh=2 fvgs=16 bos=25 sigs=0 wrong_side=2 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=0
      2 trend=bearish atr_ratio=1.03 obs=3 obs_fresh=2 fvgs=15 bos=26 sigs=0 wrong_side=2 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=0
      2 trend=bearish atr_ratio=1.03 obs=12 obs_fresh=12 fvgs=15 bos=28 sigs=0 wrong_side=7 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=5 near_gap_pct=0.176
      2 trend=bearish atr_ratio=1.02 obs=3 obs_fresh=2 fvgs=17 bos=27 sigs=0 wrong_side=2 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=0
      2 trend=bearish atr_ratio=0.9 obs=4 obs_fresh=3 fvgs=13 bos=25 sigs=0 wrong_side=3 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=0
      2 trend=bearish atr_ratio=0.9 obs=11 obs_fresh=11 fvgs=15 bos=27 sigs=0 wrong_side=7 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=4 near_gap_pct=0.007
      2 trend=bearish atr_ratio=0.99 obs=12 obs_fresh=12 fvgs=16 bos=26 sigs=0 wrong_side=7 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=5 near_gap_pct=0.03
      2 trend=bearish atr_ratio=0.91 obs=4 obs_fresh=3 fvgs=13 bos=25 sigs=0 wrong_side=3 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=0
      2 trend=bearish atr_ratio=0.85 obs=4 obs_fresh=3 fvgs=12 bos=25 sigs=0 wrong_side=3 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=0
      2 trend=bearish atr_ratio=0.82 obs=4 obs_fresh=3 fvgs=12 bos=25 sigs=0 wrong_side=3 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=0
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
  diag: trend=bearish atr_ratio=1.06 obs=3 obs_fresh=2 fvgs=15 bos=26 sigs=0 wrong_side=2 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=0
[12:10:35] tick balance=$361.07
  diag: trend=bearish atr_ratio=1.05 obs=3 obs_fresh=2 fvgs=15 bos=25 sigs=0 wrong_side=2 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=0
[12:11:39] tick balance=$360.63
  diag: trend=bearish atr_ratio=1.06 obs=3 obs_fresh=2 fvgs=15 bos=25 sigs=0 wrong_side=2 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=0
[12:12:42] tick balance=$357.84
  diag: trend=bearish atr_ratio=1.08 obs=3 obs_fresh=2 fvgs=15 bos=25 sigs=0 wrong_side=2 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=0
[12:13:46] tick balance=$358.55
  diag: trend=bearish atr_ratio=1.08 obs=3 obs_fresh=2 fvgs=15 bos=25 sigs=0 wrong_side=2 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=0
[12:14:49] tick balance=$358.02
  diag: trend=bearish atr_ratio=1.08 obs=3 obs_fresh=2 fvgs=15 bos=25 sigs=0 wrong_side=2 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=0
[12:15:52] tick balance=$361.04
  diag: trend=bearish atr_ratio=1.06 obs=3 obs_fresh=2 fvgs=14 bos=24 sigs=0 wrong_side=2 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=0
[12:16:55] tick balance=$359.58
  diag: trend=bearish atr_ratio=1.06 obs=3 obs_fresh=2 fvgs=14 bos=24 sigs=0 wrong_side=2 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=0
[12:17:58] tick balance=$360.02
  diag: trend=bearish atr_ratio=1.06 obs=3 obs_fresh=2 fvgs=14 bos=24 sigs=0 wrong_side=2 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=0
[12:19:00] tick balance=$360.34
  diag: trend=bearish atr_ratio=1.06 obs=3 obs_fresh=2 fvgs=14 bos=24 sigs=0 wrong_side=2 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=0
[12:20:02] tick balance=$359.69
  diag: trend=bearish atr_ratio=1.04 obs=3 obs_fresh=2 fvgs=14 bos=24 sigs=0 wrong_side=2 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=0
[12:21:04] tick balance=$357.97
  diag: trend=bearish atr_ratio=1.06 obs=3 obs_fresh=2 fvgs=14 bos=24 sigs=0 wrong_side=2 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=0
[12:22:07] tick balance=$354.59
  diag: trend=bearish atr_ratio=1.09 obs=3 obs_fresh=2 fvgs=14 bos=24 sigs=0 wrong_side=2 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=0
[12:23:11] tick balance=$354.04
  diag: trend=bearish atr_ratio=1.09 obs=3 obs_fresh=2 fvgs=14 bos=24 sigs=0 wrong_side=2 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=0
[12:24:14] tick balance=$355.52
  diag: trend=bearish atr_ratio=1.09 obs=3 obs_fresh=2 fvgs=14 bos=25 sigs=0 wrong_side=2 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=0
[12:25:18] tick balance=$356.11
  diag: trend=bearish atr_ratio=1.05 obs=4 obs_fresh=3 fvgs=14 bos=25 sigs=0 wrong_side=3 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=0
[12:26:21] tick balance=$355.12
  diag: trend=bearish atr_ratio=1.07 obs=4 obs_fresh=3 fvgs=14 bos=25 sigs=0 wrong_side=3 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=0
[12:27:25] tick balance=$355.98
  diag: trend=bearish atr_ratio=1.07 obs=4 obs_fresh=3 fvgs=14 bos=25 sigs=0 wrong_side=3 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=0
[12:28:28] tick balance=$351.38
  diag: trend=bearish atr_ratio=1.09 obs=4 obs_fresh=3 fvgs=14 bos=25 sigs=0 wrong_side=3 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=0
[12:29:31] tick balance=$354.03
  diag: trend=bearish atr_ratio=1.09 obs=4 obs_fresh=3 fvgs=14 bos=25 sigs=0 wrong_side=3 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=0
[12:30:34] tick balance=$354.02
  diag: trend=bearish atr_ratio=1.03 obs=4 obs_fresh=3 fvgs=14 bos=25 sigs=0 wrong_side=3 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=0
[12:31:38] tick balance=$354.23
  diag: trend=bearish atr_ratio=1.03 obs=4 obs_fresh=3 fvgs=14 bos=25 sigs=0 wrong_side=3 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=0
[12:32:40] tick balance=$353.58
  diag: trend=bearish atr_ratio=1.03 obs=4 obs_fresh=3 fvgs=14 bos=25 sigs=0 wrong_side=3 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=0
[12:33:43] tick balance=$353.45
  diag: trend=bearish atr_ratio=1.03 obs=4 obs_fresh=3 fvgs=14 bos=25 sigs=0 wrong_side=3 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=0
[12:34:47] tick balance=$352.93
  diag: trend=bearish atr_ratio=1.03 obs=4 obs_fresh=3 fvgs=14 bos=25 sigs=0 wrong_side=3 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=0
[12:35:50] tick balance=$353.70
  diag: trend=bearish atr_ratio=0.9 obs=4 obs_fresh=3 fvgs=13 bos=25 sigs=0 wrong_side=3 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=0
[12:36:53] tick balance=$354.59
  diag: trend=bearish atr_ratio=0.9 obs=4 obs_fresh=3 fvgs=13 bos=25 sigs=0 wrong_side=3 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=0
[12:37:56] tick balance=$354.76
  diag: trend=bearish atr_ratio=0.91 obs=4 obs_fresh=3 fvgs=13 bos=25 sigs=0 wrong_side=3 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=0
[12:38:59] tick balance=$353.39
  diag: trend=bearish atr_ratio=0.91 obs=4 obs_fresh=3 fvgs=13 bos=25 sigs=0 wrong_side=3 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=0
[12:40:02] tick balance=$355.16
  diag: trend=bearish atr_ratio=0.86 obs=4 obs_fresh=3 fvgs=14 bos=25 sigs=0 wrong_side=3 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=0
[12:41:05] tick balance=$355.98
  diag: trend=bearish atr_ratio=0.87 obs=5 obs_fresh=4 fvgs=14 bos=25 sigs=0 wrong_side=3 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=1 near_gap_pct=0.014
[12:42:08] tick balance=$356.03
  diag: trend=bearish atr_ratio=0.87 obs=5 obs_fresh=4 fvgs=14 bos=26 sigs=0 wrong_side=3 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=1 near_gap_pct=0.015
[12:43:11] tick balance=$354.92
  diag: trend=bearish atr_ratio=0.87 obs=4 obs_fresh=3 fvgs=13 bos=25 sigs=0 wrong_side=3 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=0
[12:44:15] tick balance=$353.15
  diag: trend=bearish atr_ratio=0.89 obs=4 obs_fresh=3 fvgs=13 bos=24 sigs=0 wrong_side=3 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=0
[12:45:18] tick balance=$353.35
  diag: trend=bearish atr_ratio=0.82 obs=4 obs_fresh=3 fvgs=12 bos=25 sigs=0 wrong_side=3 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=0
[12:46:21] tick balance=$353.55
  diag: trend=bearish atr_ratio=0.82 obs=4 obs_fresh=3 fvgs=12 bos=25 sigs=0 wrong_side=3 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=0
[12:47:24] tick balance=$356.18
  diag: trend=bearish atr_ratio=0.85 obs=4 obs_fresh=3 fvgs=12 bos=25 sigs=0 wrong_side=3 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=0
[12:48:27] tick balance=$353.93
  diag: trend=bearish atr_ratio=0.85 obs=4 obs_fresh=3 fvgs=12 bos=25 sigs=0 wrong_side=3 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=0
[12:49:30] tick balance=$350.83
  diag: trend=bearish atr_ratio=0.87 obs=5 obs_fresh=4 fvgs=12 bos=26 sigs=0 wrong_side=4 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=0
[12:50:33] tick balance=$348.98
  diag: trend=bearish atr_ratio=0.85 obs=5 obs_fresh=4 fvgs=13 bos=25 sigs=0 wrong_side=4 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=0
[12:51:35] tick balance=$343.94
  diag: trend=bearish atr_ratio=0.89 obs=5 obs_fresh=4 fvgs=13 bos=25 sigs=0 wrong_side=4 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=0
🤖 <b>SMC Bot Started</b> — ▶️ ACTIVE
Balance: <b>$344.85</b>
BTC Price: <b>$75,152.30</b>
Leverage: <b>x30</b>
Risk: <b>5.0%</b> ($17.24)
R:R min: <b>2.5</b>
Max positions: <b>2</b>
Daily limits: <b>+$88.61</b> / <b>-$70.89</b>
Max trades/day: <b>10</b>
Breakeven: at <b>50%</b> to TP
Commands: /start /stop /status /help
[*] Scanning every 60s...
[TG poll] drained backlog, starting offset=0
[12:52:21] tick balance=$344.84
  diag: trend=bearish skip=trend_immature trend_age_s=0 need_s=900
[12:53:24] tick balance=$345.06
  diag: trend=bearish skip=trend_immature trend_age_s=62 need_s=900
[12:54:28] tick balance=$345.17
  diag: trend=bearish skip=trend_immature trend_age_s=126 need_s=900
```
