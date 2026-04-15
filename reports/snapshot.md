# Bot Snapshot — 2026-04-15 22:55 UTC

## Service: active
balance=$391.54

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
2026-04-15|363.1|28.44|0
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
    202 trend_htf=ranging trend_mid=ranging skip=trend_mismatch
      1 trend=bullish skip=trend_immature trend_age_s=867 need_s=900
      1 trend=bullish skip=trend_immature trend_age_s=805 need_s=900
      1 trend=bullish skip=trend_immature trend_age_s=743 need_s=900
      1 trend=bullish skip=trend_immature trend_age_s=682 need_s=900
      1 trend=bullish skip=trend_immature trend_age_s=62 need_s=900
      1 trend=bullish skip=trend_immature trend_age_s=619 need_s=900
      1 trend=bullish skip=trend_immature trend_age_s=558 need_s=900
      1 trend=bullish skip=trend_immature trend_age_s=496 need_s=900
      1 trend=bullish skip=trend_immature trend_age_s=434 need_s=900
      1 trend=bullish skip=trend_immature trend_age_s=372 need_s=900
      1 trend=bullish skip=trend_immature trend_age_s=310 need_s=900
      1 trend=bullish skip=trend_immature trend_age_s=248 need_s=900
      1 trend=bullish skip=trend_immature trend_age_s=186 need_s=900
      1 trend=bullish skip=trend_immature trend_age_s=124 need_s=900
      1 trend=bullish skip=trend_immature trend_age_s=0 need_s=900
      1 trend=bullish atr_ratio=1.2 obs=9 obs_fresh=5 fvgs=13 bos=25 sigs=0 wrong_side=2 price_out=2 bos_miss=0 risk_neg=0 liquidity_trap=1 near_gap_pct=0.522
      1 trend=bullish atr_ratio=1.2 obs=8 obs_fresh=4 fvgs=11 bos=24 sigs=0 wrong_side=2 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=2 near_gap_pct=0.328
      1 trend=bullish atr_ratio=1.25 obs=9 obs_fresh=5 fvgs=12 bos=25 sigs=0 wrong_side=2 price_out=1 bos_miss=0 risk_neg=0 liquidity_trap=2 near_gap_pct=0.311
      1 trend=bullish atr_ratio=1.23 obs=9 obs_fresh=5 fvgs=13 bos=25 sigs=0 wrong_side=2 price_out=1 bos_miss=0 risk_neg=0 liquidity_trap=2 near_gap_pct=0.391
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
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[00:08:32] tick balance=$388.15
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[00:09:34] tick balance=$388.15
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[00:10:35] tick balance=$388.15
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[00:11:41] tick balance=$388.15
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[00:12:46] tick balance=$388.15
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[00:13:48] tick balance=$388.15
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[00:14:50] tick balance=$388.15
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[00:15:52] tick balance=$388.15
  diag: trend=bullish skip=trend_immature trend_age_s=0 need_s=900
[00:16:54] tick balance=$388.15
  diag: trend=bullish skip=trend_immature trend_age_s=62 need_s=900
[00:17:56] tick balance=$388.15
  diag: trend=bullish skip=trend_immature trend_age_s=124 need_s=900
[00:18:58] tick balance=$388.15
  diag: trend=bullish skip=trend_immature trend_age_s=186 need_s=900
[00:20:00] tick balance=$388.15
  diag: trend=bullish skip=trend_immature trend_age_s=248 need_s=900
[00:21:02] tick balance=$388.15
  diag: trend=bullish skip=trend_immature trend_age_s=310 need_s=900
[00:22:04] tick balance=$388.15
  diag: trend=bullish skip=trend_immature trend_age_s=372 need_s=900
[00:23:06] tick balance=$388.15
  diag: trend=bullish skip=trend_immature trend_age_s=434 need_s=900
[00:24:08] tick balance=$388.15
  diag: trend=bullish skip=trend_immature trend_age_s=496 need_s=900
[00:25:10] tick balance=$388.15
  diag: trend=bullish skip=trend_immature trend_age_s=558 need_s=900
[00:26:12] tick balance=$388.15
  diag: trend=bullish skip=trend_immature trend_age_s=619 need_s=900
[00:27:14] tick balance=$388.15
  diag: trend=bullish skip=trend_immature trend_age_s=682 need_s=900
[00:28:15] tick balance=$388.15
  diag: trend=bullish skip=trend_immature trend_age_s=743 need_s=900
[00:29:17] tick balance=$388.15
  diag: trend=bullish skip=trend_immature trend_age_s=805 need_s=900
[00:30:19] tick balance=$388.15
  diag: trend=bullish skip=trend_immature trend_age_s=867 need_s=900
[00:31:21] tick balance=$388.15
[!] R:R too low, skipping: Long: OB+FVG confluence + BOS
  diag: trend=bullish atr_ratio=1.02 obs=8 obs_fresh=8 fvgs=12 bos=24 sigs=1 wrong_side=0 price_out=1 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=0.275
[00:32:23] tick balance=$388.15
✅ <b>LONG Opened</b>
Entry: <b>$74,983.1</b>
SL: <b>$74,395.1</b>
TP: <b>$76,474.7</b>
Vol: <b>326</b> contracts
Risk: <b>$19.41</b>
Daily PnL: <b>$+25.05</b>
Reason: Long: OB+FVG confluence + BOS
  diag: trend=bullish atr_ratio=1.03 obs=8 obs_fresh=7 fvgs=12 bos=24 sigs=1 wrong_side=1 price_out=1 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=0.267
[00:33:27] tick balance=$387.56
  diag: trend=bullish atr_ratio=1.03 obs=8 obs_fresh=6 fvgs=12 bos=25 sigs=1 wrong_side=2 price_out=1 bos_miss=0 risk_neg=0 liquidity_trap=1 near_gap_pct=0.235 skip=side_busy open_sides=['BUY']
[00:34:30] tick balance=$386.92
  diag: trend=bullish atr_ratio=1.03 obs=8 obs_fresh=5 fvgs=12 bos=24 sigs=0 wrong_side=2 price_out=1 bos_miss=0 risk_neg=0 liquidity_trap=2 near_gap_pct=0.208
[00:35:33] tick balance=$387.23
  diag: trend=bullish atr_ratio=1.05 obs=8 obs_fresh=5 fvgs=12 bos=24 sigs=0 wrong_side=2 price_out=1 bos_miss=0 risk_neg=0 liquidity_trap=2 near_gap_pct=0.223
[00:36:36] tick balance=$387.05
  diag: trend=bullish atr_ratio=1.05 obs=8 obs_fresh=5 fvgs=12 bos=24 sigs=0 wrong_side=2 price_out=1 bos_miss=0 risk_neg=0 liquidity_trap=2 near_gap_pct=0.212
[00:37:38] tick balance=$387.19
  diag: trend=bullish atr_ratio=1.05 obs=8 obs_fresh=5 fvgs=12 bos=25 sigs=0 wrong_side=2 price_out=1 bos_miss=0 risk_neg=0 liquidity_trap=2 near_gap_pct=0.216
[00:38:40] tick balance=$387.59
  diag: trend=bullish atr_ratio=1.05 obs=8 obs_fresh=5 fvgs=12 bos=25 sigs=0 wrong_side=2 price_out=1 bos_miss=0 risk_neg=0 liquidity_trap=2 near_gap_pct=0.236
[00:39:42] tick balance=$399.86
  diag: trend=bullish atr_ratio=1.19 obs=9 obs_fresh=6 fvgs=12 bos=25 sigs=1 wrong_side=2 price_out=3 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=0.459 skip=side_busy open_sides=['BUY']
[00:40:44] tick balance=$394.61
  diag: trend=bullish atr_ratio=1.2 obs=9 obs_fresh=5 fvgs=13 bos=25 sigs=0 wrong_side=2 price_out=2 bos_miss=0 risk_neg=0 liquidity_trap=1 near_gap_pct=0.522
[00:41:46] tick balance=$392.78
  diag: trend=bullish atr_ratio=1.21 obs=9 obs_fresh=5 fvgs=13 bos=25 sigs=0 wrong_side=2 price_out=1 bos_miss=0 risk_neg=0 liquidity_trap=2 near_gap_pct=0.441
[00:42:49] tick balance=$391.42
  diag: trend=bullish atr_ratio=1.23 obs=9 obs_fresh=5 fvgs=13 bos=25 sigs=0 wrong_side=2 price_out=1 bos_miss=0 risk_neg=0 liquidity_trap=2 near_gap_pct=0.391
[00:43:51] tick balance=$391.30
  diag: trend=bullish atr_ratio=1.23 obs=9 obs_fresh=5 fvgs=13 bos=25 sigs=0 wrong_side=2 price_out=1 bos_miss=0 risk_neg=0 liquidity_trap=2 near_gap_pct=0.387
[00:44:53] tick balance=$389.58
  diag: trend=bullish atr_ratio=1.25 obs=9 obs_fresh=5 fvgs=12 bos=25 sigs=0 wrong_side=2 price_out=1 bos_miss=0 risk_neg=0 liquidity_trap=2 near_gap_pct=0.311
[00:45:56] tick balance=$390.54
  diag: trend=bullish atr_ratio=1.21 obs=8 obs_fresh=4 fvgs=12 bos=25 sigs=0 wrong_side=2 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=2 near_gap_pct=0.356
[00:46:58] tick balance=$389.52
  diag: trend=bullish atr_ratio=1.22 obs=8 obs_fresh=4 fvgs=12 bos=25 sigs=0 wrong_side=2 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=2 near_gap_pct=0.315
[00:48:01] tick balance=$389.63
  diag: trend=bullish atr_ratio=1.22 obs=8 obs_fresh=4 fvgs=12 bos=25 sigs=0 wrong_side=2 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=2 near_gap_pct=0.316
[00:49:03] tick balance=$392.40
  diag: trend=bullish atr_ratio=1.22 obs=8 obs_fresh=4 fvgs=12 bos=24 sigs=0 wrong_side=2 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=2 near_gap_pct=0.424
[00:50:06] tick balance=$391.59
  diag: trend=bullish atr_ratio=1.16 obs=8 obs_fresh=4 fvgs=11 bos=24 sigs=0 wrong_side=2 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=2 near_gap_pct=0.403
[00:51:09] tick balance=$391.84
  diag: trend=bullish atr_ratio=1.19 obs=8 obs_fresh=4 fvgs=11 bos=24 sigs=0 wrong_side=2 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=2 near_gap_pct=0.404
[00:52:11] tick balance=$389.90
  diag: trend=bullish atr_ratio=1.2 obs=8 obs_fresh=4 fvgs=11 bos=24 sigs=0 wrong_side=2 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=2 near_gap_pct=0.328
[00:53:13] tick balance=$389.87
  diag: trend=bullish atr_ratio=1.21 obs=8 obs_fresh=4 fvgs=11 bos=24 sigs=0 wrong_side=2 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=2 near_gap_pct=0.318
[00:54:16] tick balance=$391.54
  diag: trend=bullish atr_ratio=1.21 obs=8 obs_fresh=4 fvgs=11 bos=24 sigs=0 wrong_side=2 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=2 near_gap_pct=0.397
```
