# Bot Snapshot — 2026-04-18 10:55 UTC

## Service: active
balance=$339.74

## Config
POST_CLOSE_COOLDOWN: int = 180 # 3 мин техническая пауза после закрытия
RISK_PCT: float = 0.05 # 5% от баланса на сделку
ADX_MIN: float = 20.0 # ADX < 20 → choppy market, skip entry

## Trades (last 20)
```
23|SELL|76513.3||open|2026-04-18 09:55:19|
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
9|BUY|74842.7|-22.95|closed|2026-04-14 15:24:35|2026-04-14 17:34:53
8|BUY|75630.3|-3.46|closed|2026-04-14 14:22:42|2026-04-14 15:00:43
7|SELL|70843.3|-11.35|closed|2026-04-12 15:59:14|2026-04-12 17:51:45
6|SELL|70977.6|16.89|closed|2026-04-12 13:15:20|2026-04-12 14:43:04
5|SELL|71364.3|13.27|closed|2026-04-12 10:57:04|2026-04-12 13:01:46
4|SELL|71492.1|13.27|closed|2026-04-12 10:41:17|2026-04-12 10:42:19
```

## Daily PnL
```
2026-04-18|311.88|27.86|0
2026-04-17|328.7|-16.81|0
2026-04-16|381.29|-52.59|0
2026-04-15|363.1|17.9|0
2026-04-14|413.74|-50.64|0
2026-04-13|413.74|0.0|0
2026-04-12|423.86|-10.12|0
```

## Open Positions
```
23|SELL|76513.3|open
```

## Diag Summary (last ~4h)
```
     87 trend_htf=ranging trend_mid=ranging skip=trend_mismatch
      2 trend=bearish atr_ratio=1.1 obs=11 obs_fresh=9 fvgs=12 bos=24 sigs=0 wrong_side=5 price_out=4 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=0.847
      1 trend=bearish skip=trend_immature trend_age_s=870 need_s=900
      1 trend=bearish skip=trend_immature trend_age_s=807 need_s=900
      1 trend=bearish skip=trend_immature trend_age_s=745 need_s=900
      1 trend=bearish skip=trend_immature trend_age_s=682 need_s=900
      1 trend=bearish skip=trend_immature trend_age_s=62 need_s=900
      1 trend=bearish skip=trend_immature trend_age_s=620 need_s=900
      1 trend=bearish skip=trend_immature trend_age_s=558 need_s=900
      1 trend=bearish skip=trend_immature trend_age_s=496 need_s=900
      1 trend=bearish skip=trend_immature trend_age_s=434 need_s=900
      1 trend=bearish skip=trend_immature trend_age_s=372 need_s=900
      1 trend=bearish skip=trend_immature trend_age_s=311 need_s=900
      1 trend=bearish skip=trend_immature trend_age_s=248 need_s=900
      1 trend=bearish skip=trend_immature trend_age_s=187 need_s=900
      1 trend=bearish skip=trend_immature trend_age_s=124 need_s=900
      1 trend=bearish skip=trend_immature trend_age_s=0 need_s=900
      1 trend=bearish atr_ratio=1.9 obs=8 obs_fresh=8 fvgs=10 bos=26 sigs=0 wrong_side=3 price_out=1 bos_miss=0 risk_neg=0 liquidity_trap=4 near_gap_pct=0.501
      1 trend=bearish atr_ratio=1.9 obs=8 obs_fresh=8 fvgs=10 bos=25 sigs=0 wrong_side=3 price_out=2 bos_miss=0 risk_neg=0 liquidity_trap=3 near_gap_pct=0.556
      1 trend=bearish atr_ratio=1.9 obs=8 obs_fresh=8 fvgs=10 bos=25 sigs=0 wrong_side=3 price_out=1 bos_miss=0 risk_neg=0 liquidity_trap=4 near_gap_pct=0.484
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
  diag: trend=bearish atr_ratio=1.3 obs=11 obs_fresh=10 fvgs=12 bos=25 sigs=0 wrong_side=5 price_out=5 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=0.719
[12:04:47] tick balance=$323.06
  diag: trend=bearish atr_ratio=1.3 obs=11 obs_fresh=10 fvgs=12 bos=26 sigs=0 wrong_side=5 price_out=5 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=0.734
[12:05:50] tick balance=$326.31
  diag: trend=bearish atr_ratio=1.28 obs=12 obs_fresh=11 fvgs=13 bos=26 sigs=1 wrong_side=5 price_out=5 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=0.212 skip=side_busy open_sides=['SELL']
[12:06:54] tick balance=$323.29
  diag: trend=bearish atr_ratio=1.3 obs=11 obs_fresh=10 fvgs=13 bos=25 sigs=0 wrong_side=5 price_out=5 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=0.73
[12:07:57] tick balance=$325.64
  diag: trend=bearish atr_ratio=1.32 obs=12 obs_fresh=10 fvgs=13 bos=25 sigs=0 wrong_side=5 price_out=5 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=0.777
[12:09:00] tick balance=$333.78
[change_stop_loss] id=498167452 new_sl=76508.3 tp_preserved=76006.3 resp={'success': True, 'code': 0}
[partial_close] symbol=BTC_USDT pos_type=2 vol=231 resp={'success': False, 'code': 2009, 'message': 'Position is nonexistent or closed'}
[partial_tp] partial_close rejected: {'success': False, 'code': 2009, 'message': 'Position is nonexistent or closed'}
  diag: trend=bearish atr_ratio=1.34 obs=12 obs_fresh=10 fvgs=13 bos=25 sigs=0 wrong_side=5 price_out=5 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=0.913
[12:10:04] tick balance=$335.46
  diag: trend=bearish atr_ratio=1.27 obs=12 obs_fresh=10 fvgs=14 bos=25 sigs=0 wrong_side=5 price_out=5 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=0.945
[12:11:07] tick balance=$334.64
  diag: trend=bearish atr_ratio=1.29 obs=12 obs_fresh=10 fvgs=14 bos=24 sigs=0 wrong_side=5 price_out=5 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=0.915
[12:12:09] tick balance=$336.65
  diag: trend=bearish atr_ratio=1.32 obs=12 obs_fresh=10 fvgs=14 bos=25 sigs=0 wrong_side=5 price_out=5 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=0.974
[12:13:13] tick balance=$338.29
  diag: trend=bearish atr_ratio=1.32 obs=12 obs_fresh=10 fvgs=14 bos=24 sigs=0 wrong_side=5 price_out=5 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=0.958
[12:14:17] tick balance=$333.38
  diag: trend=bearish atr_ratio=1.32 obs=12 obs_fresh=10 fvgs=14 bos=24 sigs=0 wrong_side=5 price_out=5 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=0.907
[12:15:20] tick balance=$328.37
  diag: trend=bearish atr_ratio=1.17 obs=12 obs_fresh=10 fvgs=14 bos=25 sigs=0 wrong_side=5 price_out=5 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=0.821
[12:16:24] tick balance=$326.25
  diag: trend=bearish atr_ratio=1.18 obs=12 obs_fresh=10 fvgs=14 bos=25 sigs=0 wrong_side=5 price_out=5 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=0.789
[12:17:27] tick balance=$326.70
  diag: trend=bearish atr_ratio=1.18 obs=12 obs_fresh=10 fvgs=14 bos=25 sigs=0 wrong_side=5 price_out=5 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=0.791
[12:18:30] tick balance=$327.87
  diag: trend=bearish atr_ratio=1.18 obs=12 obs_fresh=10 fvgs=14 bos=26 sigs=0 wrong_side=5 price_out=5 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=0.811
[12:19:34] tick balance=$327.53
  diag: trend=bearish atr_ratio=1.18 obs=12 obs_fresh=10 fvgs=14 bos=25 sigs=0 wrong_side=5 price_out=5 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=0.806
[12:20:37] tick balance=$328.85
  diag: trend=bearish atr_ratio=1.14 obs=11 obs_fresh=9 fvgs=14 bos=25 sigs=0 wrong_side=5 price_out=4 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=0.829
[12:21:40] tick balance=$329.79
  diag: trend=bearish atr_ratio=1.15 obs=11 obs_fresh=9 fvgs=13 bos=24 sigs=0 wrong_side=5 price_out=4 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=0.833
[12:22:44] tick balance=$330.72
  diag: trend=bearish atr_ratio=1.16 obs=11 obs_fresh=9 fvgs=13 bos=25 sigs=0 wrong_side=5 price_out=4 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=0.858
[12:23:47] tick balance=$328.32
  diag: trend=bearish atr_ratio=1.16 obs=11 obs_fresh=9 fvgs=13 bos=25 sigs=0 wrong_side=5 price_out=4 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=0.82
[12:24:50] tick balance=$328.79
  diag: trend=bearish atr_ratio=1.16 obs=11 obs_fresh=9 fvgs=13 bos=25 sigs=0 wrong_side=5 price_out=4 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=0.833
[12:25:53] tick balance=$327.95
  diag: trend=bearish atr_ratio=1.07 obs=11 obs_fresh=9 fvgs=12 bos=25 sigs=0 wrong_side=5 price_out=4 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=0.814
[12:26:57] tick balance=$331.59
  diag: trend=bearish atr_ratio=1.1 obs=12 obs_fresh=10 fvgs=12 bos=25 sigs=1 wrong_side=5 price_out=4 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=-0.001 skip=side_busy open_sides=['SELL']
[12:28:00] tick balance=$330.08
  diag: trend=bearish atr_ratio=1.1 obs=11 obs_fresh=9 fvgs=12 bos=24 sigs=0 wrong_side=5 price_out=4 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=0.847
[12:29:03] tick balance=$329.66
  diag: trend=bearish atr_ratio=1.1 obs=11 obs_fresh=9 fvgs=12 bos=24 sigs=0 wrong_side=5 price_out=4 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=0.847
[12:30:06] tick balance=$333.79
  diag: trend=bearish atr_ratio=1.1 obs=11 obs_fresh=9 fvgs=12 bos=24 sigs=0 wrong_side=5 price_out=4 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=0.925
[12:31:08] tick balance=$333.82
  diag: trend=bearish atr_ratio=1.11 obs=11 obs_fresh=9 fvgs=12 bos=24 sigs=0 wrong_side=5 price_out=4 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=0.914
[12:32:11] tick balance=$333.91
  diag: trend=bearish atr_ratio=1.11 obs=11 obs_fresh=9 fvgs=12 bos=24 sigs=0 wrong_side=5 price_out=4 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=0.916
[12:33:14] tick balance=$335.64
  diag: trend=bearish atr_ratio=1.11 obs=11 obs_fresh=9 fvgs=12 bos=24 sigs=0 wrong_side=5 price_out=4 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=0.946
[12:34:17] tick balance=$334.47
  diag: trend=bearish atr_ratio=1.12 obs=11 obs_fresh=9 fvgs=12 bos=24 sigs=0 wrong_side=5 price_out=4 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=0.929
[12:35:20] tick balance=$336.30
  diag: trend=bearish atr_ratio=1.08 obs=11 obs_fresh=9 fvgs=13 bos=25 sigs=0 wrong_side=5 price_out=4 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=0.961
[12:36:23] tick balance=$335.93
  diag: trend=bearish atr_ratio=1.09 obs=11 obs_fresh=9 fvgs=13 bos=24 sigs=0 wrong_side=5 price_out=4 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=0.951
[12:37:27] tick balance=$333.36
  diag: trend=bearish atr_ratio=1.09 obs=11 obs_fresh=9 fvgs=13 bos=24 sigs=0 wrong_side=5 price_out=4 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=0.906
[12:38:31] tick balance=$334.06
  diag: trend=bearish atr_ratio=1.09 obs=11 obs_fresh=9 fvgs=13 bos=24 sigs=0 wrong_side=5 price_out=4 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=0.921
[12:39:34] tick balance=$333.13
  diag: trend=bearish atr_ratio=1.09 obs=11 obs_fresh=9 fvgs=13 bos=25 sigs=0 wrong_side=5 price_out=4 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=0.902
[12:40:37] tick balance=$332.38
  diag: trend=bearish atr_ratio=1.03 obs=11 obs_fresh=9 fvgs=13 bos=24 sigs=0 wrong_side=5 price_out=4 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=0.894
[12:41:40] tick balance=$333.33
  diag: trend=bearish atr_ratio=1.03 obs=11 obs_fresh=9 fvgs=13 bos=24 sigs=0 wrong_side=5 price_out=4 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=0.906
[12:42:43] tick balance=$332.00
  diag: trend=bearish atr_ratio=1.03 obs=11 obs_fresh=9 fvgs=13 bos=25 sigs=0 wrong_side=5 price_out=4 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=0.884
[12:43:46] tick balance=$331.83
  diag: trend=bearish atr_ratio=1.04 obs=11 obs_fresh=9 fvgs=13 bos=25 sigs=0 wrong_side=5 price_out=4 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=0.886
[12:44:50] tick balance=$336.01
  diag: trend=bearish atr_ratio=1.06 obs=11 obs_fresh=9 fvgs=13 bos=25 sigs=0 wrong_side=5 price_out=4 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=0.952
[12:45:54] tick balance=$336.73
  diag: trend=bearish atr_ratio=1.03 obs=11 obs_fresh=9 fvgs=13 bos=26 sigs=0 wrong_side=5 price_out=4 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=0.966
[12:46:57] tick balance=$338.71
  diag: trend=bearish atr_ratio=1.05 obs=12 obs_fresh=10 fvgs=13 bos=26 sigs=0 wrong_side=5 price_out=4 bos_miss=0 risk_neg=0 liquidity_trap=1 near_gap_pct=0.03
[12:47:59] tick balance=$335.69
  diag: trend=bearish atr_ratio=1.05 obs=11 obs_fresh=9 fvgs=13 bos=27 sigs=0 wrong_side=5 price_out=4 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=0.945
[12:49:03] tick balance=$332.37
  diag: trend=bearish atr_ratio=1.07 obs=11 obs_fresh=9 fvgs=13 bos=27 sigs=0 wrong_side=5 price_out=4 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=0.892
[12:50:06] tick balance=$335.84
  diag: trend=bearish atr_ratio=1.06 obs=11 obs_fresh=9 fvgs=13 bos=27 sigs=0 wrong_side=5 price_out=4 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=0.952
[12:51:09] tick balance=$337.04
  diag: trend=bearish atr_ratio=1.07 obs=11 obs_fresh=9 fvgs=13 bos=26 sigs=0 wrong_side=5 price_out=4 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=0.973
[12:52:12] tick balance=$341.10
  diag: trend=bearish atr_ratio=1.1 obs=11 obs_fresh=9 fvgs=13 bos=26 sigs=0 wrong_side=5 price_out=4 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=1.041
[12:53:16] tick balance=$339.28
  diag: trend=bearish atr_ratio=1.1 obs=11 obs_fresh=9 fvgs=13 bos=26 sigs=0 wrong_side=5 price_out=4 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=1.021
[12:54:19] tick balance=$339.74
  diag: trend=bearish atr_ratio=1.1 obs=11 obs_fresh=9 fvgs=13 bos=26 sigs=0 wrong_side=5 price_out=4 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=1.024
```
