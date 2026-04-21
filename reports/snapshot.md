# Bot Snapshot — 2026-04-21 18:55 UTC

## Service: active
balance=$301.06

## Config
POST_CLOSE_COOLDOWN: int = 180 # 3 мин техническая пауза после закрытия
RISK_PCT: float = 0.01 # 1% для старта на HYPE (вернём к 5% после 5+ сделок)
ADX_MIN: float = 20.0 # ADX < 20 → choppy market, skip entry

## Trades (last 20)
```
29|SELL|40.4|3.85|closed|2026-04-21 14:00:28|2026-04-21 15:27:47
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
```

## Daily PnL
```
2026-04-21|296.96|4.1|0
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
     29 trend=bearish skip=ema_overextended price=39.6 ema20_h4=41.6 dist=2.0 max_dist=1.4
     25 trend=bearish skip=ema_overextended price=39.9 ema20_h4=41.6 dist=1.7 max_dist=1.4
     21 trend=bearish skip=ema_overextended price=39.8 ema20_h4=41.6 dist=1.8 max_dist=1.4
     17 trend=bearish skip=ema_overextended price=40.0 ema20_h4=41.8 dist=1.8 max_dist=1.5
     17 trend=bearish skip=ema_overextended price=39.7 ema20_h4=41.6 dist=1.9 max_dist=1.4
     16 trend=bearish skip=ema_overextended price=40.1 ema20_h4=41.8 dist=1.7 max_dist=1.4
     15 trend=bearish skip=ema_overextended price=40.0 ema20_h4=41.6 dist=1.6 max_dist=1.4
     12 trend=bearish skip=ema_overextended price=39.5 ema20_h4=41.6 dist=2.1 max_dist=1.5
     10 trend=bearish skip=ema_overextended price=39.5 ema20_h4=41.6 dist=2.1 max_dist=1.4
     10 trend=bearish skip=ema_overextended price=39.4 ema20_h4=41.6 dist=2.2 max_dist=1.5
      7 trend=bearish skip=ema_overextended price=40.0 ema20_h4=41.8 dist=1.8 max_dist=1.4
      7 trend=bearish skip=ema_overextended price=39.4 ema20_h4=41.6 dist=2.1 max_dist=1.5
      5 trend=bearish skip=ema_overextended price=40.4 ema20_h4=41.8 dist=1.4 max_dist=1.4
      5 trend=bearish skip=ema_overextended price=39.9 ema20_h4=41.8 dist=1.9 max_dist=1.4
      5 trend=bearish skip=ema_overextended price=39.5 ema20_h4=41.6 dist=2.0 max_dist=1.4
      4 trend=bearish skip=ema_overextended price=40.2 ema20_h4=41.8 dist=1.6 max_dist=1.4
      4 trend=bearish skip=ema_overextended price=40.0 ema20_h4=41.6 dist=1.7 max_dist=1.4
      4 trend=bearish skip=ema_overextended price=39.9 ema20_h4=41.8 dist=1.9 max_dist=1.5
      4 trend=bearish skip=ema_overextended price=39.1 ema20_h4=41.5 dist=2.4 max_dist=1.5
      3 trend=bearish skip=ema_overextended price=40.3 ema20_h4=41.8 dist=1.6 max_dist=1.4
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
[20:04:06] tick balance=$301.06
  diag: trend=bearish skip=ema_overextended price=39.6 ema20_h4=41.6 dist=2.0 max_dist=1.4
[20:05:08] tick balance=$301.06
  diag: trend=bearish skip=ema_overextended price=39.6 ema20_h4=41.6 dist=2.0 max_dist=1.4
[20:06:09] tick balance=$301.06
  diag: trend=bearish skip=ema_overextended price=39.6 ema20_h4=41.6 dist=2.0 max_dist=1.4
[20:07:12] tick balance=$301.06
  diag: trend=bearish skip=ema_overextended price=39.6 ema20_h4=41.6 dist=2.0 max_dist=1.4
[20:08:14] tick balance=$301.06
  diag: trend=bearish skip=ema_overextended price=39.5 ema20_h4=41.6 dist=2.0 max_dist=1.4
[20:09:16] tick balance=$301.06
  diag: trend=bearish skip=ema_overextended price=39.6 ema20_h4=41.6 dist=2.0 max_dist=1.4
[20:10:18] tick balance=$301.06
  diag: trend=bearish skip=ema_overextended price=39.5 ema20_h4=41.6 dist=2.0 max_dist=1.4
[20:11:20] tick balance=$301.06
  diag: trend=bearish skip=ema_overextended price=39.5 ema20_h4=41.6 dist=2.0 max_dist=1.4
[20:12:22] tick balance=$301.06
  diag: trend=bearish skip=ema_overextended price=39.6 ema20_h4=41.6 dist=2.0 max_dist=1.4
[20:13:23] tick balance=$301.06
  diag: trend=bearish skip=ema_overextended price=39.5 ema20_h4=41.6 dist=2.1 max_dist=1.4
[20:14:25] tick balance=$301.06
  diag: trend=bearish skip=ema_overextended price=39.5 ema20_h4=41.6 dist=2.1 max_dist=1.4
[20:15:27] tick balance=$301.06
  diag: trend=bearish skip=ema_overextended price=39.5 ema20_h4=41.6 dist=2.1 max_dist=1.4
[20:16:29] tick balance=$301.06
  diag: trend=bearish skip=ema_overextended price=39.5 ema20_h4=41.6 dist=2.1 max_dist=1.4
[20:17:32] tick balance=$301.06
  diag: trend=bearish skip=ema_overextended price=39.4 ema20_h4=41.6 dist=2.2 max_dist=1.5
[20:18:34] tick balance=$301.06
  diag: trend=bearish skip=ema_overextended price=39.5 ema20_h4=41.6 dist=2.1 max_dist=1.5
[20:19:36] tick balance=$301.06
  diag: trend=bearish skip=ema_overextended price=39.4 ema20_h4=41.6 dist=2.1 max_dist=1.5
[20:20:38] tick balance=$301.06
  diag: trend=bearish skip=ema_overextended price=39.4 ema20_h4=41.6 dist=2.1 max_dist=1.5
[20:21:40] tick balance=$301.06
  diag: trend=bearish skip=ema_overextended price=39.5 ema20_h4=41.6 dist=2.1 max_dist=1.5
[20:22:42] tick balance=$301.06
  diag: trend=bearish skip=ema_overextended price=39.5 ema20_h4=41.6 dist=2.1 max_dist=1.5
[20:23:44] tick balance=$301.06
  diag: trend=bearish skip=ema_overextended price=39.5 ema20_h4=41.6 dist=2.1 max_dist=1.5
[20:24:45] tick balance=$301.06
  diag: trend=bearish skip=ema_overextended price=39.5 ema20_h4=41.6 dist=2.1 max_dist=1.5
[20:25:47] tick balance=$301.06
  diag: trend=bearish skip=ema_overextended price=39.5 ema20_h4=41.6 dist=2.1 max_dist=1.5
[20:26:49] tick balance=$301.06
  diag: trend=bearish skip=ema_overextended price=39.5 ema20_h4=41.6 dist=2.1 max_dist=1.5
[20:27:51] tick balance=$301.06
  diag: trend=bearish skip=ema_overextended price=39.5 ema20_h4=41.6 dist=2.1 max_dist=1.5
[20:28:53] tick balance=$301.06
  diag: trend=bearish skip=ema_overextended price=39.4 ema20_h4=41.6 dist=2.2 max_dist=1.5
[20:29:56] tick balance=$301.06
  diag: trend=bearish skip=ema_overextended price=39.4 ema20_h4=41.6 dist=2.2 max_dist=1.5
[20:30:57] tick balance=$301.06
  diag: trend=bearish skip=ema_overextended price=39.4 ema20_h4=41.6 dist=2.1 max_dist=1.5
[20:32:00] tick balance=$301.06
  diag: trend=bearish skip=ema_overextended price=39.4 ema20_h4=41.6 dist=2.2 max_dist=1.5
[20:33:02] tick balance=$301.06
  diag: trend=bearish skip=ema_overextended price=39.4 ema20_h4=41.6 dist=2.1 max_dist=1.5
[20:34:04] tick balance=$301.06
  diag: trend=bearish skip=ema_overextended price=39.4 ema20_h4=41.6 dist=2.2 max_dist=1.5
[20:35:05] tick balance=$301.06
  diag: trend=bearish skip=ema_overextended price=39.5 ema20_h4=41.6 dist=2.1 max_dist=1.5
[20:36:07] tick balance=$301.06
  diag: trend=bearish skip=ema_overextended price=39.5 ema20_h4=41.6 dist=2.1 max_dist=1.5
[20:37:09] tick balance=$301.06
  diag: trend=bearish skip=ema_overextended price=39.5 ema20_h4=41.6 dist=2.1 max_dist=1.5
[20:38:11] tick balance=$301.06
  diag: trend=bearish skip=ema_overextended price=39.5 ema20_h4=41.6 dist=2.1 max_dist=1.5
[20:39:13] tick balance=$301.06
  diag: trend=bearish skip=ema_overextended price=39.4 ema20_h4=41.6 dist=2.1 max_dist=1.5
[20:40:15] tick balance=$301.06
  diag: trend=bearish skip=ema_overextended price=39.4 ema20_h4=41.6 dist=2.1 max_dist=1.5
[20:41:17] tick balance=$301.06
  diag: trend=bearish skip=ema_overextended price=39.4 ema20_h4=41.6 dist=2.2 max_dist=1.5
[20:42:18] tick balance=$301.06
  diag: trend=bearish skip=ema_overextended price=39.4 ema20_h4=41.6 dist=2.2 max_dist=1.5
[20:43:20] tick balance=$301.06
  diag: trend=bearish skip=ema_overextended price=39.4 ema20_h4=41.6 dist=2.2 max_dist=1.5
[20:44:25] tick balance=$301.06
  diag: trend=bearish skip=ema_overextended price=39.4 ema20_h4=41.6 dist=2.2 max_dist=1.5
[20:45:27] tick balance=$301.06
  diag: trend=bearish skip=ema_overextended price=39.4 ema20_h4=41.6 dist=2.2 max_dist=1.5
[20:46:29] tick balance=$301.06
  diag: trend=bearish skip=ema_overextended price=39.4 ema20_h4=41.6 dist=2.1 max_dist=1.5
[20:47:33] tick balance=$301.06
  diag: trend=bearish skip=ema_overextended price=39.3 ema20_h4=41.6 dist=2.2 max_dist=1.5
[20:48:40] tick balance=$301.06
  diag: trend=bearish skip=ema_overextended price=39.2 ema20_h4=41.6 dist=2.3 max_dist=1.5
[20:49:41] tick balance=$301.06
  diag: trend=bearish skip=ema_overextended price=39.2 ema20_h4=41.5 dist=2.4 max_dist=1.5
[20:50:43] tick balance=$301.06
  diag: trend=bearish skip=ema_overextended price=39.1 ema20_h4=41.5 dist=2.4 max_dist=1.5
[20:51:45] tick balance=$301.06
  diag: trend=bearish skip=ema_overextended price=39.1 ema20_h4=41.5 dist=2.4 max_dist=1.5
[20:52:47] tick balance=$301.06
  diag: trend=bearish skip=ema_overextended price=39.1 ema20_h4=41.5 dist=2.4 max_dist=1.5
[20:53:49] tick balance=$301.06
  diag: trend=bearish skip=ema_overextended price=39.1 ema20_h4=41.5 dist=2.5 max_dist=1.5
[20:54:51] tick balance=$301.06
  diag: trend=bearish skip=ema_overextended price=39.1 ema20_h4=41.5 dist=2.4 max_dist=1.5
```
