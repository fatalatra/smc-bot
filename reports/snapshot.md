# Bot Snapshot — 2026-04-22 14:55 UTC

## Service: active
balance=$313.19

## Config
POST_CLOSE_COOLDOWN: int = 180 # 3 мин техническая пауза после закрытия
RISK_PCT: float = 0.01 # 1% для старта на HYPE (вернём к 5% после 5+ сделок)
ADX_MIN: float = 20.0 # ADX < 20 → choppy market, skip entry

## Trades (last 20)
```
32|BUY|41.1|3.34|closed|2026-04-22 12:45:58|2026-04-22 13:48:02
31|BUY|40.4|4.57|closed|2026-04-22 05:23:43|2026-04-22 10:32:03
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
```

## Daily PnL
```
2026-04-22|301.06|12.14|0
2026-04-21|296.96|4.1|0
2026-04-20|312.71|-15.75|0
2026-04-19|354.45|-41.74|0
2026-04-18|311.88|42.12|0
2026-04-17|328.7|-16.81|0
2026-04-16|381.29|-52.59|0
```

## Open Positions
```
none
```

## Diag Summary (last ~4h)
```
     72 trend_htf=ranging trend_mid=ranging skip=trend_mismatch
      3 trend=bullish atr_ratio=1.02 obs=7 obs_fresh=1 fvgs=8 bos=27 sigs=0 wrong_side=1 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=0
      2 trend=bullish atr_ratio=1.26 obs=8 obs_fresh=2 fvgs=7 bos=27 sigs=0 wrong_side=2 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=0
      2 trend=bullish atr_ratio=1.06 obs=7 obs_fresh=1 fvgs=7 bos=27 sigs=0 wrong_side=1 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=0
      2 trend=bullish atr_ratio=1.06 obs=7 obs_fresh=1 fvgs=6 bos=28 sigs=0 wrong_side=1 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=0
      2 trend=bullish atr_ratio=1.06 obs=7 obs_fresh=1 fvgs=6 bos=27 sigs=0 wrong_side=1 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=0
      2 err=no_data
      1 trend=bullish atr_ratio=1.35 obs=12 obs_fresh=11 fvgs=9 bos=25 sigs=0 wrong_side=5 price_out=6 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=0.88
      1 trend=bullish atr_ratio=1.35 obs=12 obs_fresh=11 fvgs=9 bos=25 sigs=0 wrong_side=5 price_out=6 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=0.873
      1 trend=bullish atr_ratio=1.34 obs=12 obs_fresh=11 fvgs=9 bos=25 sigs=0 wrong_side=5 price_out=6 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=0.848
      1 trend=bullish atr_ratio=1.33 obs=12 obs_fresh=12 fvgs=9 bos=26 sigs=1 wrong_side=4 price_out=6 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=-0.142 skip=low_score score=0.7
      1 trend=bullish atr_ratio=1.33 obs=12 obs_fresh=11 fvgs=9 bos=26 sigs=0 wrong_side=5 price_out=6 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=0.887
      1 trend=bullish atr_ratio=1.29 obs=8 obs_fresh=2 fvgs=6 bos=26 sigs=0 wrong_side=2 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=0
      1 trend=bullish atr_ratio=1.28 obs=8 obs_fresh=2 fvgs=6 bos=26 sigs=0 wrong_side=2 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=0
      1 trend=bullish atr_ratio=1.26 obs=8 obs_fresh=2 fvgs=6 bos=26 sigs=0 wrong_side=2 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=0
      1 trend=bullish atr_ratio=1.26 obs=14 obs_fresh=11 fvgs=10 bos=24 sigs=0 wrong_side=5 price_out=6 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=1.165
      1 trend=bullish atr_ratio=1.26 obs=14 obs_fresh=11 fvgs=10 bos=24 sigs=0 wrong_side=5 price_out=6 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=1.158
      1 trend=bullish atr_ratio=1.26 obs=14 obs_fresh=11 fvgs=10 bos=23 sigs=0 wrong_side=5 price_out=6 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=1.16
      1 trend=bullish atr_ratio=1.26 obs=12 obs_fresh=11 fvgs=9 bos=25 sigs=0 wrong_side=5 price_out=6 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=0.819
      1 trend=bullish atr_ratio=1.26 obs=12 obs_fresh=11 fvgs=9 bos=25 sigs=0 wrong_side=5 price_out=6 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=0.805
```

## Errors
```
none
```

## Last 100 Log Lines
```
[16:04:38] tick balance=$313.19
  diag: trend=bullish atr_ratio=1.04 obs=8 obs_fresh=2 fvgs=8 bos=25 sigs=0 wrong_side=1 price_out=1 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=1.8
[16:05:40] tick balance=$313.19
  diag: trend=bullish atr_ratio=1.05 obs=8 obs_fresh=2 fvgs=8 bos=25 sigs=0 wrong_side=1 price_out=1 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=1.588
[16:06:42] tick balance=$313.19
  diag: trend=bullish atr_ratio=1.08 obs=8 obs_fresh=2 fvgs=8 bos=25 sigs=0 wrong_side=1 price_out=1 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=1.655
[16:07:44] tick balance=$313.19
  diag: trend=bullish atr_ratio=1.09 obs=8 obs_fresh=2 fvgs=8 bos=25 sigs=0 wrong_side=1 price_out=1 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=1.817
[16:08:46] tick balance=$313.19
  diag: trend=bullish atr_ratio=1.1 obs=8 obs_fresh=2 fvgs=8 bos=25 sigs=0 wrong_side=1 price_out=1 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=1.729
[16:09:48] tick balance=$313.19
  diag: trend=bullish atr_ratio=1.1 obs=8 obs_fresh=2 fvgs=8 bos=25 sigs=0 wrong_side=1 price_out=1 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=1.776
[16:10:50] tick balance=$313.19
  diag: trend=bullish atr_ratio=1.01 obs=8 obs_fresh=2 fvgs=8 bos=26 sigs=0 wrong_side=1 price_out=1 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=1.817
[16:11:52] tick balance=$313.19
  diag: trend=bullish atr_ratio=1.03 obs=8 obs_fresh=2 fvgs=8 bos=26 sigs=0 wrong_side=1 price_out=1 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=1.876
[16:12:54] tick balance=$313.19
  diag: trend=bullish atr_ratio=1.03 obs=8 obs_fresh=2 fvgs=8 bos=26 sigs=0 wrong_side=1 price_out=1 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=1.874
[16:13:56] tick balance=$313.19
  diag: trend=bullish atr_ratio=1.03 obs=8 obs_fresh=2 fvgs=8 bos=27 sigs=0 wrong_side=1 price_out=1 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=1.874
[16:14:58] tick balance=$313.19
  diag: trend=bullish atr_ratio=1.03 obs=8 obs_fresh=2 fvgs=8 bos=27 sigs=0 wrong_side=1 price_out=1 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=1.902
[16:16:00] tick balance=$313.19
  diag: trend=bullish atr_ratio=1.02 obs=7 obs_fresh=1 fvgs=8 bos=27 sigs=0 wrong_side=1 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=0
[16:17:02] tick balance=$313.19
  diag: trend=bullish atr_ratio=1.02 obs=7 obs_fresh=1 fvgs=8 bos=27 sigs=0 wrong_side=1 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=0
[16:18:04] tick balance=$313.19
  diag: trend=bullish atr_ratio=1.02 obs=7 obs_fresh=1 fvgs=8 bos=27 sigs=0 wrong_side=1 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=0
[16:19:06] tick balance=$313.19
  diag: trend=bullish atr_ratio=1.05 obs=7 obs_fresh=1 fvgs=8 bos=26 sigs=0 wrong_side=1 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=0
[16:20:08] tick balance=$313.19
  diag: trend=bullish atr_ratio=1.02 obs=7 obs_fresh=1 fvgs=8 bos=26 sigs=0 wrong_side=1 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=0
[16:21:11] tick balance=$313.19
  diag: trend=bullish atr_ratio=1.03 obs=8 obs_fresh=2 fvgs=8 bos=27 sigs=0 wrong_side=2 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=0
[16:22:13] tick balance=$313.19
  diag: trend=bullish atr_ratio=1.03 obs=7 obs_fresh=1 fvgs=8 bos=27 sigs=0 wrong_side=1 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=0
[16:23:15] tick balance=$313.19
  diag: trend=bullish atr_ratio=1.06 obs=7 obs_fresh=1 fvgs=7 bos=27 sigs=0 wrong_side=1 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=0
[16:24:18] tick balance=$313.19
  diag: trend=bullish atr_ratio=1.06 obs=7 obs_fresh=1 fvgs=7 bos=27 sigs=0 wrong_side=1 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=0
[16:25:20] tick balance=$313.19
  diag: trend=bullish atr_ratio=1.01 obs=7 obs_fresh=1 fvgs=6 bos=27 sigs=0 wrong_side=1 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=0
[16:26:23] tick balance=$313.19
  diag: trend=bullish atr_ratio=1.06 obs=7 obs_fresh=1 fvgs=6 bos=27 sigs=0 wrong_side=1 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=0
[16:27:25] tick balance=$313.19
  diag: trend=bullish atr_ratio=1.06 obs=7 obs_fresh=1 fvgs=6 bos=27 sigs=0 wrong_side=1 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=0
[16:28:27] tick balance=$313.19
  diag: trend=bullish atr_ratio=1.06 obs=7 obs_fresh=1 fvgs=6 bos=28 sigs=0 wrong_side=1 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=0
[16:29:29] tick balance=$313.19
  diag: trend=bullish atr_ratio=1.06 obs=7 obs_fresh=1 fvgs=6 bos=28 sigs=0 wrong_side=1 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=0
[16:30:31] tick balance=$313.19
[!] No data, skipping...
  diag: err=no_data
[16:31:33] tick balance=$313.19
  diag: trend=bullish atr_ratio=1.07 obs=7 obs_fresh=1 fvgs=6 bos=27 sigs=0 wrong_side=1 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=0
[16:32:36] tick balance=$313.19
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[16:33:38] tick balance=$313.19
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[16:34:40] tick balance=$313.19
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[16:35:43] tick balance=$313.19
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[16:36:45] tick balance=$313.19
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[16:37:47] tick balance=$313.19
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[16:38:49] tick balance=$313.19
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[16:39:56] tick balance=$313.19
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[16:40:58] tick balance=$313.19
  diag: trend=bullish atr_ratio=1.15 obs=8 obs_fresh=2 fvgs=6 bos=28 sigs=0 wrong_side=2 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=0
[16:42:00] tick balance=$313.19
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[16:43:03] tick balance=$313.19
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[16:44:05] tick balance=$313.19
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[16:45:06] tick balance=$313.19
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[16:46:08] tick balance=$313.19
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[16:47:10] tick balance=$313.19
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[16:48:12] tick balance=$313.19
  diag: trend=bullish atr_ratio=1.19 obs=8 obs_fresh=2 fvgs=6 bos=26 sigs=0 wrong_side=2 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=0
[16:49:13] tick balance=$313.19
  diag: trend=bullish atr_ratio=1.26 obs=8 obs_fresh=2 fvgs=6 bos=26 sigs=0 wrong_side=2 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=0
[16:50:15] tick balance=$313.19
[!] No data, skipping...
  diag: err=no_data
[16:51:17] tick balance=$313.19
  diag: trend=bullish atr_ratio=1.26 obs=8 obs_fresh=2 fvgs=7 bos=27 sigs=0 wrong_side=2 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=0
[16:52:20] tick balance=$313.19
  diag: trend=bullish atr_ratio=1.26 obs=8 obs_fresh=2 fvgs=7 bos=27 sigs=0 wrong_side=2 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=0
[16:53:23] tick balance=$313.19
  diag: trend=bullish atr_ratio=1.28 obs=8 obs_fresh=2 fvgs=6 bos=26 sigs=0 wrong_side=2 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=0
[16:54:24] tick balance=$313.19
  diag: trend=bullish atr_ratio=1.29 obs=8 obs_fresh=2 fvgs=6 bos=26 sigs=0 wrong_side=2 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=0
```
