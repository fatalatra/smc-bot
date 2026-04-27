# Bot Snapshot — 2026-04-27 10:55 UTC

## Service: active
balance=$317.63

## Config
POST_CLOSE_COOLDOWN: int = 180 # 3 мин техническая пауза после закрытия
RISK_PCT: float = 0.03 # 1% для старта на HYPE (вернём к 5% после 5+ сделок)
ADX_MIN: float = 15.0 # ADX < 20 → choppy market, skip entry

## Trades (last 20)
```
35|BUY|41.9|10.0|closed|2026-04-26 20:17:37|2026-04-26 21:30:35
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
```

## Daily PnL
```
2026-04-27|317.63|0.0|0
2026-04-26|305.94|11.69|0
2026-04-25|305.94|0.0|0
2026-04-24|305.94|0.0|0
2026-04-23|313.19|-7.26|0
2026-04-22|301.06|12.14|0
2026-04-21|296.96|4.1|0
```

## Open Positions
```
none
```

## Diag Summary (last ~4h)
```
    240 trend_htf=ranging trend_mid=ranging skip=trend_mismatch
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
  range: regime=trend atr_ratio=0.85 adx=28.7 t_h4=bullish t_h1=ranging tf_conflict_s=0
[12:21:10] tick balance=$317.63
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
  range: regime=trend atr_ratio=0.85 adx=28.7 t_h4=bullish t_h1=ranging tf_conflict_s=0
[12:22:13] tick balance=$317.63
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
  range: regime=trend atr_ratio=0.85 adx=28.7 t_h4=bullish t_h1=ranging tf_conflict_s=0
[12:23:17] tick balance=$317.63
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
  range: regime=trend atr_ratio=0.85 adx=28.7 t_h4=bullish t_h1=ranging tf_conflict_s=0
[12:24:20] tick balance=$317.63
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
  range: regime=trend atr_ratio=0.85 adx=28.7 t_h4=bullish t_h1=ranging tf_conflict_s=0
[12:25:24] tick balance=$317.63
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
  range: regime=trend atr_ratio=0.86 adx=28.8 t_h4=bullish t_h1=ranging tf_conflict_s=0
[12:26:27] tick balance=$317.63
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
  range: regime=trend atr_ratio=0.86 adx=28.8 t_h4=bullish t_h1=ranging tf_conflict_s=0
[12:27:30] tick balance=$317.63
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
  range: regime=trend atr_ratio=0.86 adx=28.8 t_h4=bullish t_h1=ranging tf_conflict_s=0
[12:28:35] tick balance=$317.63
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
  range: regime=trend atr_ratio=0.86 adx=28.8 t_h4=bullish t_h1=ranging tf_conflict_s=0
[12:29:38] tick balance=$317.63
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
  range: regime=trend atr_ratio=0.86 adx=28.8 t_h4=bullish t_h1=ranging tf_conflict_s=0
[12:30:42] tick balance=$317.63
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
  range: regime=trend atr_ratio=0.78 adx=29.2 t_h4=bullish t_h1=ranging tf_conflict_s=0
[12:31:46] tick balance=$317.63
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
  range: regime=trend atr_ratio=0.79 adx=29.2 t_h4=bullish t_h1=ranging tf_conflict_s=0
[12:32:48] tick balance=$317.63
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
  range: regime=trend atr_ratio=0.8 adx=29.3 t_h4=bullish t_h1=ranging tf_conflict_s=0
[12:33:52] tick balance=$317.63
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
  range: regime=trend atr_ratio=0.8 adx=29.3 t_h4=bullish t_h1=ranging tf_conflict_s=0
[12:34:55] tick balance=$317.63
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
  range: regime=trend atr_ratio=0.8 adx=29.3 t_h4=bullish t_h1=ranging tf_conflict_s=0
[12:35:58] tick balance=$317.63
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
  range: regime=trend atr_ratio=0.8 adx=29.3 t_h4=bullish t_h1=ranging tf_conflict_s=0
[12:37:01] tick balance=$317.63
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
  range: regime=trend atr_ratio=0.8 adx=29.3 t_h4=bullish t_h1=ranging tf_conflict_s=0
[12:38:04] tick balance=$317.63
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
  range: regime=trend atr_ratio=0.8 adx=29.3 t_h4=bullish t_h1=ranging tf_conflict_s=0
[12:39:07] tick balance=$317.63
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
  range: regime=trend atr_ratio=0.81 adx=29.4 t_h4=bullish t_h1=ranging tf_conflict_s=0
[12:40:10] tick balance=$317.63
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
  range: regime=trend atr_ratio=0.81 adx=29.4 t_h4=bullish t_h1=ranging tf_conflict_s=0
[12:41:13] tick balance=$317.63
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
  range: regime=trend atr_ratio=0.81 adx=29.4 t_h4=bullish t_h1=ranging tf_conflict_s=0
[12:42:17] tick balance=$317.63
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
  range: regime=trend atr_ratio=0.81 adx=29.4 t_h4=bullish t_h1=ranging tf_conflict_s=0
[12:43:20] tick balance=$317.63
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
  range: regime=trend atr_ratio=0.81 adx=29.4 t_h4=bullish t_h1=ranging tf_conflict_s=0
[12:44:26] tick balance=$317.63
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
  range: regime=trend atr_ratio=0.81 adx=29.4 t_h4=bullish t_h1=ranging tf_conflict_s=0
[12:45:28] tick balance=$317.63
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
  range: regime=trend atr_ratio=0.79 adx=29.8 t_h4=bullish t_h1=ranging tf_conflict_s=0
[12:46:31] tick balance=$317.63
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
  range: regime=trend atr_ratio=0.81 adx=29.8 t_h4=bullish t_h1=ranging tf_conflict_s=0
[12:47:34] tick balance=$317.63
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
  range: regime=trend atr_ratio=0.81 adx=29.8 t_h4=bullish t_h1=ranging tf_conflict_s=0
[12:48:37] tick balance=$317.63
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
  range: regime=trend atr_ratio=0.81 adx=29.8 t_h4=bullish t_h1=ranging tf_conflict_s=0
[12:49:40] tick balance=$317.63
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
  range: regime=trend atr_ratio=0.81 adx=29.8 t_h4=bullish t_h1=ranging tf_conflict_s=0
[12:50:44] tick balance=$317.63
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
  range: regime=trend atr_ratio=0.81 adx=29.8 t_h4=bullish t_h1=ranging tf_conflict_s=0
[12:51:48] tick balance=$317.63
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
  range: regime=trend atr_ratio=0.81 adx=29.8 t_h4=bullish t_h1=ranging tf_conflict_s=0
[12:52:51] tick balance=$317.63
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
  range: regime=trend atr_ratio=0.81 adx=29.8 t_h4=bullish t_h1=ranging tf_conflict_s=0
[12:53:54] tick balance=$317.63
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
  range: regime=trend atr_ratio=0.82 adx=29.8 t_h4=bullish t_h1=ranging tf_conflict_s=0
[12:54:57] tick balance=$317.63
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
  range: regime=trend atr_ratio=0.82 adx=29.8 t_h4=bullish t_h1=ranging tf_conflict_s=0
```
