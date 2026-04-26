# Bot Snapshot — 2026-04-26 18:55 UTC

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
    211 trend_htf=ranging trend_mid=ranging skip=trend_mismatch
      7 trend=bullish skip=adx_low adx=11.2 min=15.0
      4 trend=bullish skip=adx_low adx=11.0 min=15.0
      2 trend=bullish skip=adx_low adx=11.1 min=15.0
      1 trend=bullish skip=trend_immature trend_age_s=877 need_s=900
      1 trend=bullish skip=trend_immature trend_age_s=814 need_s=900
      1 trend=bullish skip=trend_immature trend_age_s=752 need_s=900
      1 trend=bullish skip=trend_immature trend_age_s=689 need_s=900
      1 trend=bullish skip=trend_immature trend_age_s=62 need_s=900
      1 trend=bullish skip=trend_immature trend_age_s=627 need_s=900
      1 trend=bullish skip=trend_immature trend_age_s=564 need_s=900
      1 trend=bullish skip=trend_immature trend_age_s=501 need_s=900
      1 trend=bullish skip=trend_immature trend_age_s=439 need_s=900
      1 trend=bullish skip=trend_immature trend_age_s=376 need_s=900
      1 trend=bullish skip=trend_immature trend_age_s=313 need_s=900
      1 trend=bullish skip=trend_immature trend_age_s=250 need_s=900
      1 trend=bullish skip=trend_immature trend_age_s=187 need_s=900
      1 trend=bullish skip=trend_immature trend_age_s=125 need_s=900
      1 trend=bullish skip=trend_immature trend_age_s=0 need_s=900
      1 trend=bullish skip=adx_low adx=10.9 min=15.0
```

## Errors
```
    self.gen.throw(typ, value, traceback)
  File "/root/smc-bot/venv/lib/python3.11/site-packages/httpcore/_exceptions.py", line 14, in map_exceptions
The above exception was the direct cause of the following exception:
Traceback (most recent call last):
    with map_httpcore_exceptions():
    self.gen.throw(typ, value, traceback)
  File "/root/smc-bot/venv/lib/python3.11/site-packages/httpx/_transports/default.py", line 118, in map_httpcore_exceptions
[ERROR] [SSL: TLSV1_ALERT_INTERNAL_ERROR] tlsv1 alert internal error (_ssl.c:992)
Traceback (most recent call last):
  File "/root/smc-bot/venv/lib/python3.11/site-packages/httpx/_transports/default.py", line 101, in map_httpcore_exceptions
    with map_exceptions(exc_map):
    self.gen.throw(typ, value, traceback)
  File "/root/smc-bot/venv/lib/python3.11/site-packages/httpcore/_exceptions.py", line 14, in map_exceptions
httpcore.ConnectError: [SSL: TLSV1_ALERT_INTERNAL_ERROR] tlsv1 alert internal error (_ssl.c:992)
The above exception was the direct cause of the following exception:
Traceback (most recent call last):
    with map_httpcore_exceptions():
    self.gen.throw(typ, value, traceback)
  File "/root/smc-bot/venv/lib/python3.11/site-packages/httpx/_transports/default.py", line 118, in map_httpcore_exceptions
httpx.ConnectError: [SSL: TLSV1_ALERT_INTERNAL_ERROR] tlsv1 alert internal error (_ssl.c:992)
```

## Last 100 Log Lines
```
  range: regime=trend atr_ratio=1.04 adx=14.1 t_h4=ranging t_h1=ranging tf_conflict_s=19659
[20:20:38] tick balance=$305.94
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
  range: regime=trend atr_ratio=1.04 adx=14.1 t_h4=ranging t_h1=ranging tf_conflict_s=19721
[20:21:40] tick balance=$305.94
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
  range: regime=trend atr_ratio=1.04 adx=14.1 t_h4=ranging t_h1=ranging tf_conflict_s=19783
[20:22:43] tick balance=$305.94
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
  range: regime=trend atr_ratio=1.04 adx=14.1 t_h4=ranging t_h1=ranging tf_conflict_s=19846
[20:23:47] tick balance=$305.94
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
  range: regime=trend atr_ratio=1.04 adx=14.1 t_h4=ranging t_h1=ranging tf_conflict_s=19915
[20:24:55] tick balance=$305.94
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
  range: regime=trend atr_ratio=1.04 adx=14.1 t_h4=ranging t_h1=ranging tf_conflict_s=19978
[20:25:57] tick balance=$305.94
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
  range: regime=trend atr_ratio=1.05 adx=14.1 t_h4=ranging t_h1=ranging tf_conflict_s=20041
[20:27:00] tick balance=$305.94
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
  range: regime=trend atr_ratio=1.05 adx=14.1 t_h4=ranging t_h1=ranging tf_conflict_s=20103
[20:28:02] tick balance=$305.94
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
  range: regime=trend atr_ratio=1.05 adx=14.1 t_h4=ranging t_h1=ranging tf_conflict_s=20166
[20:29:05] tick balance=$305.94
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
  range: regime=trend atr_ratio=1.05 adx=14.1 t_h4=ranging t_h1=ranging tf_conflict_s=20228
[20:30:08] tick balance=$305.94
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
  range: regime=trend atr_ratio=1.01 adx=15.8 t_h4=ranging t_h1=ranging tf_conflict_s=20291
[20:31:11] tick balance=$305.94
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
  range: regime=trend atr_ratio=1.02 adx=15.8 t_h4=ranging t_h1=ranging tf_conflict_s=20355
[20:32:14] tick balance=$305.94
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
  range: regime=trend atr_ratio=1.02 adx=15.8 t_h4=ranging t_h1=ranging tf_conflict_s=20417
[20:33:17] tick balance=$305.94
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
  range: regime=trend atr_ratio=1.03 adx=15.8 t_h4=ranging t_h1=ranging tf_conflict_s=20479
[20:34:19] tick balance=$305.94
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
  range: regime=trend atr_ratio=1.03 adx=15.8 t_h4=ranging t_h1=ranging tf_conflict_s=20542
[20:35:22] tick balance=$305.94
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
  range: regime=trend atr_ratio=1.04 adx=15.8 t_h4=ranging t_h1=ranging tf_conflict_s=20605
[20:36:25] tick balance=$305.94
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
  range: regime=trend atr_ratio=1.04 adx=15.8 t_h4=ranging t_h1=ranging tf_conflict_s=20671
[20:37:31] tick balance=$305.94
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
  range: regime=trend atr_ratio=1.04 adx=15.8 t_h4=ranging t_h1=ranging tf_conflict_s=20734
[20:38:33] tick balance=$305.94
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
  range: regime=trend atr_ratio=1.04 adx=15.8 t_h4=ranging t_h1=ranging tf_conflict_s=20796
[20:39:36] tick balance=$305.94
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
  range: regime=trend atr_ratio=1.04 adx=15.8 t_h4=ranging t_h1=ranging tf_conflict_s=20859
[20:40:40] tick balance=$305.94
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
  range: regime=trend atr_ratio=1.04 adx=15.8 t_h4=ranging t_h1=ranging tf_conflict_s=20922
[20:41:42] tick balance=$305.94
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
  range: regime=trend atr_ratio=1.04 adx=15.7 t_h4=ranging t_h1=ranging tf_conflict_s=20985
[20:42:45] tick balance=$305.94
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
  range: regime=trend atr_ratio=1.05 adx=15.4 t_h4=ranging t_h1=ranging tf_conflict_s=21048
[20:43:48] tick balance=$305.94
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
  range: regime=trend atr_ratio=1.05 adx=15.4 t_h4=ranging t_h1=ranging tf_conflict_s=21111
[20:44:50] tick balance=$305.94
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
  range: regime=trend atr_ratio=1.05 adx=15.4 t_h4=ranging t_h1=ranging tf_conflict_s=21173
[20:45:53] tick balance=$305.94
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
  range: regime=trend atr_ratio=1.03 adx=16.6 t_h4=ranging t_h1=ranging tf_conflict_s=21236
[20:46:55] tick balance=$305.94
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
  range: regime=trend atr_ratio=1.04 adx=16.6 t_h4=ranging t_h1=ranging tf_conflict_s=21299
[20:47:58] tick balance=$305.94
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
  range: regime=trend atr_ratio=1.06 adx=16.7 t_h4=ranging t_h1=ranging tf_conflict_s=21361
[20:49:01] tick balance=$305.94
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
  range: regime=trend atr_ratio=1.07 adx=16.9 t_h4=ranging t_h1=ranging tf_conflict_s=21424
[20:50:04] tick balance=$305.94
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
  range: regime=trend atr_ratio=1.07 adx=16.9 t_h4=ranging t_h1=ranging tf_conflict_s=21492
[20:51:12] tick balance=$305.94
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
  range: regime=trend atr_ratio=1.07 adx=16.9 t_h4=ranging t_h1=ranging tf_conflict_s=21555
[20:52:15] tick balance=$305.94
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
  range: regime=trend atr_ratio=1.07 adx=16.9 t_h4=ranging t_h1=ranging tf_conflict_s=21618
[20:53:17] tick balance=$305.94
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
  range: regime=trend atr_ratio=1.08 adx=17.0 t_h4=ranging t_h1=ranging tf_conflict_s=21680
[20:54:20] tick balance=$305.94
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
  range: regime=trend atr_ratio=1.08 adx=17.0 t_h4=ranging t_h1=ranging tf_conflict_s=21743
```
