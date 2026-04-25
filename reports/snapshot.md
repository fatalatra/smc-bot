# Bot Snapshot — 2026-04-25 10:55 UTC

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
     25 trend=bullish skip=adx_low adx=12.5 min=20.0
     25 trend=bullish skip=adx_low adx=11.5 min=20.0
     15 trend=bullish skip=adx_low adx=17.1 min=20.0
     15 trend=bullish skip=adx_low adx=10.9 min=20.0
     15 trend=bullish skip=adx_low adx=10.2 min=20.0
     10 trend=bullish skip=adx_low adx=12.4 min=20.0
      9 trend=bullish skip=adx_low adx=13.8 min=20.0
      8 trend=bullish skip=adx_low adx=12.6 min=20.0
      7 trend=bullish skip=adx_low adx=11.8 min=20.0
      7 trend=bullish skip=adx_low adx=10.7 min=20.0
      6 trend_htf=ranging trend_mid=ranging skip=trend_mismatch
      6 trend=bullish skip=adx_low adx=11.4 min=20.0
      6 trend=bullish skip=adx_low adx=10.5 min=20.0
      6 trend=bullish skip=adx_low adx=10.3 min=20.0
      4 trend=bullish skip=adx_low adx=11.7 min=20.0
      4 trend=bullish skip=adx_low adx=11.3 min=20.0
      4 trend=bullish skip=adx_low adx=10.1 min=20.0
      3 trend=bullish skip=adx_low adx=12.3 min=20.0
      3 trend=bullish skip=adx_low adx=12.0 min=20.0
      2 trend=bullish skip=adx_low adx=11.2 min=20.0
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
[12:03:05] tick balance=$305.94
  diag: trend=bullish atr_ratio=1.53 obs=9 obs_fresh=9 fvgs=18 bos=24 sigs=0 wrong_side=6 price_out=3 bos_miss=0 risk_neg=0 sl_too_tight=0 liquidity_trap=0 near_gap_pct=0.762
[12:04:06] tick balance=$305.94
  diag: trend=bullish atr_ratio=1.53 obs=9 obs_fresh=9 fvgs=18 bos=25 sigs=0 wrong_side=6 price_out=3 bos_miss=0 risk_neg=0 sl_too_tight=0 liquidity_trap=0 near_gap_pct=0.709
[12:05:09] tick balance=$305.94
  diag: trend=bullish atr_ratio=1.5 obs=9 obs_fresh=9 fvgs=17 bos=25 sigs=0 wrong_side=6 price_out=3 bos_miss=0 risk_neg=0 sl_too_tight=0 liquidity_trap=0 near_gap_pct=0.707
[12:06:12] tick balance=$305.94
  diag: trend=bullish atr_ratio=1.51 obs=9 obs_fresh=9 fvgs=17 bos=25 sigs=0 wrong_side=6 price_out=2 bos_miss=0 risk_neg=0 sl_too_tight=0 liquidity_trap=1 near_gap_pct=0.666
[12:07:15] tick balance=$305.94
  diag: trend=bullish atr_ratio=1.52 obs=9 obs_fresh=9 fvgs=17 bos=25 sigs=0 wrong_side=6 price_out=2 bos_miss=0 risk_neg=0 sl_too_tight=0 liquidity_trap=1 near_gap_pct=0.683
[12:08:17] tick balance=$305.94
  diag: trend=bullish atr_ratio=1.52 obs=9 obs_fresh=9 fvgs=17 bos=25 sigs=0 wrong_side=6 price_out=3 bos_miss=0 risk_neg=0 sl_too_tight=0 liquidity_trap=0 near_gap_pct=0.719
[12:09:19] tick balance=$305.94
  diag: trend=bullish atr_ratio=1.54 obs=9 obs_fresh=9 fvgs=17 bos=26 sigs=0 wrong_side=6 price_out=3 bos_miss=0 risk_neg=0 sl_too_tight=0 liquidity_trap=0 near_gap_pct=0.757
[12:10:21] tick balance=$305.94
  diag: trend=bullish atr_ratio=1.54 obs=9 obs_fresh=9 fvgs=17 bos=26 sigs=0 wrong_side=6 price_out=3 bos_miss=0 risk_neg=0 sl_too_tight=0 liquidity_trap=0 near_gap_pct=0.733
[12:11:23] tick balance=$305.94
  diag: trend=bullish atr_ratio=1.56 obs=9 obs_fresh=9 fvgs=17 bos=27 sigs=0 wrong_side=6 price_out=2 bos_miss=0 risk_neg=0 sl_too_tight=0 liquidity_trap=1 near_gap_pct=0.693
[12:12:26] tick balance=$305.94
  diag: trend=bullish atr_ratio=1.59 obs=9 obs_fresh=9 fvgs=17 bos=27 sigs=0 wrong_side=6 price_out=3 bos_miss=0 risk_neg=0 sl_too_tight=0 liquidity_trap=0 near_gap_pct=0.855
[12:13:28] tick balance=$305.94
  diag: trend=bullish atr_ratio=1.61 obs=9 obs_fresh=9 fvgs=17 bos=26 sigs=0 wrong_side=6 price_out=3 bos_miss=0 risk_neg=0 sl_too_tight=0 liquidity_trap=0 near_gap_pct=0.935
[12:14:30] tick balance=$305.94
  diag: trend=bullish atr_ratio=1.62 obs=9 obs_fresh=9 fvgs=17 bos=26 sigs=0 wrong_side=6 price_out=3 bos_miss=0 risk_neg=0 sl_too_tight=0 liquidity_trap=0 near_gap_pct=0.947
[12:15:33] tick balance=$305.94
  diag: trend=bullish atr_ratio=1.62 obs=8 obs_fresh=8 fvgs=17 bos=26 sigs=0 wrong_side=5 price_out=3 bos_miss=0 risk_neg=0 sl_too_tight=0 liquidity_trap=0 near_gap_pct=1.021
[12:16:35] tick balance=$305.94
  diag: trend=bullish atr_ratio=1.64 obs=8 obs_fresh=8 fvgs=17 bos=26 sigs=0 wrong_side=5 price_out=3 bos_miss=0 risk_neg=0 sl_too_tight=0 liquidity_trap=0 near_gap_pct=0.897
[12:17:37] tick balance=$305.94
  diag: trend=bullish atr_ratio=1.67 obs=8 obs_fresh=8 fvgs=17 bos=27 sigs=0 wrong_side=5 price_out=3 bos_miss=0 risk_neg=0 sl_too_tight=0 liquidity_trap=0 near_gap_pct=0.802
[12:18:39] tick balance=$305.94
  diag: trend=bullish atr_ratio=1.68 obs=8 obs_fresh=8 fvgs=16 bos=27 sigs=0 wrong_side=5 price_out=3 bos_miss=0 risk_neg=0 sl_too_tight=0 liquidity_trap=0 near_gap_pct=0.769
[12:19:42] tick balance=$305.94
  diag: trend=bullish atr_ratio=1.69 obs=8 obs_fresh=8 fvgs=16 bos=27 sigs=0 wrong_side=5 price_out=3 bos_miss=0 risk_neg=0 sl_too_tight=0 liquidity_trap=0 near_gap_pct=0.764
[12:20:44] tick balance=$305.94
  diag: trend=bullish atr_ratio=1.65 obs=8 obs_fresh=8 fvgs=16 bos=27 sigs=0 wrong_side=5 price_out=3 bos_miss=0 risk_neg=0 sl_too_tight=0 liquidity_trap=0 near_gap_pct=0.774
[12:21:46] tick balance=$305.94
  diag: trend=bullish atr_ratio=1.66 obs=8 obs_fresh=8 fvgs=16 bos=27 sigs=0 wrong_side=5 price_out=3 bos_miss=0 risk_neg=0 sl_too_tight=0 liquidity_trap=0 near_gap_pct=0.805
[12:22:49] tick balance=$305.94
  diag: trend=bullish atr_ratio=1.66 obs=8 obs_fresh=8 fvgs=16 bos=26 sigs=0 wrong_side=5 price_out=3 bos_miss=0 risk_neg=0 sl_too_tight=0 liquidity_trap=0 near_gap_pct=0.788
[12:23:52] tick balance=$305.94
  diag: trend=bullish atr_ratio=1.68 obs=8 obs_fresh=8 fvgs=16 bos=26 sigs=0 wrong_side=5 price_out=3 bos_miss=0 risk_neg=0 sl_too_tight=0 liquidity_trap=0 near_gap_pct=0.838
[12:24:54] tick balance=$305.94
  diag: trend=bullish atr_ratio=1.69 obs=8 obs_fresh=8 fvgs=16 bos=26 sigs=0 wrong_side=5 price_out=3 bos_miss=0 risk_neg=0 sl_too_tight=0 liquidity_trap=0 near_gap_pct=0.9
[12:25:56] tick balance=$305.94
  diag: trend=bullish atr_ratio=1.69 obs=8 obs_fresh=8 fvgs=16 bos=26 sigs=0 wrong_side=5 price_out=3 bos_miss=0 risk_neg=0 sl_too_tight=0 liquidity_trap=0 near_gap_pct=0.89
[12:26:59] tick balance=$305.94
  diag: trend=bullish atr_ratio=1.7 obs=8 obs_fresh=8 fvgs=16 bos=26 sigs=0 wrong_side=5 price_out=3 bos_miss=0 risk_neg=0 sl_too_tight=0 liquidity_trap=0 near_gap_pct=0.857
[12:28:01] tick balance=$305.94
  diag: trend=bullish atr_ratio=1.72 obs=8 obs_fresh=8 fvgs=16 bos=26 sigs=0 wrong_side=5 price_out=3 bos_miss=0 risk_neg=0 sl_too_tight=0 liquidity_trap=0 near_gap_pct=0.759
[tick] fetch err: 
[12:30:11] tick balance=$305.94
  diag: trend=bullish atr_ratio=1.74 obs=8 obs_fresh=8 fvgs=17 bos=25 sigs=0 wrong_side=5 price_out=3 bos_miss=0 risk_neg=0 sl_too_tight=0 liquidity_trap=0 near_gap_pct=0.707
[12:31:14] tick balance=$305.94
  diag: trend=bullish atr_ratio=1.74 obs=8 obs_fresh=8 fvgs=17 bos=25 sigs=0 wrong_side=5 price_out=3 bos_miss=0 risk_neg=0 sl_too_tight=0 liquidity_trap=0 near_gap_pct=0.704
[12:32:16] tick balance=$305.94
  diag: trend=bullish atr_ratio=1.74 obs=8 obs_fresh=8 fvgs=17 bos=25 sigs=0 wrong_side=5 price_out=3 bos_miss=0 risk_neg=0 sl_too_tight=0 liquidity_trap=0 near_gap_pct=0.721
[12:33:19] tick balance=$305.94
  diag: trend=bullish atr_ratio=1.75 obs=9 obs_fresh=9 fvgs=17 bos=25 sigs=0 wrong_side=6 price_out=2 bos_miss=0 risk_neg=0 sl_too_tight=0 liquidity_trap=1 near_gap_pct=0.645
[12:34:21] tick balance=$305.94
  diag: trend=bullish atr_ratio=1.75 obs=9 obs_fresh=9 fvgs=17 bos=24 sigs=0 wrong_side=6 price_out=2 bos_miss=0 risk_neg=0 sl_too_tight=0 liquidity_trap=1 near_gap_pct=0.676
[12:35:23] tick balance=$305.94
  diag: trend=bullish atr_ratio=1.76 obs=9 obs_fresh=9 fvgs=16 bos=25 sigs=0 wrong_side=6 price_out=3 bos_miss=0 risk_neg=0 sl_too_tight=0 liquidity_trap=0 near_gap_pct=0.743
[12:36:26] tick balance=$305.94
  diag: trend=bullish atr_ratio=1.77 obs=9 obs_fresh=9 fvgs=16 bos=25 sigs=0 wrong_side=6 price_out=3 bos_miss=0 risk_neg=0 sl_too_tight=0 liquidity_trap=0 near_gap_pct=0.75
[12:37:28] tick balance=$305.94
  diag: trend=bullish atr_ratio=1.8 obs=9 obs_fresh=9 fvgs=16 bos=25 sigs=0 wrong_side=6 price_out=3 bos_miss=0 risk_neg=0 sl_too_tight=0 liquidity_trap=0 near_gap_pct=0.883
[12:38:31] tick balance=$305.94
  diag: trend=bullish atr_ratio=1.81 obs=9 obs_fresh=9 fvgs=16 bos=25 sigs=0 wrong_side=6 price_out=3 bos_miss=0 risk_neg=0 sl_too_tight=0 liquidity_trap=0 near_gap_pct=0.759
[12:39:34] tick balance=$305.94
  diag: trend=bullish atr_ratio=1.81 obs=9 obs_fresh=9 fvgs=16 bos=25 sigs=0 wrong_side=6 price_out=3 bos_miss=0 risk_neg=0 sl_too_tight=0 liquidity_trap=0 near_gap_pct=0.75
[12:40:36] tick balance=$305.94
  diag: trend=bullish atr_ratio=1.53 obs=9 obs_fresh=9 fvgs=17 bos=25 sigs=0 wrong_side=6 price_out=3 bos_miss=0 risk_neg=0 sl_too_tight=0 liquidity_trap=0 near_gap_pct=0.738
[12:41:38] tick balance=$305.94
  diag: trend=bullish atr_ratio=1.55 obs=9 obs_fresh=9 fvgs=16 bos=25 sigs=0 wrong_side=6 price_out=2 bos_miss=0 risk_neg=0 sl_too_tight=0 liquidity_trap=1 near_gap_pct=0.688
[12:42:41] tick balance=$305.94
  diag: trend=bullish atr_ratio=1.56 obs=10 obs_fresh=10 fvgs=16 bos=25 sigs=0 wrong_side=6 price_out=3 bos_miss=0 risk_neg=0 sl_too_tight=1 liquidity_trap=0 near_gap_pct=0.062
[12:43:43] tick balance=$305.94
  diag: trend=bullish atr_ratio=1.56 obs=10 obs_fresh=10 fvgs=16 bos=25 sigs=0 wrong_side=6 price_out=3 bos_miss=0 risk_neg=0 sl_too_tight=1 liquidity_trap=0 near_gap_pct=0.058
[12:44:45] tick balance=$305.94
  diag: trend=bullish atr_ratio=1.57 obs=10 obs_fresh=10 fvgs=16 bos=25 sigs=0 wrong_side=6 price_out=3 bos_miss=0 risk_neg=0 sl_too_tight=1 liquidity_trap=0 near_gap_pct=0.074
[12:45:51] tick balance=$305.94
[!] Signal score 0.7 < 0.9, skipping: Long: Pure OB + BOS
  diag: trend=bullish atr_ratio=1.37 obs=10 obs_fresh=10 fvgs=16 bos=25 sigs=1 wrong_side=6 price_out=3 bos_miss=0 risk_neg=0 sl_too_tight=0 liquidity_trap=0 near_gap_pct=0.233 skip=low_score score=0.7
[12:46:56] tick balance=$305.94
  diag: trend=bullish atr_ratio=1.38 obs=10 obs_fresh=9 fvgs=16 bos=25 sigs=0 wrong_side=6 price_out=3 bos_miss=0 risk_neg=0 sl_too_tight=0 liquidity_trap=0 near_gap_pct=0.888
[12:47:59] tick balance=$305.94
  diag: trend=bullish atr_ratio=1.38 obs=10 obs_fresh=9 fvgs=16 bos=26 sigs=0 wrong_side=6 price_out=3 bos_miss=0 risk_neg=0 sl_too_tight=0 liquidity_trap=0 near_gap_pct=0.902
[12:49:01] tick balance=$305.94
  diag: trend=bullish atr_ratio=1.38 obs=10 obs_fresh=9 fvgs=16 bos=26 sigs=0 wrong_side=6 price_out=3 bos_miss=0 risk_neg=0 sl_too_tight=0 liquidity_trap=0 near_gap_pct=0.897
[12:50:03] tick balance=$305.94
  diag: trend=bullish atr_ratio=1.24 obs=10 obs_fresh=9 fvgs=17 bos=26 sigs=0 wrong_side=6 price_out=3 bos_miss=0 risk_neg=0 sl_too_tight=0 liquidity_trap=0 near_gap_pct=0.959
[12:51:04] tick balance=$305.94
  diag: trend=bullish atr_ratio=1.27 obs=10 obs_fresh=9 fvgs=17 bos=26 sigs=0 wrong_side=6 price_out=3 bos_miss=0 risk_neg=0 sl_too_tight=0 liquidity_trap=0 near_gap_pct=0.992
[12:52:07] tick balance=$305.94
  diag: trend=bullish atr_ratio=1.3 obs=10 obs_fresh=9 fvgs=17 bos=25 sigs=0 wrong_side=6 price_out=3 bos_miss=0 risk_neg=0 sl_too_tight=0 liquidity_trap=0 near_gap_pct=1.139
[12:53:09] tick balance=$305.94
  diag: trend=bullish atr_ratio=1.34 obs=10 obs_fresh=9 fvgs=17 bos=25 sigs=0 wrong_side=6 price_out=3 bos_miss=0 risk_neg=0 sl_too_tight=0 liquidity_trap=0 near_gap_pct=1.229
[12:54:11] tick balance=$305.94
  diag: trend=bullish atr_ratio=1.34 obs=10 obs_fresh=9 fvgs=17 bos=26 sigs=0 wrong_side=6 price_out=3 bos_miss=0 risk_neg=0 sl_too_tight=0 liquidity_trap=0 near_gap_pct=1.097
```
