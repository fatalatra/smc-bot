# Bot Snapshot — 2026-04-17 14:55 UTC

## Service: active
balance=$327.74

## Config
POST_CLOSE_COOLDOWN: int = 180 # 3 мин техническая пауза после закрытия
RISK_PCT: float = 0.05 # 5% от баланса на сделку
ADX_MIN: float = 20.0 # ADX < 20 → choppy market, skip entry

## Trades (last 20)
```
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
3|SELL|71597.7|13.27|closed|2026-04-12 10:25:37|2026-04-12 10:42:19
2|SELL|73451.8|13.15|closed|2026-04-11 20:18:03|2026-04-12 08:14:54
```

## Daily PnL
```
2026-04-17|328.7|-0.95|0
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
     48 trend_htf=ranging trend_mid=ranging skip=trend_mismatch
      7 trend=bullish skip=atr_low ratio=0.6 min=0.8
      7 trend=bullish skip=atr_low ratio=0.59 min=0.8
      6 trend=bullish skip=atr_low ratio=0.67 min=0.8
      5 trend=bullish skip=atr_low ratio=0.71 min=0.8
      5 trend=bullish skip=atr_low ratio=0.68 min=0.8
      5 trend=bullish skip=atr_low ratio=0.57 min=0.8
      4 trend=bullish skip=atr_low ratio=0.73 min=0.8
      3 trend=bullish skip=atr_low ratio=0.72 min=0.8
      3 trend=bullish skip=atr_low ratio=0.58 min=0.8
      2 trend=bullish skip=atr_low ratio=0.65 min=0.8
      1 trend=bullish skip=trend_immature trend_age_s=869 need_s=900
      1 trend=bullish skip=trend_immature trend_age_s=807 need_s=900
      1 trend=bullish skip=trend_immature trend_age_s=745 need_s=900
      1 trend=bullish skip=trend_immature trend_age_s=683 need_s=900
      1 trend=bullish skip=trend_immature trend_age_s=62 need_s=900
      1 trend=bullish skip=trend_immature trend_age_s=621 need_s=900
      1 trend=bullish skip=trend_immature trend_age_s=558 need_s=900
      1 trend=bullish skip=trend_immature trend_age_s=496 need_s=900
      1 trend=bullish skip=trend_immature trend_age_s=434 need_s=900
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
  diag: trend=bullish atr_ratio=1.74 obs=11 obs_fresh=7 fvgs=11 bos=27 sigs=0 wrong_side=4 price_out=3 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=2.318
[16:10:00] tick balance=$329.31
  diag: trend=bullish atr_ratio=1.62 obs=10 obs_fresh=6 fvgs=12 bos=27 sigs=0 wrong_side=3 price_out=3 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=2.141
[16:11:02] tick balance=$329.31
  diag: trend=bullish atr_ratio=1.63 obs=10 obs_fresh=6 fvgs=12 bos=27 sigs=0 wrong_side=3 price_out=3 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=2.139
[16:12:04] tick balance=$329.31
  diag: trend=bullish atr_ratio=1.64 obs=10 obs_fresh=6 fvgs=12 bos=27 sigs=0 wrong_side=3 price_out=3 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=2.067
[16:13:07] tick balance=$329.31
  diag: trend=bullish atr_ratio=1.65 obs=10 obs_fresh=6 fvgs=12 bos=27 sigs=0 wrong_side=3 price_out=3 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=2.001
[16:14:09] tick balance=$329.31
  diag: trend=bullish atr_ratio=1.65 obs=10 obs_fresh=6 fvgs=12 bos=27 sigs=0 wrong_side=3 price_out=3 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=2.042
[16:15:10] tick balance=$329.31
  diag: trend=bullish atr_ratio=1.49 obs=10 obs_fresh=6 fvgs=12 bos=27 sigs=0 wrong_side=3 price_out=3 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=2.049
[16:16:12] tick balance=$329.31
  diag: trend=bullish atr_ratio=1.51 obs=10 obs_fresh=6 fvgs=11 bos=27 sigs=0 wrong_side=3 price_out=3 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=2.176
[16:17:15] tick balance=$329.31
  diag: trend=bullish atr_ratio=1.51 obs=10 obs_fresh=6 fvgs=11 bos=26 sigs=0 wrong_side=3 price_out=3 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=2.212
[16:18:16] tick balance=$329.31
  diag: trend=bullish atr_ratio=1.51 obs=10 obs_fresh=6 fvgs=11 bos=26 sigs=0 wrong_side=3 price_out=3 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=2.194
[16:19:18] tick balance=$329.31
  diag: trend=bullish atr_ratio=1.52 obs=10 obs_fresh=6 fvgs=11 bos=26 sigs=0 wrong_side=3 price_out=3 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=2.168
[16:20:20] tick balance=$329.31
  diag: trend=bullish atr_ratio=1.4 obs=10 obs_fresh=6 fvgs=12 bos=26 sigs=0 wrong_side=3 price_out=3 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=2.291
[16:21:23] tick balance=$329.31
  diag: trend=bullish atr_ratio=1.42 obs=10 obs_fresh=6 fvgs=12 bos=25 sigs=0 wrong_side=3 price_out=3 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=2.295
[16:22:24] tick balance=$329.31
✅ <b>LONG Opened</b>
Entry: <b>$77,434.2</b>
SL: <b>$76,803.3</b>
TP: <b>$79,009.4</b>
Vol: <b>261</b> contracts
Risk: <b>$16.47</b>
Daily PnL: <b>$+0.62</b>
Reason: Long: OB+FVG confluence + BOS
  diag: trend=bullish atr_ratio=1.45 obs=11 obs_fresh=7 fvgs=12 bos=25 sigs=1 wrong_side=3 price_out=3 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=0.367
[16:23:28] tick balance=$327.36
  diag: trend=bullish atr_ratio=1.45 obs=11 obs_fresh=6 fvgs=12 bos=25 sigs=0 wrong_side=3 price_out=3 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=2.455
[16:24:31] tick balance=$329.89
  diag: trend=bullish atr_ratio=1.49 obs=11 obs_fresh=6 fvgs=12 bos=25 sigs=0 wrong_side=3 price_out=3 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=2.567
[16:25:34] tick balance=$331.96
  diag: trend=bullish atr_ratio=1.42 obs=10 obs_fresh=5 fvgs=13 bos=26 sigs=0 wrong_side=2 price_out=3 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=2.663
[16:26:36] tick balance=$333.54
  diag: trend=bullish atr_ratio=1.44 obs=10 obs_fresh=5 fvgs=13 bos=25 sigs=0 wrong_side=2 price_out=3 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=2.756
[16:27:38] tick balance=$334.47
  diag: trend=bullish atr_ratio=1.44 obs=10 obs_fresh=5 fvgs=13 bos=25 sigs=0 wrong_side=2 price_out=3 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=2.789
[16:28:40] tick balance=$332.40
  diag: trend=bullish atr_ratio=1.44 obs=10 obs_fresh=5 fvgs=13 bos=25 sigs=0 wrong_side=2 price_out=3 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=2.694
[16:29:43] tick balance=$327.64
  diag: trend=bullish atr_ratio=1.47 obs=10 obs_fresh=5 fvgs=13 bos=26 sigs=0 wrong_side=2 price_out=3 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=2.461
[16:30:46] tick balance=$327.74
[sync] trade #21 BUY entry=77434.2 closed (manual) at price=77460.0
[real_pnl] trade #21: profit=-1.57 open_fee=0.00 close_fee=0.00 => net=-1.57
  ⏸ paused: manual close of BUY @ 77434.2 at 16:30:47
[16:31:48] tick balance=$327.74
  ⏸ paused: manual close of BUY @ 77434.2 at 16:30:47
[16:32:50] tick balance=$327.74
  ⏸ paused: manual close of BUY @ 77434.2 at 16:30:47
[16:33:51] tick balance=$327.74
  ⏸ paused: manual close of BUY @ 77434.2 at 16:30:47
[16:34:53] tick balance=$327.74
  ⏸ paused: manual close of BUY @ 77434.2 at 16:30:47
[tg] resume
[16:35:54] tick balance=$327.74
  diag: trend=bullish atr_ratio=1.38 obs=10 obs_fresh=5 fvgs=12 bos=26 sigs=0 wrong_side=2 price_out=3 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=2.791
[16:36:56] tick balance=$327.74
  diag: trend=bullish atr_ratio=1.38 obs=11 obs_fresh=6 fvgs=12 bos=27 sigs=1 wrong_side=2 price_out=3 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=0.05
[16:37:58] tick balance=$327.74
  diag: trend=bullish atr_ratio=1.4 obs=11 obs_fresh=5 fvgs=12 bos=27 sigs=0 wrong_side=2 price_out=3 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=2.93
[16:39:00] tick balance=$327.74
  diag: trend=bullish atr_ratio=1.4 obs=11 obs_fresh=5 fvgs=12 bos=27 sigs=0 wrong_side=2 price_out=3 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=2.977
[16:40:01] tick balance=$327.74
  diag: trend=bullish atr_ratio=1.26 obs=11 obs_fresh=5 fvgs=13 bos=26 sigs=0 wrong_side=2 price_out=3 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=3.034
[16:41:04] tick balance=$327.74
  diag: trend=bullish atr_ratio=1.27 obs=11 obs_fresh=5 fvgs=13 bos=26 sigs=0 wrong_side=2 price_out=3 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=3.065
[16:42:06] tick balance=$327.74
  diag: trend=bullish atr_ratio=1.28 obs=11 obs_fresh=5 fvgs=13 bos=26 sigs=0 wrong_side=2 price_out=3 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=3.131
[16:43:08] tick balance=$327.74
  diag: trend=bullish atr_ratio=1.29 obs=11 obs_fresh=5 fvgs=13 bos=26 sigs=0 wrong_side=2 price_out=3 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=3.219
[16:44:10] tick balance=$327.74
  diag: trend=bullish atr_ratio=1.31 obs=11 obs_fresh=5 fvgs=13 bos=26 sigs=0 wrong_side=2 price_out=3 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=3.038
[16:45:12] tick balance=$327.74
  diag: trend=bullish atr_ratio=1.28 obs=11 obs_fresh=5 fvgs=14 bos=27 sigs=0 wrong_side=2 price_out=3 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=3.162
[16:46:13] tick balance=$327.74
  diag: trend=bullish atr_ratio=1.31 obs=11 obs_fresh=5 fvgs=13 bos=27 sigs=0 wrong_side=2 price_out=3 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=3.044
[16:47:15] tick balance=$327.74
  diag: trend=bullish atr_ratio=1.33 obs=11 obs_fresh=5 fvgs=13 bos=27 sigs=0 wrong_side=2 price_out=3 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=2.984
[16:48:18] tick balance=$327.74
  diag: trend=bullish atr_ratio=1.33 obs=11 obs_fresh=5 fvgs=13 bos=28 sigs=0 wrong_side=2 price_out=3 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=3.069
[16:49:20] tick balance=$327.74
  diag: trend=bullish atr_ratio=1.33 obs=11 obs_fresh=5 fvgs=13 bos=28 sigs=0 wrong_side=2 price_out=3 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=3.054
[16:50:23] tick balance=$327.74
  diag: trend=bullish atr_ratio=1.22 obs=11 obs_fresh=5 fvgs=13 bos=28 sigs=0 wrong_side=2 price_out=3 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=3.075
[16:51:24] tick balance=$327.74
  diag: trend=bullish atr_ratio=1.23 obs=11 obs_fresh=5 fvgs=13 bos=28 sigs=0 wrong_side=2 price_out=3 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=3.068
[16:52:26] tick balance=$327.74
  diag: trend=bullish atr_ratio=1.24 obs=11 obs_fresh=5 fvgs=13 bos=28 sigs=0 wrong_side=2 price_out=3 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=3.222
[16:53:28] tick balance=$327.74
  diag: trend=bullish atr_ratio=1.24 obs=11 obs_fresh=5 fvgs=13 bos=28 sigs=0 wrong_side=2 price_out=3 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=3.146
[16:54:31] tick balance=$327.74
  diag: trend=bullish atr_ratio=1.26 obs=11 obs_fresh=5 fvgs=13 bos=28 sigs=0 wrong_side=2 price_out=3 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=2.949
```
