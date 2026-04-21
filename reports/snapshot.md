# Bot Snapshot — 2026-04-21 14:55 UTC

## Service: active
balance=$297.45

## Config
POST_CLOSE_COOLDOWN: int = 180 # 3 мин техническая пауза после закрытия
RISK_PCT: float = 0.01 # 1% для старта на HYPE (вернём к 5% после 5+ сделок)
ADX_MIN: float = 20.0 # ADX < 20 → choppy market, skip entry

## Trades (last 20)
```
29|SELL|40.4||open|2026-04-21 14:00:28|
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
```

## Daily PnL
```
2026-04-21|296.96|0.49|0
2026-04-20|312.71|-15.75|0
2026-04-19|354.45|-41.74|0
2026-04-18|311.88|42.12|0
2026-04-17|328.7|-16.81|0
2026-04-16|381.29|-52.59|0
2026-04-15|363.1|17.9|0
```

## Open Positions
```
29|SELL|40.4|open
```

## Diag Summary (last ~4h)
```
     23 trend_htf=ranging trend_mid=ranging skip=trend_mismatch
     16 trend=bearish skip=ema_overextended price=40.3 ema20_h4=41.8 dist=1.5 max_dist=1.4
     15 trend=bearish skip=adx_low adx=10.3 min=20.0
     14 trend=bearish skip=adx_low adx=13.1 min=20.0
     12 trend=bearish skip=ema_overextended price=40.4 ema20_h4=41.8 dist=1.4 max_dist=1.4
     11 trend=bearish skip=adx_low adx=9.5 min=20.0
     11 trend=bearish skip=adx_low adx=14.3 min=20.0
     10 trend=bearish skip=ema_overextended price=40.2 ema20_h4=41.8 dist=1.6 max_dist=1.4
      8 trend=bearish skip=ema_overextended price=40.4 ema20_h4=41.8 dist=1.5 max_dist=1.4
      8 trend=bearish skip=adx_low adx=10.7 min=20.0
      7 trend=bearish skip=adx_low adx=15.8 min=20.0
      7 trend=bearish skip=adx_low adx=15.1 min=20.0
      7 trend=bearish skip=adx_low adx=11.8 min=20.0
      7 trend=bearish skip=adx_low adx=10.2 min=20.0
      6 trend=bearish skip=adx_low adx=10.0 min=20.0
      5 trend=bearish skip=adx_low adx=9.4 min=20.0
      5 trend=bearish skip=adx_low adx=9.3 min=20.0
      5 trend=bearish skip=adx_low adx=11.6 min=20.0
      4 trend=bearish skip=adx_low adx=9.1 min=20.0
      4 trend=bearish skip=adx_low adx=14.2 min=20.0
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
[16:02:33] tick balance=$297.17
  diag: trend=bearish skip=ema_overextended price=40.4 ema20_h4=41.8 dist=1.4 max_dist=1.4
[16:03:36] tick balance=$297.70
  diag: trend=bearish skip=ema_overextended price=40.3 ema20_h4=41.8 dist=1.5 max_dist=1.4
[16:04:38] tick balance=$297.33
  diag: trend=bearish skip=ema_overextended price=40.4 ema20_h4=41.8 dist=1.5 max_dist=1.4
[16:05:41] tick balance=$297.26
  diag: trend=bearish skip=ema_overextended price=40.4 ema20_h4=41.8 dist=1.4 max_dist=1.4
[16:06:44] tick balance=$297.62
  diag: trend=bearish skip=ema_overextended price=40.3 ema20_h4=41.8 dist=1.5 max_dist=1.4
[16:07:47] tick balance=$298.02
  diag: trend=bearish skip=ema_overextended price=40.3 ema20_h4=41.8 dist=1.5 max_dist=1.4
[16:08:51] tick balance=$297.45
  diag: trend=bearish skip=ema_overextended price=40.4 ema20_h4=41.8 dist=1.5 max_dist=1.4
[16:09:54] tick balance=$297.08
  diag: trend=bearish skip=ema_overextended price=40.4 ema20_h4=41.8 dist=1.4 max_dist=1.4
[16:10:58] tick balance=$297.45
  diag: trend=bearish skip=ema_overextended price=40.4 ema20_h4=41.8 dist=1.5 max_dist=1.4
[16:12:02] tick balance=$297.06
  diag: trend=bearish skip=ema_overextended price=40.4 ema20_h4=41.8 dist=1.4 max_dist=1.4
[16:13:04] tick balance=$297.56
  diag: trend=bearish skip=ema_overextended price=40.3 ema20_h4=41.8 dist=1.5 max_dist=1.4
[16:14:08] tick balance=$297.67
  diag: trend=bearish skip=ema_overextended price=40.3 ema20_h4=41.8 dist=1.5 max_dist=1.4
[16:15:11] tick balance=$296.61
  diag: trend=bearish atr_ratio=1.17 obs=9 obs_fresh=8 fvgs=19 bos=32 sigs=0 wrong_side=5 price_out=2 bos_miss=0 risk_neg=0 liquidity_trap=1 near_gap_pct=0.484
[16:16:15] tick balance=$296.13
  diag: trend=bearish atr_ratio=1.19 obs=9 obs_fresh=8 fvgs=19 bos=32 sigs=0 wrong_side=5 price_out=1 bos_miss=0 risk_neg=0 liquidity_trap=2 near_gap_pct=0.38
[16:17:17] tick balance=$295.32
  diag: trend=bearish atr_ratio=1.23 obs=9 obs_fresh=8 fvgs=19 bos=32 sigs=0 wrong_side=5 price_out=1 bos_miss=0 risk_neg=0 liquidity_trap=2 near_gap_pct=0.101
[16:18:20] tick balance=$295.63
  diag: trend=bearish atr_ratio=1.23 obs=9 obs_fresh=8 fvgs=19 bos=32 sigs=0 wrong_side=5 price_out=1 bos_miss=0 risk_neg=0 liquidity_trap=2 near_gap_pct=0.192
[16:19:23] tick balance=$295.72
  diag: trend=bearish atr_ratio=1.23 obs=9 obs_fresh=8 fvgs=19 bos=33 sigs=0 wrong_side=5 price_out=1 bos_miss=0 risk_neg=0 liquidity_trap=2 near_gap_pct=0.259
[16:20:26] tick balance=$295.99
  diag: trend=bearish atr_ratio=1.23 obs=8 obs_fresh=7 fvgs=19 bos=33 sigs=0 wrong_side=4 price_out=1 bos_miss=0 risk_neg=0 liquidity_trap=2 near_gap_pct=0.385
[16:21:29] tick balance=$295.85
  diag: trend=bearish atr_ratio=1.23 obs=8 obs_fresh=7 fvgs=19 bos=33 sigs=0 wrong_side=4 price_out=1 bos_miss=0 risk_neg=0 liquidity_trap=2 near_gap_pct=0.266
[16:22:32] tick balance=$295.73
  diag: trend=bearish atr_ratio=1.23 obs=8 obs_fresh=7 fvgs=19 bos=33 sigs=0 wrong_side=4 price_out=1 bos_miss=0 risk_neg=0 liquidity_trap=2 near_gap_pct=0.241
[16:23:34] tick balance=$296.50
  diag: trend=bearish atr_ratio=1.25 obs=8 obs_fresh=7 fvgs=19 bos=32 sigs=0 wrong_side=4 price_out=2 bos_miss=0 risk_neg=0 liquidity_trap=1 near_gap_pct=0.514
[16:24:38] tick balance=$296.40
  diag: trend=bearish atr_ratio=1.26 obs=8 obs_fresh=7 fvgs=19 bos=31 sigs=0 wrong_side=4 price_out=2 bos_miss=0 risk_neg=0 liquidity_trap=1 near_gap_pct=0.467
[16:25:41] tick balance=$296.29
  diag: trend=bearish atr_ratio=1.26 obs=8 obs_fresh=7 fvgs=18 bos=32 sigs=0 wrong_side=4 price_out=2 bos_miss=0 risk_neg=0 liquidity_trap=1 near_gap_pct=0.437
[16:26:44] tick balance=$296.61
  diag: trend=bearish atr_ratio=1.29 obs=8 obs_fresh=7 fvgs=18 bos=31 sigs=0 wrong_side=4 price_out=2 bos_miss=0 risk_neg=0 liquidity_trap=1 near_gap_pct=0.511
[16:27:48] tick balance=$296.54
  diag: trend=bearish atr_ratio=1.29 obs=8 obs_fresh=7 fvgs=18 bos=31 sigs=0 wrong_side=4 price_out=2 bos_miss=0 risk_neg=0 liquidity_trap=1 near_gap_pct=0.514
[16:28:50] tick balance=$296.44
  diag: trend=bearish atr_ratio=1.29 obs=8 obs_fresh=7 fvgs=18 bos=31 sigs=0 wrong_side=4 price_out=2 bos_miss=0 risk_neg=0 liquidity_trap=1 near_gap_pct=0.491
[16:29:54] tick balance=$296.46
  diag: trend=bearish atr_ratio=1.29 obs=8 obs_fresh=7 fvgs=18 bos=31 sigs=0 wrong_side=4 price_out=2 bos_miss=0 risk_neg=0 liquidity_trap=1 near_gap_pct=0.496
[16:30:57] tick balance=$296.38
  diag: trend=bearish atr_ratio=1.19 obs=8 obs_fresh=7 fvgs=18 bos=31 sigs=0 wrong_side=4 price_out=2 bos_miss=0 risk_neg=0 liquidity_trap=1 near_gap_pct=0.457
[16:32:00] tick balance=$296.14
  diag: trend=bearish atr_ratio=1.2 obs=8 obs_fresh=7 fvgs=18 bos=31 sigs=0 wrong_side=4 price_out=1 bos_miss=0 risk_neg=0 liquidity_trap=2 near_gap_pct=0.365
[16:33:03] tick balance=$296.04
  diag: trend=bearish atr_ratio=1.21 obs=8 obs_fresh=7 fvgs=18 bos=31 sigs=0 wrong_side=4 price_out=1 bos_miss=0 risk_neg=0 liquidity_trap=2 near_gap_pct=0.343
[16:34:06] tick balance=$296.26
  diag: trend=bearish atr_ratio=1.21 obs=8 obs_fresh=7 fvgs=18 bos=31 sigs=0 wrong_side=4 price_out=2 bos_miss=0 risk_neg=0 liquidity_trap=1 near_gap_pct=0.429
[16:35:09] tick balance=$296.03
  diag: trend=bearish atr_ratio=1.17 obs=9 obs_fresh=8 fvgs=18 bos=32 sigs=0 wrong_side=5 price_out=1 bos_miss=0 risk_neg=0 liquidity_trap=2 near_gap_pct=0.343
[16:36:13] tick balance=$295.96
  diag: trend=bearish atr_ratio=1.19 obs=9 obs_fresh=8 fvgs=17 bos=32 sigs=0 wrong_side=5 price_out=1 bos_miss=0 risk_neg=0 liquidity_trap=2 near_gap_pct=0.318
[16:37:16] tick balance=$296.24
  diag: trend=bearish atr_ratio=1.19 obs=8 obs_fresh=7 fvgs=17 bos=32 sigs=0 wrong_side=4 price_out=2 bos_miss=0 risk_neg=0 liquidity_trap=1 near_gap_pct=0.434
[16:38:18] tick balance=$296.23
  diag: trend=bearish atr_ratio=1.2 obs=8 obs_fresh=7 fvgs=17 bos=33 sigs=0 wrong_side=4 price_out=2 bos_miss=0 risk_neg=0 liquidity_trap=1 near_gap_pct=0.434
[16:39:21] tick balance=$296.12
  diag: trend=bearish atr_ratio=1.2 obs=8 obs_fresh=7 fvgs=17 bos=33 sigs=0 wrong_side=4 price_out=1 bos_miss=0 risk_neg=0 liquidity_trap=2 near_gap_pct=0.377
[16:40:24] tick balance=$296.31
  diag: trend=bearish atr_ratio=1.13 obs=8 obs_fresh=7 fvgs=17 bos=34 sigs=0 wrong_side=4 price_out=2 bos_miss=0 risk_neg=0 liquidity_trap=1 near_gap_pct=0.452
[16:41:27] tick balance=$295.84
  diag: trend=bearish atr_ratio=1.15 obs=8 obs_fresh=7 fvgs=17 bos=34 sigs=0 wrong_side=4 price_out=1 bos_miss=0 risk_neg=0 liquidity_trap=2 near_gap_pct=0.286
[16:42:36] tick balance=$295.83
  diag: trend=bearish atr_ratio=1.16 obs=8 obs_fresh=7 fvgs=17 bos=34 sigs=0 wrong_side=4 price_out=1 bos_miss=0 risk_neg=0 liquidity_trap=2 near_gap_pct=0.283
[16:43:39] tick balance=$296.09
  diag: trend=bearish atr_ratio=1.16 obs=8 obs_fresh=7 fvgs=17 bos=34 sigs=0 wrong_side=4 price_out=1 bos_miss=0 risk_neg=0 liquidity_trap=2 near_gap_pct=0.377
[16:44:42] tick balance=$296.09
  diag: trend=bearish atr_ratio=1.16 obs=8 obs_fresh=7 fvgs=17 bos=35 sigs=0 wrong_side=4 price_out=1 bos_miss=0 risk_neg=0 liquidity_trap=2 near_gap_pct=0.345
[16:45:45] tick balance=$296.49
  diag: trend=bearish atr_ratio=1.09 obs=7 obs_fresh=6 fvgs=16 bos=35 sigs=0 wrong_side=3 price_out=2 bos_miss=0 risk_neg=0 liquidity_trap=1 near_gap_pct=0.516
[16:46:48] tick balance=$297.55
  diag: trend=bearish skip=ema_overextended price=40.3 ema20_h4=41.8 dist=1.5 max_dist=1.4
[16:47:51] tick balance=$297.52
  diag: trend=bearish skip=ema_overextended price=40.4 ema20_h4=41.8 dist=1.5 max_dist=1.4
[16:48:55] tick balance=$297.20
  diag: trend=bearish skip=ema_overextended price=40.4 ema20_h4=41.8 dist=1.4 max_dist=1.4
[16:49:57] tick balance=$297.05
  diag: trend=bearish skip=ema_overextended price=40.4 ema20_h4=41.8 dist=1.4 max_dist=1.4
[16:50:59] tick balance=$297.19
  diag: trend=bearish skip=ema_overextended price=40.4 ema20_h4=41.8 dist=1.4 max_dist=1.4
[16:52:02] tick balance=$297.05
  diag: trend=bearish skip=ema_overextended price=40.4 ema20_h4=41.8 dist=1.4 max_dist=1.4
[16:53:05] tick balance=$297.26
  diag: trend=bearish skip=ema_overextended price=40.4 ema20_h4=41.8 dist=1.4 max_dist=1.4
[16:54:07] tick balance=$297.45
  diag: trend=bearish skip=ema_overextended price=40.4 ema20_h4=41.8 dist=1.5 max_dist=1.4
```
