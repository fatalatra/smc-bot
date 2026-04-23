# Bot Snapshot — 2026-04-23 06:55 UTC

## Service: active
balance=$305.94

## Config
POST_CLOSE_COOLDOWN: int = 180 # 3 мин техническая пауза после закрытия
RISK_PCT: float = 0.01 # 1% для старта на HYPE (вернём к 5% после 5+ сделок)
ADX_MIN: float = 20.0 # ADX < 20 → choppy market, skip entry

## Trades (last 20)
```
34|SELL|40.6|-4.03|closed|2026-04-23 04:06:08|2026-04-23 04:10:20
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
```

## Daily PnL
```
2026-04-23|313.19|-7.26|0
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
    116 trend_htf=ranging trend_mid=ranging skip=trend_mismatch
     13 trend=bearish skip=adx_low adx=20.0 min=20.0
     11 trend=bearish skip=adx_low adx=16.7 min=20.0
     11 trend=bearish skip=adx_low adx=14.9 min=20.0
      8 trend=bearish skip=adx_low adx=18.9 min=20.0
      5 trend=bullish skip=adx_low adx=17.0 min=20.0
      3 trend=bullish skip=adx_low adx=16.8 min=20.0
      3 trend=bullish skip=adx_low adx=16.7 min=20.0
      3 trend=bullish skip=adx_low adx=13.1 min=20.0
      3 trend=bearish skip=adx_low adx=19.3 min=20.0
      3 trend=bearish skip=adx_low adx=17.9 min=20.0
      3 trend=bearish skip=adx_low adx=14.7 min=20.0
      2 trend=bullish skip=adx_low adx=13.2 min=20.0
      2 trend=bearish skip=adx_low adx=19.8 min=20.0
      2 trend=bearish skip=adx_low adx=14.6 min=20.0
      2 trend=bearish skip=adx_low adx=14.5 min=20.0
      1 trend=bullish skip=trend_immature trend_age_s=870 need_s=900
      1 trend=bullish skip=trend_immature trend_age_s=809 need_s=900
      1 trend=bullish skip=trend_immature trend_age_s=746 need_s=900
      1 trend=bullish skip=trend_immature trend_age_s=62 need_s=900
```

## Errors
```
none
```

## Last 100 Log Lines
```
[08:03:21] tick balance=$305.94
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[08:04:24] tick balance=$305.94
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[08:05:26] tick balance=$305.94
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[08:06:28] tick balance=$305.94
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[08:07:30] tick balance=$305.94
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[08:08:33] tick balance=$305.94
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[08:09:37] tick balance=$305.94
  diag: trend=bullish skip=trend_immature trend_age_s=0 need_s=900
[08:10:39] tick balance=$305.94
  diag: trend=bullish skip=trend_immature trend_age_s=62 need_s=900
[08:11:42] tick balance=$305.94
  diag: trend=bullish skip=trend_immature trend_age_s=124 need_s=900
[08:12:44] tick balance=$305.94
  diag: trend=bullish skip=trend_immature trend_age_s=186 need_s=900
[08:13:45] tick balance=$305.94
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[08:14:47] tick balance=$305.94
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[08:15:50] tick balance=$305.94
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[08:16:52] tick balance=$305.94
  diag: trend=bullish skip=trend_immature trend_age_s=434 need_s=900
[08:17:54] tick balance=$305.94
  diag: trend=bullish skip=trend_immature trend_age_s=496 need_s=900
[08:18:56] tick balance=$305.94
  diag: trend=bullish skip=trend_immature trend_age_s=559 need_s=900
[08:19:58] tick balance=$305.94
  diag: trend=bullish skip=trend_immature trend_age_s=621 need_s=900
[08:21:01] tick balance=$305.94
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[08:22:04] tick balance=$305.94
  diag: trend=bullish skip=trend_immature trend_age_s=746 need_s=900
[08:23:06] tick balance=$305.94
  diag: trend=bullish skip=trend_immature trend_age_s=809 need_s=900
[08:24:08] tick balance=$305.94
  diag: trend=bullish skip=trend_immature trend_age_s=870 need_s=900
[08:25:10] tick balance=$305.94
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[08:26:12] tick balance=$305.94
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[08:27:14] tick balance=$305.94
  diag: trend=bullish skip=adx_low adx=13.2 min=20.0
[08:28:17] tick balance=$305.94
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[08:29:20] tick balance=$305.94
  diag: trend=bullish skip=adx_low adx=13.2 min=20.0
[08:30:22] tick balance=$305.94
  diag: trend=bullish skip=adx_low adx=13.1 min=20.0
[08:31:24] tick balance=$305.94
  diag: trend=bullish skip=adx_low adx=13.1 min=20.0
[08:32:26] tick balance=$305.94
  diag: trend=bullish skip=adx_low adx=13.1 min=20.0
[08:33:28] tick balance=$305.94
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[08:34:30] tick balance=$305.94
  diag: trend=bullish skip=adx_low adx=13.0 min=20.0
[08:35:32] tick balance=$305.94
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[08:36:35] tick balance=$305.94
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[08:37:36] tick balance=$305.94
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[08:38:39] tick balance=$305.94
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[08:39:42] tick balance=$305.94
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[08:40:44] tick balance=$305.94
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[08:41:46] tick balance=$305.94
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[08:42:48] tick balance=$305.94
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[08:43:50] tick balance=$305.94
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[08:44:53] tick balance=$305.94
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[08:45:55] tick balance=$305.94
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[08:46:57] tick balance=$305.94
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[08:48:00] tick balance=$305.94
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[08:49:02] tick balance=$305.94
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[08:50:05] tick balance=$305.94
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[08:51:06] tick balance=$305.94
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[08:52:09] tick balance=$305.94
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[08:53:11] tick balance=$305.94
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[08:54:14] tick balance=$305.94
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
```
