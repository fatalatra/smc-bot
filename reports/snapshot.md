# Bot Snapshot — 2026-04-20 18:55 UTC

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
     79 trend_htf=ranging trend_mid=ranging skip=trend_mismatch
     23 trend=bearish skip=ema_overextended price=41.0 ema20_h4=42.5 dist=1.5 max_dist=1.3
     11 trend=bearish skip=ema_overextended price=40.9 ema20_h4=42.5 dist=1.6 max_dist=1.3
      9 trend=bullish skip=adx_low adx=11.7 min=20.0
      9 trend=bearish skip=ema_overextended price=41.0 ema20_h4=42.5 dist=1.4 max_dist=1.3
      8 trend=bearish skip=ema_overextended price=41.1 ema20_h4=42.6 dist=1.5 max_dist=1.4
      8 trend=bearish skip=ema_overextended price=41.0 ema20_h4=42.6 dist=1.6 max_dist=1.4
      6 trend=bearish skip=ema_overextended price=41.2 ema20_h4=42.6 dist=1.4 max_dist=1.4
      6 trend=bearish skip=adx_low adx=19.2 min=20.0
      5 trend=bullish skip=adx_low adx=12.8 min=20.0
      5 trend=bearish skip=ema_overextended price=41.2 ema20_h4=42.6 dist=1.5 max_dist=1.4
      5 trend=bearish skip=ema_overextended price=41.1 ema20_h4=42.5 dist=1.4 max_dist=1.3
      4 trend=bullish skip=adx_low adx=12.3 min=20.0
      4 trend=bearish skip=ema_overextended price=40.8 ema20_h4=42.5 dist=1.6 max_dist=1.3
      3 trend_htf=bearish trend_mid=bullish skip=trend_mismatch
      3 trend=bearish skip=ema_overextended price=40.9 ema20_h4=42.5 dist=1.5 max_dist=1.3
      2 trend=bullish skip=trend_immature trend_age_s=62 need_s=900
      2 trend=bullish skip=trend_immature trend_age_s=0 need_s=900
      2 trend=bullish skip=adx_low adx=12.9 min=20.0
      2 trend=bearish skip=ema_overextended price=41.3 ema20_h4=42.6 dist=1.4 max_dist=1.4
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
[20:03:40] tick balance=$296.96
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:04:41] tick balance=$296.96
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:05:43] tick balance=$296.96
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:06:45] tick balance=$296.96
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:07:47] tick balance=$296.96
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:08:49] tick balance=$296.96
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:09:52] tick balance=$296.96
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:10:54] tick balance=$296.96
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:11:57] tick balance=$296.96
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:12:59] tick balance=$296.96
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:14:01] tick balance=$296.96
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:15:03] tick balance=$296.96
  diag: trend=bullish skip=trend_immature trend_age_s=0 need_s=900
[20:16:05] tick balance=$296.96
  diag: trend=bullish skip=trend_immature trend_age_s=62 need_s=900
[20:17:08] tick balance=$296.96
  diag: trend=bullish skip=trend_immature trend_age_s=124 need_s=900
[20:18:09] tick balance=$296.96
  diag: trend=bullish skip=trend_immature trend_age_s=186 need_s=900
[20:19:12] tick balance=$296.96
  diag: trend=bullish skip=trend_immature trend_age_s=248 need_s=900
[20:20:14] tick balance=$296.96
  diag: trend=bullish skip=trend_immature trend_age_s=310 need_s=900
[20:21:16] tick balance=$296.96
  diag: trend=bullish skip=trend_immature trend_age_s=372 need_s=900
[20:22:18] tick balance=$296.96
  diag: trend=bullish skip=trend_immature trend_age_s=434 need_s=900
[20:23:20] tick balance=$296.96
  diag: trend=bullish skip=trend_immature trend_age_s=497 need_s=900
[20:24:23] tick balance=$296.96
  diag: trend=bullish skip=trend_immature trend_age_s=559 need_s=900
[20:25:25] tick balance=$296.96
  diag: trend=bullish skip=trend_immature trend_age_s=621 need_s=900
[20:26:28] tick balance=$296.96
  diag: trend=bullish skip=trend_immature trend_age_s=684 need_s=900
[20:27:31] tick balance=$296.96
  diag: trend=bullish skip=trend_immature trend_age_s=748 need_s=900
[20:28:34] tick balance=$296.96
  diag: trend=bullish skip=trend_immature trend_age_s=810 need_s=900
[20:29:36] tick balance=$296.96
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:30:39] tick balance=$296.96
  diag: trend=bullish skip=adx_low adx=12.9 min=20.0
[20:31:40] tick balance=$296.96
  diag: trend=bullish skip=adx_low adx=12.9 min=20.0
[20:32:42] tick balance=$296.96
  diag: trend=bullish skip=adx_low adx=12.8 min=20.0
[20:33:45] tick balance=$296.96
  diag: trend=bullish skip=adx_low adx=12.8 min=20.0
[20:34:47] tick balance=$296.96
  diag: trend=bullish skip=adx_low adx=12.8 min=20.0
[20:35:49] tick balance=$296.96
  diag: trend=bullish skip=adx_low adx=12.8 min=20.0
[20:36:52] tick balance=$296.96
  diag: trend=bullish skip=adx_low adx=12.8 min=20.0
[20:37:54] tick balance=$296.96
  diag: trend=bullish skip=adx_low adx=12.6 min=20.0
[20:38:56] tick balance=$296.96
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:39:59] tick balance=$296.96
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:41:01] tick balance=$296.96
  diag: trend=bullish skip=adx_low adx=12.3 min=20.0
[20:42:03] tick balance=$296.96
  diag: trend=bullish skip=adx_low adx=12.3 min=20.0
[20:43:06] tick balance=$296.96
  diag: trend=bullish skip=adx_low adx=12.3 min=20.0
[20:44:08] tick balance=$296.96
  diag: trend=bullish skip=adx_low adx=12.3 min=20.0
[20:45:11] tick balance=$296.96
  diag: trend=bullish skip=adx_low adx=11.7 min=20.0
[20:46:13] tick balance=$296.96
  diag: trend=bullish skip=adx_low adx=11.7 min=20.0
[20:47:16] tick balance=$296.96
  diag: trend=bullish skip=adx_low adx=11.7 min=20.0
[20:48:19] tick balance=$296.96
  diag: trend=bullish skip=adx_low adx=11.7 min=20.0
[20:49:22] tick balance=$296.96
  diag: trend=bullish skip=adx_low adx=11.7 min=20.0
[20:50:24] tick balance=$296.96
  diag: trend=bullish skip=adx_low adx=11.7 min=20.0
[20:51:27] tick balance=$296.96
  diag: trend=bullish skip=adx_low adx=11.7 min=20.0
[20:52:29] tick balance=$296.96
  diag: trend=bullish skip=adx_low adx=11.7 min=20.0
[20:53:31] tick balance=$296.96
  diag: trend=bullish skip=adx_low adx=11.7 min=20.0
[20:54:34] tick balance=$296.96
  diag: trend=bullish skip=adx_low adx=11.8 min=20.0
```
