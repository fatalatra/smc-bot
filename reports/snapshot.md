# Bot Snapshot — 2026-04-19 14:55 UTC

## Service: active
balance=$333.70

## Config
POST_CLOSE_COOLDOWN: int = 180 # 3 мин техническая пауза после закрытия
RISK_PCT: float = 0.05 # 5% от баланса на сделку
ADX_MIN: float = 20.0 # ADX < 20 → choppy market, skip entry

## Trades (last 20)
```
26|SELL|75081.6|-17.17|closed|2026-04-19 09:30:34|2026-04-19 11:10:17
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
2026-04-19|354.45|-20.75|0
2026-04-18|311.88|42.12|0
2026-04-17|328.7|-16.81|0
2026-04-16|381.29|-52.59|0
2026-04-15|363.1|17.9|0
2026-04-14|413.74|-50.64|0
2026-04-13|413.74|0.0|0
```

## Open Positions
```
none
```

## Diag Summary (last ~4h)
```
     42 trend_htf=ranging trend_mid=ranging skip=trend_mismatch
      4 trend=bearish atr_ratio=1.12 obs=4 obs_fresh=4 fvgs=12 bos=25 sigs=0 wrong_side=4 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=0
      4 trend=bearish atr_ratio=0.99 obs=4 obs_fresh=4 fvgs=12 bos=26 sigs=0 wrong_side=4 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=0
      3 trend=bearish atr_ratio=1.0 obs=5 obs_fresh=5 fvgs=12 bos=25 sigs=0 wrong_side=5 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=0
      3 trend=bearish atr_ratio=1.07 obs=5 obs_fresh=5 fvgs=12 bos=23 sigs=0 wrong_side=5 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=0
      3 trend=bearish atr_ratio=1.02 obs=5 obs_fresh=5 fvgs=12 bos=24 sigs=0 wrong_side=5 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=0
      3 trend=bearish atr_ratio=0.99 obs=4 obs_fresh=4 fvgs=12 bos=25 sigs=0 wrong_side=4 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=0
      3 trend=bearish atr_ratio=0.95 obs=4 obs_fresh=4 fvgs=12 bos=25 sigs=0 wrong_side=4 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=0
      2 trend=bullish atr_ratio=1.48 obs=8 obs_fresh=7 fvgs=12 bos=29 sigs=0 wrong_side=2 price_out=2 bos_miss=0 risk_neg=0 liquidity_trap=3 near_gap_pct=-0.112
      2 trend=bearish skip=trend_immature trend_age_s=62 need_s=900
      2 trend=bearish skip=trend_immature trend_age_s=0 need_s=900
      2 trend=bearish atr_ratio=1.25 obs=4 obs_fresh=4 fvgs=12 bos=27 sigs=0 wrong_side=4 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=0
      2 trend=bearish atr_ratio=1.12 obs=4 obs_fresh=4 fvgs=12 bos=24 sigs=0 wrong_side=4 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=0
      2 trend=bearish atr_ratio=1.0 obs=4 obs_fresh=4 fvgs=11 bos=27 sigs=0 wrong_side=4 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=0
      2 trend=bearish atr_ratio=1.02 obs=4 obs_fresh=4 fvgs=12 bos=26 sigs=0 wrong_side=4 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=0
      2 trend=bearish atr_ratio=0.99 obs=5 obs_fresh=5 fvgs=12 bos=29 sigs=0 wrong_side=5 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=0
      2 trend=bearish atr_ratio=0.99 obs=4 obs_fresh=4 fvgs=11 bos=27 sigs=0 wrong_side=4 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=0
      2 trend=bearish atr_ratio=0.98 obs=4 obs_fresh=4 fvgs=11 bos=26 sigs=0 wrong_side=4 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=0
      2 trend=bearish atr_ratio=0.97 obs=4 obs_fresh=4 fvgs=12 bos=26 sigs=0 wrong_side=4 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=0
      2 trend=bearish atr_ratio=0.97 obs=4 obs_fresh=4 fvgs=12 bos=25 sigs=0 wrong_side=4 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=0
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
[16:03:36] tick balance=$333.70
  diag: trend=bullish atr_ratio=1.5 obs=7 obs_fresh=6 fvgs=11 bos=29 sigs=0 wrong_side=1 price_out=2 bos_miss=0 risk_neg=0 liquidity_trap=3 near_gap_pct=0.065
[16:04:37] tick balance=$333.70
  diag: trend=bullish atr_ratio=1.5 obs=7 obs_fresh=6 fvgs=11 bos=29 sigs=0 wrong_side=1 price_out=2 bos_miss=0 risk_neg=0 liquidity_trap=3 near_gap_pct=0.034
[16:05:39] tick balance=$333.70
  diag: trend=bullish atr_ratio=1.45 obs=8 obs_fresh=7 fvgs=12 bos=29 sigs=0 wrong_side=2 price_out=2 bos_miss=0 risk_neg=0 liquidity_trap=3 near_gap_pct=-0.043
[16:06:41] tick balance=$333.70
  diag: trend=bullish atr_ratio=1.48 obs=8 obs_fresh=7 fvgs=12 bos=29 sigs=0 wrong_side=2 price_out=2 bos_miss=0 risk_neg=0 liquidity_trap=3 near_gap_pct=-0.096
[16:07:47] tick balance=$333.70
  diag: trend=bullish atr_ratio=1.48 obs=8 obs_fresh=7 fvgs=12 bos=29 sigs=0 wrong_side=2 price_out=2 bos_miss=0 risk_neg=0 liquidity_trap=3 near_gap_pct=-0.112
[16:08:52] tick balance=$333.70
  diag: trend=bullish atr_ratio=1.48 obs=8 obs_fresh=7 fvgs=12 bos=29 sigs=0 wrong_side=2 price_out=2 bos_miss=0 risk_neg=0 liquidity_trap=3 near_gap_pct=-0.08
[16:09:55] tick balance=$333.70
  diag: trend=bullish atr_ratio=1.48 obs=8 obs_fresh=7 fvgs=12 bos=29 sigs=0 wrong_side=2 price_out=2 bos_miss=0 risk_neg=0 liquidity_trap=3 near_gap_pct=-0.112
[16:10:57] tick balance=$333.70
  diag: trend=bullish atr_ratio=1.46 obs=8 obs_fresh=7 fvgs=12 bos=29 sigs=0 wrong_side=2 price_out=2 bos_miss=0 risk_neg=0 liquidity_trap=3 near_gap_pct=-0.063
[16:11:59] tick balance=$333.70
  diag: trend=bullish atr_ratio=1.46 obs=8 obs_fresh=7 fvgs=12 bos=29 sigs=0 wrong_side=2 price_out=2 bos_miss=0 risk_neg=0 liquidity_trap=3 near_gap_pct=-0.053
[16:13:00] tick balance=$333.70
  diag: trend=bullish atr_ratio=1.47 obs=8 obs_fresh=7 fvgs=12 bos=29 sigs=0 wrong_side=2 price_out=2 bos_miss=0 risk_neg=0 liquidity_trap=3 near_gap_pct=0.013
[16:14:02] tick balance=$333.70
  diag: trend=bullish atr_ratio=1.48 obs=8 obs_fresh=7 fvgs=12 bos=29 sigs=0 wrong_side=2 price_out=2 bos_miss=0 risk_neg=0 liquidity_trap=3 near_gap_pct=0.016
[16:15:04] tick balance=$333.70
  diag: trend=bullish atr_ratio=1.43 obs=8 obs_fresh=7 fvgs=12 bos=29 sigs=0 wrong_side=2 price_out=2 bos_miss=0 risk_neg=0 liquidity_trap=3 near_gap_pct=0.017
[16:16:05] tick balance=$333.70
  diag: trend=bullish atr_ratio=1.44 obs=8 obs_fresh=7 fvgs=12 bos=29 sigs=0 wrong_side=2 price_out=2 bos_miss=0 risk_neg=0 liquidity_trap=3 near_gap_pct=0.001
[16:17:07] tick balance=$333.70
  diag: trend=bullish atr_ratio=1.44 obs=8 obs_fresh=7 fvgs=12 bos=29 sigs=0 wrong_side=2 price_out=2 bos_miss=0 risk_neg=0 liquidity_trap=3 near_gap_pct=0.017
[16:18:10] tick balance=$333.70
  diag: trend=bullish atr_ratio=1.44 obs=8 obs_fresh=7 fvgs=12 bos=29 sigs=0 wrong_side=2 price_out=2 bos_miss=0 risk_neg=0 liquidity_trap=3 near_gap_pct=0.004
[16:19:13] tick balance=$333.70
  diag: trend=bullish atr_ratio=1.49 obs=9 obs_fresh=8 fvgs=12 bos=29 sigs=0 wrong_side=2 price_out=2 bos_miss=0 risk_neg=0 liquidity_trap=4 near_gap_pct=0.141
[16:20:14] tick balance=$333.70
  diag: trend=bullish atr_ratio=1.44 obs=9 obs_fresh=8 fvgs=13 bos=29 sigs=0 wrong_side=2 price_out=2 bos_miss=0 risk_neg=0 liquidity_trap=4 near_gap_pct=0.045
[16:21:17] tick balance=$333.70
  diag: trend=bullish atr_ratio=1.46 obs=9 obs_fresh=8 fvgs=12 bos=30 sigs=0 wrong_side=2 price_out=2 bos_miss=0 risk_neg=0 liquidity_trap=4 near_gap_pct=0.097
[16:22:19] tick balance=$333.70
  diag: trend=bullish atr_ratio=1.46 obs=9 obs_fresh=8 fvgs=12 bos=30 sigs=0 wrong_side=2 price_out=2 bos_miss=0 risk_neg=0 liquidity_trap=4 near_gap_pct=0.081
[16:23:21] tick balance=$333.70
  diag: trend=bullish atr_ratio=1.47 obs=9 obs_fresh=8 fvgs=12 bos=29 sigs=0 wrong_side=2 price_out=2 bos_miss=0 risk_neg=0 liquidity_trap=4 near_gap_pct=0.131
[16:24:23] tick balance=$333.70
  diag: trend=bullish atr_ratio=1.47 obs=9 obs_fresh=8 fvgs=12 bos=29 sigs=0 wrong_side=2 price_out=2 bos_miss=0 risk_neg=0 liquidity_trap=4 near_gap_pct=0.097
[16:25:25] tick balance=$333.70
  diag: trend=bullish atr_ratio=1.26 obs=8 obs_fresh=7 fvgs=11 bos=29 sigs=0 wrong_side=2 price_out=1 bos_miss=0 risk_neg=0 liquidity_trap=4 near_gap_pct=0.15
[16:26:27] tick balance=$333.70
  diag: trend=bullish atr_ratio=1.29 obs=8 obs_fresh=7 fvgs=11 bos=29 sigs=0 wrong_side=2 price_out=1 bos_miss=0 risk_neg=0 liquidity_trap=4 near_gap_pct=0.266
[16:27:29] tick balance=$333.70
  diag: trend=bullish atr_ratio=1.3 obs=8 obs_fresh=7 fvgs=11 bos=29 sigs=0 wrong_side=2 price_out=1 bos_miss=0 risk_neg=0 liquidity_trap=4 near_gap_pct=0.257
[16:28:31] tick balance=$333.70
  diag: trend=bullish atr_ratio=1.3 obs=8 obs_fresh=7 fvgs=11 bos=28 sigs=0 wrong_side=2 price_out=1 bos_miss=0 risk_neg=0 liquidity_trap=4 near_gap_pct=0.196
[16:29:33] tick balance=$333.70
  diag: trend=bullish atr_ratio=1.3 obs=8 obs_fresh=7 fvgs=11 bos=29 sigs=0 wrong_side=2 price_out=1 bos_miss=0 risk_neg=0 liquidity_trap=4 near_gap_pct=0.211
[16:30:36] tick balance=$333.70
  diag: trend=bullish atr_ratio=1.14 obs=8 obs_fresh=7 fvgs=12 bos=29 sigs=0 wrong_side=2 price_out=1 bos_miss=0 risk_neg=0 liquidity_trap=4 near_gap_pct=0.161
[16:31:38] tick balance=$333.70
  diag: trend=bullish atr_ratio=1.15 obs=8 obs_fresh=7 fvgs=11 bos=29 sigs=0 wrong_side=2 price_out=1 bos_miss=0 risk_neg=0 liquidity_trap=4 near_gap_pct=0.148
[16:32:40] tick balance=$333.70
  diag: trend=bullish atr_ratio=1.2 obs=8 obs_fresh=7 fvgs=11 bos=29 sigs=0 wrong_side=2 price_out=1 bos_miss=0 risk_neg=0 liquidity_trap=4 near_gap_pct=0.047
[16:33:42] tick balance=$333.70
  diag: trend=bullish atr_ratio=1.2 obs=8 obs_fresh=7 fvgs=11 bos=29 sigs=0 wrong_side=2 price_out=1 bos_miss=0 risk_neg=0 liquidity_trap=4 near_gap_pct=0.018
[16:34:44] tick balance=$333.70
  diag: trend=bullish atr_ratio=1.2 obs=8 obs_fresh=7 fvgs=11 bos=29 sigs=0 wrong_side=2 price_out=1 bos_miss=0 risk_neg=0 liquidity_trap=4 near_gap_pct=0.055
[16:35:45] tick balance=$333.70
  diag: trend=bullish atr_ratio=1.16 obs=9 obs_fresh=8 fvgs=11 bos=29 sigs=0 wrong_side=3 price_out=1 bos_miss=0 risk_neg=0 liquidity_trap=4 near_gap_pct=0.061
[16:36:48] tick balance=$333.70
  diag: trend=bullish atr_ratio=1.16 obs=9 obs_fresh=8 fvgs=11 bos=29 sigs=0 wrong_side=3 price_out=1 bos_miss=0 risk_neg=0 liquidity_trap=4 near_gap_pct=0.055
[16:37:50] tick balance=$333.70
  diag: trend=bullish atr_ratio=1.16 obs=8 obs_fresh=7 fvgs=11 bos=29 sigs=0 wrong_side=2 price_out=1 bos_miss=0 risk_neg=0 liquidity_trap=4 near_gap_pct=0.078
[16:38:51] tick balance=$333.70
  diag: trend=bullish atr_ratio=1.16 obs=8 obs_fresh=7 fvgs=11 bos=29 sigs=0 wrong_side=2 price_out=1 bos_miss=0 risk_neg=0 liquidity_trap=4 near_gap_pct=0.1
[16:39:53] tick balance=$333.70
  diag: trend=bullish atr_ratio=1.18 obs=8 obs_fresh=7 fvgs=11 bos=29 sigs=0 wrong_side=2 price_out=1 bos_miss=0 risk_neg=0 liquidity_trap=4 near_gap_pct=0.166
[16:40:56] tick balance=$333.70
  diag: trend=bullish atr_ratio=1.11 obs=8 obs_fresh=7 fvgs=11 bos=29 sigs=0 wrong_side=2 price_out=1 bos_miss=0 risk_neg=0 liquidity_trap=4 near_gap_pct=0.243
[16:41:57] tick balance=$333.70
  diag: trend=bullish atr_ratio=1.11 obs=8 obs_fresh=7 fvgs=11 bos=29 sigs=0 wrong_side=2 price_out=1 bos_miss=0 risk_neg=0 liquidity_trap=4 near_gap_pct=0.201
[16:42:58] tick balance=$333.70
  diag: trend=bullish atr_ratio=1.11 obs=8 obs_fresh=7 fvgs=11 bos=30 sigs=0 wrong_side=2 price_out=1 bos_miss=0 risk_neg=0 liquidity_trap=4 near_gap_pct=0.185
[16:44:00] tick balance=$333.70
  diag: trend=bullish atr_ratio=1.11 obs=8 obs_fresh=7 fvgs=11 bos=29 sigs=0 wrong_side=2 price_out=1 bos_miss=0 risk_neg=0 liquidity_trap=4 near_gap_pct=0.217
[16:45:02] tick balance=$333.70
  diag: trend=bullish atr_ratio=1.05 obs=7 obs_fresh=6 fvgs=12 bos=29 sigs=0 wrong_side=2 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=4 near_gap_pct=0.233
[16:46:05] tick balance=$333.70
  diag: trend=bullish atr_ratio=1.08 obs=7 obs_fresh=6 fvgs=12 bos=29 sigs=0 wrong_side=2 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=4 near_gap_pct=0.244
[16:47:08] tick balance=$333.70
  diag: trend=bullish atr_ratio=1.1 obs=7 obs_fresh=6 fvgs=12 bos=29 sigs=0 wrong_side=2 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=4 near_gap_pct=0.318
[16:48:10] tick balance=$333.70
  diag: trend=bullish atr_ratio=1.14 obs=7 obs_fresh=6 fvgs=12 bos=29 sigs=0 wrong_side=2 price_out=1 bos_miss=0 risk_neg=0 liquidity_trap=3 near_gap_pct=0.415
[16:49:12] tick balance=$333.70
  diag: trend=bullish atr_ratio=1.14 obs=7 obs_fresh=6 fvgs=12 bos=30 sigs=0 wrong_side=2 price_out=1 bos_miss=0 risk_neg=0 liquidity_trap=3 near_gap_pct=0.371
[16:50:14] tick balance=$333.70
  diag: trend=bullish atr_ratio=1.12 obs=7 obs_fresh=6 fvgs=12 bos=29 sigs=0 wrong_side=2 price_out=1 bos_miss=0 risk_neg=0 liquidity_trap=3 near_gap_pct=0.39
[16:51:17] tick balance=$333.70
  diag: trend=bullish atr_ratio=1.13 obs=7 obs_fresh=6 fvgs=12 bos=29 sigs=0 wrong_side=2 price_out=1 bos_miss=0 risk_neg=0 liquidity_trap=3 near_gap_pct=0.406
[16:52:19] tick balance=$333.70
  diag: trend=bullish atr_ratio=1.13 obs=7 obs_fresh=6 fvgs=12 bos=29 sigs=0 wrong_side=2 price_out=1 bos_miss=0 risk_neg=0 liquidity_trap=3 near_gap_pct=0.37
[16:53:21] tick balance=$333.70
  diag: trend=bullish atr_ratio=1.16 obs=7 obs_fresh=6 fvgs=12 bos=29 sigs=0 wrong_side=2 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=4 near_gap_pct=0.286
[16:54:23] tick balance=$333.70
  diag: trend=bullish atr_ratio=1.17 obs=7 obs_fresh=6 fvgs=11 bos=29 sigs=0 wrong_side=2 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=4 near_gap_pct=0.234
```
