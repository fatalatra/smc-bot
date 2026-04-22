# Bot Snapshot — 2026-04-22 10:55 UTC

## Service: active
balance=$309.45

## Config
POST_CLOSE_COOLDOWN: int = 180 # 3 мин техническая пауза после закрытия
RISK_PCT: float = 0.01 # 1% для старта на HYPE (вернём к 5% после 5+ сделок)
ADX_MIN: float = 20.0 # ADX < 20 → choppy market, skip entry

## Trades (last 20)
```
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
12|SELL|73899.1|39.1|closed|2026-04-15 06:09:07|2026-04-15 07:46:09
```

## Daily PnL
```
2026-04-22|301.06|8.39|0
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
    178 trend_htf=ranging trend_mid=ranging skip=trend_mismatch
      5 trend=bullish skip=atr_low ratio=0.7 min=0.8
      4 trend=bullish skip=atr_low ratio=0.78 min=0.8
      4 trend=bullish skip=atr_low ratio=0.74 min=0.8
      3 trend=bullish skip=atr_low ratio=0.79 min=0.8
      3 trend=bullish skip=atr_low ratio=0.77 min=0.8
      3 trend=bullish skip=atr_low ratio=0.72 min=0.8
      3 trend=bullish skip=atr_low ratio=0.68 min=0.8
      2 trend=bullish skip=atr_low ratio=0.73 min=0.8
      1 trend=bullish skip=atr_low ratio=0.8 min=0.8
      1 trend=bullish skip=atr_low ratio=0.76 min=0.8
      1 trend=bullish skip=atr_low ratio=0.75 min=0.8
      1 trend=bullish skip=atr_low ratio=0.69 min=0.8
      1 trend=bullish atr_ratio=1.06 obs=12 obs_fresh=8 fvgs=12 bos=25 sigs=0 wrong_side=5 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=3 near_gap_pct=0.049
      1 trend=bullish atr_ratio=1.06 obs=11 obs_fresh=8 fvgs=12 bos=23 sigs=0 wrong_side=5 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=3 near_gap_pct=0.049
      1 trend=bullish atr_ratio=1.06 obs=11 obs_fresh=8 fvgs=12 bos=23 sigs=0 wrong_side=5 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=3 near_gap_pct=-0.01
      1 trend=bullish atr_ratio=1.05 obs=12 obs_fresh=9 fvgs=12 bos=24 sigs=1 wrong_side=5 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=3 near_gap_pct=0.0 skip=side_busy open_sides=['BUY']
      1 trend=bullish atr_ratio=1.04 obs=13 obs_fresh=8 fvgs=12 bos=26 sigs=0 wrong_side=5 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=3 near_gap_pct=0.104
      1 trend=bullish atr_ratio=1.04 obs=12 obs_fresh=8 fvgs=12 bos=26 sigs=0 wrong_side=5 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=3 near_gap_pct=0.052
      1 trend=bullish atr_ratio=1.04 obs=11 obs_fresh=8 fvgs=12 bos=24 sigs=0 wrong_side=5 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=3 near_gap_pct=-0.052
```

## Errors
```
none
```

## Last 100 Log Lines
```
[12:08:55] tick balance=$306.04
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[12:09:59] tick balance=$305.47
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[12:11:01] tick balance=$306.37
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[12:12:04] tick balance=$306.29
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[12:13:07] tick balance=$306.23
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[TG poll] err: 
[12:14:10] tick balance=$306.02
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[12:15:13] tick balance=$306.28
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[12:16:16] tick balance=$306.57
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[12:17:19] tick balance=$306.64
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[12:18:23] tick balance=$306.85
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[12:19:25] tick balance=$307.01
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[12:20:29] tick balance=$307.23
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[12:21:32] tick balance=$307.38
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[12:22:34] tick balance=$307.83
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[12:23:37] tick balance=$307.60
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[12:24:39] tick balance=$307.82
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[12:25:42] tick balance=$307.93
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[12:26:46] tick balance=$307.93
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[12:27:49] tick balance=$308.09
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[12:28:53] tick balance=$308.26
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[12:29:56] tick balance=$308.44
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[12:30:59] tick balance=$309.32
[change_stop_loss] id=500219749 new_sl=45.4 tp_preserved=None resp={'success': True, 'code': 0}
🔄 <b>Breakeven LONG</b>
Entry: <b>$40.4</b>
New SL: <b>$45.4</b>
TP: <b>$41.1</b>
Progress: <b>61%</b> to TP
Price: <b>$40.8</b>
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[12:32:03] tick balance=$309.45
[sync] trade #31 BUY entry=40.4 closed (manual) at price=40.802
[real_pnl] trade #31: profit=4.93 open_fee=-0.18 close_fee=-0.18 => net=4.57
  diag: skip=post_close_cooldown wait_s=177
[12:33:07] tick balance=$309.45
  diag: skip=post_close_cooldown wait_s=115
[12:34:09] tick balance=$309.45
  diag: skip=post_close_cooldown wait_s=53
[12:35:12] tick balance=$309.45
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[12:36:14] tick balance=$309.45
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[12:37:17] tick balance=$309.45
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[12:38:19] tick balance=$309.45
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[12:39:21] tick balance=$309.45
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[12:40:23] tick balance=$309.45
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[12:41:26] tick balance=$309.45
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[12:42:28] tick balance=$309.45
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[12:43:29] tick balance=$309.45
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[12:44:31] tick balance=$309.45
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[12:45:34] tick balance=$309.45
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[12:46:36] tick balance=$309.45
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[12:47:38] tick balance=$309.45
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[12:48:41] tick balance=$309.45
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[12:49:43] tick balance=$309.45
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[12:50:45] tick balance=$309.45
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[12:51:48] tick balance=$309.45
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[12:52:50] tick balance=$309.45
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[12:53:52] tick balance=$309.45
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[12:54:55] tick balance=$309.45
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
```
