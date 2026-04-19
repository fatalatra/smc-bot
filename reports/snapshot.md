# Bot Snapshot — 2026-04-19 06:55 UTC

## Service: active
balance=$350.87

## Config
POST_CLOSE_COOLDOWN: int = 180 # 3 мин техническая пауза после закрытия
RISK_PCT: float = 0.05 # 5% от баланса на сделку
ADX_MIN: float = 20.0 # ADX < 20 → choppy market, skip entry

## Trades (last 20)
```
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
9|BUY|74842.7|-22.95|closed|2026-04-14 15:24:35|2026-04-14 17:34:53
8|BUY|75630.3|-3.46|closed|2026-04-14 14:22:42|2026-04-14 15:00:43
7|SELL|70843.3|-11.35|closed|2026-04-12 15:59:14|2026-04-12 17:51:45
6|SELL|70977.6|16.89|closed|2026-04-12 13:15:20|2026-04-12 14:43:04
```

## Daily PnL
```
2026-04-19|354.45|-3.58|0
2026-04-18|311.88|42.12|0
2026-04-17|328.7|-16.81|0
2026-04-16|381.29|-52.59|0
2026-04-15|363.1|17.9|0
2026-04-14|413.74|-50.64|0
2026-04-13|413.74|0.0|0
```

## Open Positions
```
none
```

## Diag Summary (last ~4h)
```
    109 trend_htf=ranging trend_mid=ranging skip=trend_mismatch
      2 trend=bearish atr_ratio=1.03 obs=12 obs_fresh=12 fvgs=15 bos=28 sigs=0 wrong_side=7 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=5 near_gap_pct=0.176
      2 trend=bearish atr_ratio=0.9 obs=11 obs_fresh=11 fvgs=15 bos=27 sigs=0 wrong_side=7 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=4 near_gap_pct=0.007
      2 trend=bearish atr_ratio=0.99 obs=12 obs_fresh=12 fvgs=16 bos=26 sigs=0 wrong_side=7 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=5 near_gap_pct=0.03
      1 trend=bearish atr_ratio=1.38 obs=12 obs_fresh=10 fvgs=18 bos=25 sigs=0 wrong_side=7 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=3 near_gap_pct=0.152
      1 trend=bearish atr_ratio=1.38 obs=12 obs_fresh=10 fvgs=18 bos=25 sigs=0 wrong_side=7 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=3 near_gap_pct=0.149
      1 trend=bearish atr_ratio=1.38 obs=12 obs_fresh=10 fvgs=18 bos=25 sigs=0 wrong_side=7 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=3 near_gap_pct=0.118
      1 trend=bearish atr_ratio=1.38 obs=12 obs_fresh=10 fvgs=18 bos=25 sigs=0 wrong_side=7 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=3 near_gap_pct=0.104
      1 trend=bearish atr_ratio=1.38 obs=12 obs_fresh=10 fvgs=18 bos=25 sigs=0 wrong_side=7 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=3 near_gap_pct=0.097
      1 trend=bearish atr_ratio=1.38 obs=12 obs_fresh=10 fvgs=18 bos=25 sigs=0 wrong_side=7 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=3 near_gap_pct=0.08
      1 trend=bearish atr_ratio=1.37 obs=13 obs_fresh=11 fvgs=18 bos=25 sigs=0 wrong_side=8 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=3 near_gap_pct=0.121
      1 trend=bearish atr_ratio=1.37 obs=13 obs_fresh=11 fvgs=18 bos=25 sigs=0 wrong_side=8 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=3 near_gap_pct=0.085
      1 trend=bearish atr_ratio=1.37 obs=12 obs_fresh=10 fvgs=18 bos=25 sigs=0 wrong_side=7 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=3 near_gap_pct=0.105
      1 trend=bearish atr_ratio=1.37 obs=12 obs_fresh=10 fvgs=18 bos=25 sigs=0 wrong_side=7 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=3 near_gap_pct=0.1
      1 trend=bearish atr_ratio=1.35 obs=14 obs_fresh=12 fvgs=18 bos=25 sigs=0 wrong_side=9 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=3 near_gap_pct=0.035
      1 trend=bearish atr_ratio=1.35 obs=13 obs_fresh=11 fvgs=18 bos=26 sigs=0 wrong_side=8 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=3 near_gap_pct=0.072
      1 trend=bearish atr_ratio=1.35 obs=12 obs_fresh=10 fvgs=18 bos=25 sigs=0 wrong_side=7 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=3 near_gap_pct=0.158
      1 trend=bearish atr_ratio=1.34 obs=14 obs_fresh=12 fvgs=18 bos=25 sigs=0 wrong_side=9 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=3 near_gap_pct=0.054
      1 trend=bearish atr_ratio=1.34 obs=12 obs_fresh=10 fvgs=18 bos=25 sigs=0 wrong_side=7 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=3 near_gap_pct=0.135
      1 trend=bearish atr_ratio=1.34 obs=12 obs_fresh=10 fvgs=17 bos=26 sigs=0 wrong_side=7 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=3 near_gap_pct=0.079
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
[08:04:36] tick balance=$350.87
  ⏸ paused: manual close of SELL @ 75705.5 at 06:18:16
[08:05:38] tick balance=$350.87
  ⏸ paused: manual close of SELL @ 75705.5 at 06:18:16
[08:06:40] tick balance=$350.87
  ⏸ paused: manual close of SELL @ 75705.5 at 06:18:16
[08:07:41] tick balance=$350.87
  ⏸ paused: manual close of SELL @ 75705.5 at 06:18:16
[08:08:43] tick balance=$350.87
  ⏸ paused: manual close of SELL @ 75705.5 at 06:18:16
[08:09:44] tick balance=$350.87
  ⏸ paused: manual close of SELL @ 75705.5 at 06:18:16
[08:10:45] tick balance=$350.87
  ⏸ paused: manual close of SELL @ 75705.5 at 06:18:16
[08:11:47] tick balance=$350.87
  ⏸ paused: manual close of SELL @ 75705.5 at 06:18:16
[08:12:49] tick balance=$350.87
  ⏸ paused: manual close of SELL @ 75705.5 at 06:18:16
[08:13:50] tick balance=$350.87
  ⏸ paused: manual close of SELL @ 75705.5 at 06:18:16
[08:14:52] tick balance=$350.87
  ⏸ paused: manual close of SELL @ 75705.5 at 06:18:16
[08:15:53] tick balance=$350.87
  ⏸ paused: manual close of SELL @ 75705.5 at 06:18:16
[08:16:55] tick balance=$350.87
  ⏸ paused: manual close of SELL @ 75705.5 at 06:18:16
[08:17:56] tick balance=$350.87
  ⏸ paused: manual close of SELL @ 75705.5 at 06:18:16
[08:18:56] tick balance=$350.87
  ⏸ paused: manual close of SELL @ 75705.5 at 06:18:16
[08:19:58] tick balance=$350.87
  ⏸ paused: manual close of SELL @ 75705.5 at 06:18:16
[08:20:58] tick balance=$350.87
  ⏸ paused: manual close of SELL @ 75705.5 at 06:18:16
[08:22:00] tick balance=$350.87
  ⏸ paused: manual close of SELL @ 75705.5 at 06:18:16
[08:23:02] tick balance=$350.87
  ⏸ paused: manual close of SELL @ 75705.5 at 06:18:16
[08:24:02] tick balance=$350.87
  ⏸ paused: manual close of SELL @ 75705.5 at 06:18:16
[08:25:04] tick balance=$350.87
  ⏸ paused: manual close of SELL @ 75705.5 at 06:18:16
[08:26:05] tick balance=$350.87
  ⏸ paused: manual close of SELL @ 75705.5 at 06:18:16
[08:27:07] tick balance=$350.87
  ⏸ paused: manual close of SELL @ 75705.5 at 06:18:16
[08:28:08] tick balance=$350.87
  ⏸ paused: manual close of SELL @ 75705.5 at 06:18:16
[08:29:10] tick balance=$350.87
  ⏸ paused: manual close of SELL @ 75705.5 at 06:18:16
[08:30:12] tick balance=$350.87
  ⏸ paused: manual close of SELL @ 75705.5 at 06:18:16
[08:31:13] tick balance=$350.87
  ⏸ paused: manual close of SELL @ 75705.5 at 06:18:16
[08:32:14] tick balance=$350.87
  ⏸ paused: manual close of SELL @ 75705.5 at 06:18:16
[08:33:16] tick balance=$350.87
  ⏸ paused: manual close of SELL @ 75705.5 at 06:18:16
[08:34:17] tick balance=$350.87
  ⏸ paused: manual close of SELL @ 75705.5 at 06:18:16
[08:35:18] tick balance=$350.87
  ⏸ paused: manual close of SELL @ 75705.5 at 06:18:16
[08:36:20] tick balance=$350.87
  ⏸ paused: manual close of SELL @ 75705.5 at 06:18:16
[08:37:22] tick balance=$350.87
  ⏸ paused: manual close of SELL @ 75705.5 at 06:18:16
[08:38:23] tick balance=$350.87
  ⏸ paused: manual close of SELL @ 75705.5 at 06:18:16
[08:39:30] tick balance=$350.87
  ⏸ paused: manual close of SELL @ 75705.5 at 06:18:16
[08:40:32] tick balance=$350.87
  ⏸ paused: manual close of SELL @ 75705.5 at 06:18:16
[08:41:33] tick balance=$350.87
  ⏸ paused: manual close of SELL @ 75705.5 at 06:18:16
[08:42:34] tick balance=$350.87
  ⏸ paused: manual close of SELL @ 75705.5 at 06:18:16
[08:43:36] tick balance=$350.87
  ⏸ paused: manual close of SELL @ 75705.5 at 06:18:16
[08:44:37] tick balance=$350.87
  ⏸ paused: manual close of SELL @ 75705.5 at 06:18:16
[08:45:39] tick balance=$350.87
  ⏸ paused: manual close of SELL @ 75705.5 at 06:18:16
[08:46:40] tick balance=$350.87
  ⏸ paused: manual close of SELL @ 75705.5 at 06:18:16
[08:47:42] tick balance=$350.87
  ⏸ paused: manual close of SELL @ 75705.5 at 06:18:16
[08:48:42] tick balance=$350.87
  ⏸ paused: manual close of SELL @ 75705.5 at 06:18:16
[08:49:44] tick balance=$350.87
  ⏸ paused: manual close of SELL @ 75705.5 at 06:18:16
[08:50:46] tick balance=$350.87
  ⏸ paused: manual close of SELL @ 75705.5 at 06:18:16
[08:51:47] tick balance=$350.87
  ⏸ paused: manual close of SELL @ 75705.5 at 06:18:16
[08:52:49] tick balance=$350.87
  ⏸ paused: manual close of SELL @ 75705.5 at 06:18:16
[08:53:50] tick balance=$350.87
  ⏸ paused: manual close of SELL @ 75705.5 at 06:18:16
[08:54:52] tick balance=$350.87
  ⏸ paused: manual close of SELL @ 75705.5 at 06:18:16
```
