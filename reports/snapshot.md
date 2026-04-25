# Bot Snapshot — 2026-04-25 14:55 UTC

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
2026-04-25|305.94|0.0|0
2026-04-24|305.94|0.0|0
2026-04-23|313.19|-7.26|0
2026-04-22|301.06|12.14|0
2026-04-21|296.96|4.1|0
2026-04-20|312.71|-15.75|0
2026-04-19|354.45|-41.74|0
```

## Open Positions
```
none
```

## Diag Summary (last ~4h)
```
      2 trend=bullish atr_ratio=1.12 obs=10 obs_fresh=9 fvgs=17 bos=23 sigs=0 wrong_side=7 price_out=2 bos_miss=0 risk_neg=0 sl_too_tight=0 liquidity_trap=0 near_gap_pct=0.712
      2 trend=bullish atr_ratio=1.03 obs=9 obs_fresh=8 fvgs=17 bos=28 sigs=0 wrong_side=6 price_out=2 bos_miss=0 risk_neg=0 sl_too_tight=0 liquidity_trap=0 near_gap_pct=-0.181
      2 trend=bullish atr_ratio=1.01 obs=8 obs_fresh=7 fvgs=14 bos=30 sigs=0 wrong_side=5 price_out=1 bos_miss=1 risk_neg=0 sl_too_tight=0 liquidity_trap=0 near_gap_pct=-0.005
      2 trend=bullish atr_ratio=0.94 obs=9 obs_fresh=8 fvgs=18 bos=27 sigs=0 wrong_side=6 price_out=1 bos_miss=1 risk_neg=0 sl_too_tight=0 liquidity_trap=0 near_gap_pct=-0.405
      2 trend=bullish atr_ratio=0.86 obs=8 obs_fresh=7 fvgs=16 bos=32 sigs=0 wrong_side=5 price_out=1 bos_miss=1 risk_neg=0 sl_too_tight=0 liquidity_trap=0 near_gap_pct=0.314
      1 trend=bullish atr_ratio=1.3 obs=11 obs_fresh=10 fvgs=17 bos=23 sigs=0 wrong_side=7 price_out=3 bos_miss=0 risk_neg=0 sl_too_tight=0 liquidity_trap=0 near_gap_pct=1.064
      1 trend=bullish atr_ratio=1.3 obs=10 obs_fresh=9 fvgs=19 bos=25 sigs=0 wrong_side=6 price_out=3 bos_miss=0 risk_neg=0 sl_too_tight=0 liquidity_trap=0 near_gap_pct=1.357
      1 trend=bullish atr_ratio=1.3 obs=10 obs_fresh=9 fvgs=19 bos=24 sigs=0 wrong_side=6 price_out=3 bos_miss=0 risk_neg=0 sl_too_tight=0 liquidity_trap=0 near_gap_pct=1.284
      1 trend=bullish atr_ratio=1.3 obs=10 obs_fresh=9 fvgs=17 bos=25 sigs=0 wrong_side=6 price_out=3 bos_miss=0 risk_neg=0 sl_too_tight=0 liquidity_trap=0 near_gap_pct=1.139
      1 trend=bullish atr_ratio=1.38 obs=10 obs_fresh=9 fvgs=16 bos=26 sigs=0 wrong_side=6 price_out=3 bos_miss=0 risk_neg=0 sl_too_tight=0 liquidity_trap=0 near_gap_pct=0.902
      1 trend=bullish atr_ratio=1.38 obs=10 obs_fresh=9 fvgs=16 bos=26 sigs=0 wrong_side=6 price_out=3 bos_miss=0 risk_neg=0 sl_too_tight=0 liquidity_trap=0 near_gap_pct=0.897
      1 trend=bullish atr_ratio=1.38 obs=10 obs_fresh=9 fvgs=16 bos=25 sigs=0 wrong_side=6 price_out=3 bos_miss=0 risk_neg=0 sl_too_tight=0 liquidity_trap=0 near_gap_pct=0.888
      1 trend=bullish atr_ratio=1.34 obs=10 obs_fresh=9 fvgs=17 bos=26 sigs=0 wrong_side=6 price_out=3 bos_miss=0 risk_neg=0 sl_too_tight=0 liquidity_trap=0 near_gap_pct=1.097
      1 trend=bullish atr_ratio=1.34 obs=10 obs_fresh=9 fvgs=17 bos=25 sigs=0 wrong_side=6 price_out=3 bos_miss=0 risk_neg=0 sl_too_tight=0 liquidity_trap=0 near_gap_pct=1.229
      1 trend=bullish atr_ratio=1.32 obs=10 obs_fresh=9 fvgs=18 bos=25 sigs=0 wrong_side=6 price_out=3 bos_miss=0 risk_neg=0 sl_too_tight=0 liquidity_trap=0 near_gap_pct=1.253
      1 trend=bullish atr_ratio=1.31 obs=11 obs_fresh=10 fvgs=18 bos=23 sigs=0 wrong_side=7 price_out=3 bos_miss=0 risk_neg=0 sl_too_tight=0 liquidity_trap=0 near_gap_pct=0.985
      1 trend=bullish atr_ratio=1.31 obs=11 obs_fresh=10 fvgs=18 bos=22 sigs=0 wrong_side=7 price_out=3 bos_miss=0 risk_neg=0 sl_too_tight=0 liquidity_trap=0 near_gap_pct=0.973
      1 trend=bullish atr_ratio=1.31 obs=10 obs_fresh=9 fvgs=18 bos=26 sigs=0 wrong_side=6 price_out=3 bos_miss=0 risk_neg=0 sl_too_tight=0 liquidity_trap=0 near_gap_pct=1.236
      1 trend=bullish atr_ratio=1.31 obs=10 obs_fresh=9 fvgs=18 bos=25 sigs=0 wrong_side=6 price_out=3 bos_miss=0 risk_neg=0 sl_too_tight=0 liquidity_trap=0 near_gap_pct=1.267
      1 trend=bullish atr_ratio=1.31 obs=10 obs_fresh=9 fvgs=18 bos=25 sigs=0 wrong_side=6 price_out=3 bos_miss=0 risk_neg=0 sl_too_tight=0 liquidity_trap=0 near_gap_pct=1.215
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
[16:04:29] tick balance=$305.94
  diag: trend=bullish atr_ratio=0.96 obs=9 obs_fresh=8 fvgs=16 bos=28 sigs=0 wrong_side=6 price_out=2 bos_miss=0 risk_neg=0 sl_too_tight=0 liquidity_trap=0 near_gap_pct=-0.258
[16:05:31] tick balance=$305.94
  diag: trend=bullish atr_ratio=0.96 obs=9 obs_fresh=8 fvgs=17 bos=28 sigs=0 wrong_side=6 price_out=2 bos_miss=0 risk_neg=0 sl_too_tight=0 liquidity_trap=0 near_gap_pct=-0.338
[16:06:33] tick balance=$305.94
  diag: trend=bullish atr_ratio=0.98 obs=9 obs_fresh=8 fvgs=17 bos=28 sigs=0 wrong_side=6 price_out=2 bos_miss=0 risk_neg=0 sl_too_tight=0 liquidity_trap=0 near_gap_pct=-0.399
[16:07:34] tick balance=$305.94
  diag: trend=bullish atr_ratio=0.99 obs=9 obs_fresh=8 fvgs=17 bos=28 sigs=0 wrong_side=6 price_out=2 bos_miss=0 risk_neg=0 sl_too_tight=0 liquidity_trap=0 near_gap_pct=-0.379
[16:08:36] tick balance=$305.94
  diag: trend=bullish atr_ratio=1.0 obs=9 obs_fresh=8 fvgs=17 bos=29 sigs=0 wrong_side=6 price_out=2 bos_miss=0 risk_neg=0 sl_too_tight=0 liquidity_trap=0 near_gap_pct=-0.321
[16:09:37] tick balance=$305.94
  diag: trend=bullish atr_ratio=1.01 obs=9 obs_fresh=8 fvgs=17 bos=29 sigs=0 wrong_side=6 price_out=2 bos_miss=0 risk_neg=0 sl_too_tight=0 liquidity_trap=0 near_gap_pct=-0.261
[16:10:39] tick balance=$305.94
  diag: trend=bullish atr_ratio=1.02 obs=9 obs_fresh=8 fvgs=17 bos=28 sigs=0 wrong_side=6 price_out=2 bos_miss=0 risk_neg=0 sl_too_tight=0 liquidity_trap=0 near_gap_pct=-0.28
[16:11:40] tick balance=$305.94
  diag: trend=bullish atr_ratio=1.02 obs=9 obs_fresh=8 fvgs=17 bos=28 sigs=0 wrong_side=6 price_out=2 bos_miss=0 risk_neg=0 sl_too_tight=0 liquidity_trap=0 near_gap_pct=-0.237
[16:12:42] tick balance=$305.94
  diag: trend=bullish atr_ratio=1.02 obs=9 obs_fresh=8 fvgs=17 bos=28 sigs=0 wrong_side=6 price_out=2 bos_miss=0 risk_neg=0 sl_too_tight=0 liquidity_trap=0 near_gap_pct=-0.27
[16:13:44] tick balance=$305.94
  diag: trend=bullish atr_ratio=1.02 obs=9 obs_fresh=8 fvgs=17 bos=28 sigs=0 wrong_side=6 price_out=2 bos_miss=0 risk_neg=0 sl_too_tight=0 liquidity_trap=0 near_gap_pct=-0.283
[16:14:45] tick balance=$305.94
  diag: trend=bullish atr_ratio=1.03 obs=9 obs_fresh=8 fvgs=17 bos=28 sigs=0 wrong_side=6 price_out=2 bos_miss=0 risk_neg=0 sl_too_tight=0 liquidity_trap=0 near_gap_pct=-0.27
[16:15:47] tick balance=$305.94
  diag: trend=bullish atr_ratio=1.03 obs=9 obs_fresh=8 fvgs=17 bos=28 sigs=0 wrong_side=6 price_out=2 bos_miss=0 risk_neg=0 sl_too_tight=0 liquidity_trap=0 near_gap_pct=-0.195
[16:16:48] tick balance=$305.94
  diag: trend=bullish atr_ratio=1.03 obs=9 obs_fresh=8 fvgs=17 bos=28 sigs=0 wrong_side=6 price_out=2 bos_miss=0 risk_neg=0 sl_too_tight=0 liquidity_trap=0 near_gap_pct=-0.181
[16:17:50] tick balance=$305.94
  diag: trend=bullish atr_ratio=1.03 obs=9 obs_fresh=8 fvgs=17 bos=28 sigs=0 wrong_side=6 price_out=2 bos_miss=0 risk_neg=0 sl_too_tight=0 liquidity_trap=0 near_gap_pct=-0.181
[16:18:51] tick balance=$305.94
  diag: trend=bullish atr_ratio=1.03 obs=9 obs_fresh=8 fvgs=17 bos=28 sigs=0 wrong_side=6 price_out=2 bos_miss=0 risk_neg=0 sl_too_tight=0 liquidity_trap=0 near_gap_pct=-0.121
[16:19:53] tick balance=$305.94
  diag: trend=bullish atr_ratio=1.03 obs=9 obs_fresh=8 fvgs=17 bos=28 sigs=0 wrong_side=6 price_out=2 bos_miss=0 risk_neg=0 sl_too_tight=0 liquidity_trap=0 near_gap_pct=-0.183
[16:20:55] tick balance=$305.94
  diag: trend=bullish atr_ratio=0.98 obs=9 obs_fresh=8 fvgs=18 bos=29 sigs=0 wrong_side=6 price_out=2 bos_miss=0 risk_neg=0 sl_too_tight=0 liquidity_trap=0 near_gap_pct=-0.186
[16:21:56] tick balance=$305.94
  diag: trend=bullish atr_ratio=1.0 obs=9 obs_fresh=8 fvgs=18 bos=29 sigs=0 wrong_side=6 price_out=2 bos_miss=0 risk_neg=0 sl_too_tight=0 liquidity_trap=0 near_gap_pct=-0.166
[16:22:58] tick balance=$305.94
  diag: trend=bullish atr_ratio=1.0 obs=9 obs_fresh=8 fvgs=18 bos=28 sigs=0 wrong_side=6 price_out=2 bos_miss=0 risk_neg=0 sl_too_tight=0 liquidity_trap=0 near_gap_pct=-0.145
[16:23:59] tick balance=$305.94
  diag: trend=bullish atr_ratio=1.0 obs=9 obs_fresh=8 fvgs=18 bos=28 sigs=0 wrong_side=6 price_out=2 bos_miss=0 risk_neg=0 sl_too_tight=0 liquidity_trap=0 near_gap_pct=-0.118
[16:25:00] tick balance=$305.94
  diag: trend=bullish atr_ratio=1.0 obs=9 obs_fresh=8 fvgs=18 bos=28 sigs=0 wrong_side=6 price_out=2 bos_miss=0 risk_neg=0 sl_too_tight=0 liquidity_trap=0 near_gap_pct=-0.171
[16:26:02] tick balance=$305.94
  diag: trend=bullish atr_ratio=0.97 obs=9 obs_fresh=8 fvgs=18 bos=28 sigs=0 wrong_side=6 price_out=1 bos_miss=1 risk_neg=0 sl_too_tight=0 liquidity_trap=0 near_gap_pct=-0.111
[16:27:04] tick balance=$305.94
  diag: trend=bullish atr_ratio=0.97 obs=9 obs_fresh=8 fvgs=18 bos=27 sigs=0 wrong_side=6 price_out=2 bos_miss=0 risk_neg=0 sl_too_tight=0 liquidity_trap=0 near_gap_pct=-0.137
[16:28:06] tick balance=$305.94
  diag: trend=bullish atr_ratio=0.97 obs=9 obs_fresh=8 fvgs=18 bos=27 sigs=0 wrong_side=6 price_out=2 bos_miss=0 risk_neg=0 sl_too_tight=0 liquidity_trap=0 near_gap_pct=-0.118
[16:29:08] tick balance=$305.94
  diag: trend=bullish atr_ratio=1.0 obs=9 obs_fresh=8 fvgs=18 bos=27 sigs=0 wrong_side=6 price_out=1 bos_miss=1 risk_neg=0 sl_too_tight=0 liquidity_trap=0 near_gap_pct=-0.06
[16:30:10] tick balance=$305.94
  diag: trend=bullish atr_ratio=0.83 obs=8 obs_fresh=7 fvgs=18 bos=28 sigs=0 wrong_side=5 price_out=1 bos_miss=1 risk_neg=0 sl_too_tight=0 liquidity_trap=0 near_gap_pct=0.002
[16:31:12] tick balance=$305.94
  diag: trend=bullish atr_ratio=0.84 obs=8 obs_fresh=7 fvgs=18 bos=27 sigs=0 wrong_side=5 price_out=1 bos_miss=1 risk_neg=0 sl_too_tight=0 liquidity_trap=0 near_gap_pct=0.024
[16:32:14] tick balance=$305.94
  diag: trend=bullish atr_ratio=0.84 obs=8 obs_fresh=7 fvgs=18 bos=27 sigs=0 wrong_side=5 price_out=1 bos_miss=1 risk_neg=0 sl_too_tight=0 liquidity_trap=0 near_gap_pct=0.022
[16:33:16] tick balance=$305.94
  diag: trend=bullish atr_ratio=0.86 obs=8 obs_fresh=7 fvgs=18 bos=27 sigs=0 wrong_side=5 price_out=1 bos_miss=1 risk_neg=0 sl_too_tight=0 liquidity_trap=0 near_gap_pct=-0.111
[16:34:18] tick balance=$305.94
  diag: trend=bullish atr_ratio=0.88 obs=8 obs_fresh=7 fvgs=18 bos=27 sigs=0 wrong_side=5 price_out=0 bos_miss=2 risk_neg=0 sl_too_tight=0 liquidity_trap=0 near_gap_pct=-0.072
[16:35:20] tick balance=$305.94
  diag: trend=bullish atr_ratio=0.82 obs=8 obs_fresh=7 fvgs=19 bos=27 sigs=0 wrong_side=5 price_out=0 bos_miss=2 risk_neg=0 sl_too_tight=0 liquidity_trap=0 near_gap_pct=-0.041
[16:36:22] tick balance=$305.94
  diag: trend=bullish atr_ratio=0.84 obs=8 obs_fresh=7 fvgs=19 bos=26 sigs=0 wrong_side=5 price_out=0 bos_miss=2 risk_neg=0 sl_too_tight=0 liquidity_trap=0 near_gap_pct=-0.067
[16:37:23] tick balance=$305.94
  diag: trend=bullish atr_ratio=0.85 obs=8 obs_fresh=7 fvgs=19 bos=27 sigs=0 wrong_side=5 price_out=1 bos_miss=1 risk_neg=0 sl_too_tight=0 liquidity_trap=0 near_gap_pct=-0.125
[16:38:25] tick balance=$305.94
  diag: trend=bullish atr_ratio=0.86 obs=8 obs_fresh=7 fvgs=19 bos=27 sigs=0 wrong_side=5 price_out=1 bos_miss=1 risk_neg=0 sl_too_tight=0 liquidity_trap=0 near_gap_pct=-0.14
[16:39:26] tick balance=$305.94
  diag: trend=bullish atr_ratio=0.86 obs=8 obs_fresh=7 fvgs=19 bos=27 sigs=0 wrong_side=5 price_out=0 bos_miss=2 risk_neg=0 sl_too_tight=0 liquidity_trap=0 near_gap_pct=-0.091
[16:40:27] tick balance=$305.94
  diag: trend=bullish atr_ratio=0.84 obs=7 obs_fresh=7 fvgs=19 bos=27 sigs=0 wrong_side=5 price_out=1 bos_miss=1 risk_neg=0 sl_too_tight=0 liquidity_trap=0 near_gap_pct=-0.144
[16:41:28] tick balance=$305.94
  diag: trend=bullish atr_ratio=0.85 obs=7 obs_fresh=7 fvgs=19 bos=27 sigs=0 wrong_side=5 price_out=0 bos_miss=2 risk_neg=0 sl_too_tight=0 liquidity_trap=0 near_gap_pct=-0.063
[16:42:30] tick balance=$305.94
  diag: trend=bullish atr_ratio=0.86 obs=7 obs_fresh=7 fvgs=19 bos=27 sigs=0 wrong_side=5 price_out=0 bos_miss=2 risk_neg=0 sl_too_tight=0 liquidity_trap=0 near_gap_pct=-0.046
[16:43:33] tick balance=$305.94
  diag: trend=bullish atr_ratio=0.86 obs=7 obs_fresh=7 fvgs=19 bos=27 sigs=0 wrong_side=5 price_out=1 bos_miss=1 risk_neg=0 sl_too_tight=0 liquidity_trap=0 near_gap_pct=-0.116
[16:44:35] tick balance=$305.94
  diag: trend=bullish atr_ratio=0.87 obs=7 obs_fresh=7 fvgs=19 bos=27 sigs=0 wrong_side=5 price_out=1 bos_miss=1 risk_neg=0 sl_too_tight=0 liquidity_trap=0 near_gap_pct=0.024
[16:45:37] tick balance=$305.94
  diag: trend=bullish atr_ratio=0.85 obs=7 obs_fresh=7 fvgs=19 bos=26 sigs=0 wrong_side=5 price_out=1 bos_miss=1 risk_neg=0 sl_too_tight=0 liquidity_trap=0 near_gap_pct=-0.144
[16:46:39] tick balance=$305.94
  diag: trend=bullish atr_ratio=0.85 obs=7 obs_fresh=7 fvgs=19 bos=27 sigs=0 wrong_side=5 price_out=1 bos_miss=1 risk_neg=0 sl_too_tight=0 liquidity_trap=0 near_gap_pct=0.026
[16:47:41] tick balance=$305.94
  diag: trend=bullish atr_ratio=0.87 obs=7 obs_fresh=7 fvgs=19 bos=26 sigs=0 wrong_side=5 price_out=1 bos_miss=1 risk_neg=0 sl_too_tight=0 liquidity_trap=0 near_gap_pct=-0.036
[16:48:43] tick balance=$305.94
  diag: trend=bullish atr_ratio=0.88 obs=7 obs_fresh=7 fvgs=19 bos=25 sigs=0 wrong_side=5 price_out=1 bos_miss=1 risk_neg=0 sl_too_tight=0 liquidity_trap=0 near_gap_pct=-0.087
[16:49:45] tick balance=$305.94
  diag: trend=bullish atr_ratio=0.88 obs=7 obs_fresh=7 fvgs=19 bos=25 sigs=0 wrong_side=5 price_out=1 bos_miss=1 risk_neg=0 sl_too_tight=0 liquidity_trap=0 near_gap_pct=0.019
[16:50:47] tick balance=$305.94
  diag: trend=bullish atr_ratio=0.85 obs=7 obs_fresh=7 fvgs=18 bos=26 sigs=0 wrong_side=5 price_out=1 bos_miss=1 risk_neg=0 sl_too_tight=0 liquidity_trap=0 near_gap_pct=0.005
[16:51:49] tick balance=$305.94
  diag: trend=bullish atr_ratio=0.87 obs=7 obs_fresh=7 fvgs=18 bos=26 sigs=0 wrong_side=5 price_out=1 bos_miss=1 risk_neg=0 sl_too_tight=0 liquidity_trap=0 near_gap_pct=-0.065
[16:52:51] tick balance=$305.94
  diag: trend=bullish atr_ratio=0.91 obs=7 obs_fresh=7 fvgs=18 bos=26 sigs=0 wrong_side=5 price_out=2 bos_miss=0 risk_neg=0 sl_too_tight=0 liquidity_trap=0 near_gap_pct=-0.193
[16:53:53] tick balance=$305.94
  diag: trend=bullish atr_ratio=0.91 obs=7 obs_fresh=7 fvgs=18 bos=26 sigs=0 wrong_side=5 price_out=2 bos_miss=0 risk_neg=0 sl_too_tight=0 liquidity_trap=0 near_gap_pct=-0.157
[16:54:55] tick balance=$305.94
  diag: trend=bullish atr_ratio=0.92 obs=7 obs_fresh=7 fvgs=18 bos=26 sigs=0 wrong_side=5 price_out=2 bos_miss=0 risk_neg=0 sl_too_tight=0 liquidity_trap=0 near_gap_pct=-0.212
```
