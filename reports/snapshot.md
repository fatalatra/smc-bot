# Bot Snapshot — 2026-04-21 02:55 UTC

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
    199 trend_htf=ranging trend_mid=ranging skip=trend_mismatch
     21 trend=bearish skip=ema_overextended price=40.8 ema20_h4=42.2 dist=1.4 max_dist=1.4
     18 trend=bearish skip=ema_overextended price=40.7 ema20_h4=42.2 dist=1.5 max_dist=1.4
      2 trend=bearish skip=ema_overextended price=40.7 ema20_h4=42.2 dist=1.4 max_dist=1.4
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
[04:03:58] tick balance=$296.96
  diag: trend=bearish skip=ema_overextended price=40.7 ema20_h4=42.2 dist=1.5 max_dist=1.4
[04:05:00] tick balance=$296.96
  diag: trend=bearish skip=ema_overextended price=40.7 ema20_h4=42.2 dist=1.5 max_dist=1.4
[04:06:02] tick balance=$296.96
  diag: trend=bearish skip=ema_overextended price=40.7 ema20_h4=42.2 dist=1.5 max_dist=1.4
[04:07:04] tick balance=$296.96
  diag: trend=bearish skip=ema_overextended price=40.7 ema20_h4=42.2 dist=1.4 max_dist=1.4
[04:08:07] tick balance=$296.96
  diag: trend=bearish skip=ema_overextended price=40.7 ema20_h4=42.2 dist=1.5 max_dist=1.4
[04:09:08] tick balance=$296.96
  diag: trend=bearish skip=ema_overextended price=40.7 ema20_h4=42.2 dist=1.5 max_dist=1.4
[04:10:10] tick balance=$296.96
  diag: trend=bearish skip=ema_overextended price=40.7 ema20_h4=42.2 dist=1.5 max_dist=1.4
[04:11:12] tick balance=$296.96
  diag: trend=bearish skip=ema_overextended price=40.7 ema20_h4=42.2 dist=1.5 max_dist=1.4
[04:12:15] tick balance=$296.96
  diag: trend=bearish skip=ema_overextended price=40.7 ema20_h4=42.2 dist=1.5 max_dist=1.4
[04:13:17] tick balance=$296.96
  diag: trend=bearish skip=ema_overextended price=40.7 ema20_h4=42.2 dist=1.5 max_dist=1.4
[04:14:19] tick balance=$296.96
  diag: trend=bearish skip=ema_overextended price=40.7 ema20_h4=42.2 dist=1.5 max_dist=1.4
[04:15:22] tick balance=$296.96
  diag: trend=bearish skip=ema_overextended price=40.7 ema20_h4=42.2 dist=1.5 max_dist=1.4
[04:16:23] tick balance=$296.96
  diag: trend=bearish skip=ema_overextended price=40.7 ema20_h4=42.2 dist=1.5 max_dist=1.4
[04:17:25] tick balance=$296.96
  diag: trend=bearish skip=ema_overextended price=40.7 ema20_h4=42.2 dist=1.5 max_dist=1.4
[04:18:27] tick balance=$296.96
  diag: trend=bearish skip=ema_overextended price=40.8 ema20_h4=42.2 dist=1.4 max_dist=1.4
[04:19:29] tick balance=$296.96
  diag: trend=bearish skip=ema_overextended price=40.8 ema20_h4=42.2 dist=1.4 max_dist=1.4
[04:20:32] tick balance=$296.96
  diag: trend=bearish skip=ema_overextended price=40.7 ema20_h4=42.2 dist=1.5 max_dist=1.4
[04:21:34] tick balance=$296.96
  diag: trend=bearish skip=ema_overextended price=40.8 ema20_h4=42.2 dist=1.4 max_dist=1.4
[04:22:36] tick balance=$296.96
  diag: trend=bearish skip=ema_overextended price=40.8 ema20_h4=42.2 dist=1.4 max_dist=1.4
[04:23:38] tick balance=$296.96
  diag: trend=bearish skip=ema_overextended price=40.7 ema20_h4=42.2 dist=1.4 max_dist=1.4
[04:24:41] tick balance=$296.96
  diag: trend=bearish skip=ema_overextended price=40.7 ema20_h4=42.2 dist=1.5 max_dist=1.4
[04:25:43] tick balance=$296.96
  diag: trend=bearish skip=ema_overextended price=40.7 ema20_h4=42.2 dist=1.5 max_dist=1.4
[04:26:45] tick balance=$296.96
  diag: trend=bearish skip=ema_overextended price=40.7 ema20_h4=42.2 dist=1.5 max_dist=1.4
[04:27:47] tick balance=$296.96
  diag: trend=bearish skip=ema_overextended price=40.8 ema20_h4=42.2 dist=1.4 max_dist=1.4
[04:28:49] tick balance=$296.96
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[04:29:51] tick balance=$296.96
  diag: trend=bearish skip=ema_overextended price=40.8 ema20_h4=42.2 dist=1.4 max_dist=1.4
[04:30:53] tick balance=$296.96
  diag: trend=bearish skip=ema_overextended price=40.8 ema20_h4=42.2 dist=1.4 max_dist=1.4
[04:31:55] tick balance=$296.96
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[04:32:57] tick balance=$296.96
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[04:33:59] tick balance=$296.96
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[04:35:01] tick balance=$296.96
  diag: trend=bearish skip=ema_overextended price=40.8 ema20_h4=42.2 dist=1.4 max_dist=1.4
[04:36:04] tick balance=$296.96
  diag: trend=bearish skip=ema_overextended price=40.8 ema20_h4=42.2 dist=1.4 max_dist=1.4
[04:37:07] tick balance=$296.96
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[04:38:09] tick balance=$296.96
  diag: trend=bearish skip=ema_overextended price=40.8 ema20_h4=42.2 dist=1.4 max_dist=1.4
[04:39:10] tick balance=$296.96
  diag: trend=bearish skip=ema_overextended price=40.8 ema20_h4=42.2 dist=1.4 max_dist=1.4
[04:40:12] tick balance=$296.96
  diag: trend=bearish skip=ema_overextended price=40.8 ema20_h4=42.2 dist=1.4 max_dist=1.4
[04:41:15] tick balance=$296.96
  diag: trend=bearish skip=ema_overextended price=40.8 ema20_h4=42.2 dist=1.4 max_dist=1.4
[04:42:17] tick balance=$296.96
  diag: trend=bearish skip=ema_overextended price=40.8 ema20_h4=42.2 dist=1.4 max_dist=1.4
[04:43:19] tick balance=$296.96
  diag: trend=bearish skip=ema_overextended price=40.8 ema20_h4=42.2 dist=1.4 max_dist=1.4
[04:44:21] tick balance=$296.96
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[04:45:24] tick balance=$296.96
  diag: trend=bearish skip=ema_overextended price=40.8 ema20_h4=42.2 dist=1.4 max_dist=1.4
[04:46:26] tick balance=$296.96
  diag: trend=bearish skip=ema_overextended price=40.8 ema20_h4=42.2 dist=1.4 max_dist=1.4
[04:47:29] tick balance=$296.96
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[04:48:31] tick balance=$296.96
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[04:49:33] tick balance=$296.96
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[04:50:35] tick balance=$296.96
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[04:51:38] tick balance=$296.96
  diag: trend=bearish skip=ema_overextended price=40.8 ema20_h4=42.2 dist=1.4 max_dist=1.4
[04:52:40] tick balance=$296.96
  diag: trend=bearish skip=ema_overextended price=40.8 ema20_h4=42.2 dist=1.4 max_dist=1.4
[04:53:42] tick balance=$296.96
  diag: trend=bearish skip=ema_overextended price=40.8 ema20_h4=42.2 dist=1.4 max_dist=1.4
[04:54:44] tick balance=$296.96
  diag: trend=bearish skip=ema_overextended price=40.8 ema20_h4=42.2 dist=1.4 max_dist=1.4
```
