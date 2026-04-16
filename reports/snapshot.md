# Bot Snapshot — 2026-04-16 10:55 UTC

## Service: active
balance=$380.61

## Config
POST_CLOSE_COOLDOWN: int = 180 # 3 мин техническая пауза после закрытия
RISK_PCT: float = 0.05 # 5% от баланса на сделку
ADX_MIN: float = 20.0 # ADX < 20 → choppy market, skip entry

## Trades (last 20)
```
15|SELL|74394.2||open|2026-04-16 10:37:10|
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
2026-04-16|381.29|-0.68|0
2026-04-15|363.1|17.9|0
2026-04-14|413.74|-50.64|0
2026-04-13|413.74|0.0|0
2026-04-12|423.86|-10.12|0
2026-04-11|457.33|-130.15|0
```

## Open Positions
```
15|SELL|74394.2|open
```

## Diag Summary (last ~4h)
```
     53 trend_htf=ranging trend_mid=ranging skip=trend_mismatch
      3 trend=bullish skip=atr_low ratio=0.79 min=0.8
      3 trend=bullish skip=atr_low ratio=0.74 min=0.8
      3 trend=bullish skip=atr_low ratio=0.72 min=0.8
      2 trend=bullish skip=atr_low ratio=0.71 min=0.8
      2 trend=bullish atr_ratio=1.05 obs=9 obs_fresh=9 fvgs=8 bos=23 sigs=0 wrong_side=3 price_out=2 bos_miss=4 risk_neg=0 liquidity_trap=0 near_gap_pct=0.093
      1 trend=bullish skip=atr_low ratio=0.7 min=0.8
      1 trend=bullish skip=atr_low ratio=0.78 min=0.8
      1 trend=bullish skip=atr_low ratio=0.73 min=0.8
      1 trend=bullish atr_ratio=1.1 obs=7 obs_fresh=7 fvgs=8 bos=28 sigs=0 wrong_side=3 price_out=2 bos_miss=2 risk_neg=0 liquidity_trap=0 near_gap_pct=0.012
      1 trend=bullish atr_ratio=1.1 obs=7 obs_fresh=7 fvgs=8 bos=27 sigs=0 wrong_side=3 price_out=2 bos_miss=2 risk_neg=0 liquidity_trap=0 near_gap_pct=0.009
      1 trend=bullish atr_ratio=1.1 obs=7 obs_fresh=7 fvgs=7 bos=26 sigs=0 wrong_side=3 price_out=2 bos_miss=2 risk_neg=0 liquidity_trap=0 near_gap_pct=-0.046
      1 trend=bullish atr_ratio=1.15 obs=7 obs_fresh=7 fvgs=7 bos=25 sigs=0 wrong_side=3 price_out=2 bos_miss=2 risk_neg=0 liquidity_trap=0 near_gap_pct=-0.057
      1 trend=bullish atr_ratio=1.14 obs=8 obs_fresh=8 fvgs=7 bos=27 sigs=0 wrong_side=3 price_out=2 bos_miss=3 risk_neg=0 liquidity_trap=0 near_gap_pct=-0.042
      1 trend=bullish atr_ratio=1.14 obs=8 obs_fresh=8 fvgs=7 bos=26 sigs=0 wrong_side=3 price_out=2 bos_miss=3 risk_neg=0 liquidity_trap=0 near_gap_pct=-0.053
      1 trend=bullish atr_ratio=1.14 obs=8 obs_fresh=8 fvgs=7 bos=26 sigs=0 wrong_side=3 price_out=2 bos_miss=3 risk_neg=0 liquidity_trap=0 near_gap_pct=0.03
      1 trend=bullish atr_ratio=1.14 obs=8 obs_fresh=8 fvgs=7 bos=26 sigs=0 wrong_side=3 price_out=2 bos_miss=3 risk_neg=0 liquidity_trap=0 near_gap_pct=-0.016
      1 trend=bullish atr_ratio=1.14 obs=8 obs_fresh=8 fvgs=7 bos=26 sigs=0 wrong_side=3 price_out=2 bos_miss=3 risk_neg=0 liquidity_trap=0 near_gap_pct=0.01
      1 trend=bullish atr_ratio=1.14 obs=7 obs_fresh=7 fvgs=7 bos=25 sigs=0 wrong_side=3 price_out=2 bos_miss=2 risk_neg=0 liquidity_trap=0 near_gap_pct=-0.046
      1 trend=bullish atr_ratio=1.13 obs=8 obs_fresh=8 fvgs=7 bos=26 sigs=0 wrong_side=3 price_out=2 bos_miss=3 risk_neg=0 liquidity_trap=0 near_gap_pct=-0.011
```

## Errors
```
    self.gen.throw(typ, value, traceback)
  File "/root/smc-bot/venv/lib/python3.11/site-packages/httpcore/_exceptions.py", line 14, in map_exceptions
The above exception was the direct cause of the following exception:
Traceback (most recent call last):
    with map_httpcore_exceptions():
    self.gen.throw(typ, value, traceback)
  File "/root/smc-bot/venv/lib/python3.11/site-packages/httpx/_transports/default.py", line 118, in map_httpcore_exceptions
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
  diag: skip=post_close_cooldown wait_s=55
[12:10:23] tick balance=$368.95
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[12:11:25] tick balance=$368.95
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[12:12:27] tick balance=$368.95
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[12:13:29] tick balance=$368.95
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[12:14:30] tick balance=$368.95
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[12:15:32] tick balance=$368.95
  diag: trend=bearish skip=trend_immature trend_age_s=0 need_s=900
[12:16:34] tick balance=$368.95
  diag: trend=bearish skip=trend_immature trend_age_s=61 need_s=900
[12:17:35] tick balance=$368.95
  diag: trend=bearish skip=trend_immature trend_age_s=123 need_s=900
[12:18:37] tick balance=$368.95
  diag: trend=bearish skip=trend_immature trend_age_s=184 need_s=900
[12:19:38] tick balance=$368.95
  diag: trend=bearish skip=trend_immature trend_age_s=246 need_s=900
[12:20:40] tick balance=$368.95
  diag: trend=bearish skip=trend_immature trend_age_s=307 need_s=900
[12:21:42] tick balance=$368.95
  diag: trend=bearish skip=trend_immature trend_age_s=369 need_s=900
[12:22:43] tick balance=$368.95
  diag: trend=bearish skip=trend_immature trend_age_s=430 need_s=900
[12:23:45] tick balance=$368.95
  diag: trend=bearish skip=trend_immature trend_age_s=491 need_s=900
[12:24:46] tick balance=$368.95
  diag: trend=bearish skip=trend_immature trend_age_s=553 need_s=900
[12:25:48] tick balance=$368.95
  diag: trend=bearish skip=trend_immature trend_age_s=616 need_s=900
[12:26:51] tick balance=$368.95
  diag: trend=bearish skip=trend_immature trend_age_s=678 need_s=900
[12:27:52] tick balance=$368.95
  diag: trend=bearish skip=trend_immature trend_age_s=739 need_s=900
[12:28:54] tick balance=$368.95
  diag: trend=bearish skip=trend_immature trend_age_s=801 need_s=900
[12:29:56] tick balance=$368.95
  diag: trend=bearish skip=trend_immature trend_age_s=863 need_s=900
[12:30:58] tick balance=$368.95
  diag: trend=bearish atr_ratio=1.11 obs=10 obs_fresh=10 fvgs=10 bos=20 sigs=0 wrong_side=5 price_out=1 bos_miss=0 risk_neg=0 liquidity_trap=4 near_gap_pct=0.203
[12:32:00] tick balance=$368.95
  diag: trend=bearish atr_ratio=1.15 obs=10 obs_fresh=10 fvgs=10 bos=20 sigs=0 wrong_side=5 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=5 near_gap_pct=0.171
[12:33:02] tick balance=$368.95
  diag: trend=bearish atr_ratio=1.15 obs=10 obs_fresh=10 fvgs=10 bos=20 sigs=0 wrong_side=5 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=5 near_gap_pct=0.169
[12:34:04] tick balance=$368.95
  diag: trend=bearish atr_ratio=1.15 obs=10 obs_fresh=10 fvgs=10 bos=20 sigs=0 wrong_side=5 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=5 near_gap_pct=0.177
[12:35:06] tick balance=$368.95
  diag: trend=bearish atr_ratio=1.11 obs=10 obs_fresh=10 fvgs=10 bos=19 sigs=0 wrong_side=5 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=5 near_gap_pct=0.162
[12:36:07] tick balance=$368.95
  diag: trend=bearish atr_ratio=1.13 obs=10 obs_fresh=10 fvgs=10 bos=20 sigs=0 wrong_side=5 price_out=1 bos_miss=0 risk_neg=0 liquidity_trap=4 near_gap_pct=0.203
[12:37:09] tick balance=$368.95
✅ <b>SHORT Opened</b>
Entry: <b>$74,394.2</b>
SL: <b>$74,535.5</b>
TP: <b>$74,052.1</b>
Vol: <b>1335</b> contracts
Risk: <b>$18.45</b>
Daily PnL: <b>$-12.34</b>
Reason: Short: Pure OB + BOS
  diag: trend=bearish atr_ratio=1.15 obs=11 obs_fresh=11 fvgs=10 bos=20 sigs=1 wrong_side=5 price_out=1 bos_miss=0 risk_neg=0 liquidity_trap=4 near_gap_pct=-0.001
[12:38:12] tick balance=$369.35
  diag: trend=bearish atr_ratio=1.15 obs=11 obs_fresh=10 fvgs=10 bos=20 sigs=0 wrong_side=5 price_out=1 bos_miss=0 risk_neg=0 liquidity_trap=4 near_gap_pct=0.223
[12:39:15] tick balance=$368.82
  diag: trend=bearish atr_ratio=1.15 obs=11 obs_fresh=10 fvgs=10 bos=21 sigs=0 wrong_side=5 price_out=1 bos_miss=0 risk_neg=0 liquidity_trap=4 near_gap_pct=0.218
[12:40:18] tick balance=$366.58
  diag: trend=bearish atr_ratio=1.11 obs=10 obs_fresh=10 fvgs=10 bos=21 sigs=0 wrong_side=5 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=5 near_gap_pct=0.195
[12:41:20] tick balance=$370.55
  diag: trend=bearish atr_ratio=1.13 obs=10 obs_fresh=10 fvgs=10 bos=21 sigs=0 wrong_side=5 price_out=1 bos_miss=0 risk_neg=0 liquidity_trap=4 near_gap_pct=0.243
[12:42:23] tick balance=$374.64
  diag: trend=bearish atr_ratio=1.14 obs=11 obs_fresh=11 fvgs=10 bos=21 sigs=1 wrong_side=5 price_out=1 bos_miss=0 risk_neg=0 liquidity_trap=4 near_gap_pct=0.031 skip=side_busy open_sides=['SELL']
[12:43:25] tick balance=$372.28
  diag: trend=bearish atr_ratio=1.14 obs=11 obs_fresh=10 fvgs=10 bos=21 sigs=0 wrong_side=5 price_out=1 bos_miss=0 risk_neg=0 liquidity_trap=4 near_gap_pct=0.257
[12:44:27] tick balance=$374.79
  diag: trend=bearish atr_ratio=1.14 obs=11 obs_fresh=10 fvgs=10 bos=21 sigs=0 wrong_side=5 price_out=1 bos_miss=0 risk_neg=0 liquidity_trap=4 near_gap_pct=0.278
[12:45:29] tick balance=$373.64
  diag: trend=bearish atr_ratio=1.12 obs=11 obs_fresh=10 fvgs=11 bos=20 sigs=0 wrong_side=5 price_out=1 bos_miss=0 risk_neg=0 liquidity_trap=4 near_gap_pct=0.267
[12:46:31] tick balance=$376.55
  diag: trend=bearish atr_ratio=1.13 obs=11 obs_fresh=10 fvgs=11 bos=20 sigs=0 wrong_side=5 price_out=1 bos_miss=0 risk_neg=0 liquidity_trap=4 near_gap_pct=0.297
[12:47:33] tick balance=$378.82
  diag: trend=bearish atr_ratio=1.14 obs=11 obs_fresh=10 fvgs=11 bos=20 sigs=0 wrong_side=5 price_out=1 bos_miss=0 risk_neg=0 liquidity_trap=4 near_gap_pct=0.319
[12:48:35] tick balance=$387.03
  diag: trend=bearish atr_ratio=1.18 obs=11 obs_fresh=10 fvgs=11 bos=20 sigs=0 wrong_side=5 price_out=1 bos_miss=0 risk_neg=0 liquidity_trap=4 near_gap_pct=0.402
[12:49:37] tick balance=$389.54
[change_stop_loss] id=496750414 new_sl=74389.2 tp_preserved=74052.1 resp={'success': True, 'code': 0}
[partial_close] symbol=BTC_USDT pos_type=2 vol=667 resp={'success': False, 'code': 2009, 'message': 'Position is nonexistent or closed'}
[partial_tp] partial_close rejected: {'success': False, 'code': 2009, 'message': 'Position is nonexistent or closed'}
  diag: trend=bearish atr_ratio=1.18 obs=11 obs_fresh=10 fvgs=11 bos=20 sigs=0 wrong_side=5 price_out=2 bos_miss=0 risk_neg=0 liquidity_trap=3 near_gap_pct=0.428
[12:50:41] tick balance=$386.51
  diag: trend=bearish atr_ratio=1.17 obs=11 obs_fresh=10 fvgs=12 bos=20 sigs=0 wrong_side=5 price_out=1 bos_miss=0 risk_neg=0 liquidity_trap=4 near_gap_pct=0.399
[12:51:43] tick balance=$383.76
  diag: trend=bearish atr_ratio=1.17 obs=11 obs_fresh=10 fvgs=12 bos=20 sigs=0 wrong_side=5 price_out=1 bos_miss=0 risk_neg=0 liquidity_trap=4 near_gap_pct=0.369
[12:52:45] tick balance=$383.06
  diag: trend=bearish atr_ratio=1.18 obs=11 obs_fresh=10 fvgs=12 bos=20 sigs=0 wrong_side=5 price_out=1 bos_miss=0 risk_neg=0 liquidity_trap=4 near_gap_pct=0.362
[12:53:48] tick balance=$378.59
  diag: trend=bearish atr_ratio=1.2 obs=11 obs_fresh=10 fvgs=12 bos=20 sigs=0 wrong_side=5 price_out=1 bos_miss=0 risk_neg=0 liquidity_trap=4 near_gap_pct=0.31
[12:54:50] tick balance=$380.61
  diag: trend=bearish atr_ratio=1.2 obs=11 obs_fresh=10 fvgs=12 bos=20 sigs=0 wrong_side=5 price_out=1 bos_miss=0 risk_neg=0 liquidity_trap=4 near_gap_pct=0.337
```
