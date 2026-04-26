# Bot Snapshot — 2026-04-26 14:55 UTC

## Service: active
balance=$305.94

## Config
POST_CLOSE_COOLDOWN: int = 180 # 3 мин техническая пауза после закрытия
RISK_PCT: float = 0.03 # 1% для старта на HYPE (вернём к 5% после 5+ сделок)
ADX_MIN: float = 15.0 # ADX < 20 → choppy market, skip entry

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
    137 trend_htf=ranging trend_mid=ranging skip=trend_mismatch
     15 trend=bearish skip=adx_low adx=9.0 min=20.0
     14 trend=bearish skip=adx_low adx=9.4 min=20.0
     14 trend=bearish skip=adx_low adx=8.7 min=20.0
     13 trend=bearish skip=adx_low adx=9.6 min=20.0
     13 trend=bearish skip=adx_low adx=8.9 min=20.0
      9 trend=bearish skip=adx_low adx=9.8 min=20.0
      6 trend=bearish skip=adx_low adx=9.1 min=20.0
      5 trend=bearish skip=adx_low adx=9.7 min=20.0
      3 trend=bearish skip=adx_low adx=9.5 min=20.0
      1 trend=bearish skip=trend_immature trend_age_s=61 need_s=900
      1 trend=bearish skip=trend_immature trend_age_s=435 need_s=900
      1 trend=bearish skip=trend_immature trend_age_s=372 need_s=900
      1 trend=bearish skip=trend_immature trend_age_s=310 need_s=900
      1 trend=bearish skip=trend_immature trend_age_s=247 need_s=900
      1 trend=bearish skip=trend_immature trend_age_s=185 need_s=900
      1 trend=bearish skip=trend_immature trend_age_s=124 need_s=900
      1 trend=bearish skip=trend_immature trend_age_s=0 need_s=900
      1 trend=bearish skip=adx_low adx=8.5 min=20.0
      1 trend=bearish skip=adx_low adx=10.1 min=20.0
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
  range: regime=trend atr_ratio=0.91 adx=21.5 t_h4=ranging t_h1=ranging tf_conflict_s=5275
[16:20:54] tick balance=$305.94
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
  range: regime=trend atr_ratio=0.96 adx=20.9 t_h4=ranging t_h1=ranging tf_conflict_s=5337
[16:21:59] tick balance=$305.94
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
  range: regime=trend atr_ratio=0.97 adx=20.8 t_h4=ranging t_h1=ranging tf_conflict_s=5404
[16:23:04] tick balance=$305.94
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
  range: regime=trend atr_ratio=0.97 adx=20.8 t_h4=ranging t_h1=ranging tf_conflict_s=5468
[16:24:08] tick balance=$305.94
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
  range: regime=trend atr_ratio=0.97 adx=20.8 t_h4=ranging t_h1=ranging tf_conflict_s=5530
[16:25:10] tick balance=$305.94
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
  range: regime=trend atr_ratio=0.97 adx=20.8 t_h4=ranging t_h1=ranging tf_conflict_s=5594
[16:26:14] tick balance=$305.94
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
  range: regime=trend atr_ratio=0.97 adx=20.7 t_h4=ranging t_h1=ranging tf_conflict_s=5658
[16:27:18] tick balance=$305.94
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
  range: regime=trend atr_ratio=0.99 adx=20.3 t_h4=ranging t_h1=ranging tf_conflict_s=5722
[16:28:21] tick balance=$305.94
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
  range: regime=trend atr_ratio=0.99 adx=20.3 t_h4=ranging t_h1=ranging tf_conflict_s=5784
[16:29:24] tick balance=$305.94
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
  range: regime=trend atr_ratio=0.99 adx=20.3 t_h4=ranging t_h1=ranging tf_conflict_s=5848
[16:30:28] tick balance=$305.94
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
  range: regime=trend atr_ratio=0.95 adx=19.7 t_h4=ranging t_h1=ranging tf_conflict_s=5912
[16:31:32] tick balance=$305.94
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
  range: regime=trend atr_ratio=0.98 adx=19.6 t_h4=ranging t_h1=ranging tf_conflict_s=5975
[16:32:35] tick balance=$305.94
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
  range: regime=trend atr_ratio=0.98 adx=19.6 t_h4=ranging t_h1=ranging tf_conflict_s=6039
[16:33:38] tick balance=$305.94
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
  range: regime=trend atr_ratio=0.98 adx=19.6 t_h4=ranging t_h1=ranging tf_conflict_s=6102
[16:34:41] tick balance=$305.94
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
  range: regime=trend atr_ratio=0.98 adx=19.6 t_h4=ranging t_h1=ranging tf_conflict_s=6165
[16:35:45] tick balance=$305.94
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
  range: regime=trend atr_ratio=0.99 adx=19.5 t_h4=ranging t_h1=ranging tf_conflict_s=6229
[16:36:48] tick balance=$305.94
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
  range: regime=trend atr_ratio=0.99 adx=19.5 t_h4=ranging t_h1=ranging tf_conflict_s=6292
[16:37:52] tick balance=$305.94
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
  range: regime=trend atr_ratio=0.99 adx=19.5 t_h4=ranging t_h1=ranging tf_conflict_s=6355
[16:38:55] tick balance=$305.94
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
  range: regime=trend atr_ratio=0.99 adx=19.5 t_h4=ranging t_h1=ranging tf_conflict_s=6418
[16:39:58] tick balance=$305.94
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
  range: regime=trend atr_ratio=0.99 adx=19.5 t_h4=ranging t_h1=ranging tf_conflict_s=6481
[16:41:01] tick balance=$305.94
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
  range: regime=trend atr_ratio=0.99 adx=19.5 t_h4=ranging t_h1=ranging tf_conflict_s=6544
[16:42:04] tick balance=$305.94
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
  range: regime=trend atr_ratio=0.99 adx=19.3 t_h4=ranging t_h1=ranging tf_conflict_s=6607
[16:43:08] tick balance=$305.94
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
  range: regime=trend atr_ratio=0.99 adx=19.3 t_h4=ranging t_h1=ranging tf_conflict_s=6671
[16:44:11] tick balance=$305.94
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
  range: regime=trend atr_ratio=0.99 adx=19.3 t_h4=ranging t_h1=ranging tf_conflict_s=6734
[16:45:13] tick balance=$305.94
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
  range: regime=trend atr_ratio=0.96 adx=18.4 t_h4=ranging t_h1=ranging tf_conflict_s=6796
[16:46:16] tick balance=$305.94
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
  range: regime=trend atr_ratio=0.97 adx=18.4 t_h4=ranging t_h1=ranging tf_conflict_s=6862
[16:47:22] tick balance=$305.94
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
  range: regime=trend atr_ratio=0.98 adx=18.4 t_h4=ranging t_h1=ranging tf_conflict_s=6925
[16:48:26] tick balance=$305.94
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
  range: regime=trend atr_ratio=0.98 adx=18.4 t_h4=ranging t_h1=ranging tf_conflict_s=6989
[16:49:29] tick balance=$305.94
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
  range: regime=trend atr_ratio=0.98 adx=18.4 t_h4=ranging t_h1=ranging tf_conflict_s=7053
[16:50:33] tick balance=$305.94
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
  range: regime=trend atr_ratio=1.0 adx=18.1 t_h4=ranging t_h1=ranging tf_conflict_s=7116
[16:51:36] tick balance=$305.94
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
  range: regime=trend atr_ratio=1.01 adx=18.1 t_h4=ranging t_h1=ranging tf_conflict_s=7179
[16:52:39] tick balance=$305.94
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
  range: regime=trend atr_ratio=1.01 adx=18.1 t_h4=ranging t_h1=ranging tf_conflict_s=7242
[16:53:42] tick balance=$305.94
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
  range: regime=trend atr_ratio=1.01 adx=18.1 t_h4=ranging t_h1=ranging tf_conflict_s=7305
[16:54:45] tick balance=$305.94
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
  range: regime=trend atr_ratio=1.02 adx=18.3 t_h4=ranging t_h1=ranging tf_conflict_s=7369
```
