# Bot Snapshot — 2026-04-20 02:55 UTC

## Service: active
balance=$312.71

## Config
POST_CLOSE_COOLDOWN: int = 180 # 3 мин техническая пауза после закрытия
RISK_PCT: float = 0.05 # 5% от баланса на сделку
ADX_MIN: float = 20.0 # ADX < 20 → choppy market, skip entry

## Trades (last 20)
```
27|SELL|74544.9|-20.99|closed|2026-04-19 21:13:01|2026-04-19 21:29:27
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
```

## Daily PnL
```
2026-04-20|312.71|0.0|0
2026-04-19|354.45|-41.74|0
2026-04-18|311.88|42.12|0
2026-04-17|328.7|-16.81|0
2026-04-16|381.29|-52.59|0
2026-04-15|363.1|17.9|0
2026-04-14|413.74|-50.64|0
```

## Open Positions
```
none
```

## Diag Summary (last ~4h)
```
      9 trend=bearish skip=atr_low ratio=0.71 min=0.8
      6 trend=bearish skip=atr_low ratio=0.7 min=0.8
      6 trend=bearish skip=atr_low ratio=0.69 min=0.8
      5 trend=bearish skip=atr_low ratio=0.75 min=0.8
      5 trend=bearish skip=atr_low ratio=0.72 min=0.8
      4 trend=bearish skip=atr_low ratio=0.66 min=0.8
      4 trend=bearish skip=atr_low ratio=0.62 min=0.8
      3 trend=bearish skip=atr_low ratio=0.73 min=0.8
      2 trend=bearish skip=ema_overextended price=74078.0 ema20_h4=75384.7 dist=1306.7 max_dist=1214.5
      2 trend=bearish skip=atr_low ratio=0.76 min=0.8
      2 trend=bearish skip=atr_low ratio=0.68 min=0.8
      2 trend=bearish skip=atr_low ratio=0.67 min=0.8
      2 trend=bearish skip=atr_low ratio=0.65 min=0.8
      2 trend=bearish skip=atr_low ratio=0.64 min=0.8
      2 trend=bearish skip=atr_low ratio=0.63 min=0.8
      2 trend=bearish atr_ratio=0.87 obs=9 obs_fresh=7 fvgs=8 bos=25 sigs=0 wrong_side=4 price_out=3 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=-0.337
      1 trend=bearish skip=ema_overextended price=74139.4 ema20_h4=75391.9 dist=1252.5 max_dist=1214.5
      1 trend=bearish skip=ema_overextended price=74130.9 ema20_h4=75388.2 dist=1257.3 max_dist=1214.5
      1 trend=bearish skip=ema_overextended price=74127.8 ema20_h4=75388.1 dist=1260.3 max_dist=1214.5
      1 trend=bearish skip=ema_overextended price=74113.1 ema20_h4=75387.4 dist=1274.3 max_dist=1214.5
```

## Errors
```
  File "/root/smc-bot/venv/lib/python3.11/site-packages/httpx/_transports/default.py", line 101, in map_httpcore_exceptions
    with map_exceptions(exc_map):
    self.gen.throw(typ, value, traceback)
  File "/root/smc-bot/venv/lib/python3.11/site-packages/httpcore/_exceptions.py", line 14, in map_exceptions
The above exception was the direct cause of the following exception:
Traceback (most recent call last):
    with map_httpcore_exceptions():
    self.gen.throw(typ, value, traceback)
  File "/root/smc-bot/venv/lib/python3.11/site-packages/httpx/_transports/default.py", line 118, in map_httpcore_exceptions
[ERROR] 
Traceback (most recent call last):
  File "/root/smc-bot/venv/lib/python3.11/site-packages/httpx/_transports/default.py", line 101, in map_httpcore_exceptions
    with map_exceptions(exc_map):
    self.gen.throw(typ, value, traceback)
  File "/root/smc-bot/venv/lib/python3.11/site-packages/httpcore/_exceptions.py", line 14, in map_exceptions
The above exception was the direct cause of the following exception:
Traceback (most recent call last):
    with map_httpcore_exceptions():
    self.gen.throw(typ, value, traceback)
  File "/root/smc-bot/venv/lib/python3.11/site-packages/httpx/_transports/default.py", line 118, in map_httpcore_exceptions
```

## Last 100 Log Lines
```
  diag: trend=bearish skip=atr_low ratio=0.75 min=0.8
[04:04:56] tick balance=$312.71
  diag: trend=bearish skip=atr_low ratio=0.76 min=0.8
[04:05:58] tick balance=$312.71
  diag: trend=bearish skip=atr_low ratio=0.74 min=0.8
[04:07:01] tick balance=$312.71
  diag: trend=bearish skip=atr_low ratio=0.75 min=0.8
[04:08:03] tick balance=$312.71
  diag: trend=bearish skip=atr_low ratio=0.75 min=0.8
[04:09:05] tick balance=$312.71
  diag: trend=bearish skip=atr_low ratio=0.76 min=0.8
[04:10:06] tick balance=$312.71
  diag: trend=bearish skip=atr_low ratio=0.77 min=0.8
[04:11:09] tick balance=$312.71
  diag: trend=bearish skip=atr_low ratio=0.78 min=0.8
[04:12:10] tick balance=$312.71
  diag: trend=bearish skip=atr_low ratio=0.8 min=0.8
[04:13:12] tick balance=$312.71
  diag: trend=bearish atr_ratio=0.82 obs=10 obs_fresh=9 fvgs=7 bos=24 sigs=0 wrong_side=5 price_out=3 bos_miss=0 risk_neg=0 liquidity_trap=1 near_gap_pct=-0.24
[04:14:14] tick balance=$312.71
[!] Signal score 0.7 < 0.9, skipping: Short: Pure OB + BOS
  diag: trend=bearish atr_ratio=0.85 obs=10 obs_fresh=9 fvgs=7 bos=24 sigs=1 wrong_side=3 price_out=2 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=-0.123 skip=low_score score=0.7
[04:15:17] tick balance=$312.71
  diag: trend=bearish atr_ratio=0.87 obs=11 obs_fresh=9 fvgs=8 bos=24 sigs=0 wrong_side=5 price_out=2 bos_miss=0 risk_neg=0 liquidity_trap=2 near_gap_pct=0.205
[04:16:18] tick balance=$312.71
  diag: trend=bearish atr_ratio=0.88 obs=10 obs_fresh=8 fvgs=8 bos=24 sigs=0 wrong_side=5 price_out=2 bos_miss=0 risk_neg=0 liquidity_trap=1 near_gap_pct=0.339
[04:17:21] tick balance=$312.71
  diag: trend=bearish atr_ratio=0.89 obs=10 obs_fresh=8 fvgs=8 bos=25 sigs=0 wrong_side=5 price_out=2 bos_miss=0 risk_neg=0 liquidity_trap=1 near_gap_pct=0.311
[04:18:22] tick balance=$312.71
  diag: trend=bearish atr_ratio=0.9 obs=10 obs_fresh=8 fvgs=7 bos=25 sigs=0 wrong_side=5 price_out=2 bos_miss=0 risk_neg=0 liquidity_trap=1 near_gap_pct=0.266
[04:19:24] tick balance=$312.71
  diag: trend=bearish atr_ratio=0.9 obs=10 obs_fresh=8 fvgs=7 bos=25 sigs=0 wrong_side=5 price_out=2 bos_miss=0 risk_neg=0 liquidity_trap=1 near_gap_pct=0.302
[04:20:26] tick balance=$312.71
  diag: trend=bearish atr_ratio=0.88 obs=11 obs_fresh=9 fvgs=7 bos=25 sigs=0 wrong_side=5 price_out=2 bos_miss=0 risk_neg=0 liquidity_trap=2 near_gap_pct=0.105
[04:21:28] tick balance=$312.71
  diag: trend=bearish atr_ratio=0.89 obs=11 obs_fresh=9 fvgs=7 bos=25 sigs=0 wrong_side=5 price_out=2 bos_miss=0 risk_neg=0 liquidity_trap=2 near_gap_pct=0.135
[04:22:30] tick balance=$312.71
  diag: trend=bearish atr_ratio=0.89 obs=11 obs_fresh=9 fvgs=7 bos=25 sigs=0 wrong_side=5 price_out=2 bos_miss=0 risk_neg=0 liquidity_trap=2 near_gap_pct=0.128
[04:23:32] tick balance=$312.71
  diag: trend=bearish atr_ratio=0.89 obs=11 obs_fresh=9 fvgs=7 bos=24 sigs=0 wrong_side=5 price_out=2 bos_miss=0 risk_neg=0 liquidity_trap=2 near_gap_pct=0.107
[04:24:34] tick balance=$312.71
  diag: trend=bearish atr_ratio=0.9 obs=11 obs_fresh=9 fvgs=7 bos=24 sigs=0 wrong_side=5 price_out=2 bos_miss=0 risk_neg=0 liquidity_trap=2 near_gap_pct=0.041
[04:25:36] tick balance=$312.71
  diag: trend=bearish atr_ratio=0.9 obs=11 obs_fresh=9 fvgs=7 bos=24 sigs=0 wrong_side=5 price_out=2 bos_miss=0 risk_neg=0 liquidity_trap=2 near_gap_pct=0.061
[04:26:38] tick balance=$312.71
  diag: trend=bearish atr_ratio=0.91 obs=11 obs_fresh=9 fvgs=7 bos=24 sigs=0 wrong_side=5 price_out=2 bos_miss=0 risk_neg=0 liquidity_trap=2 near_gap_pct=0.07
[04:27:40] tick balance=$312.71
  diag: trend=bearish atr_ratio=0.91 obs=11 obs_fresh=9 fvgs=7 bos=24 sigs=0 wrong_side=5 price_out=2 bos_miss=0 risk_neg=0 liquidity_trap=2 near_gap_pct=0.024
[04:28:42] tick balance=$312.71
  diag: trend=bearish atr_ratio=0.92 obs=12 obs_fresh=10 fvgs=7 bos=24 sigs=0 wrong_side=6 price_out=2 bos_miss=0 risk_neg=0 liquidity_trap=2 near_gap_pct=-0.007
[04:29:45] tick balance=$312.71
  diag: trend=bearish atr_ratio=0.92 obs=11 obs_fresh=9 fvgs=7 bos=23 sigs=0 wrong_side=5 price_out=2 bos_miss=0 risk_neg=0 liquidity_trap=2 near_gap_pct=0.029
[04:30:47] tick balance=$312.71
  diag: trend=bearish atr_ratio=0.93 obs=11 obs_fresh=9 fvgs=7 bos=23 sigs=0 wrong_side=5 price_out=2 bos_miss=0 risk_neg=0 liquidity_trap=2 near_gap_pct=0.007
[04:31:49] tick balance=$312.71
  diag: trend=bearish atr_ratio=0.94 obs=11 obs_fresh=9 fvgs=7 bos=23 sigs=0 wrong_side=5 price_out=2 bos_miss=0 risk_neg=0 liquidity_trap=2 near_gap_pct=0.042
[04:32:51] tick balance=$312.71
  diag: trend=bearish atr_ratio=0.94 obs=11 obs_fresh=9 fvgs=7 bos=24 sigs=0 wrong_side=5 price_out=2 bos_miss=0 risk_neg=0 liquidity_trap=2 near_gap_pct=0.041
[04:33:53] tick balance=$312.71
  diag: trend=bearish atr_ratio=0.95 obs=11 obs_fresh=9 fvgs=7 bos=24 sigs=0 wrong_side=5 price_out=2 bos_miss=0 risk_neg=0 liquidity_trap=2 near_gap_pct=0.041
[04:34:55] tick balance=$312.71
  diag: trend=bearish atr_ratio=0.95 obs=11 obs_fresh=9 fvgs=7 bos=24 sigs=0 wrong_side=5 price_out=2 bos_miss=0 risk_neg=0 liquidity_trap=2 near_gap_pct=0.045
[04:35:58] tick balance=$312.71
  diag: trend=bearish atr_ratio=0.96 obs=11 obs_fresh=9 fvgs=6 bos=24 sigs=0 wrong_side=5 price_out=2 bos_miss=0 risk_neg=0 liquidity_trap=2 near_gap_pct=-0.001
[04:36:59] tick balance=$312.71
  diag: trend=bearish atr_ratio=0.97 obs=11 obs_fresh=9 fvgs=6 bos=24 sigs=0 wrong_side=5 price_out=2 bos_miss=0 risk_neg=0 liquidity_trap=2 near_gap_pct=-0.063
[04:38:01] tick balance=$312.71
  diag: trend=bearish atr_ratio=0.97 obs=11 obs_fresh=9 fvgs=6 bos=24 sigs=0 wrong_side=5 price_out=2 bos_miss=0 risk_neg=0 liquidity_trap=2 near_gap_pct=-0.038
[04:39:04] tick balance=$312.71
  diag: trend=bearish atr_ratio=0.97 obs=11 obs_fresh=9 fvgs=6 bos=25 sigs=0 wrong_side=5 price_out=2 bos_miss=0 risk_neg=0 liquidity_trap=2 near_gap_pct=-0.018
[04:40:06] tick balance=$312.71
  diag: trend=bearish atr_ratio=0.83 obs=11 obs_fresh=9 fvgs=6 bos=25 sigs=0 wrong_side=5 price_out=2 bos_miss=0 risk_neg=0 liquidity_trap=2 near_gap_pct=-0.03
[04:41:08] tick balance=$312.71
  diag: trend=bearish atr_ratio=0.83 obs=11 obs_fresh=9 fvgs=6 bos=25 sigs=0 wrong_side=5 price_out=2 bos_miss=0 risk_neg=0 liquidity_trap=2 near_gap_pct=-0.05
[04:42:10] tick balance=$312.71
  diag: trend=bearish atr_ratio=0.85 obs=11 obs_fresh=9 fvgs=6 bos=25 sigs=0 wrong_side=5 price_out=2 bos_miss=0 risk_neg=0 liquidity_trap=2 near_gap_pct=0.015
[04:43:11] tick balance=$312.71
  diag: trend=bearish atr_ratio=0.86 obs=11 obs_fresh=9 fvgs=6 bos=25 sigs=0 wrong_side=5 price_out=2 bos_miss=0 risk_neg=0 liquidity_trap=2 near_gap_pct=0.018
[04:44:14] tick balance=$312.71
  diag: trend=bearish atr_ratio=0.86 obs=11 obs_fresh=9 fvgs=6 bos=25 sigs=0 wrong_side=5 price_out=2 bos_miss=0 risk_neg=0 liquidity_trap=2 near_gap_pct=0.031
[04:45:16] tick balance=$312.71
  diag: trend=bearish atr_ratio=0.82 obs=11 obs_fresh=9 fvgs=6 bos=25 sigs=0 wrong_side=5 price_out=2 bos_miss=0 risk_neg=0 liquidity_trap=2 near_gap_pct=-0.041
[04:46:17] tick balance=$312.71
  diag: trend=bearish atr_ratio=0.83 obs=11 obs_fresh=9 fvgs=6 bos=26 sigs=0 wrong_side=5 price_out=2 bos_miss=0 risk_neg=0 liquidity_trap=2 near_gap_pct=-0.004
[04:47:19] tick balance=$312.71
  diag: trend=bearish atr_ratio=0.84 obs=12 obs_fresh=10 fvgs=6 bos=26 sigs=0 wrong_side=5 price_out=2 bos_miss=0 risk_neg=0 liquidity_trap=3 near_gap_pct=0.003
[04:48:22] tick balance=$312.71
  diag: trend=bearish atr_ratio=0.85 obs=11 obs_fresh=9 fvgs=6 bos=26 sigs=0 wrong_side=5 price_out=2 bos_miss=0 risk_neg=0 liquidity_trap=2 near_gap_pct=0.008
[04:49:24] tick balance=$312.71
  diag: trend=bearish atr_ratio=0.85 obs=11 obs_fresh=9 fvgs=6 bos=25 sigs=0 wrong_side=5 price_out=2 bos_miss=0 risk_neg=0 liquidity_trap=2 near_gap_pct=-0.012
[04:50:26] tick balance=$312.71
  diag: trend=bearish atr_ratio=0.8 obs=11 obs_fresh=9 fvgs=6 bos=25 sigs=0 wrong_side=5 price_out=2 bos_miss=0 risk_neg=0 liquidity_trap=2 near_gap_pct=-0.006
[04:51:28] tick balance=$312.71
  diag: trend=bearish atr_ratio=0.8 obs=11 obs_fresh=9 fvgs=6 bos=25 sigs=0 wrong_side=5 price_out=2 bos_miss=0 risk_neg=0 liquidity_trap=2 near_gap_pct=-0.022
[04:52:30] tick balance=$312.71
  diag: trend=bearish atr_ratio=0.8 obs=11 obs_fresh=9 fvgs=6 bos=25 sigs=0 wrong_side=5 price_out=2 bos_miss=0 risk_neg=0 liquidity_trap=2 near_gap_pct=0.007
[04:53:32] tick balance=$312.71
  diag: trend=bearish atr_ratio=0.8 obs=11 obs_fresh=9 fvgs=6 bos=25 sigs=0 wrong_side=5 price_out=2 bos_miss=0 risk_neg=0 liquidity_trap=2 near_gap_pct=0.021
[04:54:35] tick balance=$312.71
  diag: trend=bearish atr_ratio=0.81 obs=11 obs_fresh=9 fvgs=6 bos=25 sigs=0 wrong_side=5 price_out=2 bos_miss=0 risk_neg=0 liquidity_trap=2 near_gap_pct=0.012
```
