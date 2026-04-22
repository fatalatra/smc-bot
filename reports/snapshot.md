# Bot Snapshot — 2026-04-22 06:55 UTC

## Service: active
balance=$305.30

## Config
POST_CLOSE_COOLDOWN: int = 180 # 3 мин техническая пауза после закрытия
RISK_PCT: float = 0.01 # 1% для старта на HYPE (вернём к 5% после 5+ сделок)
ADX_MIN: float = 20.0 # ADX < 20 → choppy market, skip entry

## Trades (last 20)
```
31|BUY|40.4||open|2026-04-22 05:23:43|
30|BUY|40.0|3.22|closed|2026-04-22 04:07:10|2026-04-22 05:19:32
29|SELL|40.4|3.85|closed|2026-04-21 14:00:28|2026-04-21 15:27:47
28|SELL|74162.8|-15.75|closed|2026-04-20 05:21:50|2026-04-20 06:04:22
27|SELL|74544.9|-20.99|closed|2026-04-19 21:13:01|2026-04-19 21:29:27
26|SELL|75081.6|-17.17|closed|2026-04-19 09:30:34|2026-04-19 11:10:17
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
```

## Daily PnL
```
2026-04-22|301.06|4.25|0
2026-04-21|296.96|4.1|0
2026-04-20|312.71|-15.75|0
2026-04-19|354.45|-41.74|0
2026-04-18|311.88|42.12|0
2026-04-17|328.7|-16.81|0
2026-04-16|381.29|-52.59|0
```

## Open Positions
```
31|BUY|40.4|open
```

## Diag Summary (last ~4h)
```
      7 trend_htf=bearish trend_mid=bullish skip=trend_mismatch
      7 trend=bullish skip=atr_low ratio=0.74 min=0.8
      5 trend_htf=ranging trend_mid=ranging skip=trend_mismatch
      5 trend=bullish skip=atr_low ratio=0.73 min=0.8
      5 trend=bullish skip=atr_low ratio=0.72 min=0.8
      4 trend=bullish skip=atr_low ratio=0.71 min=0.8
      3 trend=bullish skip=trend_immature trend_age_s=186 need_s=900
      3 trend=bullish skip=trend_immature trend_age_s=0 need_s=900
      3 trend=bullish skip=atr_low ratio=0.7 min=0.8
      2 trend=bullish skip=trend_immature trend_age_s=62 need_s=900
      2 trend=bullish skip=trend_immature trend_age_s=496 need_s=900
      2 trend=bullish skip=trend_immature trend_age_s=434 need_s=900
      2 trend=bullish skip=trend_immature trend_age_s=373 need_s=900
      2 trend=bullish skip=trend_immature trend_age_s=310 need_s=900
      2 trend=bullish skip=trend_immature trend_age_s=248 need_s=900
      2 trend=bullish skip=trend_immature trend_age_s=124 need_s=900
      2 trend=bullish skip=atr_low ratio=0.79 min=0.8
      2 trend=bullish skip=atr_low ratio=0.78 min=0.8
      2 trend=bullish skip=atr_low ratio=0.69 min=0.8
      2 trend=bullish skip=atr_low ratio=0.66 min=0.8
```

## Errors
```
none
```

## Last 100 Log Lines
```
  diag: trend=bullish atr_ratio=1.06 obs=11 obs_fresh=7 fvgs=14 bos=25 sigs=0 wrong_side=5 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=2 near_gap_pct=-0.082
[08:03:41] tick balance=$303.07
  diag: trend=bullish atr_ratio=1.06 obs=11 obs_fresh=7 fvgs=14 bos=26 sigs=0 wrong_side=5 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=2 near_gap_pct=-0.117
[08:04:43] tick balance=$304.45
  diag: trend=bullish atr_ratio=1.13 obs=11 obs_fresh=7 fvgs=14 bos=25 sigs=0 wrong_side=5 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=2 near_gap_pct=-0.072
[08:05:45] tick balance=$304.48
  diag: trend=bullish atr_ratio=1.09 obs=11 obs_fresh=7 fvgs=14 bos=24 sigs=0 wrong_side=5 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=2 near_gap_pct=-0.082
[08:06:50] tick balance=$305.14
  diag: trend=bullish atr_ratio=1.11 obs=12 obs_fresh=8 fvgs=14 bos=25 sigs=0 wrong_side=5 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=3 near_gap_pct=0.052
[08:07:52] tick balance=$305.51
  diag: trend=bullish atr_ratio=1.13 obs=12 obs_fresh=8 fvgs=14 bos=25 sigs=0 wrong_side=5 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=3 near_gap_pct=0.146
[08:08:55] tick balance=$305.27
  diag: trend=bullish atr_ratio=1.13 obs=12 obs_fresh=8 fvgs=14 bos=25 sigs=0 wrong_side=5 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=3 near_gap_pct=0.096
[08:09:58] tick balance=$305.01
  diag: trend=bullish atr_ratio=1.13 obs=12 obs_fresh=8 fvgs=14 bos=25 sigs=0 wrong_side=5 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=3 near_gap_pct=0.02
[08:11:01] tick balance=$304.92
  diag: trend=bullish atr_ratio=1.13 obs=12 obs_fresh=8 fvgs=15 bos=24 sigs=0 wrong_side=5 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=3 near_gap_pct=0.002
[08:12:04] tick balance=$304.09
  diag: trend=bullish atr_ratio=1.16 obs=12 obs_fresh=8 fvgs=14 bos=24 sigs=0 wrong_side=5 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=3 near_gap_pct=-0.169
[08:13:07] tick balance=$304.23
  diag: trend=bullish atr_ratio=1.16 obs=12 obs_fresh=8 fvgs=14 bos=24 sigs=0 wrong_side=5 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=3 near_gap_pct=-0.146
[08:14:11] tick balance=$305.12
  diag: trend=bullish atr_ratio=1.16 obs=12 obs_fresh=8 fvgs=14 bos=24 sigs=0 wrong_side=5 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=3 near_gap_pct=0.062
[08:15:14] tick balance=$304.09
  diag: trend=bullish atr_ratio=1.1 obs=11 obs_fresh=8 fvgs=13 bos=24 sigs=0 wrong_side=5 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=3 near_gap_pct=-0.149
[08:16:18] tick balance=$304.54
  diag: trend=bullish atr_ratio=1.11 obs=11 obs_fresh=8 fvgs=13 bos=24 sigs=0 wrong_side=5 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=3 near_gap_pct=-0.079
[08:17:21] tick balance=$304.68
  diag: trend=bullish atr_ratio=1.12 obs=11 obs_fresh=8 fvgs=13 bos=24 sigs=0 wrong_side=5 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=3 near_gap_pct=-0.037
[08:18:25] tick balance=$305.23
  diag: trend=bullish atr_ratio=1.14 obs=11 obs_fresh=8 fvgs=13 bos=22 sigs=0 wrong_side=5 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=3 near_gap_pct=0.087
[08:19:29] tick balance=$304.83
  diag: trend=bullish atr_ratio=1.14 obs=11 obs_fresh=8 fvgs=13 bos=22 sigs=0 wrong_side=5 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=3 near_gap_pct=-0.01
[08:20:32] tick balance=$304.91
  diag: trend=bullish atr_ratio=1.18 obs=11 obs_fresh=8 fvgs=12 bos=23 sigs=0 wrong_side=5 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=3 near_gap_pct=0.01
[08:21:36] tick balance=$304.50
  diag: trend=bullish atr_ratio=1.19 obs=11 obs_fresh=8 fvgs=12 bos=23 sigs=0 wrong_side=5 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=3 near_gap_pct=-0.109
[08:22:39] tick balance=$304.41
  diag: trend=bullish atr_ratio=1.19 obs=11 obs_fresh=8 fvgs=12 bos=23 sigs=0 wrong_side=5 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=3 near_gap_pct=-0.104
[08:23:42] tick balance=$304.53
  diag: trend=bullish atr_ratio=1.19 obs=11 obs_fresh=8 fvgs=12 bos=23 sigs=0 wrong_side=5 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=3 near_gap_pct=-0.089
[08:24:45] tick balance=$304.85
  diag: trend=bullish atr_ratio=1.19 obs=11 obs_fresh=8 fvgs=12 bos=23 sigs=0 wrong_side=5 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=3 near_gap_pct=0.0
[08:25:49] tick balance=$305.12
  diag: trend=bullish atr_ratio=1.12 obs=11 obs_fresh=8 fvgs=12 bos=23 sigs=0 wrong_side=5 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=3 near_gap_pct=0.057
[08:26:52] tick balance=$305.40
  diag: trend=bullish atr_ratio=1.13 obs=11 obs_fresh=8 fvgs=12 bos=23 sigs=0 wrong_side=5 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=3 near_gap_pct=0.143
[08:27:54] tick balance=$305.69
  diag: trend=bullish atr_ratio=1.14 obs=11 obs_fresh=8 fvgs=12 bos=23 sigs=0 wrong_side=5 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=3 near_gap_pct=0.188
[08:28:57] tick balance=$305.31
  diag: trend=bullish atr_ratio=1.14 obs=11 obs_fresh=8 fvgs=12 bos=23 sigs=0 wrong_side=5 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=3 near_gap_pct=0.089
[08:30:00] tick balance=$305.41
  diag: trend=bullish atr_ratio=1.08 obs=11 obs_fresh=8 fvgs=13 bos=24 sigs=0 wrong_side=5 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=3 near_gap_pct=0.148
[08:31:03] tick balance=$305.03
  diag: trend=bullish atr_ratio=1.1 obs=11 obs_fresh=8 fvgs=12 bos=24 sigs=0 wrong_side=5 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=3 near_gap_pct=0.03
[08:32:06] tick balance=$305.24
  diag: trend=bullish atr_ratio=1.1 obs=11 obs_fresh=8 fvgs=12 bos=24 sigs=0 wrong_side=5 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=3 near_gap_pct=0.069
[08:33:09] tick balance=$305.25
  diag: trend=bullish atr_ratio=1.1 obs=11 obs_fresh=8 fvgs=12 bos=24 sigs=0 wrong_side=5 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=3 near_gap_pct=0.089
[08:34:12] tick balance=$305.20
  diag: trend=bullish atr_ratio=1.11 obs=11 obs_fresh=8 fvgs=12 bos=24 sigs=0 wrong_side=5 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=3 near_gap_pct=0.064
[TG poll] err: 
[08:35:15] tick balance=$304.79
  diag: trend=bullish atr_ratio=1.08 obs=11 obs_fresh=8 fvgs=12 bos=24 sigs=0 wrong_side=5 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=3 near_gap_pct=-0.012
[08:36:18] tick balance=$304.74
  diag: trend=bullish atr_ratio=1.08 obs=11 obs_fresh=8 fvgs=12 bos=24 sigs=0 wrong_side=5 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=3 near_gap_pct=-0.047
[08:37:21] tick balance=$304.60
  diag: trend=bullish atr_ratio=1.08 obs=11 obs_fresh=8 fvgs=12 bos=24 sigs=0 wrong_side=5 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=3 near_gap_pct=-0.05
[08:38:24] tick balance=$304.78
  diag: trend=bullish atr_ratio=1.08 obs=11 obs_fresh=8 fvgs=12 bos=24 sigs=0 wrong_side=5 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=3 near_gap_pct=-0.015
[08:39:28] tick balance=$304.69
  diag: trend=bullish atr_ratio=1.08 obs=11 obs_fresh=8 fvgs=12 bos=24 sigs=0 wrong_side=5 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=3 near_gap_pct=-0.03
[08:40:31] tick balance=$304.86
  diag: trend=bullish atr_ratio=1.05 obs=11 obs_fresh=8 fvgs=12 bos=24 sigs=0 wrong_side=5 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=3 near_gap_pct=0.0
[08:41:34] tick balance=$304.73
  diag: trend=bullish atr_ratio=1.05 obs=11 obs_fresh=8 fvgs=12 bos=24 sigs=0 wrong_side=5 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=3 near_gap_pct=-0.025
[08:42:37] tick balance=$304.49
  diag: trend=bullish atr_ratio=1.06 obs=11 obs_fresh=8 fvgs=12 bos=24 sigs=0 wrong_side=5 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=3 near_gap_pct=-0.097
[08:43:40] tick balance=$305.06
  diag: trend=bullish atr_ratio=1.06 obs=11 obs_fresh=8 fvgs=12 bos=23 sigs=0 wrong_side=5 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=3 near_gap_pct=0.049
[08:44:43] tick balance=$304.80
  diag: trend=bullish atr_ratio=1.06 obs=11 obs_fresh=8 fvgs=12 bos=23 sigs=0 wrong_side=5 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=3 near_gap_pct=-0.01
[08:45:46] tick balance=$304.75
  diag: trend=bullish atr_ratio=1.03 obs=11 obs_fresh=8 fvgs=12 bos=24 sigs=0 wrong_side=5 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=3 near_gap_pct=-0.022
[08:46:50] tick balance=$304.60
  diag: trend=bullish atr_ratio=1.03 obs=11 obs_fresh=8 fvgs=12 bos=24 sigs=0 wrong_side=5 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=3 near_gap_pct=-0.054
[08:47:52] tick balance=$304.61
  diag: trend=bullish atr_ratio=1.04 obs=11 obs_fresh=8 fvgs=12 bos=24 sigs=0 wrong_side=5 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=3 near_gap_pct=-0.052
[08:48:55] tick balance=$304.89
  diag: trend=bullish atr_ratio=1.05 obs=12 obs_fresh=9 fvgs=12 bos=24 sigs=1 wrong_side=5 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=3 near_gap_pct=0.0 skip=side_busy open_sides=['BUY']
[08:49:59] tick balance=$305.07
  diag: trend=bullish atr_ratio=1.06 obs=12 obs_fresh=8 fvgs=12 bos=25 sigs=0 wrong_side=5 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=3 near_gap_pct=0.049
[08:51:02] tick balance=$305.62
  diag: trend=bullish atr_ratio=1.03 obs=13 obs_fresh=9 fvgs=12 bos=25 sigs=1 wrong_side=5 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=3 near_gap_pct=0.106 skip=side_busy open_sides=['BUY']
[08:52:05] tick balance=$305.14
  diag: trend=bullish atr_ratio=1.03 obs=12 obs_fresh=8 fvgs=12 bos=25 sigs=0 wrong_side=5 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=3 near_gap_pct=0.03
[08:53:08] tick balance=$305.12
  diag: trend=bullish atr_ratio=1.04 obs=12 obs_fresh=8 fvgs=12 bos=26 sigs=0 wrong_side=5 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=3 near_gap_pct=0.052
[08:54:11] tick balance=$305.30
  diag: trend=bullish atr_ratio=1.04 obs=13 obs_fresh=8 fvgs=12 bos=26 sigs=0 wrong_side=5 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=3 near_gap_pct=0.104
```
