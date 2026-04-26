# Bot Snapshot — 2026-04-26 22:55 UTC

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
2026-04-26|305.94|11.69|0
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
    119 trend_htf=ranging trend_mid=ranging skip=trend_mismatch
      6 trend=bullish skip=ema_overextended price=42.1 ema20_h4=41.4 dist=0.7 max_dist=0.7
      2 trend=bullish skip=ema_overextended price=42.2 ema20_h4=41.4 dist=0.8 max_dist=0.7
      1 trend=bullish skip=ema_overextended price=42.3 ema20_h4=41.4 dist=0.9 max_dist=0.7
      1 trend=bullish skip=ema_overextended price=42.1 ema20_h4=41.4 dist=0.8 max_dist=0.7
      1 trend=bullish atr_ratio=1.69 obs=12 obs_fresh=10 fvgs=14 bos=25 sigs=0 wrong_side=4 price_out=4 bos_miss=0 risk_neg=0 sl_too_tight=0 liquidity_trap=2 near_gap_pct=0.587
      1 trend=bullish atr_ratio=1.69 obs=12 obs_fresh=10 fvgs=14 bos=25 sigs=0 wrong_side=4 price_out=4 bos_miss=0 risk_neg=0 sl_too_tight=0 liquidity_trap=2 near_gap_pct=0.565
      1 trend=bullish atr_ratio=1.69 obs=12 obs_fresh=10 fvgs=14 bos=25 sigs=0 wrong_side=4 price_out=4 bos_miss=0 risk_neg=0 sl_too_tight=0 liquidity_trap=2 near_gap_pct=0.52
      1 trend=bullish atr_ratio=1.68 obs=13 obs_fresh=11 fvgs=15 bos=25 sigs=0 wrong_side=4 price_out=5 bos_miss=0 risk_neg=0 sl_too_tight=0 liquidity_trap=2 near_gap_pct=0.504
      1 trend=bullish atr_ratio=1.68 obs=13 obs_fresh=11 fvgs=15 bos=25 sigs=0 wrong_side=4 price_out=5 bos_miss=0 risk_neg=0 sl_too_tight=0 liquidity_trap=2 near_gap_pct=0.416
      1 trend=bullish atr_ratio=1.67 obs=13 obs_fresh=12 fvgs=15 bos=25 sigs=1 wrong_side=3 price_out=5 bos_miss=0 risk_neg=0 sl_too_tight=0 liquidity_trap=2 near_gap_pct=0.096
      1 trend=bullish atr_ratio=1.67 obs=13 obs_fresh=12 fvgs=15 bos=25 sigs=0 wrong_side=4 price_out=5 bos_miss=0 risk_neg=0 sl_too_tight=1 liquidity_trap=2 near_gap_pct=0.043
      1 trend=bullish atr_ratio=1.67 obs=12 obs_fresh=10 fvgs=14 bos=26 sigs=0 wrong_side=4 price_out=6 bos_miss=0 risk_neg=0 sl_too_tight=0 liquidity_trap=0 near_gap_pct=0.705
      1 trend=bullish atr_ratio=1.67 obs=12 obs_fresh=10 fvgs=14 bos=25 sigs=0 wrong_side=4 price_out=4 bos_miss=0 risk_neg=0 sl_too_tight=0 liquidity_trap=2 near_gap_pct=0.551
      1 trend=bullish atr_ratio=1.67 obs=12 obs_fresh=10 fvgs=14 bos=25 sigs=0 wrong_side=4 price_out=4 bos_miss=0 risk_neg=0 sl_too_tight=0 liquidity_trap=2 near_gap_pct=0.527
      1 trend=bullish atr_ratio=1.67 obs=12 obs_fresh=10 fvgs=14 bos=24 sigs=0 wrong_side=4 price_out=4 bos_miss=0 risk_neg=0 sl_too_tight=0 liquidity_trap=2 near_gap_pct=0.615
      1 trend=bullish atr_ratio=1.67 obs=12 obs_fresh=10 fvgs=14 bos=24 sigs=0 wrong_side=4 price_out=4 bos_miss=0 risk_neg=0 sl_too_tight=0 liquidity_trap=2 near_gap_pct=0.601
      1 trend=bullish atr_ratio=1.66 obs=12 obs_fresh=10 fvgs=14 bos=24 sigs=0 wrong_side=4 price_out=4 bos_miss=0 risk_neg=0 sl_too_tight=0 liquidity_trap=2 near_gap_pct=0.601
      1 trend=bullish atr_ratio=1.65 obs=13 obs_fresh=13 fvgs=15 bos=24 sigs=1 wrong_side=2 price_out=5 bos_miss=0 risk_neg=0 sl_too_tight=0 liquidity_trap=0 near_gap_pct=0.01
      1 trend=bullish atr_ratio=1.65 obs=12 obs_fresh=10 fvgs=14 bos=26 sigs=0 wrong_side=4 price_out=5 bos_miss=0 risk_neg=0 sl_too_tight=0 liquidity_trap=1 near_gap_pct=0.672
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
  range: regime=trend atr_ratio=1.57 adx=46.0 t_h4=ranging t_h1=ranging tf_conflict_s=34039
[00:20:20] tick balance=$317.63
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
  range: regime=trend atr_ratio=1.57 adx=46.0 t_h4=ranging t_h1=ranging tf_conflict_s=34103
[00:21:23] tick balance=$317.63
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
  range: regime=trend atr_ratio=1.57 adx=46.0 t_h4=ranging t_h1=ranging tf_conflict_s=34166
[00:22:26] tick balance=$317.63
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
  range: regime=trend atr_ratio=1.57 adx=46.0 t_h4=ranging t_h1=ranging tf_conflict_s=34229
[00:23:29] tick balance=$317.63
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
  range: regime=trend atr_ratio=1.57 adx=46.0 t_h4=ranging t_h1=ranging tf_conflict_s=34292
[00:24:32] tick balance=$317.63
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
  range: regime=trend atr_ratio=1.57 adx=46.0 t_h4=ranging t_h1=ranging tf_conflict_s=34355
[00:25:34] tick balance=$317.63
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
  range: regime=trend atr_ratio=1.6 adx=46.3 t_h4=ranging t_h1=ranging tf_conflict_s=34418
[00:26:38] tick balance=$317.63
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
  range: regime=trend atr_ratio=1.6 adx=46.3 t_h4=ranging t_h1=ranging tf_conflict_s=34482
[00:27:41] tick balance=$317.63
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
  range: regime=trend atr_ratio=1.6 adx=46.3 t_h4=ranging t_h1=ranging tf_conflict_s=34544
[00:28:44] tick balance=$317.63
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
  range: regime=trend atr_ratio=1.6 adx=46.3 t_h4=ranging t_h1=ranging tf_conflict_s=34608
[00:29:47] tick balance=$317.63
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
  range: regime=trend atr_ratio=1.6 adx=46.3 t_h4=ranging t_h1=ranging tf_conflict_s=34671
[00:30:51] tick balance=$317.63
  diag: trend=bullish atr_ratio=1.18 obs=11 obs_fresh=8 fvgs=12 bos=23 sigs=0 wrong_side=5 price_out=2 bos_miss=0 risk_neg=0 sl_too_tight=0 liquidity_trap=1 near_gap_pct=0.193
  range: regime=trend atr_ratio=1.58 adx=47.7 t_h4=ranging t_h1=ranging tf_conflict_s=34734
[00:31:54] tick balance=$317.63
  diag: trend=bullish skip=ema_overextended price=42.1 ema20_h4=41.4 dist=0.7 max_dist=0.7
  range: regime=trend atr_ratio=1.59 adx=47.7 t_h4=ranging t_h1=ranging tf_conflict_s=34797
[00:32:57] tick balance=$317.63
  diag: trend=bullish atr_ratio=1.19 obs=11 obs_fresh=8 fvgs=12 bos=24 sigs=0 wrong_side=5 price_out=2 bos_miss=0 risk_neg=0 sl_too_tight=0 liquidity_trap=1 near_gap_pct=0.188
  range: regime=trend atr_ratio=1.59 adx=47.7 t_h4=ranging t_h1=ranging tf_conflict_s=34860
[00:34:00] tick balance=$317.63
  diag: trend=bullish atr_ratio=1.23 obs=11 obs_fresh=8 fvgs=11 bos=24 sigs=0 wrong_side=5 price_out=2 bos_miss=0 risk_neg=0 sl_too_tight=1 liquidity_trap=0 near_gap_pct=-0.036
  range: regime=trend atr_ratio=1.61 adx=47.7 t_h4=ranging t_h1=ranging tf_conflict_s=34924
[00:35:04] tick balance=$317.63
  diag: trend=bullish atr_ratio=1.19 obs=11 obs_fresh=8 fvgs=12 bos=24 sigs=0 wrong_side=5 price_out=0 bos_miss=0 risk_neg=0 sl_too_tight=1 liquidity_trap=2 near_gap_pct=-0.129
  range: regime=trend atr_ratio=1.63 adx=47.5 t_h4=ranging t_h1=ranging tf_conflict_s=34987
[00:36:07] tick balance=$317.63
  diag: trend=bullish atr_ratio=1.22 obs=11 obs_fresh=8 fvgs=12 bos=25 sigs=0 wrong_side=5 price_out=1 bos_miss=0 risk_neg=0 sl_too_tight=1 liquidity_trap=1 near_gap_pct=-0.043
  range: regime=trend atr_ratio=1.63 adx=47.5 t_h4=ranging t_h1=ranging tf_conflict_s=35050
[00:37:09] tick balance=$317.63
  diag: trend=bullish atr_ratio=1.22 obs=11 obs_fresh=8 fvgs=12 bos=25 sigs=0 wrong_side=5 price_out=1 bos_miss=0 risk_neg=0 sl_too_tight=1 liquidity_trap=1 near_gap_pct=-0.041
  range: regime=trend atr_ratio=1.63 adx=47.5 t_h4=ranging t_h1=ranging tf_conflict_s=35113
[00:38:12] tick balance=$317.63
  diag: trend=bullish atr_ratio=1.22 obs=11 obs_fresh=8 fvgs=12 bos=25 sigs=0 wrong_side=5 price_out=2 bos_miss=0 risk_neg=0 sl_too_tight=1 liquidity_trap=0 near_gap_pct=0.014
  range: regime=trend atr_ratio=1.63 adx=47.5 t_h4=ranging t_h1=ranging tf_conflict_s=35175
[00:39:15] tick balance=$317.63
  diag: trend=bullish atr_ratio=1.22 obs=11 obs_fresh=8 fvgs=12 bos=25 sigs=0 wrong_side=5 price_out=2 bos_miss=0 risk_neg=0 sl_too_tight=1 liquidity_trap=0 near_gap_pct=-0.026
  range: regime=trend atr_ratio=1.63 adx=47.5 t_h4=ranging t_h1=ranging tf_conflict_s=35238
[00:40:17] tick balance=$317.63
  diag: trend=bullish atr_ratio=1.1 obs=11 obs_fresh=8 fvgs=12 bos=25 sigs=0 wrong_side=5 price_out=2 bos_miss=0 risk_neg=0 sl_too_tight=1 liquidity_trap=0 near_gap_pct=-0.026
  range: regime=trend atr_ratio=1.63 adx=47.5 t_h4=ranging t_h1=ranging tf_conflict_s=35301
[00:41:21] tick balance=$317.63
  diag: trend=bullish atr_ratio=1.12 obs=11 obs_fresh=8 fvgs=12 bos=24 sigs=0 wrong_side=5 price_out=1 bos_miss=0 risk_neg=0 sl_too_tight=1 liquidity_trap=1 near_gap_pct=-0.083
  range: regime=trend atr_ratio=1.63 adx=47.5 t_h4=ranging t_h1=ranging tf_conflict_s=35364
[00:42:23] tick balance=$317.63
  diag: trend=bullish atr_ratio=1.12 obs=11 obs_fresh=8 fvgs=12 bos=24 sigs=0 wrong_side=5 price_out=0 bos_miss=0 risk_neg=0 sl_too_tight=1 liquidity_trap=2 near_gap_pct=-0.126
  range: regime=trend atr_ratio=1.63 adx=47.5 t_h4=ranging t_h1=ranging tf_conflict_s=35427
[00:43:27] tick balance=$317.63
  diag: trend=bullish atr_ratio=1.13 obs=11 obs_fresh=8 fvgs=12 bos=24 sigs=0 wrong_side=5 price_out=0 bos_miss=0 risk_neg=0 sl_too_tight=1 liquidity_trap=2 near_gap_pct=-0.167
  range: regime=trend atr_ratio=1.63 adx=47.5 t_h4=ranging t_h1=ranging tf_conflict_s=35490
[00:44:30] tick balance=$317.63
  diag: trend=bullish atr_ratio=1.13 obs=11 obs_fresh=8 fvgs=12 bos=23 sigs=0 wrong_side=5 price_out=1 bos_miss=0 risk_neg=0 sl_too_tight=1 liquidity_trap=1 near_gap_pct=-0.076
  range: regime=trend atr_ratio=1.63 adx=47.5 t_h4=ranging t_h1=ranging tf_conflict_s=35553
[00:45:33] tick balance=$317.63
  diag: trend=bullish atr_ratio=1.07 obs=11 obs_fresh=8 fvgs=12 bos=23 sigs=0 wrong_side=5 price_out=2 bos_miss=0 risk_neg=0 sl_too_tight=1 liquidity_trap=0 near_gap_pct=-0.021
  range: regime=trend atr_ratio=1.56 adx=48.7 t_h4=ranging t_h1=ranging tf_conflict_s=35616
[00:46:36] tick balance=$317.63
  diag: trend=bullish atr_ratio=1.08 obs=11 obs_fresh=8 fvgs=12 bos=23 sigs=0 wrong_side=5 price_out=1 bos_miss=0 risk_neg=0 sl_too_tight=1 liquidity_trap=1 near_gap_pct=-0.048
  range: regime=trend atr_ratio=1.56 adx=48.7 t_h4=ranging t_h1=ranging tf_conflict_s=35679
[00:47:39] tick balance=$317.63
  diag: trend=bullish atr_ratio=1.08 obs=11 obs_fresh=8 fvgs=12 bos=23 sigs=0 wrong_side=5 price_out=1 bos_miss=0 risk_neg=0 sl_too_tight=1 liquidity_trap=1 near_gap_pct=-0.055
  range: regime=trend atr_ratio=1.56 adx=48.7 t_h4=ranging t_h1=ranging tf_conflict_s=35742
[00:48:42] tick balance=$317.63
  diag: trend=bullish atr_ratio=1.09 obs=11 obs_fresh=8 fvgs=12 bos=23 sigs=0 wrong_side=5 price_out=2 bos_miss=0 risk_neg=0 sl_too_tight=1 liquidity_trap=0 near_gap_pct=0.029
  range: regime=trend atr_ratio=1.57 adx=48.7 t_h4=ranging t_h1=ranging tf_conflict_s=35805
[00:49:45] tick balance=$317.63
  diag: trend=bullish skip=ema_overextended price=42.1 ema20_h4=41.4 dist=0.7 max_dist=0.7
  range: regime=trend atr_ratio=1.6 adx=48.7 t_h4=ranging t_h1=ranging tf_conflict_s=35868
[00:50:48] tick balance=$317.63
  diag: trend=bullish skip=ema_overextended price=42.1 ema20_h4=41.4 dist=0.8 max_dist=0.7
  range: regime=trend atr_ratio=1.62 adx=48.9 t_h4=ranging t_h1=ranging tf_conflict_s=35932
[00:51:51] tick balance=$317.63
  diag: trend=bullish skip=ema_overextended price=42.2 ema20_h4=41.4 dist=0.8 max_dist=0.7
  range: regime=trend atr_ratio=1.62 adx=48.9 t_h4=ranging t_h1=ranging tf_conflict_s=35995
[00:52:55] tick balance=$317.63
  diag: trend=bullish skip=ema_overextended price=42.2 ema20_h4=41.4 dist=0.8 max_dist=0.7
  range: regime=trend atr_ratio=1.63 adx=49.0 t_h4=ranging t_h1=ranging tf_conflict_s=36058
[00:53:58] tick balance=$317.63
  diag: trend=bullish skip=ema_overextended price=42.3 ema20_h4=41.4 dist=0.9 max_dist=0.7
  range: regime=trend atr_ratio=1.66 adx=49.3 t_h4=ranging t_h1=ranging tf_conflict_s=36121
```
