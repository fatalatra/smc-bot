# Bot Snapshot — 2026-04-17 02:55 UTC

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
2026-04-17|328.7|0.0|0
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
    133 trend_htf=ranging trend_mid=ranging skip=trend_mismatch
      7 trend=bullish skip=atr_low ratio=0.74 min=0.8
      6 trend=bullish skip=atr_low ratio=0.8 min=0.8
      6 trend=bullish skip=atr_low ratio=0.76 min=0.8
      6 trend=bullish skip=atr_low ratio=0.72 min=0.8
      6 trend=bullish skip=atr_low ratio=0.69 min=0.8
      5 trend=bullish skip=atr_low ratio=0.77 min=0.8
      4 trend=bullish skip=atr_low ratio=0.73 min=0.8
      3 trend=bullish skip=atr_low ratio=0.7 min=0.8
      3 trend=bullish skip=atr_low ratio=0.79 min=0.8
      2 trend=bullish skip=atr_low ratio=0.75 min=0.8
      2 trend=bullish skip=atr_low ratio=0.71 min=0.8
      1 trend=bullish skip=atr_low ratio=0.78 min=0.8
      1 trend=bullish atr_ratio=0.9 obs=12 obs_fresh=12 fvgs=9 bos=24 sigs=0 wrong_side=4 price_out=1 bos_miss=0 risk_neg=0 liquidity_trap=7 near_gap_pct=-0.0
      1 trend=bullish atr_ratio=0.9 obs=12 obs_fresh=12 fvgs=10 bos=24 sigs=0 wrong_side=4 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=8 near_gap_pct=-0.061
      1 trend=bullish atr_ratio=0.93 obs=13 obs_fresh=13 fvgs=9 bos=25 sigs=0 wrong_side=5 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=8 near_gap_pct=0.003
      1 trend=bullish atr_ratio=0.93 obs=12 obs_fresh=12 fvgs=9 bos=25 sigs=0 wrong_side=4 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=8 near_gap_pct=-0.093
      1 trend=bullish atr_ratio=0.93 obs=12 obs_fresh=12 fvgs=9 bos=24 sigs=0 wrong_side=4 price_out=2 bos_miss=0 risk_neg=0 liquidity_trap=6 near_gap_pct=-0.02
      1 trend=bullish atr_ratio=0.93 obs=11 obs_fresh=11 fvgs=9 bos=23 sigs=0 wrong_side=4 price_out=2 bos_miss=0 risk_neg=0 liquidity_trap=5 near_gap_pct=-0.051
      1 trend=bullish atr_ratio=0.92 obs=12 obs_fresh=12 fvgs=9 bos=24 sigs=0 wrong_side=4 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=8 near_gap_pct=-0.088
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
[04:04:07] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[04:05:08] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[04:06:10] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[04:07:12] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[04:08:14] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[04:09:17] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[04:10:19] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[04:11:20] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[04:12:23] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[04:13:25] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[04:14:26] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[04:15:28] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[04:16:30] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[04:17:32] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[04:18:34] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[04:19:36] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[04:20:37] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[04:21:40] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[04:22:43] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[04:23:44] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[04:24:46] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[04:25:49] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[04:26:51] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[04:27:53] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[04:28:54] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[04:29:56] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[04:30:59] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[04:32:01] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[04:33:02] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[04:34:04] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[04:35:06] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[04:36:08] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[04:37:10] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[04:38:11] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[04:39:13] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[04:40:15] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[04:41:17] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[04:42:19] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[04:43:21] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[04:44:23] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[04:45:25] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[04:46:27] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[04:47:28] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[04:48:31] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[04:49:34] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[04:50:36] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[04:51:37] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[04:52:39] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[04:53:41] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[04:54:43] tick balance=$328.70
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
```
