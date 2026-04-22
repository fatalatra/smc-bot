# Bot Snapshot — 2026-04-22 02:55 UTC

## Service: active
balance=$301.06

## Config
POST_CLOSE_COOLDOWN: int = 180 # 3 мин техническая пауза после закрытия
RISK_PCT: float = 0.01 # 1% для старта на HYPE (вернём к 5% после 5+ сделок)
ADX_MIN: float = 20.0 # ADX < 20 → choppy market, skip entry

## Trades (last 20)
```
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
11|BUY|74056.1|-3.16|closed|2026-04-14 19:38:54|2026-04-14 21:21:29
10|BUY|74270.7|-18.86|closed|2026-04-14 19:08:32|2026-04-14 19:33:51
```

## Daily PnL
```
2026-04-22|301.06|0.0|0
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
     33 trend=bearish skip=ema_overextended price=39.8 ema20_h4=41.2 dist=1.4 max_dist=1.4
     27 trend_htf=ranging trend_mid=ranging skip=trend_mismatch
     21 trend=bearish skip=ema_overextended price=39.8 ema20_h4=41.2 dist=1.4 max_dist=1.3
     21 trend=bearish skip=ema_overextended price=39.7 ema20_h4=41.2 dist=1.5 max_dist=1.4
     18 trend=bearish skip=ema_overextended price=39.7 ema20_h4=41.3 dist=1.7 max_dist=1.5
     15 trend=bearish skip=ema_overextended price=39.5 ema20_h4=41.3 dist=1.8 max_dist=1.5
     11 trend=bearish skip=ema_overextended price=39.7 ema20_h4=41.4 dist=1.6 max_dist=1.5
      7 trend=bearish skip=ema_overextended price=39.8 ema20_h4=41.4 dist=1.6 max_dist=1.5
      5 trend=bearish skip=ema_overextended price=39.7 ema20_h4=41.2 dist=1.5 max_dist=1.3
      5 trend=bearish skip=ema_overextended price=39.6 ema20_h4=41.2 dist=1.6 max_dist=1.4
      4 trend=bearish skip=ema_overextended price=39.6 ema20_h4=41.3 dist=1.7 max_dist=1.5
      3 trend=bearish skip=ema_overextended price=39.9 ema20_h4=41.2 dist=1.4 max_dist=1.4
      3 trend=bearish skip=ema_overextended price=39.8 ema20_h4=41.4 dist=1.5 max_dist=1.5
      3 trend=bearish skip=ema_overextended price=39.8 ema20_h4=41.2 dist=1.5 max_dist=1.4
      3 trend=bearish skip=ema_overextended price=39.6 ema20_h4=41.3 dist=1.8 max_dist=1.5
      3 trend=bearish skip=ema_overextended price=39.5 ema20_h4=41.3 dist=1.9 max_dist=1.5
      2 trend=bearish skip=ema_overextended price=39.7 ema20_h4=41.3 dist=1.6 max_dist=1.5
      2 trend=bearish skip=atr_low ratio=0.76 min=0.8
      2 trend=bearish skip=atr_low ratio=0.74 min=0.8
      1 trend=bullish skip=trend_immature trend_age_s=62 need_s=900
```

## Errors
```
none
```

## Last 100 Log Lines
```
  diag: trend=bearish skip=ema_overextended price=39.8 ema20_h4=41.2 dist=1.4 max_dist=1.4
[04:04:58] tick balance=$301.06
  diag: trend=bearish skip=ema_overextended price=39.8 ema20_h4=41.2 dist=1.4 max_dist=1.4
[04:05:59] tick balance=$301.06
  diag: trend=bearish skip=ema_overextended price=39.8 ema20_h4=41.2 dist=1.4 max_dist=1.4
[04:07:01] tick balance=$301.06
  diag: trend=bearish skip=ema_overextended price=39.8 ema20_h4=41.2 dist=1.4 max_dist=1.4
[04:08:04] tick balance=$301.06
  diag: trend=bearish skip=ema_overextended price=39.8 ema20_h4=41.2 dist=1.4 max_dist=1.4
[04:09:06] tick balance=$301.06
  diag: trend=bearish skip=ema_overextended price=39.8 ema20_h4=41.2 dist=1.4 max_dist=1.4
[04:10:07] tick balance=$301.06
  diag: trend=bearish skip=ema_overextended price=39.8 ema20_h4=41.2 dist=1.4 max_dist=1.4
[04:11:09] tick balance=$301.06
  diag: trend=bearish atr_ratio=0.95 obs=11 obs_fresh=10 fvgs=10 bos=24 sigs=0 wrong_side=5 price_out=3 bos_miss=0 risk_neg=0 liquidity_trap=2 near_gap_pct=-0.085
[04:12:11] tick balance=$301.06
  diag: trend=bearish atr_ratio=0.98 obs=11 obs_fresh=10 fvgs=10 bos=23 sigs=0 wrong_side=5 price_out=4 bos_miss=0 risk_neg=0 liquidity_trap=1 near_gap_pct=-0.22
[04:13:13] tick balance=$301.06
  diag: trend=bearish atr_ratio=1.01 obs=11 obs_fresh=10 fvgs=10 bos=23 sigs=0 wrong_side=5 price_out=4 bos_miss=0 risk_neg=0 liquidity_trap=1 near_gap_pct=-0.307
[04:14:15] tick balance=$301.06
  diag: trend=bearish atr_ratio=1.01 obs=11 obs_fresh=10 fvgs=10 bos=24 sigs=0 wrong_side=5 price_out=4 bos_miss=0 risk_neg=0 liquidity_trap=1 near_gap_pct=-0.208
[04:15:17] tick balance=$301.06
  diag: trend=bearish atr_ratio=1.01 obs=11 obs_fresh=10 fvgs=11 bos=23 sigs=0 wrong_side=5 price_out=4 bos_miss=0 risk_neg=0 liquidity_trap=1 near_gap_pct=-0.263
[04:16:18] tick balance=$301.06
  diag: trend=bearish atr_ratio=1.02 obs=11 obs_fresh=10 fvgs=11 bos=23 sigs=0 wrong_side=5 price_out=3 bos_miss=0 risk_neg=0 liquidity_trap=2 near_gap_pct=-0.133
[04:17:21] tick balance=$301.06
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[04:18:22] tick balance=$301.06
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[04:19:24] tick balance=$301.06
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[04:20:26] tick balance=$301.06
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[04:21:29] tick balance=$301.06
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[04:22:32] tick balance=$301.06
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[04:23:33] tick balance=$301.06
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[04:24:35] tick balance=$301.06
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[04:25:37] tick balance=$301.06
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[04:26:39] tick balance=$301.06
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[04:27:41] tick balance=$301.06
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[04:28:43] tick balance=$301.06
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[04:29:44] tick balance=$301.06
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[04:30:46] tick balance=$301.06
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[04:31:48] tick balance=$301.06
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[04:32:51] tick balance=$301.06
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[04:33:54] tick balance=$301.06
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[04:34:55] tick balance=$301.06
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[04:35:57] tick balance=$301.06
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[04:37:00] tick balance=$301.06
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[04:38:02] tick balance=$301.06
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[04:39:05] tick balance=$301.06
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[04:40:07] tick balance=$301.06
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[04:41:10] tick balance=$301.06
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[TG poll] err: 
[04:42:12] tick balance=$301.06
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[04:43:14] tick balance=$301.06
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[04:44:16] tick balance=$301.06
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[04:45:19] tick balance=$301.06
  diag: trend=bullish skip=trend_immature trend_age_s=0 need_s=900
[04:46:21] tick balance=$301.06
  diag: trend=bullish skip=trend_immature trend_age_s=62 need_s=900
[04:47:23] tick balance=$301.06
  diag: trend=bullish skip=trend_immature trend_age_s=124 need_s=900
[04:48:26] tick balance=$301.06
  diag: trend=bullish skip=trend_immature trend_age_s=186 need_s=900
[04:49:27] tick balance=$301.06
  diag: trend=bullish skip=trend_immature trend_age_s=248 need_s=900
[04:50:30] tick balance=$301.06
  diag: trend=bullish skip=trend_immature trend_age_s=310 need_s=900
[04:51:32] tick balance=$301.06
  diag: trend=bullish skip=trend_immature trend_age_s=373 need_s=900
[04:52:34] tick balance=$301.06
  diag: trend=bullish skip=trend_immature trend_age_s=434 need_s=900
[04:53:36] tick balance=$301.06
  diag: trend=bullish skip=trend_immature trend_age_s=496 need_s=900
[04:54:38] tick balance=$301.06
  diag: trend=bullish skip=trend_immature trend_age_s=558 need_s=900
```
