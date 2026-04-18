# Bot Snapshot — 2026-04-18 06:55 UTC

## Service: active
balance=$311.88

## Config
POST_CLOSE_COOLDOWN: int = 180 # 3 мин техническая пауза после закрытия
RISK_PCT: float = 0.05 # 5% от баланса на сделку
ADX_MIN: float = 20.0 # ADX < 20 → choppy market, skip entry

## Trades (last 20)
```
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
9|BUY|74842.7|-22.95|closed|2026-04-14 15:24:35|2026-04-14 17:34:53
8|BUY|75630.3|-3.46|closed|2026-04-14 14:22:42|2026-04-14 15:00:43
7|SELL|70843.3|-11.35|closed|2026-04-12 15:59:14|2026-04-12 17:51:45
6|SELL|70977.6|16.89|closed|2026-04-12 13:15:20|2026-04-12 14:43:04
5|SELL|71364.3|13.27|closed|2026-04-12 10:57:04|2026-04-12 13:01:46
4|SELL|71492.1|13.27|closed|2026-04-12 10:41:17|2026-04-12 10:42:19
3|SELL|71597.7|13.27|closed|2026-04-12 10:25:37|2026-04-12 10:42:19
```

## Daily PnL
```
2026-04-18|311.88|0.0|0
2026-04-17|328.7|-16.81|0
2026-04-16|381.29|-52.59|0
2026-04-15|363.1|17.9|0
2026-04-14|413.74|-50.64|0
2026-04-13|413.74|0.0|0
2026-04-12|423.86|-10.12|0
```

## Open Positions
```
none
```

## Diag Summary (last ~4h)
```
    111 trend_htf=ranging trend_mid=ranging skip=trend_mismatch
      2 trend=bullish atr_ratio=1.06 obs=10 obs_fresh=10 fvgs=10 bos=30 sigs=0 wrong_side=5 price_out=2 bos_miss=3 risk_neg=0 liquidity_trap=0 near_gap_pct=-0.048
      1 trend=bullish skip=ema_overextended price=77294.6 ema20_h4=75389.0 dist=1905.6 max_dist=1554.8
      1 trend=bullish skip=ema_overextended price=77287.5 ema20_h4=75388.3 dist=1899.2 max_dist=1554.8
      1 trend=bullish skip=ema_overextended price=77270.0 ema20_h4=75386.6 dist=1883.4 max_dist=1554.8
      1 trend=bullish skip=ema_overextended price=77260.0 ema20_h4=75385.7 dist=1874.3 max_dist=1554.8
      1 trend=bullish skip=ema_overextended price=77258.1 ema20_h4=75385.5 dist=1872.6 max_dist=1554.8
      1 trend=bullish skip=ema_overextended price=77254.8 ema20_h4=75385.2 dist=1869.6 max_dist=1554.8
      1 trend=bullish skip=ema_overextended price=77254.5 ema20_h4=75385.2 dist=1869.3 max_dist=1554.8
      1 trend=bullish skip=ema_overextended price=77252.9 ema20_h4=75385.0 dist=1867.9 max_dist=1554.8
      1 trend=bullish skip=ema_overextended price=77252.8 ema20_h4=75385.0 dist=1867.8 max_dist=1554.8
      1 trend=bullish skip=ema_overextended price=77250.1 ema20_h4=75384.7 dist=1865.4 max_dist=1554.8
      1 trend=bullish skip=ema_overextended price=77249.7 ema20_h4=75384.1 dist=1865.6 max_dist=1554.8
      1 trend=bullish skip=ema_overextended price=77244.3 ema20_h4=75384.2 dist=1860.1 max_dist=1554.8
      1 trend=bullish skip=ema_overextended price=77244.2 ema20_h4=75384.2 dist=1860.0 max_dist=1554.8
      1 trend=bullish skip=ema_overextended price=77243.7 ema20_h4=75384.1 dist=1859.6 max_dist=1554.8
      1 trend=bullish skip=ema_overextended price=77243.3 ema20_h4=75384.2 dist=1859.1 max_dist=1554.8
      1 trend=bullish skip=ema_overextended price=77243.3 ema20_h4=75384.1 dist=1859.2 max_dist=1554.8
      1 trend=bullish skip=ema_overextended price=77243.2 ema20_h4=75384.1 dist=1859.1 max_dist=1554.8
      1 trend=bullish skip=ema_overextended price=77238.6 ema20_h4=75383.6 dist=1855.0 max_dist=1554.8
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
[08:04:07] tick balance=$311.88
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[08:05:09] tick balance=$311.88
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[08:06:12] tick balance=$311.88
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[08:07:14] tick balance=$311.88
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[08:08:16] tick balance=$311.88
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[08:09:18] tick balance=$311.88
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[08:10:20] tick balance=$311.88
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[08:11:23] tick balance=$311.88
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[08:12:26] tick balance=$311.88
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[08:13:28] tick balance=$311.88
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[08:14:30] tick balance=$311.88
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[08:15:34] tick balance=$311.88
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[08:16:36] tick balance=$311.88
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[08:17:38] tick balance=$311.88
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[08:18:40] tick balance=$311.88
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[08:19:42] tick balance=$311.88
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[08:20:44] tick balance=$311.88
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[08:21:45] tick balance=$311.88
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[08:22:47] tick balance=$311.88
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[08:23:50] tick balance=$311.88
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[08:24:52] tick balance=$311.88
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[08:25:54] tick balance=$311.88
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[08:26:57] tick balance=$311.88
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[08:27:59] tick balance=$311.88
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[08:29:01] tick balance=$311.88
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[08:30:03] tick balance=$311.88
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[08:31:05] tick balance=$311.88
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[08:32:07] tick balance=$311.88
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[08:33:09] tick balance=$311.88
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[08:34:12] tick balance=$311.88
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[08:35:14] tick balance=$311.88
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[08:36:16] tick balance=$311.88
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[08:37:18] tick balance=$311.88
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[08:38:21] tick balance=$311.88
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[08:39:23] tick balance=$311.88
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[08:40:25] tick balance=$311.88
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[08:41:28] tick balance=$311.88
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[08:42:30] tick balance=$311.88
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[08:43:32] tick balance=$311.88
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[08:44:35] tick balance=$311.88
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[08:45:37] tick balance=$311.88
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[08:46:40] tick balance=$311.88
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[08:47:42] tick balance=$311.88
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[08:48:43] tick balance=$311.88
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[08:49:46] tick balance=$311.88
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[08:50:48] tick balance=$311.88
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[08:51:50] tick balance=$311.88
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[08:52:52] tick balance=$311.88
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[08:53:54] tick balance=$311.88
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[08:54:56] tick balance=$311.88
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
```
