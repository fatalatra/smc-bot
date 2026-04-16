# Bot Snapshot — 2026-04-16 18:55 UTC

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
    142 trend_htf=ranging trend_mid=ranging skip=trend_mismatch
      4 trend=bearish skip=atr_low ratio=0.75 min=0.8
      3 trend=bearish skip=atr_low ratio=0.74 min=0.8
      2 trend=bearish atr_ratio=0.85 obs=10 obs_fresh=8 fvgs=13 bos=25 sigs=0 wrong_side=4 price_out=4 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=0.836
      1 trend=bearish skip=atr_low ratio=0.79 min=0.8
      1 trend=bearish skip=atr_low ratio=0.76 min=0.8
      1 trend=bearish skip=atr_low ratio=0.72 min=0.8
      1 trend=bearish atr_ratio=1.9 obs=7 obs_fresh=7 fvgs=16 bos=26 sigs=0 wrong_side=3 price_out=4 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=-0.625
      1 trend=bearish atr_ratio=1.88 obs=7 obs_fresh=7 fvgs=16 bos=27 sigs=0 wrong_side=3 price_out=4 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=-0.522
      1 trend=bearish atr_ratio=1.88 obs=7 obs_fresh=7 fvgs=16 bos=27 sigs=0 wrong_side=3 price_out=4 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=-0.495
      1 trend=bearish atr_ratio=1.88 obs=7 obs_fresh=7 fvgs=16 bos=26 sigs=0 wrong_side=3 price_out=4 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=-0.558
      1 trend=bearish atr_ratio=1.88 obs=7 obs_fresh=7 fvgs=16 bos=26 sigs=0 wrong_side=3 price_out=4 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=-0.501
      1 trend=bearish atr_ratio=1.87 obs=7 obs_fresh=7 fvgs=15 bos=26 sigs=0 wrong_side=3 price_out=4 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=-0.531
      1 trend=bearish atr_ratio=1.87 obs=7 obs_fresh=7 fvgs=15 bos=26 sigs=0 wrong_side=3 price_out=4 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=-0.505
      1 trend=bearish atr_ratio=1.86 obs=7 obs_fresh=7 fvgs=15 bos=25 sigs=0 wrong_side=3 price_out=3 bos_miss=0 risk_neg=0 liquidity_trap=1 near_gap_pct=-0.742
      1 trend=bearish atr_ratio=1.85 obs=8 obs_fresh=7 fvgs=15 bos=25 sigs=0 wrong_side=3 price_out=3 bos_miss=0 risk_neg=0 liquidity_trap=1 near_gap_pct=-0.405
      1 trend=bearish atr_ratio=1.85 obs=8 obs_fresh=7 fvgs=15 bos=25 sigs=0 wrong_side=3 price_out=3 bos_miss=0 risk_neg=0 liquidity_trap=1 near_gap_pct=-0.328
      1 trend=bearish atr_ratio=1.85 obs=7 obs_fresh=7 fvgs=15 bos=25 sigs=0 wrong_side=3 price_out=3 bos_miss=0 risk_neg=0 liquidity_trap=1 near_gap_pct=-0.441
      1 trend=bearish atr_ratio=1.84 obs=8 obs_fresh=8 fvgs=15 bos=26 sigs=1 wrong_side=3 price_out=3 bos_miss=0 risk_neg=0 liquidity_trap=1 near_gap_pct=0.032
      1 trend=bearish atr_ratio=1.84 obs=7 obs_fresh=7 fvgs=15 bos=27 sigs=0 wrong_side=3 price_out=4 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=-0.61
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
[20:03:18] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:04:20] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:05:22] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:06:24] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:07:26] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:08:28] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:09:29] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:10:32] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:11:34] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:12:36] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:13:37] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:14:40] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:15:42] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:16:43] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:17:45] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:18:47] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:19:49] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:20:51] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:21:53] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:22:55] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:23:57] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:25:00] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:26:02] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:27:04] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:28:06] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:29:08] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:30:11] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:31:12] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:32:14] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:33:16] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:34:18] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:35:21] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:36:22] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:37:25] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:38:27] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:39:29] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:40:32] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:41:34] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:42:36] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:43:38] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:44:41] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:45:44] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:46:45] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:47:48] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:48:50] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:49:52] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:50:54] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:51:56] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:52:58] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:53:59] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
```
