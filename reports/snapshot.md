# Bot Snapshot — 2026-04-17 06:55 UTC

## Service: active
balance=$328.70

## Config
POST_CLOSE_COOLDOWN: int = 180 # 3 мин техническая пауза после закрытия
RISK_PCT: float = 0.05 # 5% от баланса на сделку
ADX_MIN: float = 20.0 # ADX < 20 → choppy market, skip entry

## Trades (last 20)
```
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
3|SELL|71597.7|13.27|closed|2026-04-12 10:25:37|2026-04-12 10:42:19
2|SELL|73451.8|13.15|closed|2026-04-11 20:18:03|2026-04-12 08:14:54
1|SELL|73575.9|13.15|closed|2026-04-11 20:01:37|2026-04-12 08:14:54
```

## Daily PnL
```
2026-04-17|328.7|0.0|0
2026-04-16|381.29|-52.59|0
2026-04-15|363.1|17.9|0
2026-04-14|413.74|-50.64|0
2026-04-13|413.74|0.0|0
2026-04-12|423.86|-10.12|0
2026-04-11|457.33|-130.15|0
```

## Open Positions
```
none
```

## Diag Summary (last ~4h)
```
    210 trend_htf=ranging trend_mid=ranging skip=trend_mismatch
      3 trend=bearish skip=atr_low ratio=0.78 min=0.8
      2 trend=bearish skip=atr_low ratio=0.75 min=0.8
      2 trend=bearish skip=atr_low ratio=0.74 min=0.8
      1 trend=bearish skip=trend_immature trend_age_s=870 need_s=900
      1 trend=bearish skip=trend_immature trend_age_s=808 need_s=900
      1 trend=bearish skip=trend_immature trend_age_s=746 need_s=900
      1 trend=bearish skip=trend_immature trend_age_s=684 need_s=900
      1 trend=bearish skip=trend_immature trend_age_s=62 need_s=900
      1 trend=bearish skip=trend_immature trend_age_s=622 need_s=900
      1 trend=bearish skip=trend_immature trend_age_s=560 need_s=900
      1 trend=bearish skip=trend_immature trend_age_s=498 need_s=900
      1 trend=bearish skip=trend_immature trend_age_s=436 need_s=900
      1 trend=bearish skip=trend_immature trend_age_s=374 need_s=900
      1 trend=bearish skip=trend_immature trend_age_s=312 need_s=900
      1 trend=bearish skip=trend_immature trend_age_s=250 need_s=900
      1 trend=bearish skip=trend_immature trend_age_s=187 need_s=900
      1 trend=bearish skip=trend_immature trend_age_s=125 need_s=900
      1 trend=bearish skip=trend_immature trend_age_s=0 need_s=900
      1 trend=bearish skip=atr_low ratio=0.8 min=0.8
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
[08:04:01] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[08:05:03] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[08:06:05] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[08:07:07] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[08:08:09] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[08:09:12] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[08:10:14] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[08:11:16] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[08:12:18] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[08:13:20] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[08:14:22] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[08:15:24] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[08:16:26] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[08:17:28] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[08:18:31] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[08:19:34] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[08:20:36] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[08:21:38] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[08:22:39] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[08:23:42] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[08:24:43] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[08:25:45] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[08:26:48] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[08:27:49] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[08:28:51] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[08:29:53] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[08:30:55] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[08:31:57] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[08:32:59] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[08:34:00] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[08:35:02] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[08:36:04] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[08:37:06] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[08:38:08] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[08:39:09] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[08:40:11] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[08:41:13] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[08:42:15] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[08:43:16] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[08:44:19] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[08:45:20] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[08:46:23] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[08:47:25] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[08:48:27] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[08:49:30] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[08:50:31] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[08:51:34] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[08:52:35] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[08:53:37] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[08:54:39] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
```
