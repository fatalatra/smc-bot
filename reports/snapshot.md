# Bot Snapshot — 2026-04-19 22:55 UTC

## Service: active
balance=$312.71

## Config
POST_CLOSE_COOLDOWN: int = 180 # 3 мин техническая пауза после закрытия
RISK_PCT: float = 0.05 # 5% от баланса на сделку
ADX_MIN: float = 20.0 # ADX < 20 → choppy market, skip entry

## Trades (last 20)
```
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
9|BUY|74842.7|-22.95|closed|2026-04-14 15:24:35|2026-04-14 17:34:53
8|BUY|75630.3|-3.46|closed|2026-04-14 14:22:42|2026-04-14 15:00:43
```

## Daily PnL
```
2026-04-19|354.45|-41.74|0
2026-04-18|311.88|42.12|0
2026-04-17|328.7|-16.81|0
2026-04-16|381.29|-52.59|0
2026-04-15|363.1|17.9|0
2026-04-14|413.74|-50.64|0
2026-04-13|413.74|0.0|0
```

## Open Positions
```
none
```

## Diag Summary (last ~4h)
```
     10 trend=bearish skip=atr_low ratio=0.7 min=0.8
     10 trend=bearish skip=atr_low ratio=0.79 min=0.8
     10 trend=bearish skip=atr_low ratio=0.78 min=0.8
     10 trend=bearish skip=atr_low ratio=0.76 min=0.8
      7 trend=bearish skip=atr_low ratio=0.71 min=0.8
      6 trend=bearish skip=atr_low ratio=0.75 min=0.8
      5 trend=bearish skip=atr_low ratio=0.8 min=0.8
      5 trend=bearish skip=atr_low ratio=0.77 min=0.8
      4 trend=bearish skip=atr_low ratio=0.72 min=0.8
      3 trend=bearish skip=atr_low ratio=0.69 min=0.8
      3 trend=bearish skip=atr_low ratio=0.68 min=0.8
      2 trend=bearish skip=atr_low ratio=0.74 min=0.8
      2 trend=bearish skip=atr_low ratio=0.73 min=0.8
      1 trend=bearish skip=ema_overextended price=74153.0 ema20_h4=75390.0 dist=1237.0 max_dist=1201.5
      1 trend=bearish skip=ema_overextended price=74150.0 ema20_h4=75390.6 dist=1240.6 max_dist=1209.3
      1 trend=bearish skip=ema_overextended price=74131.5 ema20_h4=75390.0 dist=1258.5 max_dist=1214.5
      1 trend=bearish skip=ema_overextended price=74130.9 ema20_h4=75388.2 dist=1257.3 max_dist=1214.5
      1 trend=bearish skip=ema_overextended price=74127.8 ema20_h4=75388.1 dist=1260.3 max_dist=1214.5
      1 trend=bearish skip=ema_overextended price=74113.1 ema20_h4=75387.4 dist=1274.3 max_dist=1214.5
      1 trend=bearish skip=ema_overextended price=74113.0 ema20_h4=75387.4 dist=1274.4 max_dist=1209.3
```

## Errors
```
    self.gen.throw(typ, value, traceback)
  File "/root/smc-bot/venv/lib/python3.11/site-packages/httpcore/_exceptions.py", line 14, in map_exceptions
httpcore.ConnectError: [Errno -2] Name or service not known
The above exception was the direct cause of the following exception:
Traceback (most recent call last):
    with map_httpcore_exceptions():
    self.gen.throw(typ, value, traceback)
  File "/root/smc-bot/venv/lib/python3.11/site-packages/httpx/_transports/default.py", line 118, in map_httpcore_exceptions
httpx.ConnectError: [Errno -2] Name or service not known
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
[00:03:43] tick balance=$312.71
  diag: trend=bearish skip=ema_overextended price=74047.1 ema20_h4=75378.3 dist=1331.2 max_dist=1203.4
[00:04:44] tick balance=$312.71
  diag: trend=bearish skip=ema_overextended price=73862.9 ema20_h4=75360.7 dist=1497.8 max_dist=1204.1
[00:05:47] tick balance=$312.71
  diag: trend=bearish skip=ema_overextended price=73894.5 ema20_h4=75366.7 dist=1472.2 max_dist=1209.3
[00:06:49] tick balance=$312.71
  diag: trend=bearish skip=ema_overextended price=73994.1 ema20_h4=75376.9 dist=1382.8 max_dist=1209.3
[00:07:52] tick balance=$312.71
  diag: trend=bearish skip=ema_overextended price=74082.0 ema20_h4=75388.2 dist=1306.2 max_dist=1209.3
[00:08:54] tick balance=$312.71
  diag: trend=bearish skip=ema_overextended price=74075.4 ema20_h4=75384.5 dist=1309.1 max_dist=1209.3
[00:09:56] tick balance=$312.71
  diag: trend=bearish skip=ema_overextended price=74150.0 ema20_h4=75390.6 dist=1240.6 max_dist=1209.3
[00:10:59] tick balance=$312.71
  diag: trend=bearish skip=ema_overextended price=74113.0 ema20_h4=75387.4 dist=1274.4 max_dist=1209.3
[00:12:00] tick balance=$312.71
  diag: trend=bearish skip=ema_overextended price=73970.6 ema20_h4=75376.3 dist=1405.7 max_dist=1209.3
[00:13:03] tick balance=$312.71
  diag: trend=bearish skip=ema_overextended price=73984.7 ema20_h4=75376.5 dist=1391.8 max_dist=1209.3
[00:14:05] tick balance=$312.71
  diag: trend=bearish skip=ema_overextended price=74007.7 ema20_h4=75377.5 dist=1369.8 max_dist=1209.3
[00:15:07] tick balance=$312.71
  diag: trend=bearish skip=ema_overextended price=73952.6 ema20_h4=75372.7 dist=1420.1 max_dist=1209.3
[00:16:09] tick balance=$312.71
  diag: trend=bearish skip=ema_overextended price=73825.3 ema20_h4=75359.6 dist=1534.3 max_dist=1209.3
[00:17:11] tick balance=$312.71
  diag: trend=bearish skip=ema_overextended price=73939.9 ema20_h4=75371.5 dist=1431.6 max_dist=1209.3
[00:18:13] tick balance=$312.71
  diag: trend=bearish skip=ema_overextended price=73999.9 ema20_h4=75378.0 dist=1378.1 max_dist=1209.3
[00:19:16] tick balance=$312.71
  diag: trend=bearish skip=ema_overextended price=73962.3 ema20_h4=75374.6 dist=1412.3 max_dist=1209.3
[00:20:17] tick balance=$312.71
  diag: trend=bearish skip=ema_overextended price=73950.0 ema20_h4=75372.4 dist=1422.4 max_dist=1209.3
[00:21:19] tick balance=$312.71
  diag: trend=bearish skip=ema_overextended price=73808.9 ema20_h4=75356.5 dist=1547.6 max_dist=1209.3
[00:22:22] tick balance=$312.71
  diag: trend=bearish skip=ema_overextended price=73846.8 ema20_h4=75360.9 dist=1514.1 max_dist=1214.5
[00:23:24] tick balance=$312.71
  diag: trend=bearish skip=ema_overextended price=73748.8 ema20_h4=75354.3 dist=1605.5 max_dist=1214.5
[00:24:26] tick balance=$312.71
  diag: trend=bearish skip=ema_overextended price=73809.1 ema20_h4=75359.6 dist=1550.5 max_dist=1214.5
[00:25:27] tick balance=$312.71
  diag: trend=bearish skip=ema_overextended price=73866.0 ema20_h4=75364.7 dist=1498.7 max_dist=1214.5
[00:26:30] tick balance=$312.71
  diag: trend=bearish skip=ema_overextended price=73788.0 ema20_h4=75358.8 dist=1570.8 max_dist=1214.5
[00:27:32] tick balance=$312.71
  diag: trend=bearish skip=ema_overextended price=73867.7 ema20_h4=75364.6 dist=1496.9 max_dist=1214.5
[00:28:34] tick balance=$312.71
  diag: trend=bearish skip=ema_overextended price=73974.7 ema20_h4=75374.8 dist=1400.1 max_dist=1214.5
[00:29:36] tick balance=$312.71
  diag: trend=bearish skip=ema_overextended price=73970.5 ema20_h4=75373.7 dist=1403.2 max_dist=1214.5
[00:30:38] tick balance=$312.71
  diag: trend=bearish skip=ema_overextended price=73894.5 ema20_h4=75367.7 dist=1473.2 max_dist=1214.5
[00:31:40] tick balance=$312.71
  diag: trend=bearish skip=ema_overextended price=73956.3 ema20_h4=75373.1 dist=1416.8 max_dist=1214.5
[00:32:43] tick balance=$312.71
  diag: trend=bearish skip=ema_overextended price=74022.1 ema20_h4=75378.7 dist=1356.6 max_dist=1214.5
[00:33:45] tick balance=$312.71
  diag: trend=bearish skip=ema_overextended price=73989.2 ema20_h4=75373.3 dist=1384.1 max_dist=1214.5
[00:34:46] tick balance=$312.71
  diag: trend=bearish skip=ema_overextended price=74002.2 ema20_h4=75377.5 dist=1375.3 max_dist=1214.5
[00:35:48] tick balance=$312.71
  diag: trend=bearish skip=ema_overextended price=74034.4 ema20_h4=75380.5 dist=1346.1 max_dist=1214.5
[00:36:51] tick balance=$312.71
  diag: trend=bearish skip=ema_overextended price=74131.5 ema20_h4=75390.0 dist=1258.5 max_dist=1214.5
[00:37:53] tick balance=$312.71
  diag: trend=bearish skip=ema_overextended price=74070.1 ema20_h4=75384.2 dist=1314.1 max_dist=1214.5
[00:38:55] tick balance=$312.71
  diag: trend=bearish skip=ema_overextended price=74098.9 ema20_h4=75386.6 dist=1287.7 max_dist=1214.5
[00:39:57] tick balance=$312.71
  diag: trend=bearish skip=ema_overextended price=74059.0 ema20_h4=75383.5 dist=1324.5 max_dist=1214.5
[00:40:59] tick balance=$312.71
  diag: trend=bearish skip=ema_overextended price=74070.0 ema20_h4=75383.9 dist=1313.9 max_dist=1214.5
[00:42:01] tick balance=$312.71
  diag: trend=bearish skip=ema_overextended price=74107.3 ema20_h4=75387.5 dist=1280.2 max_dist=1214.5
[00:43:03] tick balance=$312.71
  diag: trend=bearish skip=ema_overextended price=74130.9 ema20_h4=75388.2 dist=1257.3 max_dist=1214.5
[00:44:05] tick balance=$312.71
  diag: trend=bearish skip=ema_overextended price=74081.3 ema20_h4=75385.0 dist=1303.7 max_dist=1214.5
[00:45:07] tick balance=$312.71
  diag: trend=bearish skip=ema_overextended price=74127.8 ema20_h4=75388.1 dist=1260.3 max_dist=1214.5
[00:46:11] tick balance=$312.71
  diag: trend=bearish skip=ema_overextended price=74077.0 ema20_h4=75384.5 dist=1307.5 max_dist=1214.5
[00:47:20] tick balance=$312.71
  diag: trend=bearish skip=ema_overextended price=74062.0 ema20_h4=75383.1 dist=1321.1 max_dist=1214.5
[00:48:22] tick balance=$312.71
  diag: trend=bearish skip=ema_overextended price=74059.1 ema20_h4=75382.9 dist=1323.8 max_dist=1214.5
[00:49:24] tick balance=$312.71
  diag: trend=bearish skip=ema_overextended price=74003.1 ema20_h4=75377.6 dist=1374.5 max_dist=1214.5
[00:50:26] tick balance=$312.71
  diag: trend=bearish skip=ema_overextended price=74064.8 ema20_h4=75383.6 dist=1318.8 max_dist=1214.5
[00:51:28] tick balance=$312.71
  diag: trend=bearish skip=ema_overextended price=74052.8 ema20_h4=75382.3 dist=1329.5 max_dist=1214.5
[00:52:31] tick balance=$312.71
  diag: trend=bearish skip=ema_overextended price=74113.1 ema20_h4=75387.4 dist=1274.3 max_dist=1214.5
[00:53:32] tick balance=$312.71
  diag: trend=bearish skip=ema_overextended price=74103.0 ema20_h4=75387.1 dist=1284.1 max_dist=1214.5
[00:54:35] tick balance=$312.71
  diag: trend=bearish skip=ema_overextended price=74078.0 ema20_h4=75384.7 dist=1306.7 max_dist=1214.5
```
