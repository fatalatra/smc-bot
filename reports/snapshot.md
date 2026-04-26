# Bot Snapshot — 2026-04-26 10:55 UTC

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
2026-04-26|305.94|0.0|0
2026-04-25|305.94|0.0|0
2026-04-24|305.94|0.0|0
2026-04-23|313.19|-7.26|0
2026-04-22|301.06|12.14|0
2026-04-21|296.96|4.1|0
2026-04-20|312.71|-15.75|0
```

## Open Positions
```
none
```

## Diag Summary (last ~4h)
```
     65 trend_htf=ranging trend_mid=ranging skip=trend_mismatch
     33 trend=bearish skip=adx_low adx=10.6 min=20.0
     24 trend=bearish skip=adx_low adx=10.7 min=20.0
     13 trend=bearish skip=adx_low adx=11.2 min=20.0
     10 trend=bearish skip=adx_low adx=9.7 min=20.0
      9 trend=bearish skip=adx_low adx=9.2 min=20.0
      9 trend=bearish skip=adx_low adx=12.7 min=20.0
      9 trend=bearish skip=adx_low adx=10.5 min=20.0
      7 trend=bearish skip=adx_low adx=13.0 min=20.0
      7 trend=bearish skip=adx_low adx=11.9 min=20.0
      7 trend=bearish skip=adx_low adx=10.0 min=20.0
      6 trend=bearish skip=adx_low adx=9.0 min=20.0
      6 trend=bearish skip=adx_low adx=12.6 min=20.0
      4 trend=bearish skip=adx_low adx=9.8 min=20.0
      3 trend=bearish skip=adx_low adx=9.5 min=20.0
      3 trend=bearish skip=adx_low adx=10.8 min=20.0
      2 trend=bearish skip=adx_low adx=8.9 min=20.0
      2 trend=bearish skip=adx_low adx=12.8 min=20.0
      2 trend=bearish skip=adx_low adx=10.3 min=20.0
      1 trend=bearish skip=trend_immature trend_age_s=869 need_s=900
```

## Errors
```
    self.gen.throw(typ, value, traceback)
  File "/root/smc-bot/venv/lib/python3.11/site-packages/httpcore/_exceptions.py", line 14, in map_exceptions
httpcore.ConnectError: [Errno -2] Name or service not known
The above exception was the direct cause of the following exception:
Traceback (most recent call last):
    with map_httpcore_exceptions():
    self.gen.throw(typ, value, traceback)
  File "/root/smc-bot/venv/lib/python3.11/site-packages/httpx/_transports/default.py", line 118, in map_httpcore_exceptions
httpx.ConnectError: [Errno -2] Name or service not known
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
  diag: trend=bearish skip=adx_low adx=10.0 min=20.0
[12:04:19] tick balance=$305.94
  diag: trend=bearish skip=adx_low adx=10.0 min=20.0
[12:05:21] tick balance=$305.94
  diag: trend=bearish skip=adx_low adx=10.0 min=20.0
[12:06:24] tick balance=$305.94
  diag: trend=bearish skip=adx_low adx=10.0 min=20.0
[12:07:25] tick balance=$305.94
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[12:08:28] tick balance=$305.94
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[12:09:30] tick balance=$305.94
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[12:10:33] tick balance=$305.94
  diag: trend=bearish skip=adx_low adx=9.7 min=20.0
[12:11:35] tick balance=$305.94
  diag: trend=bearish skip=adx_low adx=9.7 min=20.0
[12:12:37] tick balance=$305.94
  diag: trend=bearish skip=adx_low adx=9.7 min=20.0
[12:13:39] tick balance=$305.94
  diag: trend=bearish skip=adx_low adx=9.7 min=20.0
[12:14:41] tick balance=$305.94
  diag: trend=bearish skip=adx_low adx=9.7 min=20.0
[12:15:44] tick balance=$305.94
  diag: trend=bearish skip=adx_low adx=9.2 min=20.0
[12:16:46] tick balance=$305.94
  diag: trend=bearish skip=adx_low adx=9.2 min=20.0
[12:17:48] tick balance=$305.94
  diag: trend=bearish skip=adx_low adx=9.2 min=20.0
[12:18:50] tick balance=$305.94
  diag: trend=bearish skip=adx_low adx=9.2 min=20.0
[12:19:52] tick balance=$305.94
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[12:20:54] tick balance=$305.94
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[12:21:56] tick balance=$305.94
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[12:22:58] tick balance=$305.94
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[12:24:01] tick balance=$305.94
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[12:25:03] tick balance=$305.94
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[12:26:06] tick balance=$305.94
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[12:27:08] tick balance=$305.94
  diag: trend=bearish skip=adx_low adx=9.2 min=20.0
[12:28:10] tick balance=$305.94
  diag: trend=bearish skip=adx_low adx=9.2 min=20.0
[12:29:12] tick balance=$305.94
  diag: trend=bearish skip=adx_low adx=9.2 min=20.0
[12:30:14] tick balance=$305.94
  diag: trend=bearish skip=adx_low adx=8.7 min=20.0
[12:31:16] tick balance=$305.94
  diag: trend=bearish skip=adx_low adx=8.9 min=20.0
[12:32:18] tick balance=$305.94
  diag: trend=bearish skip=adx_low adx=8.9 min=20.0
[12:33:19] tick balance=$305.94
  diag: trend=bearish skip=adx_low adx=9.0 min=20.0
[12:34:21] tick balance=$305.94
  diag: trend=bearish skip=adx_low adx=9.0 min=20.0
[12:35:23] tick balance=$305.94
  diag: trend=bearish skip=adx_low adx=9.0 min=20.0
[12:36:26] tick balance=$305.94
  diag: trend=bearish skip=adx_low adx=9.0 min=20.0
[12:37:29] tick balance=$305.94
  diag: trend=bearish skip=adx_low adx=9.0 min=20.0
[12:38:31] tick balance=$305.94
  diag: trend=bearish skip=adx_low adx=9.0 min=20.0
[12:39:33] tick balance=$305.94
  diag: trend=bearish skip=adx_low adx=9.2 min=20.0
[12:40:35] tick balance=$305.94
  diag: trend=bearish skip=adx_low adx=9.2 min=20.0
[12:41:37] tick balance=$305.94
  diag: trend=bearish skip=adx_low adx=9.3 min=20.0
[12:42:39] tick balance=$305.94
  diag: trend=bearish skip=adx_low adx=9.5 min=20.0
[12:43:42] tick balance=$305.94
  diag: trend=bearish skip=adx_low adx=9.5 min=20.0
[12:44:44] tick balance=$305.94
  diag: trend=bearish skip=adx_low adx=9.5 min=20.0
[12:45:46] tick balance=$305.94
  diag: trend=bearish skip=adx_low adx=9.7 min=20.0
[12:46:47] tick balance=$305.94
  diag: trend=bearish skip=adx_low adx=9.7 min=20.0
[12:47:49] tick balance=$305.94
  diag: trend=bearish skip=adx_low adx=9.7 min=20.0
[12:48:51] tick balance=$305.94
  diag: trend=bearish skip=adx_low adx=9.7 min=20.0
[12:49:52] tick balance=$305.94
  diag: trend=bearish skip=adx_low adx=9.7 min=20.0
[12:50:54] tick balance=$305.94
  diag: trend=bearish skip=adx_low adx=9.8 min=20.0
[12:51:55] tick balance=$305.94
  diag: trend=bearish skip=adx_low adx=9.8 min=20.0
[12:52:57] tick balance=$305.94
  diag: trend=bearish skip=adx_low adx=9.8 min=20.0
[12:53:58] tick balance=$305.94
  diag: trend=bearish skip=adx_low adx=9.8 min=20.0
[12:55:00] tick balance=$305.94
```
