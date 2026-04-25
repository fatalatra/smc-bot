# Bot Snapshot — 2026-04-25 18:55 UTC

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
     93 trend_htf=ranging trend_mid=ranging skip=trend_mismatch
      3 trend=bullish skip=adx_low adx=19.0 min=20.0
      1 trend=bullish skip=adx_low adx=19.8 min=20.0
      1 trend=bullish skip=adx_low adx=19.2 min=20.0
      1 trend=bullish skip=adx_low adx=19.1 min=20.0
      1 trend=bullish atr_ratio=0.9 obs=7 obs_fresh=7 fvgs=18 bos=27 sigs=0 wrong_side=5 price_out=2 bos_miss=0 risk_neg=0 sl_too_tight=0 liquidity_trap=0 near_gap_pct=-0.241
      1 trend=bullish atr_ratio=0.9 obs=7 obs_fresh=7 fvgs=17 bos=27 sigs=0 wrong_side=5 price_out=1 bos_miss=0 risk_neg=0 sl_too_tight=1 liquidity_trap=0 near_gap_pct=-0.072
      1 trend=bullish atr_ratio=0.9 obs=7 obs_fresh=7 fvgs=17 bos=26 sigs=0 wrong_side=5 price_out=1 bos_miss=1 risk_neg=0 sl_too_tight=0 liquidity_trap=0 near_gap_pct=-0.039
      1 trend=bullish atr_ratio=0.9 obs=7 obs_fresh=7 fvgs=16 bos=27 sigs=0 wrong_side=4 price_out=2 bos_miss=0 risk_neg=0 sl_too_tight=1 liquidity_trap=0 near_gap_pct=0.005
      1 trend=bullish atr_ratio=0.9 obs=6 obs_fresh=6 fvgs=16 bos=28 sigs=0 wrong_side=4 price_out=1 bos_miss=1 risk_neg=0 sl_too_tight=0 liquidity_trap=0 near_gap_pct=-0.116
      1 trend=bullish atr_ratio=0.9 obs=6 obs_fresh=6 fvgs=15 bos=26 sigs=0 wrong_side=4 price_out=0 bos_miss=2 risk_neg=0 sl_too_tight=0 liquidity_trap=0 near_gap_pct=-0.046
      1 trend=bullish atr_ratio=0.98 obs=7 obs_fresh=7 fvgs=17 bos=27 sigs=0 wrong_side=5 price_out=2 bos_miss=0 risk_neg=0 sl_too_tight=0 liquidity_trap=0 near_gap_pct=-0.309
      1 trend=bullish atr_ratio=0.98 obs=7 obs_fresh=7 fvgs=17 bos=27 sigs=0 wrong_side=5 price_out=2 bos_miss=0 risk_neg=0 sl_too_tight=0 liquidity_trap=0 near_gap_pct=-0.258
      1 trend=bullish atr_ratio=0.98 obs=6 obs_fresh=6 fvgs=17 bos=27 sigs=0 wrong_side=4 price_out=0 bos_miss=2 risk_neg=0 sl_too_tight=0 liquidity_trap=0 near_gap_pct=-0.077
      1 trend=bullish atr_ratio=0.97 obs=8 obs_fresh=8 fvgs=16 bos=26 sigs=0 wrong_side=5 price_out=2 bos_miss=0 risk_neg=0 sl_too_tight=1 liquidity_trap=0 near_gap_pct=-0.108
      1 trend=bullish atr_ratio=0.97 obs=8 obs_fresh=8 fvgs=16 bos=26 sigs=0 wrong_side=5 price_out=2 bos_miss=0 risk_neg=0 sl_too_tight=1 liquidity_trap=0 near_gap_pct=0.002
      1 trend=bullish atr_ratio=0.97 obs=7 obs_fresh=7 fvgs=17 bos=27 sigs=0 wrong_side=5 price_out=2 bos_miss=0 risk_neg=0 sl_too_tight=0 liquidity_trap=0 near_gap_pct=-0.237
      1 trend=bullish atr_ratio=0.97 obs=7 obs_fresh=7 fvgs=17 bos=27 sigs=0 wrong_side=5 price_out=2 bos_miss=0 risk_neg=0 sl_too_tight=0 liquidity_trap=0 near_gap_pct=-0.232
      1 trend=bullish atr_ratio=0.97 obs=7 obs_fresh=7 fvgs=17 bos=27 sigs=0 wrong_side=5 price_out=2 bos_miss=0 risk_neg=0 sl_too_tight=0 liquidity_trap=0 near_gap_pct=-0.198
      1 trend=bullish atr_ratio=0.97 obs=7 obs_fresh=7 fvgs=16 bos=26 sigs=0 wrong_side=4 price_out=2 bos_miss=0 risk_neg=0 sl_too_tight=1 liquidity_trap=0 near_gap_pct=-0.082
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
[20:04:05] tick balance=$305.94
  diag: trend=bearish atr_ratio=0.91 obs=6 obs_fresh=6 fvgs=16 bos=29 sigs=0 wrong_side=3 price_out=2 bos_miss=0 risk_neg=0 sl_too_tight=1 liquidity_trap=0 near_gap_pct=-0.119
[20:05:06] tick balance=$305.94
  diag: trend=bearish atr_ratio=0.85 obs=6 obs_fresh=6 fvgs=15 bos=29 sigs=0 wrong_side=3 price_out=2 bos_miss=0 risk_neg=0 sl_too_tight=1 liquidity_trap=0 near_gap_pct=-0.085
[20:06:09] tick balance=$305.94
  diag: trend=bearish atr_ratio=0.87 obs=6 obs_fresh=6 fvgs=15 bos=28 sigs=0 wrong_side=3 price_out=2 bos_miss=0 risk_neg=0 sl_too_tight=1 liquidity_trap=0 near_gap_pct=-0.102
[20:07:11] tick balance=$305.94
  diag: trend=bearish atr_ratio=0.89 obs=6 obs_fresh=6 fvgs=15 bos=29 sigs=0 wrong_side=3 price_out=2 bos_miss=0 risk_neg=0 sl_too_tight=1 liquidity_trap=0 near_gap_pct=-0.083
[20:08:14] tick balance=$305.94
  diag: trend=bearish atr_ratio=0.89 obs=6 obs_fresh=6 fvgs=15 bos=28 sigs=0 wrong_side=3 price_out=2 bos_miss=0 risk_neg=0 sl_too_tight=1 liquidity_trap=0 near_gap_pct=-0.127
[20:09:16] tick balance=$305.94
  diag: trend=bearish atr_ratio=0.9 obs=6 obs_fresh=6 fvgs=15 bos=28 sigs=0 wrong_side=3 price_out=2 bos_miss=0 risk_neg=0 sl_too_tight=1 liquidity_trap=0 near_gap_pct=-0.209
[20:10:18] tick balance=$305.94
  diag: trend=bearish atr_ratio=0.86 obs=6 obs_fresh=6 fvgs=15 bos=28 sigs=0 wrong_side=3 price_out=2 bos_miss=0 risk_neg=0 sl_too_tight=1 liquidity_trap=0 near_gap_pct=-0.168
[20:11:19] tick balance=$305.94
  diag: trend=bearish atr_ratio=0.88 obs=6 obs_fresh=6 fvgs=15 bos=28 sigs=0 wrong_side=3 price_out=2 bos_miss=0 risk_neg=0 sl_too_tight=1 liquidity_trap=0 near_gap_pct=-0.241
[20:12:20] tick balance=$305.94
  diag: trend=bearish atr_ratio=0.88 obs=6 obs_fresh=6 fvgs=15 bos=27 sigs=0 wrong_side=3 price_out=2 bos_miss=0 risk_neg=0 sl_too_tight=1 liquidity_trap=0 near_gap_pct=-0.212
[20:13:22] tick balance=$305.94
  diag: trend=bearish atr_ratio=0.88 obs=6 obs_fresh=6 fvgs=15 bos=27 sigs=0 wrong_side=3 price_out=2 bos_miss=0 risk_neg=0 sl_too_tight=1 liquidity_trap=0 near_gap_pct=-0.229
[20:14:23] tick balance=$305.94
  diag: trend=bearish atr_ratio=0.89 obs=6 obs_fresh=6 fvgs=15 bos=27 sigs=0 wrong_side=3 price_out=2 bos_miss=0 risk_neg=0 sl_too_tight=1 liquidity_trap=0 near_gap_pct=-0.221
[20:15:25] tick balance=$305.94
  diag: trend=bearish atr_ratio=0.85 obs=6 obs_fresh=6 fvgs=15 bos=28 sigs=0 wrong_side=3 price_out=2 bos_miss=0 risk_neg=0 sl_too_tight=1 liquidity_trap=0 near_gap_pct=-0.158
[20:16:27] tick balance=$305.94
  diag: trend=bearish atr_ratio=0.88 obs=6 obs_fresh=6 fvgs=15 bos=28 sigs=0 wrong_side=3 price_out=2 bos_miss=0 risk_neg=0 sl_too_tight=1 liquidity_trap=0 near_gap_pct=-0.216
[20:17:29] tick balance=$305.94
  diag: trend=bearish atr_ratio=0.88 obs=6 obs_fresh=6 fvgs=15 bos=28 sigs=0 wrong_side=3 price_out=2 bos_miss=0 risk_neg=0 sl_too_tight=1 liquidity_trap=0 near_gap_pct=-0.173
[20:18:31] tick balance=$305.94
  diag: trend=bearish atr_ratio=0.88 obs=6 obs_fresh=6 fvgs=15 bos=28 sigs=0 wrong_side=3 price_out=2 bos_miss=0 risk_neg=0 sl_too_tight=1 liquidity_trap=0 near_gap_pct=-0.207
[20:19:33] tick balance=$305.94
  diag: trend=bearish atr_ratio=0.89 obs=6 obs_fresh=6 fvgs=15 bos=27 sigs=0 wrong_side=3 price_out=2 bos_miss=0 risk_neg=0 sl_too_tight=1 liquidity_trap=0 near_gap_pct=-0.262
[20:20:35] tick balance=$305.94
  diag: trend=bearish atr_ratio=0.87 obs=6 obs_fresh=6 fvgs=15 bos=27 sigs=0 wrong_side=3 price_out=2 bos_miss=0 risk_neg=0 sl_too_tight=1 liquidity_trap=0 near_gap_pct=-0.279
[20:21:37] tick balance=$305.94
  diag: trend=bearish atr_ratio=0.88 obs=6 obs_fresh=6 fvgs=14 bos=27 sigs=0 wrong_side=3 price_out=3 bos_miss=0 risk_neg=0 sl_too_tight=0 liquidity_trap=0 near_gap_pct=-0.296
[20:22:38] tick balance=$305.94
  diag: trend=bearish atr_ratio=0.88 obs=6 obs_fresh=6 fvgs=14 bos=27 sigs=0 wrong_side=3 price_out=2 bos_miss=0 risk_neg=0 sl_too_tight=1 liquidity_trap=0 near_gap_pct=-0.282
[20:23:40] tick balance=$305.94
  diag: trend=bearish atr_ratio=0.88 obs=6 obs_fresh=6 fvgs=14 bos=28 sigs=0 wrong_side=3 price_out=3 bos_miss=0 risk_neg=0 sl_too_tight=0 liquidity_trap=0 near_gap_pct=-0.296
[20:24:42] tick balance=$305.94
  diag: trend=bearish atr_ratio=0.9 obs=6 obs_fresh=6 fvgs=14 bos=28 sigs=0 wrong_side=3 price_out=2 bos_miss=0 risk_neg=0 sl_too_tight=1 liquidity_trap=0 near_gap_pct=-0.284
[20:25:44] tick balance=$305.94
  diag: trend=bearish atr_ratio=0.88 obs=6 obs_fresh=6 fvgs=14 bos=28 sigs=0 wrong_side=3 price_out=3 bos_miss=0 risk_neg=0 sl_too_tight=0 liquidity_trap=0 near_gap_pct=-0.304
[20:26:46] tick balance=$305.94
  diag: trend=bearish atr_ratio=0.89 obs=6 obs_fresh=6 fvgs=14 bos=29 sigs=0 wrong_side=3 price_out=3 bos_miss=0 risk_neg=0 sl_too_tight=0 liquidity_trap=0 near_gap_pct=-0.33
[20:27:47] tick balance=$305.94
  diag: trend=bearish atr_ratio=0.89 obs=6 obs_fresh=6 fvgs=14 bos=29 sigs=0 wrong_side=3 price_out=3 bos_miss=0 risk_neg=0 sl_too_tight=0 liquidity_trap=0 near_gap_pct=-0.338
[20:28:49] tick balance=$305.94
  diag: trend=bearish atr_ratio=0.89 obs=6 obs_fresh=6 fvgs=14 bos=29 sigs=0 wrong_side=3 price_out=3 bos_miss=0 risk_neg=0 sl_too_tight=0 liquidity_trap=0 near_gap_pct=-0.335
[20:29:52] tick balance=$305.94
  diag: trend=bearish atr_ratio=0.91 obs=6 obs_fresh=6 fvgs=14 bos=29 sigs=0 wrong_side=3 price_out=3 bos_miss=0 risk_neg=0 sl_too_tight=0 liquidity_trap=0 near_gap_pct=-0.405
[20:30:53] tick balance=$305.94
  diag: trend=bearish atr_ratio=0.82 obs=6 obs_fresh=6 fvgs=13 bos=28 sigs=0 wrong_side=3 price_out=3 bos_miss=0 risk_neg=0 sl_too_tight=0 liquidity_trap=0 near_gap_pct=-0.4
[20:31:56] tick balance=$305.94
  diag: trend=bearish atr_ratio=0.84 obs=6 obs_fresh=6 fvgs=13 bos=28 sigs=0 wrong_side=3 price_out=2 bos_miss=0 risk_neg=0 sl_too_tight=0 liquidity_trap=1 near_gap_pct=-0.451
[20:32:57] tick balance=$305.94
  diag: trend=bearish atr_ratio=0.85 obs=6 obs_fresh=6 fvgs=13 bos=28 sigs=0 wrong_side=3 price_out=2 bos_miss=0 risk_neg=0 sl_too_tight=0 liquidity_trap=1 near_gap_pct=-0.461
[20:33:59] tick balance=$305.94
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:35:00] tick balance=$305.94
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:36:02] tick balance=$305.94
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:37:04] tick balance=$305.94
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:38:06] tick balance=$305.94
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:39:08] tick balance=$305.94
  diag: trend=bearish atr_ratio=0.87 obs=6 obs_fresh=6 fvgs=13 bos=28 sigs=0 wrong_side=3 price_out=2 bos_miss=0 risk_neg=0 sl_too_tight=0 liquidity_trap=1 near_gap_pct=-0.512
[20:40:09] tick balance=$305.94
  diag: trend=bearish atr_ratio=0.86 obs=6 obs_fresh=6 fvgs=13 bos=27 sigs=0 wrong_side=3 price_out=3 bos_miss=0 risk_neg=0 sl_too_tight=0 liquidity_trap=0 near_gap_pct=-0.42
[20:41:11] tick balance=$305.94
  diag: trend=bearish atr_ratio=0.86 obs=6 obs_fresh=6 fvgs=13 bos=27 sigs=0 wrong_side=3 price_out=3 bos_miss=0 risk_neg=0 sl_too_tight=0 liquidity_trap=0 near_gap_pct=-0.396
[20:42:13] tick balance=$305.94
  diag: trend=bearish atr_ratio=0.88 obs=6 obs_fresh=6 fvgs=13 bos=26 sigs=0 wrong_side=3 price_out=3 bos_miss=0 risk_neg=0 sl_too_tight=0 liquidity_trap=0 near_gap_pct=-0.4
[20:43:14] tick balance=$305.94
  diag: trend=bearish atr_ratio=0.88 obs=6 obs_fresh=6 fvgs=13 bos=26 sigs=0 wrong_side=3 price_out=3 bos_miss=0 risk_neg=0 sl_too_tight=0 liquidity_trap=0 near_gap_pct=-0.379
[20:44:16] tick balance=$305.94
  diag: trend=bearish atr_ratio=0.88 obs=6 obs_fresh=6 fvgs=13 bos=26 sigs=0 wrong_side=3 price_out=3 bos_miss=0 risk_neg=0 sl_too_tight=0 liquidity_trap=0 near_gap_pct=-0.371
[20:45:18] tick balance=$305.94
  diag: trend=bearish atr_ratio=0.83 obs=6 obs_fresh=6 fvgs=14 bos=25 sigs=0 wrong_side=3 price_out=3 bos_miss=0 risk_neg=0 sl_too_tight=0 liquidity_trap=0 near_gap_pct=-0.364
[20:46:20] tick balance=$305.94
  diag: trend=bearish atr_ratio=0.85 obs=6 obs_fresh=6 fvgs=13 bos=25 sigs=0 wrong_side=3 price_out=3 bos_miss=0 risk_neg=0 sl_too_tight=0 liquidity_trap=0 near_gap_pct=-0.422
[20:47:22] tick balance=$305.94
  diag: trend=bearish atr_ratio=0.85 obs=6 obs_fresh=6 fvgs=13 bos=26 sigs=0 wrong_side=3 price_out=3 bos_miss=0 risk_neg=0 sl_too_tight=0 liquidity_trap=0 near_gap_pct=-0.371
[20:48:24] tick balance=$305.94
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:49:26] tick balance=$305.94
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:50:27] tick balance=$305.94
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:51:29] tick balance=$305.94
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:52:31] tick balance=$305.94
  diag: trend=bearish atr_ratio=0.86 obs=6 obs_fresh=6 fvgs=13 bos=26 sigs=0 wrong_side=3 price_out=2 bos_miss=0 risk_neg=0 sl_too_tight=0 liquidity_trap=1 near_gap_pct=-0.454
[20:53:33] tick balance=$305.94
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:54:34] tick balance=$305.94
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
```
