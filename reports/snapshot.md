# Bot Snapshot — 2026-04-16 22:55 UTC

## Service: active
balance=$328.70

## Config
POST_CLOSE_COOLDOWN: int = 180 # 3 мин техническая пауза после закрытия
RISK_PCT: float = 0.05 # 5% от баланса на сделку
ADX_MIN: float = 20.0 # ADX < 20 → choppy market, skip entry

## Trades (last 20)
```
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
3|SELL|71597.7|13.27|closed|2026-04-12 10:25:37|2026-04-12 10:42:19
2|SELL|73451.8|13.15|closed|2026-04-11 20:18:03|2026-04-12 08:14:54
1|SELL|73575.9|13.15|closed|2026-04-11 20:01:37|2026-04-12 08:14:54
```

## Daily PnL
```
2026-04-16|381.29|-52.59|0
2026-04-15|363.1|17.9|0
2026-04-14|413.74|-50.64|0
2026-04-13|413.74|0.0|0
2026-04-12|423.86|-10.12|0
2026-04-11|457.33|-130.15|0
```

## Open Positions
```
none
```

## Diag Summary (last ~4h)
```
    194 trend_htf=ranging trend_mid=ranging skip=trend_mismatch
      7 trend=bullish skip=atr_low ratio=0.69 min=0.8
      4 trend=bullish skip=atr_low ratio=0.7 min=0.8
      3 trend=bullish skip=atr_low ratio=0.68 min=0.8
      2 trend=bullish skip=atr_low ratio=0.78 min=0.8
      2 trend=bullish skip=atr_low ratio=0.73 min=0.8
      2 trend=bullish skip=atr_low ratio=0.71 min=0.8
      2 trend=bullish skip=atr_low ratio=0.67 min=0.8
      1 trend=bullish skip=trend_immature trend_age_s=62 need_s=900
      1 trend=bullish skip=trend_immature trend_age_s=248 need_s=900
      1 trend=bullish skip=trend_immature trend_age_s=186 need_s=900
      1 trend=bullish skip=trend_immature trend_age_s=124 need_s=900
      1 trend=bullish skip=trend_immature trend_age_s=0 need_s=900
      1 trend=bullish skip=atr_low ratio=0.77 min=0.8
      1 trend=bullish skip=atr_low ratio=0.76 min=0.8
      1 trend=bullish skip=atr_low ratio=0.72 min=0.8
      1 trend=bullish atr_ratio=0.8 obs=9 obs_fresh=9 fvgs=13 bos=27 sigs=0 wrong_side=3 price_out=1 bos_miss=0 risk_neg=0 liquidity_trap=5 near_gap_pct=-0.093
      1 trend=bullish atr_ratio=0.8 obs=8 obs_fresh=8 fvgs=13 bos=26 sigs=0 wrong_side=3 price_out=3 bos_miss=0 risk_neg=0 liquidity_trap=2 near_gap_pct=-0.095
      1 trend=bullish atr_ratio=0.82 obs=9 obs_fresh=9 fvgs=13 bos=26 sigs=0 wrong_side=3 price_out=3 bos_miss=0 risk_neg=0 liquidity_trap=3 near_gap_pct=-0.056
      1 trend=bullish atr_ratio=0.81 obs=9 obs_fresh=9 fvgs=14 bos=27 sigs=0 wrong_side=3 price_out=1 bos_miss=0 risk_neg=0 liquidity_trap=5 near_gap_pct=-0.061
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
[00:04:25] tick balance=$328.70
  diag: trend=bullish atr_ratio=0.81 obs=9 obs_fresh=9 fvgs=13 bos=27 sigs=0 wrong_side=3 price_out=1 bos_miss=0 risk_neg=0 liquidity_trap=5 near_gap_pct=-0.055
[00:05:27] tick balance=$328.70
  diag: trend=bullish skip=atr_low ratio=0.78 min=0.8
[00:06:28] tick balance=$328.70
  diag: trend=bullish atr_ratio=0.81 obs=10 obs_fresh=10 fvgs=14 bos=26 sigs=0 wrong_side=3 price_out=1 bos_miss=0 risk_neg=0 liquidity_trap=6 near_gap_pct=-0.123
[00:07:31] tick balance=$328.70
  diag: trend=bullish atr_ratio=0.81 obs=10 obs_fresh=10 fvgs=14 bos=26 sigs=0 wrong_side=3 price_out=1 bos_miss=0 risk_neg=0 liquidity_trap=6 near_gap_pct=-0.149
[00:08:32] tick balance=$328.70
  diag: trend=bullish atr_ratio=0.81 obs=9 obs_fresh=9 fvgs=14 bos=26 sigs=0 wrong_side=3 price_out=1 bos_miss=0 risk_neg=0 liquidity_trap=5 near_gap_pct=-0.047
[00:09:34] tick balance=$328.70
  diag: trend=bullish atr_ratio=0.81 obs=9 obs_fresh=9 fvgs=14 bos=27 sigs=0 wrong_side=3 price_out=1 bos_miss=0 risk_neg=0 liquidity_trap=5 near_gap_pct=-0.061
[00:10:36] tick balance=$328.70
  diag: trend=bullish atr_ratio=0.8 obs=9 obs_fresh=9 fvgs=13 bos=27 sigs=0 wrong_side=3 price_out=1 bos_miss=0 risk_neg=0 liquidity_trap=5 near_gap_pct=-0.093
[00:11:38] tick balance=$328.70
  diag: trend=bullish atr_ratio=0.81 obs=9 obs_fresh=9 fvgs=13 bos=26 sigs=0 wrong_side=3 price_out=1 bos_miss=0 risk_neg=0 liquidity_trap=5 near_gap_pct=-0.089
[00:12:40] tick balance=$328.70
  diag: trend=bullish atr_ratio=0.81 obs=9 obs_fresh=9 fvgs=13 bos=27 sigs=0 wrong_side=3 price_out=2 bos_miss=0 risk_neg=0 liquidity_trap=4 near_gap_pct=-0.04
[00:13:42] tick balance=$328.70
  diag: trend=bullish atr_ratio=0.81 obs=9 obs_fresh=9 fvgs=13 bos=26 sigs=0 wrong_side=3 price_out=2 bos_miss=0 risk_neg=0 liquidity_trap=4 near_gap_pct=-0.001
[00:14:44] tick balance=$328.70
  diag: trend=bullish atr_ratio=0.82 obs=9 obs_fresh=9 fvgs=13 bos=26 sigs=0 wrong_side=3 price_out=3 bos_miss=0 risk_neg=0 liquidity_trap=3 near_gap_pct=-0.056
[00:15:47] tick balance=$328.70
  diag: trend=bullish atr_ratio=0.8 obs=8 obs_fresh=8 fvgs=13 bos=26 sigs=0 wrong_side=3 price_out=3 bos_miss=0 risk_neg=0 liquidity_trap=2 near_gap_pct=-0.095
[00:16:49] tick balance=$328.70
  diag: trend=bullish atr_ratio=0.81 obs=8 obs_fresh=8 fvgs=13 bos=26 sigs=0 wrong_side=3 price_out=3 bos_miss=0 risk_neg=0 liquidity_trap=2 near_gap_pct=-0.083
[00:17:50] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[00:18:52] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[00:19:54] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[00:20:56] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[00:21:58] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[00:23:00] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[00:24:03] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[00:25:05] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[00:26:08] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[00:27:09] tick balance=$328.70
  diag: trend=bullish skip=atr_low ratio=0.78 min=0.8
[00:28:11] tick balance=$328.70
  diag: trend=bullish atr_ratio=0.81 obs=8 obs_fresh=8 fvgs=14 bos=26 sigs=0 wrong_side=3 price_out=1 bos_miss=0 risk_neg=0 liquidity_trap=4 near_gap_pct=-0.04
[00:29:13] tick balance=$328.70
  diag: trend=bullish atr_ratio=0.81 obs=8 obs_fresh=8 fvgs=14 bos=26 sigs=0 wrong_side=3 price_out=3 bos_miss=0 risk_neg=0 liquidity_trap=2 near_gap_pct=-0.102
[00:30:15] tick balance=$328.70
  diag: trend=bullish skip=atr_low ratio=0.71 min=0.8
[00:31:16] tick balance=$328.70
  diag: trend=bullish skip=atr_low ratio=0.72 min=0.8
[00:32:18] tick balance=$328.70
  diag: trend=bullish skip=atr_low ratio=0.73 min=0.8
[00:33:20] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[00:34:22] tick balance=$328.70
  diag: trend=bullish skip=atr_low ratio=0.73 min=0.8
[00:35:24] tick balance=$328.70
  diag: trend=bullish skip=atr_low ratio=0.69 min=0.8
[00:36:26] tick balance=$328.70
  diag: trend=bullish skip=atr_low ratio=0.69 min=0.8
[00:37:28] tick balance=$328.70
  diag: trend=bullish skip=atr_low ratio=0.7 min=0.8
[00:38:30] tick balance=$328.70
  diag: trend=bullish skip=atr_low ratio=0.7 min=0.8
[00:39:32] tick balance=$328.70
  diag: trend=bullish skip=atr_low ratio=0.71 min=0.8
[00:40:33] tick balance=$328.70
  diag: trend=bullish skip=atr_low ratio=0.67 min=0.8
[00:41:36] tick balance=$328.70
  diag: trend=bullish skip=atr_low ratio=0.68 min=0.8
[00:42:38] tick balance=$328.70
  diag: trend=bullish skip=atr_low ratio=0.68 min=0.8
[00:43:39] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[00:44:41] tick balance=$328.70
  diag: trend=bullish skip=atr_low ratio=0.69 min=0.8
[00:45:42] tick balance=$328.70
  diag: trend=bullish skip=atr_low ratio=0.67 min=0.8
[00:46:43] tick balance=$328.70
  diag: trend=bullish skip=atr_low ratio=0.68 min=0.8
[00:47:45] tick balance=$328.70
  diag: trend=bullish skip=atr_low ratio=0.69 min=0.8
[00:48:47] tick balance=$328.70
  diag: trend=bullish skip=atr_low ratio=0.69 min=0.8
[00:49:49] tick balance=$328.70
  diag: trend=bullish skip=atr_low ratio=0.69 min=0.8
[00:50:51] tick balance=$328.70
  diag: trend=bullish skip=atr_low ratio=0.69 min=0.8
[00:51:53] tick balance=$328.70
  diag: trend=bullish skip=atr_low ratio=0.7 min=0.8
[00:52:55] tick balance=$328.70
  diag: trend=bullish skip=atr_low ratio=0.7 min=0.8
[00:53:57] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[00:54:59] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
```
