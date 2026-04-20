# Bot Snapshot — 2026-04-20 06:55 UTC

## Service: active
balance=$296.96

## Config
POST_CLOSE_COOLDOWN: int = 180 # 3 мин техническая пауза после закрытия
RISK_PCT: float = 0.05 # 5% от баланса на сделку
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
2026-04-20|312.71|-15.75|0
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
     16 trend=bearish skip=atr_low ratio=0.71 min=0.8
     16 trend=bearish skip=adx_low adx=18.8 min=20.0
     11 trend=bearish skip=atr_low ratio=0.69 min=0.8
     10 trend=bearish skip=atr_low ratio=0.79 min=0.8
     10 trend=bearish skip=adx_low adx=19.7 min=20.0
      9 trend=bearish skip=atr_low ratio=0.74 min=0.8
      9 trend=bearish skip=atr_low ratio=0.73 min=0.8
      8 trend=bearish skip=adx_low adx=19.9 min=20.0
      6 trend=bearish skip=atr_low ratio=0.7 min=0.8
      6 trend=bearish skip=adx_low adx=20.0 min=20.0
      5 trend_htf=ranging trend_mid=ranging skip=trend_mismatch
      5 trend=bearish skip=atr_low ratio=0.77 min=0.8
      5 trend=bearish skip=atr_low ratio=0.72 min=0.8
      5 trend=bearish skip=atr_low ratio=0.64 min=0.8
      5 trend=bearish skip=atr_low ratio=0.62 min=0.8
      4 trend=bearish skip=atr_low ratio=0.67 min=0.8
      4 trend=bearish skip=adx_low adx=19.8 min=20.0
      4 trend=bearish skip=adx_low adx=18.6 min=20.0
      4 trend=bearish skip=adx_low adx=17.9 min=20.0
      3 trend=bearish skip=atr_low ratio=0.61 min=0.8
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
[08:04:22] tick balance=$296.96
[sync] trade #28 SELL entry=74162.8 closed (sl) at price=74397.7
[real_pnl] trade #28: profit=-15.75 open_fee=0.00 close_fee=0.00 => net=-15.75
  diag: skip=post_close_cooldown wait_s=178
[08:05:26] tick balance=$296.96
  diag: skip=post_close_cooldown wait_s=115
[08:06:28] tick balance=$296.96
  diag: skip=post_close_cooldown wait_s=53
[08:07:31] tick balance=$296.96
  diag: trend=bearish skip=adx_low adx=19.7 min=20.0
[08:08:33] tick balance=$296.96
  diag: trend=bearish skip=adx_low adx=19.7 min=20.0
[08:09:36] tick balance=$296.96
  diag: trend=bearish skip=adx_low adx=19.7 min=20.0
[08:10:37] tick balance=$296.96
  diag: trend=bearish skip=adx_low adx=19.7 min=20.0
[08:11:40] tick balance=$296.96
  diag: trend=bearish skip=adx_low adx=19.7 min=20.0
[08:12:42] tick balance=$296.96
  diag: trend=bearish skip=adx_low adx=19.7 min=20.0
[08:13:45] tick balance=$296.96
  diag: trend=bearish skip=adx_low adx=19.7 min=20.0
[08:14:47] tick balance=$296.96
  diag: trend=bearish skip=adx_low adx=19.7 min=20.0
[08:15:49] tick balance=$296.96
  diag: trend=bearish skip=adx_low adx=18.8 min=20.0
[08:16:51] tick balance=$296.96
  diag: trend=bearish skip=adx_low adx=18.8 min=20.0
[08:17:54] tick balance=$296.96
  diag: trend=bearish skip=adx_low adx=18.8 min=20.0
[08:18:56] tick balance=$296.96
  diag: trend=bearish skip=adx_low adx=18.8 min=20.0
[08:19:58] tick balance=$296.96
  diag: trend=bearish skip=adx_low adx=18.8 min=20.0
[08:21:01] tick balance=$296.96
  diag: trend=bearish skip=adx_low adx=18.8 min=20.0
[08:22:03] tick balance=$296.96
  diag: trend=bearish skip=adx_low adx=18.8 min=20.0
[08:23:05] tick balance=$296.96
  diag: trend=bearish skip=adx_low adx=18.8 min=20.0
[08:24:08] tick balance=$296.96
  diag: trend=bearish skip=adx_low adx=18.8 min=20.0
[08:25:10] tick balance=$296.96
  diag: trend=bearish skip=adx_low adx=18.8 min=20.0
[08:26:12] tick balance=$296.96
  diag: trend=bearish skip=adx_low adx=18.8 min=20.0
[08:27:14] tick balance=$296.96
  diag: trend=bearish skip=adx_low adx=18.8 min=20.0
[08:28:16] tick balance=$296.96
  diag: trend=bearish skip=adx_low adx=18.8 min=20.0
[08:29:19] tick balance=$296.96
  diag: trend=bearish skip=adx_low adx=18.8 min=20.0
[08:30:21] tick balance=$296.96
  diag: trend=bearish skip=adx_low adx=17.8 min=20.0
[08:31:23] tick balance=$296.96
  diag: trend=bearish skip=adx_low adx=17.6 min=20.0
[08:32:25] tick balance=$296.96
  diag: trend=bearish skip=adx_low adx=17.6 min=20.0
[08:33:28] tick balance=$296.96
  diag: trend=bearish skip=adx_low adx=17.7 min=20.0
[08:34:30] tick balance=$296.96
  diag: trend=bearish skip=adx_low adx=17.7 min=20.0
[08:35:32] tick balance=$296.96
  diag: trend=bearish skip=adx_low adx=17.7 min=20.0
[08:36:35] tick balance=$296.96
  diag: trend=bearish skip=adx_low adx=17.9 min=20.0
[08:37:37] tick balance=$296.96
  diag: trend=bearish skip=adx_low adx=17.9 min=20.0
[08:38:40] tick balance=$296.96
  diag: trend=bearish skip=adx_low adx=17.9 min=20.0
[08:39:42] tick balance=$296.96
  diag: trend=bearish skip=adx_low adx=17.9 min=20.0
[08:40:44] tick balance=$296.96
  diag: trend=bearish skip=adx_low adx=18.7 min=20.0
[08:41:46] tick balance=$296.96
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[08:42:48] tick balance=$296.96
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[08:43:50] tick balance=$296.96
  diag: trend=bearish skip=adx_low adx=19.3 min=20.0
[08:44:52] tick balance=$296.96
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[08:45:54] tick balance=$296.96
  diag: trend=bearish skip=adx_low adx=19.9 min=20.0
[08:46:57] tick balance=$296.96
  diag: trend=bearish skip=adx_low adx=19.9 min=20.0
[08:47:59] tick balance=$296.96
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[08:49:02] tick balance=$296.96
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[08:50:04] tick balance=$296.96
  diag: trend=bearish skip=adx_low adx=19.9 min=20.0
[08:51:07] tick balance=$296.96
  diag: trend=bearish skip=adx_low adx=19.9 min=20.0
[08:52:10] tick balance=$296.96
  diag: trend=bearish skip=adx_low adx=19.9 min=20.0
[08:53:12] tick balance=$296.96
  diag: trend=bearish skip=adx_low adx=19.9 min=20.0
[08:54:14] tick balance=$296.96
  diag: trend=bearish skip=adx_low adx=19.9 min=20.0
```
