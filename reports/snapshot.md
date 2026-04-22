# Bot Snapshot — 2026-04-22 18:55 UTC

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
    209 trend_htf=ranging trend_mid=ranging skip=trend_mismatch
      3 trend=bullish skip=atr_low ratio=0.8 min=0.8
      2 trend=bullish atr_ratio=1.26 obs=8 obs_fresh=2 fvgs=7 bos=27 sigs=0 wrong_side=2 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=0
      2 trend=bullish atr_ratio=1.23 obs=8 obs_fresh=2 fvgs=6 bos=27 sigs=0 wrong_side=2 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=0
      2 trend=bullish atr_ratio=0.85 obs=9 obs_fresh=4 fvgs=7 bos=29 sigs=0 wrong_side=4 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=0
      2 err=no_data
      1 trend=bullish skip=atr_low ratio=0.79 min=0.8
      1 trend=bullish atr_ratio=1.29 obs=8 obs_fresh=2 fvgs=6 bos=26 sigs=0 wrong_side=2 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=0
      1 trend=bullish atr_ratio=1.28 obs=8 obs_fresh=2 fvgs=6 bos=26 sigs=0 wrong_side=2 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=0
      1 trend=bullish atr_ratio=1.26 obs=8 obs_fresh=2 fvgs=6 bos=26 sigs=0 wrong_side=2 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=0
      1 trend=bullish atr_ratio=1.22 obs=8 obs_fresh=2 fvgs=6 bos=26 sigs=0 wrong_side=2 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=0
      1 trend=bullish atr_ratio=1.22 obs=7 obs_fresh=2 fvgs=6 bos=27 sigs=0 wrong_side=2 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=0
      1 trend=bullish atr_ratio=1.21 obs=8 obs_fresh=2 fvgs=6 bos=26 sigs=0 wrong_side=2 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=0
      1 trend=bullish atr_ratio=1.19 obs=8 obs_fresh=2 fvgs=6 bos=26 sigs=0 wrong_side=2 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=0
      1 trend=bullish atr_ratio=0.8 obs=9 obs_fresh=4 fvgs=8 bos=29 sigs=0 wrong_side=4 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=0
      1 trend=bullish atr_ratio=0.87 obs=10 obs_fresh=6 fvgs=7 bos=27 sigs=1 wrong_side=2 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=0.046 skip=low_score score=0.7
      1 trend=bullish atr_ratio=0.86 obs=9 obs_fresh=4 fvgs=7 bos=29 sigs=0 wrong_side=4 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=0
      1 trend=bullish atr_ratio=0.85 obs=9 obs_fresh=6 fvgs=7 bos=27 sigs=1 wrong_side=2 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=0.002 skip=low_score score=0.7
      1 trend=bullish atr_ratio=0.85 obs=9 obs_fresh=4 fvgs=7 bos=30 sigs=0 wrong_side=4 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=0
      1 trend=bullish atr_ratio=0.84 obs=9 obs_fresh=4 fvgs=7 bos=30 sigs=0 wrong_side=4 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=0
```

## Errors
```
none
```

## Last 100 Log Lines
```
[20:04:15] tick balance=$313.19
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:05:17] tick balance=$313.19
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:06:20] tick balance=$313.19
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:07:22] tick balance=$313.19
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:08:24] tick balance=$313.19
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:09:26] tick balance=$313.19
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:10:29] tick balance=$313.19
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:11:31] tick balance=$313.19
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:12:33] tick balance=$313.19
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:13:36] tick balance=$313.19
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:14:38] tick balance=$313.19
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:15:41] tick balance=$313.19
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:16:43] tick balance=$313.19
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:17:45] tick balance=$313.19
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:18:47] tick balance=$313.19
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:19:49] tick balance=$313.19
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:20:52] tick balance=$313.19
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:21:54] tick balance=$313.19
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:22:56] tick balance=$313.19
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:23:58] tick balance=$313.19
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:25:00] tick balance=$313.19
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:26:02] tick balance=$313.19
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:27:04] tick balance=$313.19
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:28:06] tick balance=$313.19
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:29:08] tick balance=$313.19
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:30:10] tick balance=$313.19
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:31:12] tick balance=$313.19
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:32:14] tick balance=$313.19
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:33:16] tick balance=$313.19
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:34:18] tick balance=$313.19
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:35:20] tick balance=$313.19
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:36:22] tick balance=$313.19
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:37:24] tick balance=$313.19
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:38:26] tick balance=$313.19
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:39:29] tick balance=$313.19
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:40:31] tick balance=$313.19
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:41:33] tick balance=$313.19
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:42:35] tick balance=$313.19
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:43:36] tick balance=$313.19
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:44:38] tick balance=$313.19
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:45:40] tick balance=$313.19
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:46:43] tick balance=$313.19
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:47:45] tick balance=$313.19
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:48:47] tick balance=$313.19
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:49:49] tick balance=$313.19
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:50:51] tick balance=$313.19
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:51:53] tick balance=$313.19
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:52:55] tick balance=$313.19
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:53:57] tick balance=$313.19
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:54:59] tick balance=$313.19
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
```
