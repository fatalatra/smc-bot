# Bot Snapshot — 2026-04-27 14:55 UTC

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
     96 trend_htf=ranging trend_mid=ranging skip=trend_mismatch
      7 trend=bearish skip=atr_low ratio=0.77 min=0.8
      5 trend=bearish atr_ratio=0.87 obs=8 obs_fresh=5 fvgs=12 bos=26 sigs=0 wrong_side=5 price_out=0 bos_miss=0 risk_neg=0 sl_too_tight=0 liquidity_trap=0
      4 trend=bearish skip=atr_low ratio=0.8 min=0.8
      3 trend=bearish skip=atr_low ratio=0.75 min=0.8
      3 trend=bearish skip=atr_low ratio=0.74 min=0.8
      3 trend=bearish atr_ratio=1.26 obs=9 obs_fresh=6 fvgs=9 bos=26 sigs=0 wrong_side=6 price_out=0 bos_miss=0 risk_neg=0 sl_too_tight=0 liquidity_trap=0
      3 trend=bearish atr_ratio=0.95 obs=8 obs_fresh=5 fvgs=12 bos=26 sigs=0 wrong_side=5 price_out=0 bos_miss=0 risk_neg=0 sl_too_tight=0 liquidity_trap=0
      3 trend=bearish atr_ratio=0.84 obs=8 obs_fresh=5 fvgs=12 bos=26 sigs=0 wrong_side=5 price_out=0 bos_miss=0 risk_neg=0 sl_too_tight=0 liquidity_trap=0
      2 trend=bearish skip=atr_low ratio=0.78 min=0.8
      2 trend=bearish atr_ratio=1.3 obs=9 obs_fresh=6 fvgs=9 bos=26 sigs=0 wrong_side=6 price_out=0 bos_miss=0 risk_neg=0 sl_too_tight=0 liquidity_trap=0
      2 trend=bearish atr_ratio=1.0 obs=8 obs_fresh=5 fvgs=13 bos=25 sigs=0 wrong_side=5 price_out=0 bos_miss=0 risk_neg=0 sl_too_tight=0 liquidity_trap=0
      2 trend=bearish atr_ratio=1.01 obs=8 obs_fresh=5 fvgs=13 bos=25 sigs=0 wrong_side=5 price_out=0 bos_miss=0 risk_neg=0 sl_too_tight=0 liquidity_trap=0
      2 trend=bearish atr_ratio=0.99 obs=8 obs_fresh=5 fvgs=12 bos=25 sigs=0 wrong_side=5 price_out=0 bos_miss=0 risk_neg=0 sl_too_tight=0 liquidity_trap=0
      2 trend=bearish atr_ratio=0.94 obs=8 obs_fresh=5 fvgs=12 bos=26 sigs=0 wrong_side=5 price_out=0 bos_miss=0 risk_neg=0 sl_too_tight=0 liquidity_trap=0
      2 trend=bearish atr_ratio=0.91 obs=9 obs_fresh=6 fvgs=13 bos=27 sigs=0 wrong_side=6 price_out=0 bos_miss=0 risk_neg=0 sl_too_tight=0 liquidity_trap=0
      2 trend=bearish atr_ratio=0.91 obs=9 obs_fresh=6 fvgs=13 bos=26 sigs=0 wrong_side=6 price_out=0 bos_miss=0 risk_neg=0 sl_too_tight=0 liquidity_trap=0
      2 trend=bearish atr_ratio=0.89 obs=9 obs_fresh=6 fvgs=13 bos=27 sigs=0 wrong_side=6 price_out=0 bos_miss=0 risk_neg=0 sl_too_tight=0 liquidity_trap=0
      2 trend=bearish atr_ratio=0.88 obs=9 obs_fresh=6 fvgs=12 bos=27 sigs=0 wrong_side=6 price_out=0 bos_miss=0 risk_neg=0 sl_too_tight=0 liquidity_trap=0
      2 trend=bearish atr_ratio=0.88 obs=9 obs_fresh=6 fvgs=12 bos=26 sigs=0 wrong_side=6 price_out=0 bos_miss=0 risk_neg=0 sl_too_tight=0 liquidity_trap=0
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
[16:19:24] tick balance=$317.63
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
  range: regime=trend atr_ratio=0.84 adx=22.4 t_h4=bullish t_h1=ranging tf_conflict_s=0
[16:20:27] tick balance=$317.63
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
  range: regime=trend atr_ratio=0.84 adx=22.5 t_h4=bullish t_h1=ranging tf_conflict_s=0
[16:21:30] tick balance=$317.63
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
  range: regime=trend atr_ratio=0.85 adx=22.5 t_h4=bullish t_h1=ranging tf_conflict_s=0
[16:22:33] tick balance=$317.63
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
  range: regime=trend atr_ratio=0.85 adx=22.5 t_h4=bullish t_h1=ranging tf_conflict_s=0
[16:23:38] tick balance=$317.63
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
  range: regime=trend atr_ratio=0.85 adx=22.5 t_h4=bullish t_h1=ranging tf_conflict_s=0
[16:24:41] tick balance=$317.63
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
  range: regime=trend atr_ratio=0.85 adx=22.5 t_h4=bullish t_h1=ranging tf_conflict_s=0
[tick] fetch err: 
[16:26:58] tick balance=$317.63
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
  range: regime=trend atr_ratio=0.85 adx=22.7 t_h4=bullish t_h1=ranging tf_conflict_s=0
[16:28:01] tick balance=$317.63
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
  range: regime=trend atr_ratio=0.85 adx=22.7 t_h4=bullish t_h1=ranging tf_conflict_s=0
[16:29:05] tick balance=$317.63
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
  range: regime=trend atr_ratio=0.85 adx=22.7 t_h4=bullish t_h1=ranging tf_conflict_s=0
[16:30:08] tick balance=$317.63
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
  range: regime=trend atr_ratio=0.83 adx=23.1 t_h4=bullish t_h1=ranging tf_conflict_s=0
[16:31:11] tick balance=$317.63
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
  range: regime=trend atr_ratio=0.85 adx=23.1 t_h4=bullish t_h1=ranging tf_conflict_s=0
[16:32:14] tick balance=$317.63
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
  range: regime=trend atr_ratio=0.86 adx=23.2 t_h4=bullish t_h1=ranging tf_conflict_s=0
[16:33:18] tick balance=$317.63
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
  range: regime=trend atr_ratio=0.87 adx=23.4 t_h4=bullish t_h1=ranging tf_conflict_s=0
[16:34:21] tick balance=$317.63
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
  range: regime=trend atr_ratio=0.87 adx=23.4 t_h4=bullish t_h1=ranging tf_conflict_s=0
[16:35:24] tick balance=$317.63
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
  range: regime=trend atr_ratio=0.87 adx=23.4 t_h4=bullish t_h1=ranging tf_conflict_s=0
[16:36:28] tick balance=$317.63
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
  range: regime=trend atr_ratio=0.88 adx=23.5 t_h4=bullish t_h1=ranging tf_conflict_s=0
[16:37:30] tick balance=$317.63
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
  range: regime=trend atr_ratio=0.89 adx=23.7 t_h4=bullish t_h1=ranging tf_conflict_s=0
[16:38:35] tick balance=$317.63
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
  range: regime=trend atr_ratio=0.89 adx=23.7 t_h4=bullish t_h1=ranging tf_conflict_s=0
[16:39:38] tick balance=$317.63
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
  range: regime=trend atr_ratio=0.9 adx=23.7 t_h4=bullish t_h1=ranging tf_conflict_s=0
[16:40:42] tick balance=$317.63
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
  range: regime=trend atr_ratio=0.9 adx=23.8 t_h4=bullish t_h1=ranging tf_conflict_s=0
[16:41:45] tick balance=$317.63
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
  range: regime=trend atr_ratio=0.9 adx=23.8 t_h4=bullish t_h1=ranging tf_conflict_s=0
[16:42:49] tick balance=$317.63
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
  range: regime=trend atr_ratio=0.9 adx=23.8 t_h4=bullish t_h1=ranging tf_conflict_s=0
[16:43:52] tick balance=$317.63
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
  range: regime=trend atr_ratio=0.9 adx=23.8 t_h4=bullish t_h1=ranging tf_conflict_s=0
[16:44:55] tick balance=$317.63
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
  range: regime=trend atr_ratio=0.9 adx=23.8 t_h4=bullish t_h1=ranging tf_conflict_s=0
[16:45:58] tick balance=$317.63
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
  range: regime=trend atr_ratio=0.87 adx=24.8 t_h4=bullish t_h1=ranging tf_conflict_s=0
[16:47:01] tick balance=$317.63
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
  range: regime=trend atr_ratio=0.88 adx=24.8 t_h4=bullish t_h1=ranging tf_conflict_s=0
[16:48:05] tick balance=$317.63
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
  range: regime=trend atr_ratio=0.88 adx=24.8 t_h4=bullish t_h1=ranging tf_conflict_s=0
[16:49:08] tick balance=$317.63
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
  range: regime=trend atr_ratio=0.88 adx=24.8 t_h4=bullish t_h1=ranging tf_conflict_s=0
[16:50:11] tick balance=$317.63
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
  range: regime=trend atr_ratio=0.88 adx=24.8 t_h4=bullish t_h1=ranging tf_conflict_s=0
[16:51:14] tick balance=$317.63
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
  range: regime=trend atr_ratio=0.91 adx=24.5 t_h4=bullish t_h1=ranging tf_conflict_s=0
[16:52:17] tick balance=$317.63
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
  range: regime=trend atr_ratio=0.91 adx=24.4 t_h4=bullish t_h1=ranging tf_conflict_s=0
[16:53:21] tick balance=$317.63
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
  range: regime=trend atr_ratio=0.92 adx=24.1 t_h4=bullish t_h1=ranging tf_conflict_s=0
[16:54:25] tick balance=$317.63
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
  range: regime=trend atr_ratio=0.93 adx=23.9 t_h4=bullish t_h1=ranging tf_conflict_s=0
```
