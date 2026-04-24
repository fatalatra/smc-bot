# Bot Snapshot — 2026-04-24 02:55 UTC

## Service: active
balance=$305.94

## Config
POST_CLOSE_COOLDOWN: int = 180 # 3 мин техническая пауза после закрытия
RISK_PCT: float = 0.03 # 1% для старта на HYPE (вернём к 5% после 5+ сделок)
ADX_MIN: float = 20.0 # ADX < 20 → choppy market, skip entry

## Trades (last 20)
```
34|SELL|40.6|-4.03|closed|2026-04-23 04:06:08|2026-04-23 04:10:20
33|BUY|41.2|-5.49|closed|2026-04-23 00:03:56|2026-04-23 00:10:14
32|BUY|41.1|3.34|closed|2026-04-22 12:45:58|2026-04-22 13:48:02
31|BUY|40.4|4.57|closed|2026-04-22 05:23:43|2026-04-22 10:32:03
30|BUY|40.0|3.22|closed|2026-04-22 04:07:10|2026-04-22 05:19:32
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
```

## Daily PnL
```
2026-04-24|305.94|0.0|0
2026-04-23|313.19|-7.26|0
2026-04-22|301.06|12.14|0
2026-04-21|296.96|4.1|0
2026-04-20|312.71|-15.75|0
2026-04-19|354.45|-41.74|0
2026-04-18|311.88|42.12|0
```

## Open Positions
```
none
```

## Diag Summary (last ~4h)
```
     35 trend_htf=ranging trend_mid=ranging skip=trend_mismatch
     21 trend=bullish skip=adx_low adx=10.8 min=20.0
     15 trend=bullish skip=adx_low adx=11.9 min=20.0
     12 trend=bullish skip=adx_low adx=12.8 min=20.0
     11 trend=bullish skip=adx_low adx=10.9 min=20.0
     10 trend=bullish skip=adx_low adx=11.1 min=20.0
     10 trend=bullish skip=adx_low adx=11.0 min=20.0
      9 trend=bullish skip=adx_low adx=9.8 min=20.0
      9 trend=bullish skip=adx_low adx=11.5 min=20.0
      9 trend=bullish skip=adx_low adx=10.7 min=20.0
      9 trend=bullish skip=adx_low adx=10.5 min=20.0
      8 trend=bullish skip=adx_low adx=13.4 min=20.0
      8 trend=bullish skip=adx_low adx=11.4 min=20.0
      7 trend=bullish skip=adx_low adx=11.7 min=20.0
      6 trend=bullish skip=adx_low adx=9.6 min=20.0
      5 trend=bullish skip=adx_low adx=10.4 min=20.0
      4 trend=bullish skip=adx_low adx=13.6 min=20.0
      3 trend=bullish skip=adx_low adx=9.9 min=20.0
      3 trend=bullish skip=adx_low adx=9.5 min=20.0
      3 trend=bullish skip=adx_low adx=11.8 min=20.0
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
[04:04:00] tick balance=$305.94
  diag: trend=bullish skip=adx_low adx=10.8 min=20.0
[04:05:02] tick balance=$305.94
  diag: trend=bullish skip=adx_low adx=10.9 min=20.0
[04:06:04] tick balance=$305.94
  diag: trend=bullish skip=adx_low adx=10.9 min=20.0
[04:07:07] tick balance=$305.94
  diag: trend=bullish skip=adx_low adx=10.9 min=20.0
[04:08:09] tick balance=$305.94
  diag: trend=bullish skip=adx_low adx=10.9 min=20.0
[04:09:11] tick balance=$305.94
  diag: trend=bullish skip=adx_low adx=10.9 min=20.0
[04:10:13] tick balance=$305.94
  diag: trend=bullish skip=adx_low adx=10.9 min=20.0
[04:11:15] tick balance=$305.94
  diag: trend=bullish skip=adx_low adx=10.9 min=20.0
[04:12:17] tick balance=$305.94
  diag: trend=bullish skip=adx_low adx=10.9 min=20.0
[04:13:19] tick balance=$305.94
  diag: trend=bullish skip=adx_low adx=10.9 min=20.0
[04:14:22] tick balance=$305.94
  diag: trend=bullish skip=adx_low adx=10.9 min=20.0
[04:15:24] tick balance=$305.94
  diag: trend=bullish skip=adx_low adx=11.8 min=20.0
[04:16:26] tick balance=$305.94
  diag: trend=bullish skip=adx_low adx=11.8 min=20.0
[04:17:28] tick balance=$305.94
  diag: trend=bullish skip=adx_low adx=11.8 min=20.0
[04:18:30] tick balance=$305.94
  diag: trend=bullish skip=adx_low adx=11.6 min=20.0
[04:19:32] tick balance=$305.94
  diag: trend=bullish skip=adx_low adx=11.6 min=20.0
[04:20:35] tick balance=$305.94
  diag: trend=bullish skip=adx_low adx=11.6 min=20.0
[04:21:37] tick balance=$305.94
  diag: trend=bullish skip=adx_low adx=11.3 min=20.0
[04:22:38] tick balance=$305.94
  diag: trend=bullish skip=adx_low adx=11.2 min=20.0
[04:23:40] tick balance=$305.94
  diag: trend=bullish skip=adx_low adx=11.1 min=20.0
[04:24:42] tick balance=$305.94
  diag: trend=bullish skip=adx_low adx=11.1 min=20.0
[04:25:44] tick balance=$305.94
  diag: trend=bullish skip=adx_low adx=11.1 min=20.0
[04:26:46] tick balance=$305.94
  diag: trend=bullish skip=adx_low adx=11.1 min=20.0
[04:27:49] tick balance=$305.94
  diag: trend=bullish skip=adx_low adx=11.0 min=20.0
[04:28:51] tick balance=$305.94
  diag: trend=bullish skip=adx_low adx=10.8 min=20.0
[04:29:53] tick balance=$305.94
  diag: trend=bullish skip=adx_low adx=10.8 min=20.0
[04:30:55] tick balance=$305.94
  diag: trend=bullish skip=adx_low adx=10.7 min=20.0
[04:31:57] tick balance=$305.94
  diag: trend=bullish skip=adx_low adx=10.7 min=20.0
[04:32:59] tick balance=$305.94
  diag: trend=bullish skip=adx_low adx=10.7 min=20.0
[04:34:01] tick balance=$305.94
  diag: trend=bullish skip=adx_low adx=10.7 min=20.0
[04:35:04] tick balance=$305.94
  diag: trend=bullish skip=adx_low adx=10.7 min=20.0
[04:36:06] tick balance=$305.94
  diag: trend=bullish skip=adx_low adx=10.7 min=20.0
[04:37:09] tick balance=$305.94
  diag: trend=bullish skip=adx_low adx=10.8 min=20.0
[04:38:11] tick balance=$305.94
  diag: trend=bullish skip=adx_low adx=10.8 min=20.0
[04:39:13] tick balance=$305.94
  diag: trend=bullish skip=adx_low adx=10.8 min=20.0
[04:40:16] tick balance=$305.94
  diag: trend=bullish skip=adx_low adx=10.8 min=20.0
[04:41:18] tick balance=$305.94
  diag: trend=bullish skip=adx_low adx=10.8 min=20.0
[04:42:20] tick balance=$305.94
  diag: trend=bullish skip=adx_low adx=10.8 min=20.0
[04:43:22] tick balance=$305.94
  diag: trend=bullish skip=adx_low adx=10.8 min=20.0
[04:44:25] tick balance=$305.94
  diag: trend=bullish skip=adx_low adx=10.8 min=20.0
[04:45:27] tick balance=$305.94
  diag: trend=bullish skip=adx_low adx=10.9 min=20.0
[04:46:30] tick balance=$305.94
  diag: trend=bullish skip=adx_low adx=11.0 min=20.0
[04:47:32] tick balance=$305.94
  diag: trend=bullish skip=adx_low adx=11.0 min=20.0
[04:48:34] tick balance=$305.94
  diag: trend=bullish skip=adx_low adx=11.0 min=20.0
[04:49:36] tick balance=$305.94
  diag: trend=bullish skip=adx_low adx=11.0 min=20.0
[04:50:38] tick balance=$305.94
  diag: trend=bullish skip=adx_low adx=11.0 min=20.0
[04:51:41] tick balance=$305.94
  diag: trend=bullish skip=adx_low adx=11.0 min=20.0
[04:52:44] tick balance=$305.94
  diag: trend=bullish skip=adx_low adx=11.0 min=20.0
[04:53:45] tick balance=$305.94
  diag: trend=bullish skip=adx_low adx=11.0 min=20.0
[04:54:48] tick balance=$305.94
  diag: trend=bullish skip=adx_low adx=11.0 min=20.0
```
