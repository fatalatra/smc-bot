# Bot Snapshot — 2026-04-16 06:55 UTC

## Service: active
balance=$387.26

## Config
POST_CLOSE_COOLDOWN: int = 180 # 3 мин техническая пауза после закрытия
RISK_PCT: float = 0.05 # 5% от баланса на сделку
ADX_MIN: float = 20.0 # ADX < 20 → choppy market, skip entry

## Trades (last 20)
```
14|BUY|74983.1||open|2026-04-15 22:32:25|
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
2026-04-16|381.29|5.97|0
2026-04-15|363.1|17.9|0
2026-04-14|413.74|-50.64|0
2026-04-13|413.74|0.0|0
2026-04-12|423.86|-10.12|0
2026-04-11|457.33|-130.15|0
```

## Open Positions
```
14|BUY|74983.1|open
```

## Diag Summary (last ~4h)
```
     16 trend_htf=ranging trend_mid=ranging skip=trend_mismatch
     12 trend=bullish skip=atr_low ratio=0.68 min=0.8
     11 trend=bullish skip=atr_low ratio=0.74 min=0.8
     10 trend=bullish skip=atr_low ratio=0.66 min=0.8
      9 trend=bullish skip=atr_low ratio=0.67 min=0.8
      8 trend=bullish skip=atr_low ratio=0.72 min=0.8
      8 trend=bullish skip=atr_low ratio=0.71 min=0.8
      6 trend=bullish skip=atr_low ratio=0.7 min=0.8
      6 trend=bullish skip=atr_low ratio=0.69 min=0.8
      5 trend=bullish skip=atr_low ratio=0.77 min=0.8
      4 trend=bullish skip=atr_low ratio=0.75 min=0.8
      3 trend=bullish skip=atr_low ratio=0.78 min=0.8
      3 trend=bullish skip=atr_low ratio=0.65 min=0.8
      2 trend=bullish skip=atr_low ratio=0.8 min=0.8
      2 trend=bullish skip=atr_low ratio=0.79 min=0.8
      2 trend=bullish skip=atr_low ratio=0.76 min=0.8
      2 trend=bullish skip=atr_low ratio=0.73 min=0.8
      2 trend=bullish atr_ratio=0.96 obs=7 obs_fresh=6 fvgs=12 bos=30 sigs=0 wrong_side=4 price_out=0 bos_miss=2 risk_neg=0 liquidity_trap=0 near_gap_pct=0.098
      1 trend=bullish skip=atr_low ratio=0.64 min=0.8
      1 trend=bullish atr_ratio=1.2 obs=11 obs_fresh=10 fvgs=11 bos=24 sigs=0 wrong_side=6 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=4 near_gap_pct=0.251
```

## Errors
```
    self.gen.throw(typ, value, traceback)
  File "/root/smc-bot/venv/lib/python3.11/site-packages/httpcore/_exceptions.py", line 14, in map_exceptions
httpcore.ConnectError: [SSL: TLSV1_ALERT_INTERNAL_ERROR] tlsv1 alert internal error (_ssl.c:992)
The above exception was the direct cause of the following exception:
Traceback (most recent call last):
    with map_httpcore_exceptions():
    self.gen.throw(typ, value, traceback)
  File "/root/smc-bot/venv/lib/python3.11/site-packages/httpx/_transports/default.py", line 118, in map_httpcore_exceptions
httpx.ConnectError: [SSL: TLSV1_ALERT_INTERNAL_ERROR] tlsv1 alert internal error (_ssl.c:992)
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
[08:02:49] tick balance=$390.08
  diag: trend=bullish skip=atr_low ratio=0.66 min=0.8
[08:03:53] tick balance=$388.61
  diag: trend=bullish skip=atr_low ratio=0.67 min=0.8
[08:04:57] tick balance=$388.12
  diag: trend=bullish skip=atr_low ratio=0.67 min=0.8
[08:06:00] tick balance=$388.40
  diag: trend=bullish skip=atr_low ratio=0.66 min=0.8
[08:07:03] tick balance=$389.28
  diag: trend=bullish skip=atr_low ratio=0.68 min=0.8
[08:08:07] tick balance=$389.10
  diag: trend=bullish skip=atr_low ratio=0.68 min=0.8
[08:09:10] tick balance=$390.01
  diag: trend=bullish skip=atr_low ratio=0.68 min=0.8
[08:10:12] tick balance=$389.85
  diag: trend=bullish skip=atr_low ratio=0.66 min=0.8
[08:11:15] tick balance=$389.76
  diag: trend=bullish skip=atr_low ratio=0.66 min=0.8
[08:12:18] tick balance=$388.88
  diag: trend=bullish skip=atr_low ratio=0.68 min=0.8
[08:13:21] tick balance=$390.29
  diag: trend=bullish skip=atr_low ratio=0.68 min=0.8
[08:14:24] tick balance=$390.19
  diag: trend=bullish skip=atr_low ratio=0.68 min=0.8
[08:15:28] tick balance=$388.82
  diag: trend=bullish skip=atr_low ratio=0.66 min=0.8
[08:16:31] tick balance=$388.18
  diag: trend=bullish skip=atr_low ratio=0.66 min=0.8
[08:17:33] tick balance=$389.46
  diag: trend=bullish skip=atr_low ratio=0.67 min=0.8
[08:18:37] tick balance=$389.91
  diag: trend=bullish skip=atr_low ratio=0.68 min=0.8
[08:19:39] tick balance=$389.88
  diag: trend=bullish skip=atr_low ratio=0.68 min=0.8
[08:20:43] tick balance=$388.69
  diag: trend=bullish skip=atr_low ratio=0.69 min=0.8
[08:21:47] tick balance=$388.62
  diag: trend=bullish skip=atr_low ratio=0.69 min=0.8
[08:22:49] tick balance=$388.60
  diag: trend=bullish skip=atr_low ratio=0.69 min=0.8
[08:23:53] tick balance=$388.89
  diag: trend=bullish skip=atr_low ratio=0.7 min=0.8
[08:24:55] tick balance=$389.06
  diag: trend=bullish skip=atr_low ratio=0.7 min=0.8
[08:25:58] tick balance=$388.27
  diag: trend=bullish skip=atr_low ratio=0.66 min=0.8
[08:27:02] tick balance=$389.04
  diag: trend=bullish skip=atr_low ratio=0.67 min=0.8
[08:28:04] tick balance=$388.97
  diag: trend=bullish skip=atr_low ratio=0.67 min=0.8
[08:29:07] tick balance=$388.51
  diag: trend=bullish skip=atr_low ratio=0.67 min=0.8
[08:30:11] tick balance=$388.15
  diag: trend=bullish skip=atr_low ratio=0.64 min=0.8
[08:31:15] tick balance=$388.40
  diag: trend=bullish skip=atr_low ratio=0.65 min=0.8
[08:32:18] tick balance=$387.73
  diag: trend=bullish skip=atr_low ratio=0.66 min=0.8
[08:33:21] tick balance=$388.06
  diag: trend=bullish skip=atr_low ratio=0.66 min=0.8
[08:34:25] tick balance=$386.76
  diag: trend=bullish skip=atr_low ratio=0.67 min=0.8
[08:35:28] tick balance=$387.33
  diag: trend=bullish skip=atr_low ratio=0.66 min=0.8
[08:36:31] tick balance=$387.31
  diag: trend=bullish skip=atr_low ratio=0.67 min=0.8
[08:37:33] tick balance=$387.23
  diag: trend=bullish skip=atr_low ratio=0.68 min=0.8
[08:38:35] tick balance=$387.65
  diag: trend=bullish skip=atr_low ratio=0.68 min=0.8
[08:39:38] tick balance=$387.94
  diag: trend=bullish skip=atr_low ratio=0.68 min=0.8
[08:40:40] tick balance=$387.06
  diag: trend=bullish skip=atr_low ratio=0.67 min=0.8
[08:41:43] tick balance=$384.38
  diag: trend=bullish skip=atr_low ratio=0.71 min=0.8
[08:42:45] tick balance=$385.20
  diag: trend=bullish skip=atr_low ratio=0.74 min=0.8
[08:43:48] tick balance=$385.46
  diag: trend=bullish skip=atr_low ratio=0.74 min=0.8
[08:44:51] tick balance=$385.40
  diag: trend=bullish skip=atr_low ratio=0.74 min=0.8
[08:45:54] tick balance=$385.06
  diag: trend=bullish skip=atr_low ratio=0.71 min=0.8
[08:46:57] tick balance=$384.71
  diag: trend=bullish skip=atr_low ratio=0.72 min=0.8
[08:48:00] tick balance=$385.56
  diag: trend=bullish skip=atr_low ratio=0.72 min=0.8
[08:49:03] tick balance=$386.71
  diag: trend=bullish skip=atr_low ratio=0.74 min=0.8
[08:50:07] tick balance=$387.60
  diag: trend=bullish skip=atr_low ratio=0.7 min=0.8
[08:51:11] tick balance=$387.69
  diag: trend=bullish skip=atr_low ratio=0.71 min=0.8
[08:52:13] tick balance=$388.69
  diag: trend=bullish skip=atr_low ratio=0.72 min=0.8
[08:53:16] tick balance=$388.04
  diag: trend=bullish skip=atr_low ratio=0.73 min=0.8
[08:54:20] tick balance=$387.26
  diag: trend=bullish skip=atr_low ratio=0.74 min=0.8
```
