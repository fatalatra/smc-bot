# Bot Snapshot — 2026-04-21 06:55 UTC

## Service: active
balance=$296.96

## Config
POST_CLOSE_COOLDOWN: int = 180 # 3 мин техническая пауза после закрытия
RISK_PCT: float = 0.01 # 1% для старта на HYPE (вернём к 5% после 5+ сделок)
ADX_MIN: float = 20.0 # ADX < 20 → choppy market, skip entry

## Trades (last 20)
```
28|SELL|74162.8|-15.75|closed|2026-04-20 05:21:50|2026-04-20 06:04:22
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
```

## Daily PnL
```
2026-04-21|296.96|0.0|0
2026-04-20|312.71|-15.75|0
2026-04-19|354.45|-41.74|0
2026-04-18|311.88|42.12|0
2026-04-17|328.7|-16.81|0
2026-04-16|381.29|-52.59|0
2026-04-15|363.1|17.9|0
```

## Open Positions
```
none
```

## Diag Summary (last ~4h)
```
     96 trend_htf=ranging trend_mid=ranging skip=trend_mismatch
     22 trend=bearish skip=ema_overextended price=40.8 ema20_h4=42.2 dist=1.4 max_dist=1.4
     14 trend=bearish skip=adx_low adx=14.7 min=20.0
     13 trend=bearish skip=adx_low adx=13.1 min=20.0
     11 trend=bearish skip=adx_low adx=12.7 min=20.0
     10 trend=bearish skip=adx_low adx=12.6 min=20.0
      8 trend=bearish skip=adx_low adx=15.2 min=20.0
      7 trend=bearish skip=adx_low adx=12.9 min=20.0
      7 trend=bearish skip=adx_low adx=12.5 min=20.0
      6 trend=bearish skip=adx_low adx=13.8 min=20.0
      5 trend=bearish skip=adx_low adx=14.2 min=20.0
      5 trend=bearish skip=adx_low adx=12.3 min=20.0
      5 trend=bearish skip=adx_low adx=12.0 min=20.0
      4 trend=bearish skip=adx_low adx=13.7 min=20.0
      4 trend=bearish skip=adx_low adx=12.8 min=20.0
      3 trend=bearish skip=ema_overextended price=40.7 ema20_h4=42.2 dist=1.5 max_dist=1.4
      3 trend=bearish skip=ema_overextended price=40.7 ema20_h4=42.2 dist=1.4 max_dist=1.4
      3 trend=bearish skip=adx_low adx=14.1 min=20.0
      3 trend=bearish skip=adx_low adx=13.9 min=20.0
      3 trend=bearish skip=adx_low adx=12.2 min=20.0
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
[08:03:34] tick balance=$296.96
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[08:04:37] tick balance=$296.96
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[08:05:39] tick balance=$296.96
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[08:06:41] tick balance=$296.96
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[08:07:43] tick balance=$296.96
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[08:08:45] tick balance=$296.96
  diag: trend=bearish skip=adx_low adx=12.5 min=20.0
[08:09:47] tick balance=$296.96
  diag: trend=bearish skip=adx_low adx=12.5 min=20.0
[08:10:49] tick balance=$296.96
  diag: trend=bearish skip=adx_low adx=12.5 min=20.0
[08:11:52] tick balance=$296.96
  diag: trend=bearish skip=adx_low adx=12.5 min=20.0
[08:12:54] tick balance=$296.96
  diag: trend=bearish skip=adx_low adx=12.4 min=20.0
[08:13:57] tick balance=$296.96
  diag: trend=bearish skip=adx_low adx=12.6 min=20.0
[08:14:59] tick balance=$296.96
  diag: trend=bearish skip=adx_low adx=12.6 min=20.0
[08:16:01] tick balance=$296.96
  diag: trend=bearish skip=adx_low adx=12.3 min=20.0
[08:17:03] tick balance=$296.96
  diag: trend=bearish skip=adx_low adx=12.3 min=20.0
[08:18:05] tick balance=$296.96
  diag: trend=bearish skip=adx_low adx=12.3 min=20.0
[08:19:08] tick balance=$296.96
  diag: trend=bearish skip=adx_low adx=12.3 min=20.0
[08:20:10] tick balance=$296.96
  diag: trend=bearish skip=adx_low adx=12.5 min=20.0
[08:21:11] tick balance=$296.96
  diag: trend=bearish skip=adx_low adx=12.6 min=20.0
[08:22:14] tick balance=$296.96
  diag: trend=bearish skip=adx_low adx=12.6 min=20.0
[08:23:16] tick balance=$296.96
  diag: trend=bearish skip=adx_low adx=12.6 min=20.0
[08:24:19] tick balance=$296.96
  diag: trend=bearish skip=adx_low adx=12.6 min=20.0
[08:25:20] tick balance=$296.96
  diag: trend=bearish skip=adx_low adx=12.6 min=20.0
[08:26:22] tick balance=$296.96
  diag: trend=bearish skip=adx_low adx=12.6 min=20.0
[08:27:24] tick balance=$296.96
  diag: trend=bearish skip=adx_low adx=12.6 min=20.0
[08:28:26] tick balance=$296.96
  diag: trend=bearish skip=adx_low adx=12.6 min=20.0
[08:29:28] tick balance=$296.96
  diag: trend=bearish skip=adx_low adx=12.7 min=20.0
[08:30:29] tick balance=$296.96
  diag: trend=bearish skip=adx_low adx=12.8 min=20.0
[08:31:31] tick balance=$296.96
  diag: trend=bearish skip=adx_low adx=12.8 min=20.0
[08:32:34] tick balance=$296.96
  diag: trend=bearish skip=adx_low adx=12.8 min=20.0
[08:33:37] tick balance=$296.96
  diag: trend=bearish skip=adx_low adx=12.8 min=20.0
[08:34:39] tick balance=$296.96
  diag: trend=bearish skip=adx_low adx=12.5 min=20.0
[08:35:42] tick balance=$296.96
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[08:36:45] tick balance=$296.96
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[08:37:47] tick balance=$296.96
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[08:38:49] tick balance=$296.96
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[08:39:51] tick balance=$296.96
  diag: trend=bearish skip=adx_low adx=12.0 min=20.0
[08:40:53] tick balance=$296.96
  diag: trend=bearish skip=adx_low adx=12.0 min=20.0
[08:41:55] tick balance=$296.96
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[08:42:57] tick balance=$296.96
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[08:43:59] tick balance=$296.96
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[08:45:01] tick balance=$296.96
  diag: trend=bearish skip=adx_low adx=12.0 min=20.0
[08:46:02] tick balance=$296.96
  diag: trend=bearish skip=adx_low adx=11.4 min=20.0
[08:47:05] tick balance=$296.96
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[08:48:07] tick balance=$296.96
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[08:49:09] tick balance=$296.96
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[08:50:11] tick balance=$296.96
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[08:51:14] tick balance=$296.96
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[08:52:16] tick balance=$296.96
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[08:53:18] tick balance=$296.96
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[08:54:19] tick balance=$296.96
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
```
