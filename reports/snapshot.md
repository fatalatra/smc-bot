# Bot Snapshot — 2026-04-16 02:55 UTC

## Service: active
balance=$383.00

## Config
POST_CLOSE_COOLDOWN: int = 180 # 3 мин техническая пауза после закрытия
RISK_PCT: float = 0.05 # 5% от баланса на сделку
ADX_MIN: float = 20.0 # ADX < 20 → choppy market, skip entry

## Trades (last 20)
```
14|BUY|74983.1||open|2026-04-15 22:32:25|
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
2026-04-16|381.29|1.71|0
2026-04-15|363.1|17.9|0
2026-04-14|413.74|-50.64|0
2026-04-13|413.74|0.0|0
2026-04-12|423.86|-10.12|0
2026-04-11|457.33|-130.15|0
```

## Open Positions
```
14|BUY|74983.1|open
```

## Diag Summary (last ~4h)
```
    177 trend_htf=ranging trend_mid=ranging skip=trend_mismatch
      1 trend=bullish skip=atr_low ratio=0.79 min=0.8
      1 trend=bullish skip=atr_low ratio=0.78 min=0.8
      1 trend=bullish skip=atr_low ratio=0.77 min=0.8
      1 trend=bullish skip=atr_low ratio=0.76 min=0.8
      1 trend=bullish atr_ratio=1.2 obs=8 obs_fresh=4 fvgs=11 bos=24 sigs=0 wrong_side=2 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=2 near_gap_pct=0.328
      1 trend=bullish atr_ratio=1.28 obs=9 obs_fresh=5 fvgs=12 bos=25 sigs=0 wrong_side=3 price_out=0 bos_miss=2 risk_neg=0 liquidity_trap=0 near_gap_pct=-0.058
      1 trend=bullish atr_ratio=1.28 obs=9 obs_fresh=5 fvgs=12 bos=25 sigs=0 wrong_side=3 price_out=0 bos_miss=2 risk_neg=0 liquidity_trap=0 near_gap_pct=-0.007
      1 trend=bullish atr_ratio=1.28 obs=9 obs_fresh=5 fvgs=12 bos=24 sigs=0 wrong_side=3 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=2 near_gap_pct=-0.061
      1 trend=bullish atr_ratio=1.28 obs=9 obs_fresh=5 fvgs=12 bos=24 sigs=0 wrong_side=3 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=2 near_gap_pct=-0.057
      1 trend=bullish atr_ratio=1.26 obs=9 obs_fresh=5 fvgs=12 bos=25 sigs=0 wrong_side=3 price_out=0 bos_miss=2 risk_neg=0 liquidity_trap=0 near_gap_pct=0.053
      1 trend=bullish atr_ratio=1.26 obs=9 obs_fresh=5 fvgs=12 bos=25 sigs=0 wrong_side=3 price_out=0 bos_miss=2 risk_neg=0 liquidity_trap=0 near_gap_pct=-0.03
      1 trend=bullish atr_ratio=1.26 obs=9 obs_fresh=5 fvgs=12 bos=25 sigs=0 wrong_side=3 price_out=0 bos_miss=2 risk_neg=0 liquidity_trap=0 near_gap_pct=0.021
      1 trend=bullish atr_ratio=1.26 obs=9 obs_fresh=5 fvgs=12 bos=24 sigs=0 wrong_side=3 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=2 near_gap_pct=0.009
      1 trend=bullish atr_ratio=1.25 obs=9 obs_fresh=5 fvgs=12 bos=25 sigs=0 wrong_side=3 price_out=0 bos_miss=2 risk_neg=0 liquidity_trap=0 near_gap_pct=0.031
      1 trend=bullish atr_ratio=1.25 obs=9 obs_fresh=5 fvgs=12 bos=25 sigs=0 wrong_side=2 price_out=1 bos_miss=0 risk_neg=0 liquidity_trap=2 near_gap_pct=0.311
      1 trend=bullish atr_ratio=1.24 obs=9 obs_fresh=5 fvgs=12 bos=24 sigs=0 wrong_side=3 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=2 near_gap_pct=0.119
      1 trend=bullish atr_ratio=1.24 obs=9 obs_fresh=5 fvgs=11 bos=24 sigs=0 wrong_side=3 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=2 near_gap_pct=0.199
      1 trend=bullish atr_ratio=1.24 obs=9 obs_fresh=5 fvgs=11 bos=24 sigs=0 wrong_side=3 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=2 near_gap_pct=0.196
      1 trend=bullish atr_ratio=1.24 obs=9 obs_fresh=5 fvgs=11 bos=24 sigs=0 wrong_side=3 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=2 near_gap_pct=0.17
```

## Errors
```
    self.gen.throw(typ, value, traceback)
  File "/root/smc-bot/venv/lib/python3.11/site-packages/httpcore/_exceptions.py", line 14, in map_exceptions
httpcore.ConnectError: [SSL: TLSV1_ALERT_INTERNAL_ERROR] tlsv1 alert internal error (_ssl.c:992)
The above exception was the direct cause of the following exception:
Traceback (most recent call last):
    with map_httpcore_exceptions():
    self.gen.throw(typ, value, traceback)
  File "/root/smc-bot/venv/lib/python3.11/site-packages/httpx/_transports/default.py", line 118, in map_httpcore_exceptions
httpx.ConnectError: [SSL: TLSV1_ALERT_INTERNAL_ERROR] tlsv1 alert internal error (_ssl.c:992)
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
[04:02:44] tick balance=$377.26
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[04:03:47] tick balance=$376.92
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[04:04:49] tick balance=$377.09
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[04:05:53] tick balance=$377.50
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[04:06:56] tick balance=$378.37
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[04:07:59] tick balance=$378.76
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[04:09:03] tick balance=$376.99
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[04:10:06] tick balance=$374.85
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[04:11:09] tick balance=$377.86
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[04:12:11] tick balance=$376.52
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[04:13:14] tick balance=$378.29
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[04:14:16] tick balance=$377.98
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[04:15:19] tick balance=$375.91
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[04:16:22] tick balance=$377.15
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[04:17:24] tick balance=$375.61
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[04:18:27] tick balance=$375.33
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[04:19:30] tick balance=$375.62
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[04:20:33] tick balance=$377.13
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[04:21:35] tick balance=$378.07
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[04:22:38] tick balance=$379.21
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[04:23:40] tick balance=$378.91
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[04:24:43] tick balance=$378.44
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[04:25:46] tick balance=$379.52
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[04:26:49] tick balance=$382.34
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[04:27:51] tick balance=$381.06
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[04:28:53] tick balance=$381.11
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[04:29:55] tick balance=$383.15
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[04:30:58] tick balance=$384.86
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[04:32:02] tick balance=$388.09
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[04:33:05] tick balance=$388.30
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[04:34:09] tick balance=$387.91
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[04:35:12] tick balance=$386.36
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[04:36:15] tick balance=$388.27
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[04:37:18] tick balance=$388.39
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[04:38:22] tick balance=$388.03
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[04:39:25] tick balance=$389.02
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[04:40:28] tick balance=$391.17
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[04:41:31] tick balance=$390.81
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[04:42:34] tick balance=$391.78
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[04:43:37] tick balance=$394.66
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[04:44:40] tick balance=$394.46
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[04:45:42] tick balance=$395.01
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[04:46:44] tick balance=$390.63
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[04:47:48] tick balance=$388.30
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[04:48:51] tick balance=$386.06
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[04:49:54] tick balance=$386.96
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[04:50:57] tick balance=$386.50
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[04:52:00] tick balance=$385.52
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[04:53:03] tick balance=$383.72
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[04:54:05] tick balance=$383.00
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
```
