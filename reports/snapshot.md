# Bot Snapshot — 2026-04-15 14:55 UTC

## Service: active
balance=$402.72

## Config
POST_CLOSE_COOLDOWN: int = 1800 # 30 мин после закрытия
RISK_PCT: float = 0.05 # 5% от баланса на сделку
ADX_MIN: float = 20.0 # ADX < 20 → choppy market, skip entry

## Trades (last 20)
```
13|BUY|74275.5||open|2026-04-15 13:30:37|
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
2026-04-15|363.1|39.62|0
2026-04-14|413.74|-50.64|0
2026-04-13|413.74|0.0|0
2026-04-12|423.86|-10.12|0
2026-04-11|457.33|-130.15|0
```

## Open Positions
```
13|BUY|74275.5|open
```

## Diag Summary (last ~4h)
```
    204 trend_htf=ranging trend_mid=ranging skip=trend_mismatch
      2 trend=bearish atr_ratio=1.15 obs=7 obs_fresh=7 fvgs=19 bos=21 sigs=0 wrong_side=5 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=2 near_gap_pct=0.066
      2 trend=bearish atr_ratio=1.09 obs=7 obs_fresh=7 fvgs=17 bos=23 sigs=0 wrong_side=5 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=2 near_gap_pct=0.072
      1 trend=bullish atr_ratio=1.54 obs=8 obs_fresh=7 fvgs=13 bos=25 sigs=0 wrong_side=3 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=4 near_gap_pct=0.111
      1 trend=bullish atr_ratio=1.53 obs=8 obs_fresh=7 fvgs=13 bos=25 sigs=0 wrong_side=3 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=4 near_gap_pct=0.245
      1 trend=bullish atr_ratio=1.53 obs=8 obs_fresh=7 fvgs=13 bos=25 sigs=0 wrong_side=3 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=4 near_gap_pct=0.151
      1 trend=bullish atr_ratio=1.52 obs=8 obs_fresh=8 fvgs=13 bos=25 sigs=1 wrong_side=2 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=3 near_gap_pct=0.047 skip=side_busy open_sides=['BUY']
      1 trend=bullish atr_ratio=1.52 obs=8 obs_fresh=7 fvgs=13 bos=25 sigs=0 wrong_side=3 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=4 near_gap_pct=0.188
      1 trend=bullish atr_ratio=1.51 obs=9 obs_fresh=8 fvgs=13 bos=26 sigs=0 wrong_side=4 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=4 near_gap_pct=0.056
      1 trend=bullish atr_ratio=1.51 obs=9 obs_fresh=8 fvgs=13 bos=25 sigs=0 wrong_side=4 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=4 near_gap_pct=0.027
      1 trend=bullish atr_ratio=1.51 obs=8 obs_fresh=7 fvgs=13 bos=25 sigs=0 wrong_side=3 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=4 near_gap_pct=0.072
      1 trend=bullish atr_ratio=1.08 obs=7 obs_fresh=6 fvgs=13 bos=22 sigs=1 wrong_side=1 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=2 near_gap_pct=-0.08 skip=side_busy open_sides=['BUY']
      1 trend=bullish atr_ratio=0.99 obs=7 obs_fresh=7 fvgs=13 bos=21 sigs=1 wrong_side=0 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=1 near_gap_pct=0.019
      1 trend=bearish atr_ratio=1.18 obs=7 obs_fresh=7 fvgs=18 bos=22 sigs=0 wrong_side=5 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=2 near_gap_pct=0.108
      1 trend=bearish atr_ratio=1.17 obs=7 obs_fresh=7 fvgs=18 bos=23 sigs=0 wrong_side=5 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=2 near_gap_pct=0.153
      1 trend=bearish atr_ratio=1.17 obs=7 obs_fresh=7 fvgs=18 bos=23 sigs=0 wrong_side=5 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=2 near_gap_pct=0.146
      1 trend=bearish atr_ratio=1.17 obs=7 obs_fresh=7 fvgs=18 bos=22 sigs=0 wrong_side=5 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=2 near_gap_pct=0.198
      1 trend=bearish atr_ratio=1.17 obs=7 obs_fresh=7 fvgs=18 bos=22 sigs=0 wrong_side=5 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=2 near_gap_pct=0.161
      1 trend=bearish atr_ratio=1.17 obs=7 obs_fresh=7 fvgs=18 bos=22 sigs=0 wrong_side=5 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=2 near_gap_pct=0.149
      1 trend=bearish atr_ratio=1.16 obs=7 obs_fresh=7 fvgs=19 bos=21 sigs=0 wrong_side=5 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=2 near_gap_pct=0.042
```

## Errors
```
The above exception was the direct cause of the following exception:
Traceback (most recent call last):
    with map_httpcore_exceptions():
    self.gen.throw(typ, value, traceback)
  File "/root/smc-bot/venv/lib/python3.11/site-packages/httpx/_transports/default.py", line 118, in map_httpcore_exceptions
httpx.ConnectError: [SSL: TLSV1_ALERT_INTERNAL_ERROR] tlsv1 alert internal error (_ssl.c:992)
[sol watch err] [SSL: TLSV1_ALERT_INTERNAL_ERROR] tlsv1 alert internal error (_ssl.c:992)
[ERROR] [SSL: TLSV1_ALERT_INTERNAL_ERROR] tlsv1 alert internal error (_ssl.c:992)
Traceback (most recent call last):
  File "/root/smc-bot/venv/lib/python3.11/site-packages/httpx/_transports/default.py", line 101, in map_httpcore_exceptions
    with map_exceptions(exc_map):
    self.gen.throw(typ, value, traceback)
  File "/root/smc-bot/venv/lib/python3.11/site-packages/httpcore/_exceptions.py", line 14, in map_exceptions
httpcore.ConnectError: [SSL: TLSV1_ALERT_INTERNAL_ERROR] tlsv1 alert internal error (_ssl.c:992)
The above exception was the direct cause of the following exception:
Traceback (most recent call last):
    with map_httpcore_exceptions():
    self.gen.throw(typ, value, traceback)
  File "/root/smc-bot/venv/lib/python3.11/site-packages/httpx/_transports/default.py", line 118, in map_httpcore_exceptions
httpx.ConnectError: [SSL: TLSV1_ALERT_INTERNAL_ERROR] tlsv1 alert internal error (_ssl.c:992)
```

## Last 100 Log Lines
```
[16:02:53] tick balance=$397.36
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[16:04:00] tick balance=$398.99
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[16:05:04] tick balance=$395.63
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[16:06:07] tick balance=$395.41
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[16:07:10] tick balance=$395.49
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[16:08:13] tick balance=$394.37
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[16:09:17] tick balance=$393.90
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[16:10:20] tick balance=$397.23
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[16:11:24] tick balance=$398.28
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[16:12:28] tick balance=$399.49
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[16:13:31] tick balance=$397.43
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[16:14:35] tick balance=$398.50
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[16:15:39] tick balance=$403.44
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[16:16:43] tick balance=$407.64
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[16:17:45] tick balance=$408.16
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[16:18:49] tick balance=$406.59
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[16:19:52] tick balance=$404.57
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[16:20:54] tick balance=$405.10
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[16:21:58] tick balance=$409.45
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[16:23:01] tick balance=$409.69
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[16:24:05] tick balance=$409.81
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[16:25:09] tick balance=$412.68
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[16:26:12] tick balance=$414.64
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[16:27:16] tick balance=$414.05
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[16:28:19] tick balance=$412.44
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[16:29:21] tick balance=$411.90
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[16:30:25] tick balance=$410.22
  diag: trend=bullish atr_ratio=1.52 obs=8 obs_fresh=8 fvgs=13 bos=25 sigs=1 wrong_side=2 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=3 near_gap_pct=0.047 skip=side_busy open_sides=['BUY']
[16:31:30] tick balance=$411.39
  diag: trend=bullish atr_ratio=1.52 obs=8 obs_fresh=7 fvgs=13 bos=25 sigs=0 wrong_side=3 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=4 near_gap_pct=0.188
[16:32:33] tick balance=$412.53
  diag: trend=bullish atr_ratio=1.53 obs=8 obs_fresh=7 fvgs=13 bos=25 sigs=0 wrong_side=3 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=4 near_gap_pct=0.245
[16:33:36] tick balance=$410.28
  diag: trend=bullish atr_ratio=1.53 obs=8 obs_fresh=7 fvgs=13 bos=25 sigs=0 wrong_side=3 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=4 near_gap_pct=0.151
[16:34:39] tick balance=$409.42
  diag: trend=bullish atr_ratio=1.54 obs=8 obs_fresh=7 fvgs=13 bos=25 sigs=0 wrong_side=3 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=4 near_gap_pct=0.111
[16:35:43] tick balance=$407.33
  diag: trend=bullish atr_ratio=1.51 obs=9 obs_fresh=8 fvgs=13 bos=25 sigs=0 wrong_side=4 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=4 near_gap_pct=0.027
[16:36:46] tick balance=$408.79
  diag: trend=bullish atr_ratio=1.51 obs=8 obs_fresh=7 fvgs=13 bos=25 sigs=0 wrong_side=3 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=4 near_gap_pct=0.072
[16:37:49] tick balance=$408.16
  diag: trend=bullish atr_ratio=1.51 obs=9 obs_fresh=8 fvgs=13 bos=26 sigs=0 wrong_side=4 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=4 near_gap_pct=0.056
[16:38:54] tick balance=$403.65
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[16:39:58] tick balance=$397.44
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[16:41:03] tick balance=$400.15
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[16:42:07] tick balance=$399.58
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[16:43:11] tick balance=$397.80
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[16:44:15] tick balance=$397.19
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[16:45:18] tick balance=$398.47
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[16:46:22] tick balance=$397.45
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[16:47:26] tick balance=$397.76
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[16:48:29] tick balance=$398.40
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[16:49:31] tick balance=$401.22
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[16:50:35] tick balance=$404.32
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[16:51:39] tick balance=$403.16
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[16:52:43] tick balance=$401.05
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[16:53:46] tick balance=$402.90
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[16:54:50] tick balance=$402.72
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
```
