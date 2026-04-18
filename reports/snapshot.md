# Bot Snapshot — 2026-04-18 22:55 UTC

## Service: active
balance=$347.24

## Config
POST_CLOSE_COOLDOWN: int = 180 # 3 мин техническая пауза после закрытия
RISK_PCT: float = 0.05 # 5% от баланса на сделку
ADX_MIN: float = 20.0 # ADX < 20 → choppy market, skip entry

## Trades (last 20)
```
25|SELL|75705.5||open|2026-04-18 19:15:28|
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
6|SELL|70977.6|16.89|closed|2026-04-12 13:15:20|2026-04-12 14:43:04
```

## Daily PnL
```
2026-04-18|311.88|35.36|0
2026-04-17|328.7|-16.81|0
2026-04-16|381.29|-52.59|0
2026-04-15|363.1|17.9|0
2026-04-14|413.74|-50.64|0
2026-04-13|413.74|0.0|0
2026-04-12|423.86|-10.12|0
```

## Open Positions
```
25|SELL|75705.5|open
```

## Diag Summary (last ~4h)
```
     98 trend_htf=ranging trend_mid=ranging skip=trend_mismatch
     12 trend=bearish skip=atr_low ratio=0.75 min=0.8
      9 trend=bearish skip=atr_low ratio=0.77 min=0.8
      8 trend=bearish skip=atr_low ratio=0.78 min=0.8
      7 trend=bearish skip=atr_low ratio=0.71 min=0.8
      5 trend=bearish skip=atr_low ratio=0.79 min=0.8
      4 trend=bearish skip=atr_low ratio=0.74 min=0.8
      4 trend=bearish skip=atr_low ratio=0.73 min=0.8
      4 trend=bearish atr_ratio=0.86 obs=12 obs_fresh=4 fvgs=11 bos=27 sigs=0 wrong_side=4 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=0
      3 trend=bearish skip=atr_low ratio=0.76 min=0.8
      3 trend=bearish atr_ratio=0.89 obs=13 obs_fresh=5 fvgs=12 bos=27 sigs=0 wrong_side=5 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=0
      3 trend=bearish atr_ratio=0.85 obs=12 obs_fresh=4 fvgs=11 bos=27 sigs=0 wrong_side=4 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=0
      3 trend=bearish atr_ratio=0.84 obs=13 obs_fresh=5 fvgs=10 bos=27 sigs=0 wrong_side=5 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=0
      2 trend=bearish skip=atr_low ratio=0.7 min=0.8
      2 trend=bearish skip=atr_low ratio=0.72 min=0.8
      2 trend=bearish skip=atr_low ratio=0.69 min=0.8
      2 trend=bearish atr_ratio=0.88 obs=13 obs_fresh=5 fvgs=12 bos=26 sigs=0 wrong_side=5 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=0
      2 trend=bearish atr_ratio=0.88 obs=13 obs_fresh=5 fvgs=10 bos=27 sigs=0 wrong_side=5 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=0
      2 trend=bearish atr_ratio=0.87 obs=13 obs_fresh=5 fvgs=10 bos=27 sigs=0 wrong_side=5 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=0
      2 trend=bearish atr_ratio=0.85 obs=12 obs_fresh=4 fvgs=12 bos=27 sigs=0 wrong_side=4 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=0
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
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[00:02:43] tick balance=$349.58
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[00:03:47] tick balance=$353.85
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[00:04:50] tick balance=$355.95
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[00:05:53] tick balance=$355.67
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[00:06:57] tick balance=$358.47
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[00:08:00] tick balance=$357.15
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[00:09:03] tick balance=$358.26
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[00:10:06] tick balance=$358.21
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[00:11:09] tick balance=$357.99
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[00:12:12] tick balance=$358.58
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[00:13:14] tick balance=$356.83
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[00:14:17] tick balance=$357.92
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[00:15:20] tick balance=$358.82
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[00:16:23] tick balance=$359.08
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[00:17:26] tick balance=$357.35
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[00:18:29] tick balance=$356.17
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[00:19:32] tick balance=$357.74
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[00:20:35] tick balance=$357.91
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[00:21:39] tick balance=$356.40
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[00:22:42] tick balance=$355.38
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[00:23:46] tick balance=$355.13
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[00:24:50] tick balance=$354.72
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[00:25:52] tick balance=$354.26
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[00:26:55] tick balance=$354.27
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[00:27:58] tick balance=$353.99
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[00:29:01] tick balance=$353.32
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[00:30:05] tick balance=$352.89
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[00:31:09] tick balance=$351.84
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[00:32:11] tick balance=$349.95
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[00:33:15] tick balance=$348.74
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[00:34:18] tick balance=$348.14
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[00:35:20] tick balance=$347.44
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[00:36:23] tick balance=$348.38
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[00:37:26] tick balance=$347.99
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[00:38:28] tick balance=$347.49
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[00:39:31] tick balance=$347.02
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[00:40:34] tick balance=$349.37
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[00:41:38] tick balance=$351.01
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[00:42:41] tick balance=$351.40
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[00:43:43] tick balance=$350.93
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[00:44:47] tick balance=$349.63
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[00:45:50] tick balance=$348.42
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[00:46:53] tick balance=$347.01
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[00:47:56] tick balance=$345.99
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[00:49:00] tick balance=$346.59
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[00:50:03] tick balance=$345.73
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[00:51:06] tick balance=$344.84
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[tick] fetch err: 
[00:53:17] tick balance=$347.05
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[00:54:19] tick balance=$347.24
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
```
