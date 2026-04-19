# Bot Snapshot — 2026-04-19 02:55 UTC

## Service: active
balance=$363.38

## Config
POST_CLOSE_COOLDOWN: int = 180 # 3 мин техническая пауза после закрытия
RISK_PCT: float = 0.05 # 5% от баланса на сделку
ADX_MIN: float = 20.0 # ADX < 20 → choppy market, skip entry

## Trades (last 20)
```
25|SELL|75705.5||open|2026-04-18 19:15:28|
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
9|BUY|74842.7|-22.95|closed|2026-04-14 15:24:35|2026-04-14 17:34:53
8|BUY|75630.3|-3.46|closed|2026-04-14 14:22:42|2026-04-14 15:00:43
7|SELL|70843.3|-11.35|closed|2026-04-12 15:59:14|2026-04-12 17:51:45
6|SELL|70977.6|16.89|closed|2026-04-12 13:15:20|2026-04-12 14:43:04
```

## Daily PnL
```
2026-04-19|354.45|8.93|0
2026-04-18|311.88|42.12|0
2026-04-17|328.7|-16.81|0
2026-04-16|381.29|-52.59|0
2026-04-15|363.1|17.9|0
2026-04-14|413.74|-50.64|0
2026-04-13|413.74|0.0|0
```

## Open Positions
```
25|SELL|75705.5|open
```

## Diag Summary (last ~4h)
```
    188 trend_htf=ranging trend_mid=ranging skip=trend_mismatch
      2 trend=bearish atr_ratio=1.03 obs=12 obs_fresh=12 fvgs=15 bos=28 sigs=0 wrong_side=7 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=5 near_gap_pct=0.176
      2 trend=bearish atr_ratio=0.9 obs=11 obs_fresh=11 fvgs=15 bos=27 sigs=0 wrong_side=7 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=4 near_gap_pct=0.007
      2 trend=bearish atr_ratio=0.99 obs=12 obs_fresh=12 fvgs=16 bos=26 sigs=0 wrong_side=7 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=5 near_gap_pct=0.03
      1 trend=bearish atr_ratio=1.1 obs=12 obs_fresh=12 fvgs=15 bos=25 sigs=0 wrong_side=7 price_out=1 bos_miss=0 risk_neg=0 liquidity_trap=4 near_gap_pct=-0.078
      1 trend=bearish atr_ratio=1.15 obs=12 obs_fresh=12 fvgs=15 bos=25 sigs=0 wrong_side=7 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=5 near_gap_pct=-0.003
      1 trend=bearish atr_ratio=1.14 obs=12 obs_fresh=12 fvgs=14 bos=25 sigs=0 wrong_side=7 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=5 near_gap_pct=0.006
      1 trend=bearish atr_ratio=1.14 obs=12 obs_fresh=12 fvgs=14 bos=24 sigs=0 wrong_side=7 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=5 near_gap_pct=0.045
      1 trend=bearish atr_ratio=1.13 obs=13 obs_fresh=13 fvgs=14 bos=25 sigs=0 wrong_side=8 price_out=2 bos_miss=0 risk_neg=0 liquidity_trap=3 near_gap_pct=-0.099
      1 trend=bearish atr_ratio=1.13 obs=13 obs_fresh=13 fvgs=14 bos=25 sigs=0 wrong_side=8 price_out=1 bos_miss=0 risk_neg=0 liquidity_trap=4 near_gap_pct=-0.048
      1 trend=bearish atr_ratio=1.13 obs=13 obs_fresh=13 fvgs=14 bos=24 sigs=0 wrong_side=8 price_out=1 bos_miss=0 risk_neg=0 liquidity_trap=4 near_gap_pct=-0.066
      1 trend=bearish atr_ratio=1.13 obs=12 obs_fresh=12 fvgs=14 bos=25 sigs=0 wrong_side=7 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=5 near_gap_pct=0.02
      1 trend=bearish atr_ratio=1.13 obs=12 obs_fresh=12 fvgs=14 bos=25 sigs=0 wrong_side=7 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=5 near_gap_pct=0.019
      1 trend=bearish atr_ratio=1.12 obs=12 obs_fresh=12 fvgs=15 bos=25 sigs=0 wrong_side=7 price_out=1 bos_miss=0 risk_neg=0 liquidity_trap=4 near_gap_pct=-0.038
      1 trend=bearish atr_ratio=1.12 obs=12 obs_fresh=12 fvgs=15 bos=25 sigs=0 wrong_side=7 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=5 near_gap_pct=-0.048
      1 trend=bearish atr_ratio=1.12 obs=12 obs_fresh=12 fvgs=15 bos=25 sigs=0 wrong_side=7 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=5 near_gap_pct=-0.027
      1 trend=bearish atr_ratio=1.0 obs=13 obs_fresh=13 fvgs=16 bos=27 sigs=0 wrong_side=7 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=6 near_gap_pct=0.187
      1 trend=bearish atr_ratio=1.06 obs=12 obs_fresh=12 fvgs=15 bos=26 sigs=0 wrong_side=7 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=5 near_gap_pct=0.151
      1 trend=bearish atr_ratio=1.06 obs=12 obs_fresh=12 fvgs=15 bos=26 sigs=0 wrong_side=7 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=5 near_gap_pct=0.099
      1 trend=bearish atr_ratio=1.06 obs=12 obs_fresh=12 fvgs=14 bos=25 sigs=0 wrong_side=7 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=5 near_gap_pct=0.074
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
  diag: trend=bearish atr_ratio=0.99 obs=12 obs_fresh=12 fvgs=16 bos=26 sigs=0 wrong_side=7 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=5 near_gap_pct=0.03
[04:04:42] tick balance=$360.80
  diag: trend=bearish atr_ratio=0.99 obs=12 obs_fresh=12 fvgs=16 bos=26 sigs=0 wrong_side=7 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=5 near_gap_pct=0.03
[04:05:45] tick balance=$359.96
  diag: trend=bearish atr_ratio=0.97 obs=11 obs_fresh=11 fvgs=15 bos=26 sigs=0 wrong_side=7 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=4 near_gap_pct=0.012
[04:06:48] tick balance=$361.21
  diag: trend=bearish atr_ratio=0.98 obs=11 obs_fresh=11 fvgs=15 bos=26 sigs=0 wrong_side=7 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=4 near_gap_pct=0.039
[04:07:52] tick balance=$361.66
  diag: trend=bearish atr_ratio=0.98 obs=11 obs_fresh=11 fvgs=15 bos=26 sigs=0 wrong_side=7 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=4 near_gap_pct=0.048
[04:08:55] tick balance=$359.48
  diag: trend=bearish atr_ratio=0.98 obs=11 obs_fresh=11 fvgs=15 bos=26 sigs=0 wrong_side=7 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=4 near_gap_pct=0.003
[04:09:58] tick balance=$359.97
  diag: trend=bearish atr_ratio=0.98 obs=11 obs_fresh=11 fvgs=15 bos=27 sigs=0 wrong_side=7 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=4 near_gap_pct=0.004
[04:11:01] tick balance=$359.69
  diag: trend=bearish atr_ratio=0.9 obs=11 obs_fresh=11 fvgs=15 bos=27 sigs=0 wrong_side=7 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=4 near_gap_pct=0.007
[04:12:05] tick balance=$359.87
  diag: trend=bearish atr_ratio=0.9 obs=11 obs_fresh=11 fvgs=15 bos=27 sigs=0 wrong_side=7 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=4 near_gap_pct=0.01
[04:13:07] tick balance=$359.70
  diag: trend=bearish atr_ratio=0.9 obs=11 obs_fresh=11 fvgs=15 bos=27 sigs=0 wrong_side=7 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=4 near_gap_pct=0.007
[04:14:10] tick balance=$359.68
  diag: trend=bearish atr_ratio=0.9 obs=11 obs_fresh=11 fvgs=15 bos=27 sigs=0 wrong_side=7 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=4 near_gap_pct=0.006
[04:15:13] tick balance=$356.63
  diag: trend=bearish atr_ratio=0.85 obs=12 obs_fresh=12 fvgs=16 bos=26 sigs=0 wrong_side=8 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=4 near_gap_pct=-0.054
[04:16:16] tick balance=$358.50
  diag: trend=bearish atr_ratio=0.86 obs=12 obs_fresh=12 fvgs=16 bos=26 sigs=0 wrong_side=8 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=4 near_gap_pct=-0.009
[04:17:19] tick balance=$358.42
  diag: trend=bearish atr_ratio=0.86 obs=12 obs_fresh=12 fvgs=16 bos=27 sigs=0 wrong_side=8 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=4 near_gap_pct=-0.018
[04:18:21] tick balance=$356.28
  diag: trend=bearish atr_ratio=0.86 obs=12 obs_fresh=12 fvgs=16 bos=27 sigs=0 wrong_side=8 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=4 near_gap_pct=-0.061
[04:19:24] tick balance=$356.81
  diag: trend=bearish atr_ratio=0.86 obs=12 obs_fresh=12 fvgs=16 bos=27 sigs=0 wrong_side=8 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=4 near_gap_pct=-0.05
[04:20:27] tick balance=$355.80
  diag: trend=bearish atr_ratio=0.82 obs=11 obs_fresh=11 fvgs=17 bos=27 sigs=0 wrong_side=7 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=4 near_gap_pct=-0.07
[04:21:30] tick balance=$354.31
  diag: trend=bearish atr_ratio=0.84 obs=11 obs_fresh=11 fvgs=17 bos=27 sigs=0 wrong_side=7 price_out=1 bos_miss=0 risk_neg=0 liquidity_trap=3 near_gap_pct=-0.099
[04:22:33] tick balance=$357.42
  diag: trend=bearish atr_ratio=0.85 obs=11 obs_fresh=11 fvgs=17 bos=26 sigs=0 wrong_side=7 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=4 near_gap_pct=-0.038
[04:23:36] tick balance=$358.01
  diag: trend=bearish atr_ratio=0.86 obs=11 obs_fresh=11 fvgs=16 bos=27 sigs=0 wrong_side=7 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=4 near_gap_pct=-0.019
[04:24:39] tick balance=$364.11
  diag: trend=bearish atr_ratio=0.95 obs=12 obs_fresh=12 fvgs=16 bos=27 sigs=0 wrong_side=7 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=5 near_gap_pct=0.082
[04:25:42] tick balance=$370.78
[change_stop_loss] id=498423545 new_sl=75700.5 tp_preserved=75052.2 resp={'success': True, 'code': 0}
[partial_close] symbol=BTC_USDT pos_type=2 vol=201 resp={'success': False, 'code': 2009, 'message': 'Position is nonexistent or closed'}
[partial_tp] partial_close rejected: {'success': False, 'code': 2009, 'message': 'Position is nonexistent or closed'}
  diag: trend=bearish atr_ratio=1.0 obs=13 obs_fresh=13 fvgs=16 bos=27 sigs=0 wrong_side=7 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=6 near_gap_pct=0.187
[04:26:47] tick balance=$367.30
  diag: trend=bearish atr_ratio=1.02 obs=12 obs_fresh=12 fvgs=16 bos=27 sigs=0 wrong_side=7 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=5 near_gap_pct=0.122
[04:27:49] tick balance=$366.90
  diag: trend=bearish atr_ratio=1.02 obs=12 obs_fresh=12 fvgs=16 bos=28 sigs=0 wrong_side=7 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=5 near_gap_pct=0.11
[04:28:52] tick balance=$369.27
  diag: trend=bearish atr_ratio=1.02 obs=13 obs_fresh=13 fvgs=16 bos=28 sigs=0 wrong_side=7 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=6 near_gap_pct=0.157
[04:29:55] tick balance=$368.56
  diag: trend=bearish atr_ratio=1.02 obs=12 obs_fresh=12 fvgs=16 bos=28 sigs=0 wrong_side=7 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=5 near_gap_pct=0.143
[04:30:58] tick balance=$369.92
  diag: trend=bearish atr_ratio=1.03 obs=12 obs_fresh=12 fvgs=15 bos=28 sigs=0 wrong_side=7 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=5 near_gap_pct=0.176
[04:32:00] tick balance=$370.25
  diag: trend=bearish atr_ratio=1.03 obs=12 obs_fresh=12 fvgs=15 bos=28 sigs=0 wrong_side=7 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=5 near_gap_pct=0.176
[04:33:04] tick balance=$366.03
  diag: trend=bearish atr_ratio=1.06 obs=12 obs_fresh=12 fvgs=15 bos=26 sigs=0 wrong_side=7 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=5 near_gap_pct=0.099
[04:34:07] tick balance=$368.66
  diag: trend=bearish atr_ratio=1.06 obs=12 obs_fresh=12 fvgs=15 bos=26 sigs=0 wrong_side=7 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=5 near_gap_pct=0.151
[04:35:11] tick balance=$368.12
  diag: trend=bearish atr_ratio=1.01 obs=12 obs_fresh=12 fvgs=14 bos=26 sigs=0 wrong_side=7 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=5 near_gap_pct=0.143
[04:36:14] tick balance=$368.36
  diag: trend=bearish atr_ratio=1.03 obs=12 obs_fresh=12 fvgs=14 bos=26 sigs=0 wrong_side=7 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=5 near_gap_pct=0.139
[04:37:17] tick balance=$368.05
  diag: trend=bearish atr_ratio=1.03 obs=12 obs_fresh=12 fvgs=14 bos=25 sigs=0 wrong_side=7 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=5 near_gap_pct=0.133
[04:38:20] tick balance=$368.16
  diag: trend=bearish atr_ratio=1.03 obs=12 obs_fresh=12 fvgs=14 bos=25 sigs=0 wrong_side=7 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=5 near_gap_pct=0.136
[04:39:23] tick balance=$365.07
  diag: trend=bearish atr_ratio=1.06 obs=12 obs_fresh=12 fvgs=14 bos=25 sigs=0 wrong_side=7 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=5 near_gap_pct=0.074
[04:40:25] tick balance=$362.27
  diag: trend=bearish atr_ratio=1.02 obs=13 obs_fresh=13 fvgs=14 bos=25 sigs=0 wrong_side=8 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=5 near_gap_pct=0.028
[04:41:28] tick balance=$360.61
  diag: trend=bearish atr_ratio=1.03 obs=13 obs_fresh=13 fvgs=14 bos=25 sigs=0 wrong_side=8 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=5 near_gap_pct=-0.003
[04:42:31] tick balance=$354.51
  diag: trend=bearish atr_ratio=1.13 obs=13 obs_fresh=13 fvgs=14 bos=25 sigs=0 wrong_side=8 price_out=2 bos_miss=0 risk_neg=0 liquidity_trap=3 near_gap_pct=-0.099
[04:43:34] tick balance=$356.03
  diag: trend=bearish atr_ratio=1.13 obs=13 obs_fresh=13 fvgs=14 bos=24 sigs=0 wrong_side=8 price_out=1 bos_miss=0 risk_neg=0 liquidity_trap=4 near_gap_pct=-0.066
[04:44:37] tick balance=$356.78
  diag: trend=bearish atr_ratio=1.13 obs=13 obs_fresh=13 fvgs=14 bos=25 sigs=0 wrong_side=8 price_out=1 bos_miss=0 risk_neg=0 liquidity_trap=4 near_gap_pct=-0.048
[04:45:40] tick balance=$355.40
  diag: trend=bearish atr_ratio=1.1 obs=12 obs_fresh=12 fvgs=15 bos=25 sigs=0 wrong_side=7 price_out=1 bos_miss=0 risk_neg=0 liquidity_trap=4 near_gap_pct=-0.078
[04:46:44] tick balance=$358.17
  diag: trend=bearish atr_ratio=1.12 obs=12 obs_fresh=12 fvgs=15 bos=25 sigs=0 wrong_side=7 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=5 near_gap_pct=-0.027
[04:47:47] tick balance=$357.43
  diag: trend=bearish atr_ratio=1.12 obs=12 obs_fresh=12 fvgs=15 bos=25 sigs=0 wrong_side=7 price_out=1 bos_miss=0 risk_neg=0 liquidity_trap=4 near_gap_pct=-0.038
[04:48:49] tick balance=$358.63
  diag: trend=bearish atr_ratio=1.12 obs=12 obs_fresh=12 fvgs=15 bos=25 sigs=0 wrong_side=7 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=5 near_gap_pct=-0.048
[04:49:52] tick balance=$361.15
  diag: trend=bearish atr_ratio=1.15 obs=12 obs_fresh=12 fvgs=15 bos=25 sigs=0 wrong_side=7 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=5 near_gap_pct=-0.003
[04:50:55] tick balance=$362.25
  diag: trend=bearish atr_ratio=1.13 obs=12 obs_fresh=12 fvgs=14 bos=25 sigs=0 wrong_side=7 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=5 near_gap_pct=0.02
[04:51:58] tick balance=$362.30
  diag: trend=bearish atr_ratio=1.13 obs=12 obs_fresh=12 fvgs=14 bos=25 sigs=0 wrong_side=7 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=5 near_gap_pct=0.019
[04:53:00] tick balance=$361.64
  diag: trend=bearish atr_ratio=1.14 obs=12 obs_fresh=12 fvgs=14 bos=25 sigs=0 wrong_side=7 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=5 near_gap_pct=0.006
[04:54:03] tick balance=$363.38
  diag: trend=bearish atr_ratio=1.14 obs=12 obs_fresh=12 fvgs=14 bos=24 sigs=0 wrong_side=7 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=5 near_gap_pct=0.045
```
