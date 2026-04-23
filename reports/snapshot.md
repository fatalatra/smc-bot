# Bot Snapshot — 2026-04-23 02:55 UTC

## Service: active
balance=$309.15

## Config
POST_CLOSE_COOLDOWN: int = 180 # 3 мин техническая пауза после закрытия
RISK_PCT: float = 0.01 # 1% для старта на HYPE (вернём к 5% после 5+ сделок)
ADX_MIN: float = 20.0 # ADX < 20 → choppy market, skip entry

## Trades (last 20)
```
33|BUY|41.2|-5.49|closed|2026-04-23 00:03:56|2026-04-23 00:10:14
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
```

## Daily PnL
```
2026-04-23|313.19|-4.05|0
2026-04-22|301.06|12.14|0
2026-04-21|296.96|4.1|0
2026-04-20|312.71|-15.75|0
2026-04-19|354.45|-41.74|0
2026-04-18|311.88|42.12|0
2026-04-17|328.7|-16.81|0
```

## Open Positions
```
none
```

## Diag Summary (last ~4h)
```
     97 trend_htf=ranging trend_mid=ranging skip=trend_mismatch
     11 trend=bullish skip=adx_low adx=18.6 min=20.0
     10 trend=bullish skip=adx_low adx=16.9 min=20.0
      9 trend=bullish skip=adx_low adx=17.4 min=20.0
      9 trend=bullish skip=adx_low adx=16.5 min=20.0
      8 trend=bullish skip=adx_low adx=19.8 min=20.0
      4 trend=bullish skip=adx_low adx=17.6 min=20.0
      3 trend=bullish skip=adx_low adx=18.4 min=20.0
      3 trend=bullish skip=adx_low adx=17.0 min=20.0
      3 trend=bullish skip=adx_low adx=16.6 min=20.0
      2 trend=bullish skip=adx_low adx=16.7 min=20.0
      2 trend=bullish atr_ratio=1.31 obs=10 obs_fresh=8 fvgs=12 bos=27 sigs=0 wrong_side=4 price_out=2 bos_miss=2 risk_neg=0 liquidity_trap=0 near_gap_pct=0.38
      2 trend=bullish atr_ratio=1.2 obs=12 obs_fresh=10 fvgs=14 bos=27 sigs=0 wrong_side=5 price_out=1 bos_miss=4 risk_neg=0 liquidity_trap=0 near_gap_pct=0.046
      2 trend=bullish atr_ratio=1.22 obs=11 obs_fresh=9 fvgs=13 bos=28 sigs=0 wrong_side=5 price_out=0 bos_miss=4 risk_neg=0 liquidity_trap=0 near_gap_pct=-0.156
      1 trend=bullish skip=adx_low adx=17.5 min=20.0
      1 trend=bullish skip=adx_low adx=17.1 min=20.0
      1 trend=bullish skip=adx_low adx=16.3 min=20.0
      1 trend=bullish atr_ratio=1.3 obs=11 obs_fresh=9 fvgs=12 bos=27 sigs=0 wrong_side=4 price_out=3 bos_miss=2 risk_neg=0 liquidity_trap=0 near_gap_pct=0.452
      1 trend=bullish atr_ratio=1.38 obs=11 obs_fresh=9 fvgs=12 bos=29 sigs=0 wrong_side=4 price_out=1 bos_miss=4 risk_neg=0 liquidity_trap=0 near_gap_pct=0.112
      1 trend=bullish atr_ratio=1.38 obs=11 obs_fresh=9 fvgs=12 bos=28 sigs=0 wrong_side=4 price_out=0 bos_miss=5 risk_neg=0 liquidity_trap=0 near_gap_pct=-0.1
```

## Errors
```
none
```

## Last 100 Log Lines
```
[04:04:09] tick balance=$309.15
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[04:05:11] tick balance=$309.15
  diag: trend=bullish skip=adx_low adx=16.9 min=20.0
[04:06:12] tick balance=$309.15
  diag: trend=bullish skip=adx_low adx=16.9 min=20.0
[04:07:15] tick balance=$309.15
  diag: trend=bullish skip=adx_low adx=16.9 min=20.0
[04:08:17] tick balance=$309.15
  diag: trend=bullish skip=adx_low adx=16.9 min=20.0
[04:09:19] tick balance=$309.15
  diag: trend=bullish skip=adx_low adx=16.9 min=20.0
[04:10:21] tick balance=$309.15
  diag: trend=bullish skip=adx_low adx=16.9 min=20.0
[04:11:24] tick balance=$309.15
  diag: trend=bullish skip=adx_low adx=16.9 min=20.0
[04:12:26] tick balance=$309.15
  diag: trend=bullish skip=adx_low adx=16.9 min=20.0
[04:13:28] tick balance=$309.15
  diag: trend=bullish skip=adx_low adx=16.9 min=20.0
[04:14:30] tick balance=$309.15
  diag: trend=bullish skip=adx_low adx=16.9 min=20.0
[04:15:31] tick balance=$309.15
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[04:16:33] tick balance=$309.15
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[04:17:36] tick balance=$309.15
  diag: trend=bullish skip=adx_low adx=16.5 min=20.0
[04:18:37] tick balance=$309.15
  diag: trend=bullish skip=adx_low adx=16.5 min=20.0
[04:19:39] tick balance=$309.15
  diag: trend=bullish skip=adx_low adx=16.5 min=20.0
[04:20:41] tick balance=$309.15
  diag: trend=bullish skip=adx_low adx=16.5 min=20.0
[04:21:43] tick balance=$309.15
  diag: trend=bullish skip=adx_low adx=16.5 min=20.0
[04:22:44] tick balance=$309.15
  diag: trend=bullish skip=adx_low adx=16.5 min=20.0
[04:23:46] tick balance=$309.15
  diag: trend=bullish skip=adx_low adx=16.5 min=20.0
[04:24:48] tick balance=$309.15
  diag: trend=bullish skip=adx_low adx=16.5 min=20.0
[04:25:49] tick balance=$309.15
  diag: trend=bullish skip=adx_low adx=16.6 min=20.0
[04:26:51] tick balance=$309.15
  diag: trend=bullish skip=adx_low adx=16.6 min=20.0
[04:27:52] tick balance=$309.15
  diag: trend=bullish skip=adx_low adx=16.6 min=20.0
[04:28:54] tick balance=$309.15
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[04:29:56] tick balance=$309.15
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[04:30:58] tick balance=$309.15
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[04:32:00] tick balance=$309.15
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[04:33:02] tick balance=$309.15
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[04:34:03] tick balance=$309.15
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[04:35:05] tick balance=$309.15
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[04:36:07] tick balance=$309.15
  diag: trend=bullish skip=adx_low adx=16.7 min=20.0
[04:37:08] tick balance=$309.15
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[04:38:10] tick balance=$309.15
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[04:39:12] tick balance=$309.15
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[04:40:14] tick balance=$309.15
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[04:41:16] tick balance=$309.15
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[04:42:18] tick balance=$309.15
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[04:43:20] tick balance=$309.15
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[04:44:22] tick balance=$309.15
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[04:45:24] tick balance=$309.15
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[04:46:26] tick balance=$309.15
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[04:47:28] tick balance=$309.15
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[04:48:30] tick balance=$309.15
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[04:49:32] tick balance=$309.15
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[04:50:34] tick balance=$309.15
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[04:51:36] tick balance=$309.15
  diag: trend=bullish skip=adx_low adx=17.1 min=20.0
[04:52:37] tick balance=$309.15
  diag: trend=bullish skip=adx_low adx=17.0 min=20.0
[04:53:39] tick balance=$309.15
  diag: trend=bullish skip=adx_low adx=17.0 min=20.0
[04:54:41] tick balance=$309.15
  diag: trend=bullish skip=adx_low adx=17.0 min=20.0
```
