# Bot Snapshot — 2026-04-16 14:55 UTC

## Service: active
balance=$366.80

## Config
POST_CLOSE_COOLDOWN: int = 180 # 3 мин техническая пауза после закрытия
RISK_PCT: float = 0.05 # 5% от баланса на сделку
ADX_MIN: float = 20.0 # ADX < 20 → choppy market, skip entry

## Trades (last 20)
```
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
2|SELL|73451.8|13.15|closed|2026-04-11 20:18:03|2026-04-12 08:14:54
1|SELL|73575.9|13.15|closed|2026-04-11 20:01:37|2026-04-12 08:14:54
```

## Daily PnL
```
2026-04-16|381.29|-14.48|0
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
    109 trend_htf=ranging trend_mid=ranging skip=trend_mismatch
      2 trend=bearish atr_ratio=1.19 obs=10 obs_fresh=9 fvgs=12 bos=19 sigs=0 wrong_side=4 price_out=1 bos_miss=0 risk_neg=0 liquidity_trap=4 near_gap_pct=0.36
      2 trend=bearish atr_ratio=1.02 obs=9 obs_fresh=8 fvgs=11 bos=21 sigs=0 wrong_side=4 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=4 near_gap_pct=0.387
      2 trend=bearish atr_ratio=0.93 obs=9 obs_fresh=8 fvgs=11 bos=22 sigs=0 wrong_side=4 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=4 near_gap_pct=0.361
      1 trend=bearish atr_ratio=2.0 obs=7 obs_fresh=6 fvgs=16 bos=27 sigs=0 wrong_side=2 price_out=3 bos_miss=0 risk_neg=0 liquidity_trap=1 near_gap_pct=-0.439
      1 trend=bearish atr_ratio=1.9 obs=7 obs_fresh=7 fvgs=16 bos=26 sigs=0 wrong_side=3 price_out=4 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=-0.625
      1 trend=bearish atr_ratio=1.9 obs=6 obs_fresh=6 fvgs=17 bos=27 sigs=0 wrong_side=2 price_out=3 bos_miss=0 risk_neg=0 liquidity_trap=1 near_gap_pct=-0.387
      1 trend=bearish atr_ratio=1.9 obs=6 obs_fresh=5 fvgs=15 bos=28 sigs=0 wrong_side=1 price_out=3 bos_miss=0 risk_neg=0 liquidity_trap=1 near_gap_pct=0.098
      1 trend=bearish atr_ratio=1.9 obs=5 obs_fresh=4 fvgs=14 bos=29 sigs=0 wrong_side=1 price_out=3 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=1.427
      1 trend=bearish atr_ratio=1.9 obs=5 obs_fresh=4 fvgs=14 bos=28 sigs=0 wrong_side=1 price_out=3 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=1.41
      1 trend=bearish atr_ratio=1.99 obs=7 obs_fresh=6 fvgs=17 bos=28 sigs=0 wrong_side=2 price_out=3 bos_miss=0 risk_neg=0 liquidity_trap=1 near_gap_pct=-0.437
      1 trend=bearish atr_ratio=1.99 obs=7 obs_fresh=6 fvgs=17 bos=27 sigs=0 wrong_side=2 price_out=3 bos_miss=0 risk_neg=0 liquidity_trap=1 near_gap_pct=-0.456
      1 trend=bearish atr_ratio=1.99 obs=7 obs_fresh=6 fvgs=17 bos=27 sigs=0 wrong_side=2 price_out=3 bos_miss=0 risk_neg=0 liquidity_trap=1 near_gap_pct=-0.41
      1 trend=bearish atr_ratio=1.99 obs=7 obs_fresh=6 fvgs=16 bos=28 sigs=0 wrong_side=2 price_out=3 bos_miss=0 risk_neg=0 liquidity_trap=1 near_gap_pct=-0.355
      1 trend=bearish atr_ratio=1.99 obs=7 obs_fresh=6 fvgs=16 bos=28 sigs=0 wrong_side=2 price_out=3 bos_miss=0 risk_neg=0 liquidity_trap=1 near_gap_pct=-0.316
      1 trend=bearish atr_ratio=1.99 obs=7 obs_fresh=6 fvgs=16 bos=28 sigs=0 wrong_side=2 price_out=3 bos_miss=0 risk_neg=0 liquidity_trap=1 near_gap_pct=-0.293
      1 trend=bearish atr_ratio=1.98 obs=7 obs_fresh=6 fvgs=17 bos=28 sigs=0 wrong_side=2 price_out=3 bos_miss=0 risk_neg=0 liquidity_trap=1 near_gap_pct=-0.381
      1 trend=bearish atr_ratio=1.98 obs=7 obs_fresh=6 fvgs=17 bos=27 sigs=0 wrong_side=2 price_out=3 bos_miss=0 risk_neg=0 liquidity_trap=1 near_gap_pct=-0.355
      1 trend=bearish atr_ratio=1.96 obs=6 obs_fresh=5 fvgs=16 bos=29 sigs=0 wrong_side=1 price_out=3 bos_miss=0 risk_neg=0 liquidity_trap=1 near_gap_pct=-0.226
      1 trend=bearish atr_ratio=1.96 obs=6 obs_fresh=5 fvgs=15 bos=29 sigs=0 wrong_side=1 price_out=3 bos_miss=0 risk_neg=0 liquidity_trap=1 near_gap_pct=-0.206
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
[16:03:16] tick balance=$366.80
  diag: trend=bearish atr_ratio=1.74 obs=5 obs_fresh=4 fvgs=14 bos=29 sigs=0 wrong_side=1 price_out=3 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=1.322
[16:04:17] tick balance=$366.80
  diag: trend=bearish atr_ratio=1.74 obs=5 obs_fresh=4 fvgs=14 bos=29 sigs=0 wrong_side=1 price_out=3 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=1.318
[16:05:19] tick balance=$366.80
  diag: trend=bearish atr_ratio=1.74 obs=5 obs_fresh=4 fvgs=14 bos=29 sigs=0 wrong_side=1 price_out=3 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=1.372
[16:06:22] tick balance=$366.80
  diag: trend=bearish atr_ratio=1.76 obs=5 obs_fresh=4 fvgs=14 bos=29 sigs=0 wrong_side=1 price_out=3 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=1.246
[16:07:23] tick balance=$366.80
  diag: trend=bearish atr_ratio=1.78 obs=5 obs_fresh=4 fvgs=14 bos=29 sigs=0 wrong_side=1 price_out=3 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=1.148
[16:08:25] tick balance=$366.80
  diag: trend=bearish atr_ratio=1.81 obs=5 obs_fresh=4 fvgs=14 bos=29 sigs=0 wrong_side=1 price_out=3 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=0.993
[16:09:27] tick balance=$366.80
  diag: trend=bearish atr_ratio=1.81 obs=5 obs_fresh=4 fvgs=14 bos=29 sigs=0 wrong_side=1 price_out=3 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=1.063
[16:10:28] tick balance=$366.80
  diag: trend=bearish atr_ratio=1.8 obs=5 obs_fresh=4 fvgs=14 bos=29 sigs=0 wrong_side=1 price_out=3 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=0.981
[16:11:29] tick balance=$366.80
  diag: trend=bearish atr_ratio=1.81 obs=5 obs_fresh=4 fvgs=14 bos=29 sigs=0 wrong_side=1 price_out=3 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=1.05
[16:12:32] tick balance=$366.80
  diag: trend=bearish atr_ratio=1.82 obs=5 obs_fresh=4 fvgs=14 bos=30 sigs=0 wrong_side=1 price_out=3 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=1.081
[16:13:34] tick balance=$366.80
  diag: trend=bearish atr_ratio=1.82 obs=5 obs_fresh=4 fvgs=14 bos=30 sigs=0 wrong_side=1 price_out=3 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=1.078
[16:14:35] tick balance=$366.80
  diag: trend=bearish atr_ratio=1.82 obs=5 obs_fresh=4 fvgs=14 bos=30 sigs=0 wrong_side=1 price_out=3 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=1.128
[16:15:37] tick balance=$366.80
  diag: trend=bearish atr_ratio=1.82 obs=5 obs_fresh=4 fvgs=14 bos=30 sigs=0 wrong_side=1 price_out=3 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=1.057
[16:16:39] tick balance=$366.80
  diag: trend=bearish atr_ratio=1.84 obs=5 obs_fresh=4 fvgs=14 bos=30 sigs=0 wrong_side=1 price_out=3 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=1.252
[16:17:41] tick balance=$366.80
  diag: trend=bearish atr_ratio=1.86 obs=5 obs_fresh=4 fvgs=14 bos=29 sigs=0 wrong_side=1 price_out=3 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=1.376
[16:18:43] tick balance=$366.80
  diag: trend=bearish atr_ratio=1.9 obs=5 obs_fresh=4 fvgs=14 bos=29 sigs=0 wrong_side=1 price_out=3 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=1.427
[16:19:44] tick balance=$366.80
  diag: trend=bearish atr_ratio=1.9 obs=5 obs_fresh=4 fvgs=14 bos=28 sigs=0 wrong_side=1 price_out=3 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=1.41
[16:20:46] tick balance=$366.80
  diag: trend=bearish atr_ratio=1.9 obs=6 obs_fresh=5 fvgs=15 bos=28 sigs=0 wrong_side=1 price_out=3 bos_miss=0 risk_neg=0 liquidity_trap=1 near_gap_pct=0.098
[16:21:47] tick balance=$366.80
  diag: trend=bearish atr_ratio=1.91 obs=6 obs_fresh=5 fvgs=15 bos=28 sigs=0 wrong_side=1 price_out=3 bos_miss=0 risk_neg=0 liquidity_trap=1 near_gap_pct=0.038
[16:22:49] tick balance=$366.80
  diag: trend=bearish atr_ratio=1.91 obs=6 obs_fresh=5 fvgs=15 bos=28 sigs=0 wrong_side=1 price_out=3 bos_miss=0 risk_neg=0 liquidity_trap=1 near_gap_pct=0.136
[16:23:51] tick balance=$366.80
  diag: trend=bearish atr_ratio=1.92 obs=6 obs_fresh=5 fvgs=15 bos=28 sigs=0 wrong_side=1 price_out=3 bos_miss=0 risk_neg=0 liquidity_trap=1 near_gap_pct=0.179
[16:24:53] tick balance=$366.80
  diag: trend=bearish atr_ratio=1.93 obs=6 obs_fresh=5 fvgs=15 bos=28 sigs=0 wrong_side=1 price_out=3 bos_miss=0 risk_neg=0 liquidity_trap=1 near_gap_pct=0.128
[16:25:55] tick balance=$366.80
  diag: trend=bearish atr_ratio=1.91 obs=6 obs_fresh=5 fvgs=15 bos=28 sigs=0 wrong_side=1 price_out=3 bos_miss=0 risk_neg=0 liquidity_trap=1 near_gap_pct=0.056
[16:26:57] tick balance=$366.80
  diag: trend=bearish atr_ratio=1.92 obs=6 obs_fresh=5 fvgs=15 bos=29 sigs=0 wrong_side=1 price_out=3 bos_miss=0 risk_neg=0 liquidity_trap=1 near_gap_pct=0.071
[16:28:00] tick balance=$366.80
  diag: trend=bearish atr_ratio=1.92 obs=6 obs_fresh=5 fvgs=15 bos=29 sigs=0 wrong_side=1 price_out=3 bos_miss=0 risk_neg=0 liquidity_trap=1 near_gap_pct=0.014
[16:29:02] tick balance=$366.80
  diag: trend=bearish atr_ratio=1.96 obs=6 obs_fresh=5 fvgs=15 bos=29 sigs=0 wrong_side=1 price_out=3 bos_miss=0 risk_neg=0 liquidity_trap=1 near_gap_pct=-0.206
[16:30:04] tick balance=$366.80
  diag: trend=bearish atr_ratio=1.96 obs=6 obs_fresh=5 fvgs=16 bos=29 sigs=0 wrong_side=1 price_out=3 bos_miss=0 risk_neg=0 liquidity_trap=1 near_gap_pct=-0.226
[16:31:07] tick balance=$366.80
  diag: trend=bearish atr_ratio=1.99 obs=7 obs_fresh=6 fvgs=16 bos=28 sigs=0 wrong_side=2 price_out=3 bos_miss=0 risk_neg=0 liquidity_trap=1 near_gap_pct=-0.355
[16:32:09] tick balance=$366.80
  diag: trend=bearish atr_ratio=1.99 obs=7 obs_fresh=6 fvgs=16 bos=28 sigs=0 wrong_side=2 price_out=3 bos_miss=0 risk_neg=0 liquidity_trap=1 near_gap_pct=-0.293
[16:33:11] tick balance=$366.80
  diag: trend=bearish atr_ratio=1.99 obs=7 obs_fresh=6 fvgs=16 bos=28 sigs=0 wrong_side=2 price_out=3 bos_miss=0 risk_neg=0 liquidity_trap=1 near_gap_pct=-0.316
[16:34:12] tick balance=$366.80
  diag: trend=bearish atr_ratio=2.0 obs=7 obs_fresh=6 fvgs=16 bos=27 sigs=0 wrong_side=2 price_out=3 bos_miss=0 risk_neg=0 liquidity_trap=1 near_gap_pct=-0.439
[16:35:15] tick balance=$366.80
  diag: trend=bearish atr_ratio=1.98 obs=7 obs_fresh=6 fvgs=17 bos=27 sigs=0 wrong_side=2 price_out=3 bos_miss=0 risk_neg=0 liquidity_trap=1 near_gap_pct=-0.355
[16:36:17] tick balance=$366.80
  diag: trend=bearish atr_ratio=1.98 obs=7 obs_fresh=6 fvgs=17 bos=28 sigs=0 wrong_side=2 price_out=3 bos_miss=0 risk_neg=0 liquidity_trap=1 near_gap_pct=-0.381
[16:37:19] tick balance=$366.80
  diag: trend=bearish atr_ratio=1.99 obs=7 obs_fresh=6 fvgs=17 bos=28 sigs=0 wrong_side=2 price_out=3 bos_miss=0 risk_neg=0 liquidity_trap=1 near_gap_pct=-0.437
[16:38:23] tick balance=$366.80
  diag: trend=bearish atr_ratio=1.99 obs=7 obs_fresh=6 fvgs=17 bos=27 sigs=0 wrong_side=2 price_out=3 bos_miss=0 risk_neg=0 liquidity_trap=1 near_gap_pct=-0.456
[16:39:26] tick balance=$366.80
  diag: trend=bearish atr_ratio=1.99 obs=7 obs_fresh=6 fvgs=17 bos=27 sigs=0 wrong_side=2 price_out=3 bos_miss=0 risk_neg=0 liquidity_trap=1 near_gap_pct=-0.41
[16:40:33] tick balance=$366.80
  diag: trend=bearish atr_ratio=1.9 obs=6 obs_fresh=6 fvgs=17 bos=27 sigs=0 wrong_side=2 price_out=3 bos_miss=0 risk_neg=0 liquidity_trap=1 near_gap_pct=-0.387
[16:41:40] tick balance=$366.80
  diag: trend=bearish atr_ratio=1.91 obs=6 obs_fresh=6 fvgs=17 bos=27 sigs=0 wrong_side=2 price_out=3 bos_miss=0 risk_neg=0 liquidity_trap=1 near_gap_pct=-0.376
[16:42:43] tick balance=$366.80
  diag: trend=bearish atr_ratio=1.91 obs=6 obs_fresh=6 fvgs=17 bos=26 sigs=0 wrong_side=2 price_out=3 bos_miss=0 risk_neg=0 liquidity_trap=1 near_gap_pct=-0.37
[16:43:46] tick balance=$366.80
  diag: trend=bearish atr_ratio=1.92 obs=6 obs_fresh=6 fvgs=17 bos=26 sigs=0 wrong_side=2 price_out=4 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=-0.484
[16:44:48] tick balance=$366.80
  diag: trend=bearish atr_ratio=1.94 obs=6 obs_fresh=6 fvgs=17 bos=26 sigs=0 wrong_side=2 price_out=3 bos_miss=0 risk_neg=0 liquidity_trap=1 near_gap_pct=-0.441
[16:45:51] tick balance=$366.80
  diag: trend=bearish atr_ratio=1.88 obs=7 obs_fresh=7 fvgs=16 bos=26 sigs=0 wrong_side=3 price_out=4 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=-0.558
[16:46:53] tick balance=$366.80
  diag: trend=bearish atr_ratio=1.88 obs=7 obs_fresh=7 fvgs=16 bos=27 sigs=0 wrong_side=3 price_out=4 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=-0.522
[16:47:55] tick balance=$366.80
  diag: trend=bearish atr_ratio=1.88 obs=7 obs_fresh=7 fvgs=16 bos=27 sigs=0 wrong_side=3 price_out=4 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=-0.495
[16:48:57] tick balance=$366.80
  diag: trend=bearish atr_ratio=1.88 obs=7 obs_fresh=7 fvgs=16 bos=26 sigs=0 wrong_side=3 price_out=4 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=-0.501
[16:49:59] tick balance=$366.80
  diag: trend=bearish atr_ratio=1.9 obs=7 obs_fresh=7 fvgs=16 bos=26 sigs=0 wrong_side=3 price_out=4 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=-0.625
[16:51:00] tick balance=$366.80
  diag: trend=bearish atr_ratio=1.84 obs=7 obs_fresh=7 fvgs=15 bos=27 sigs=0 wrong_side=3 price_out=4 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=-0.61
[16:52:02] tick balance=$366.80
  diag: trend=bearish atr_ratio=1.86 obs=7 obs_fresh=7 fvgs=15 bos=25 sigs=0 wrong_side=3 price_out=3 bos_miss=0 risk_neg=0 liquidity_trap=1 near_gap_pct=-0.742
[16:53:04] tick balance=$366.80
  diag: trend=bearish atr_ratio=1.87 obs=7 obs_fresh=7 fvgs=15 bos=26 sigs=0 wrong_side=3 price_out=4 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=-0.531
[16:54:06] tick balance=$366.80
  diag: trend=bearish atr_ratio=1.87 obs=7 obs_fresh=7 fvgs=15 bos=26 sigs=0 wrong_side=3 price_out=4 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=-0.505
```
