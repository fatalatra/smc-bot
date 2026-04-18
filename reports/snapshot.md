# Bot Snapshot — 2026-04-18 14:55 UTC

## Service: active
balance=$351.02

## Config
POST_CLOSE_COOLDOWN: int = 180 # 3 мин техническая пауза после закрытия
RISK_PCT: float = 0.05 # 5% от баланса на сделку
ADX_MIN: float = 20.0 # ADX < 20 → choppy market, skip entry

## Trades (last 20)
```
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
6|SELL|70977.6|16.89|closed|2026-04-12 13:15:20|2026-04-12 14:43:04
5|SELL|71364.3|13.27|closed|2026-04-12 10:57:04|2026-04-12 13:01:46
4|SELL|71492.1|13.27|closed|2026-04-12 10:41:17|2026-04-12 10:42:19
```

## Daily PnL
```
2026-04-18|311.88|39.13|0
2026-04-17|328.7|-16.81|0
2026-04-16|381.29|-52.59|0
2026-04-15|363.1|17.9|0
2026-04-14|413.74|-50.64|0
2026-04-13|413.74|0.0|0
2026-04-12|423.86|-10.12|0
```

## Open Positions
```
none
```

## Diag Summary (last ~4h)
```
      9 trend=bearish skip=atr_low ratio=0.79 min=0.8
      7 trend_htf=ranging trend_mid=ranging skip=trend_mismatch
      6 trend=bearish skip=atr_low ratio=0.75 min=0.8
      3 trend=bearish skip=atr_low ratio=0.8 min=0.8
      2 trend=bearish skip=atr_low ratio=0.76 min=0.8
      2 trend=bearish skip=atr_low ratio=0.74 min=0.8
      2 trend=bearish skip=atr_low ratio=0.73 min=0.8
      2 trend=bearish atr_ratio=0.88 obs=9 obs_fresh=6 fvgs=15 bos=30 sigs=0 wrong_side=4 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=2 near_gap_pct=-0.045
      1 trend=bearish skip=atr_low ratio=0.78 min=0.8
      1 trend=bearish atr_ratio=1.1 obs=9 obs_fresh=6 fvgs=15 bos=29 sigs=0 wrong_side=4 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=2 near_gap_pct=-0.023
      1 trend=bearish atr_ratio=1.1 obs=8 obs_fresh=5 fvgs=16 bos=26 sigs=0 wrong_side=4 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=1 near_gap_pct=-0.051
      1 trend=bearish atr_ratio=1.1 obs=11 obs_fresh=9 fvgs=13 bos=26 sigs=0 wrong_side=5 price_out=4 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=1.041
      1 trend=bearish atr_ratio=1.1 obs=11 obs_fresh=9 fvgs=13 bos=26 sigs=0 wrong_side=5 price_out=4 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=1.024
      1 trend=bearish atr_ratio=1.1 obs=11 obs_fresh=9 fvgs=13 bos=26 sigs=0 wrong_side=5 price_out=4 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=1.021
      1 trend=bearish atr_ratio=1.13 obs=9 obs_fresh=6 fvgs=16 bos=26 sigs=0 wrong_side=4 price_out=2 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=-0.09
      1 trend=bearish atr_ratio=1.13 obs=9 obs_fresh=6 fvgs=16 bos=26 sigs=0 wrong_side=4 price_out=1 bos_miss=0 risk_neg=0 liquidity_trap=1 near_gap_pct=-0.045
      1 trend=bearish atr_ratio=1.12 obs=9 obs_fresh=6 fvgs=16 bos=26 sigs=0 wrong_side=4 price_out=2 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=-0.111
      1 trend=bearish atr_ratio=1.12 obs=9 obs_fresh=6 fvgs=16 bos=26 sigs=0 wrong_side=4 price_out=1 bos_miss=0 risk_neg=0 liquidity_trap=1 near_gap_pct=-0.074
      1 trend=bearish atr_ratio=1.12 obs=9 obs_fresh=6 fvgs=16 bos=25 sigs=0 wrong_side=4 price_out=2 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=-0.083
      1 trend=bearish atr_ratio=1.12 obs=9 obs_fresh=6 fvgs=15 bos=27 sigs=0 wrong_side=4 price_out=2 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=-0.09
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
[16:03:25] tick balance=$351.02
  diag: trend=bearish atr_ratio=0.89 obs=9 obs_fresh=7 fvgs=16 bos=28 sigs=0 wrong_side=3 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=4 near_gap_pct=0.013
[16:04:27] tick balance=$351.02
  diag: trend=bearish atr_ratio=0.89 obs=9 obs_fresh=7 fvgs=16 bos=27 sigs=0 wrong_side=3 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=4 near_gap_pct=0.012
[16:05:30] tick balance=$351.02
  diag: trend=bearish atr_ratio=0.87 obs=8 obs_fresh=7 fvgs=15 bos=27 sigs=0 wrong_side=3 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=4 near_gap_pct=0.048
[16:06:32] tick balance=$351.02
  diag: trend=bearish atr_ratio=0.88 obs=8 obs_fresh=7 fvgs=15 bos=27 sigs=0 wrong_side=3 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=4 near_gap_pct=0.048
[16:07:34] tick balance=$351.02
  diag: trend=bearish atr_ratio=0.88 obs=8 obs_fresh=7 fvgs=15 bos=27 sigs=0 wrong_side=3 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=4 near_gap_pct=0.008
[16:08:36] tick balance=$351.02
  diag: trend=bearish atr_ratio=0.88 obs=8 obs_fresh=7 fvgs=15 bos=28 sigs=0 wrong_side=3 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=4 near_gap_pct=-0.008
[16:09:38] tick balance=$351.02
  diag: trend=bearish atr_ratio=0.9 obs=8 obs_fresh=7 fvgs=15 bos=28 sigs=0 wrong_side=3 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=4 near_gap_pct=0.01
[16:10:40] tick balance=$351.02
  diag: trend=bearish atr_ratio=0.89 obs=8 obs_fresh=7 fvgs=14 bos=28 sigs=0 wrong_side=3 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=4 near_gap_pct=-0.017
[16:11:42] tick balance=$351.02
  diag: trend=bearish atr_ratio=0.89 obs=8 obs_fresh=7 fvgs=14 bos=28 sigs=0 wrong_side=3 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=4 near_gap_pct=-0.016
[16:12:44] tick balance=$351.02
  diag: trend=bearish atr_ratio=0.89 obs=8 obs_fresh=7 fvgs=14 bos=27 sigs=0 wrong_side=3 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=4 near_gap_pct=-0.015
[16:13:46] tick balance=$351.02
  diag: trend=bearish atr_ratio=0.9 obs=8 obs_fresh=7 fvgs=14 bos=27 sigs=0 wrong_side=3 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=4 near_gap_pct=-0.018
[16:14:50] tick balance=$351.02
  diag: trend=bearish atr_ratio=0.91 obs=8 obs_fresh=7 fvgs=14 bos=27 sigs=0 wrong_side=3 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=4 near_gap_pct=-0.056
[16:15:52] tick balance=$351.02
  diag: trend=bearish atr_ratio=0.91 obs=8 obs_fresh=7 fvgs=14 bos=27 sigs=0 wrong_side=3 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=4 near_gap_pct=-0.053
[16:16:55] tick balance=$351.02
  diag: trend=bearish atr_ratio=0.92 obs=8 obs_fresh=7 fvgs=14 bos=27 sigs=0 wrong_side=3 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=4 near_gap_pct=-0.055
[16:17:57] tick balance=$351.02
  diag: trend=bearish atr_ratio=0.92 obs=8 obs_fresh=7 fvgs=14 bos=27 sigs=0 wrong_side=3 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=4 near_gap_pct=-0.057
[16:18:59] tick balance=$351.02
  diag: trend=bearish atr_ratio=0.92 obs=8 obs_fresh=7 fvgs=14 bos=28 sigs=0 wrong_side=3 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=4 near_gap_pct=-0.053
[16:20:01] tick balance=$351.02
  diag: trend=bearish atr_ratio=0.92 obs=8 obs_fresh=7 fvgs=14 bos=28 sigs=0 wrong_side=3 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=4 near_gap_pct=-0.031
[16:21:03] tick balance=$351.02
  diag: trend=bearish atr_ratio=0.93 obs=8 obs_fresh=7 fvgs=14 bos=27 sigs=0 wrong_side=3 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=4 near_gap_pct=-0.015
[16:22:05] tick balance=$351.02
  diag: trend=bearish atr_ratio=0.96 obs=9 obs_fresh=8 fvgs=14 bos=27 sigs=0 wrong_side=3 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=5 near_gap_pct=0.052
[16:23:07] tick balance=$351.02
  diag: trend=bearish atr_ratio=0.99 obs=9 obs_fresh=8 fvgs=14 bos=27 sigs=0 wrong_side=3 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=5 near_gap_pct=0.154
[16:24:09] tick balance=$351.02
  diag: trend=bearish atr_ratio=1.01 obs=9 obs_fresh=8 fvgs=14 bos=27 sigs=0 wrong_side=3 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=5 near_gap_pct=0.18
[16:25:12] tick balance=$351.02
  diag: trend=bearish atr_ratio=0.96 obs=9 obs_fresh=8 fvgs=15 bos=28 sigs=0 wrong_side=3 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=5 near_gap_pct=0.127
[16:26:14] tick balance=$351.02
  diag: trend=bearish atr_ratio=1.01 obs=9 obs_fresh=8 fvgs=15 bos=27 sigs=0 wrong_side=3 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=5 near_gap_pct=0.009
[16:27:17] tick balance=$351.02
  diag: trend=bearish atr_ratio=1.01 obs=9 obs_fresh=8 fvgs=15 bos=27 sigs=0 wrong_side=3 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=5 near_gap_pct=0.014
[16:28:19] tick balance=$351.02
  diag: trend=bearish atr_ratio=1.02 obs=9 obs_fresh=8 fvgs=15 bos=27 sigs=0 wrong_side=3 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=5 near_gap_pct=-0.029
[16:29:21] tick balance=$351.02
  diag: trend=bearish atr_ratio=1.02 obs=9 obs_fresh=8 fvgs=15 bos=27 sigs=0 wrong_side=3 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=5 near_gap_pct=-0.022
[16:30:23] tick balance=$351.02
  diag: trend=bearish atr_ratio=0.99 obs=9 obs_fresh=8 fvgs=15 bos=27 sigs=0 wrong_side=3 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=5 near_gap_pct=-0.04
[16:31:25] tick balance=$351.02
  diag: trend=bearish atr_ratio=1.0 obs=9 obs_fresh=8 fvgs=15 bos=27 sigs=0 wrong_side=3 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=5 near_gap_pct=-0.036
[16:32:28] tick balance=$351.02
  diag: trend=bearish atr_ratio=1.01 obs=10 obs_fresh=9 fvgs=15 bos=27 sigs=0 wrong_side=4 price_out=3 bos_miss=0 risk_neg=0 liquidity_trap=2 near_gap_pct=-0.072
[16:33:31] tick balance=$351.02
  diag: trend=bearish atr_ratio=1.01 obs=10 obs_fresh=9 fvgs=15 bos=26 sigs=0 wrong_side=4 price_out=2 bos_miss=0 risk_neg=0 liquidity_trap=3 near_gap_pct=-0.06
[16:34:33] tick balance=$351.02
  diag: trend=bearish atr_ratio=1.02 obs=10 obs_fresh=9 fvgs=15 bos=26 sigs=0 wrong_side=4 price_out=3 bos_miss=0 risk_neg=0 liquidity_trap=2 near_gap_pct=-0.08
[16:35:36] tick balance=$351.02
  diag: trend=bearish atr_ratio=0.98 obs=10 obs_fresh=9 fvgs=15 bos=26 sigs=0 wrong_side=4 price_out=4 bos_miss=0 risk_neg=0 liquidity_trap=1 near_gap_pct=-0.067
[16:36:37] tick balance=$351.02
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[16:37:39] tick balance=$351.02
  diag: trend=bearish atr_ratio=0.99 obs=10 obs_fresh=9 fvgs=15 bos=25 sigs=0 wrong_side=4 price_out=3 bos_miss=0 risk_neg=0 liquidity_trap=2 near_gap_pct=-0.034
[16:38:41] tick balance=$351.02
  diag: trend=bearish atr_ratio=0.99 obs=10 obs_fresh=9 fvgs=15 bos=26 sigs=0 wrong_side=4 price_out=4 bos_miss=0 risk_neg=0 liquidity_trap=1 near_gap_pct=-0.06
[16:39:44] tick balance=$351.02
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[16:40:47] tick balance=$351.02
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[16:41:49] tick balance=$351.02
  diag: trend=bearish atr_ratio=0.96 obs=10 obs_fresh=9 fvgs=16 bos=25 sigs=0 wrong_side=4 price_out=4 bos_miss=0 risk_neg=0 liquidity_trap=1 near_gap_pct=-0.058
[16:42:51] tick balance=$351.02
  diag: trend=bearish atr_ratio=0.97 obs=10 obs_fresh=9 fvgs=15 bos=26 sigs=0 wrong_side=4 price_out=4 bos_miss=0 risk_neg=0 liquidity_trap=1 near_gap_pct=-0.051
[16:43:54] tick balance=$351.02
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[16:44:56] tick balance=$351.02
  diag: trend=bearish atr_ratio=1.0 obs=10 obs_fresh=9 fvgs=15 bos=26 sigs=0 wrong_side=4 price_out=1 bos_miss=0 risk_neg=0 liquidity_trap=4 near_gap_pct=-0.043
[16:45:58] tick balance=$351.02
  diag: trend=bearish atr_ratio=0.94 obs=10 obs_fresh=9 fvgs=15 bos=26 sigs=0 wrong_side=4 price_out=4 bos_miss=0 risk_neg=0 liquidity_trap=1 near_gap_pct=-0.04
[16:47:00] tick balance=$351.02
  diag: trend=bearish atr_ratio=0.94 obs=10 obs_fresh=9 fvgs=15 bos=27 sigs=0 wrong_side=4 price_out=3 bos_miss=0 risk_neg=0 liquidity_trap=2 near_gap_pct=-0.074
[16:48:02] tick balance=$351.02
  diag: trend=bearish atr_ratio=0.94 obs=11 obs_fresh=10 fvgs=15 bos=27 sigs=0 wrong_side=4 price_out=1 bos_miss=0 risk_neg=0 liquidity_trap=5 near_gap_pct=-0.036
[16:49:05] tick balance=$351.02
  diag: trend=bearish atr_ratio=0.94 obs=11 obs_fresh=10 fvgs=15 bos=27 sigs=0 wrong_side=4 price_out=1 bos_miss=0 risk_neg=0 liquidity_trap=5 near_gap_pct=-0.057
[16:50:06] tick balance=$351.02
  diag: trend=bearish atr_ratio=0.83 obs=11 obs_fresh=10 fvgs=15 bos=28 sigs=0 wrong_side=4 price_out=3 bos_miss=0 risk_neg=0 liquidity_trap=3 near_gap_pct=-0.068
[16:51:08] tick balance=$351.02
  diag: trend=bearish atr_ratio=0.84 obs=11 obs_fresh=10 fvgs=15 bos=28 sigs=0 wrong_side=4 price_out=4 bos_miss=0 risk_neg=0 liquidity_trap=2 near_gap_pct=-0.018
[16:52:11] tick balance=$351.02
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[16:53:14] tick balance=$351.02
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[16:54:15] tick balance=$351.02
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
```
