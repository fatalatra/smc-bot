# Bot Snapshot — 2026-04-18 02:55 UTC

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
      2 trend=bullish skip=ema_overextended price=77227.2 ema20_h4=75382.5 dist=1844.7 max_dist=1544.7
      2 trend=bullish skip=ema_overextended price=77203.8 ema20_h4=75380.3 dist=1823.5 max_dist=1544.7
      2 trend=bullish skip=ema_overextended price=77180.1 ema20_h4=75378.1 dist=1802.0 max_dist=1544.7
      2 trend=bullish skip=ema_overextended price=77130.3 ema20_h4=75373.3 dist=1757.0 max_dist=1544.7
      1 trend=bullish skip=ema_overextended price=77381.2 ema20_h4=75221.8 dist=2159.4 max_dist=1643.0
      1 trend=bullish skip=ema_overextended price=77344.1 ema20_h4=75218.6 dist=2125.5 max_dist=1643.0
      1 trend=bullish skip=ema_overextended price=77343.6 ema20_h4=75393.6 dist=1950.0 max_dist=1551.4
      1 trend=bullish skip=ema_overextended price=77340.4 ema20_h4=75392.8 dist=1947.6 max_dist=1554.8
      1 trend=bullish skip=ema_overextended price=77333.4 ema20_h4=75217.2 dist=2116.2 max_dist=1643.0
      1 trend=bullish skip=ema_overextended price=77332.1 ema20_h4=75392.6 dist=1939.5 max_dist=1554.8
      1 trend=bullish skip=ema_overextended price=77330.6 ema20_h4=75217.0 dist=2113.6 max_dist=1643.0
      1 trend=bullish skip=ema_overextended price=77329.4 ema20_h4=75392.3 dist=1937.1 max_dist=1549.2
      1 trend=bullish skip=ema_overextended price=77326.3 ema20_h4=75216.5 dist=2109.8 max_dist=1643.0
      1 trend=bullish skip=ema_overextended price=77325.3 ema20_h4=75391.7 dist=1933.6 max_dist=1554.8
      1 trend=bullish skip=ema_overextended price=77324.1 ema20_h4=75391.0 dist=1933.1 max_dist=1549.1
      1 trend=bullish skip=ema_overextended price=77320.1 ema20_h4=75390.6 dist=1929.5 max_dist=1549.0
      1 trend=bullish skip=ema_overextended price=77319.0 ema20_h4=75215.9 dist=2103.1 max_dist=1643.0
      1 trend=bullish skip=ema_overextended price=77317.6 ema20_h4=75391.0 dist=1926.6 max_dist=1549.0
      1 trend=bullish skip=ema_overextended price=77317.3 ema20_h4=75215.7 dist=2101.6 max_dist=1643.0
      1 trend=bullish skip=ema_overextended price=77316.0 ema20_h4=75390.9 dist=1925.1 max_dist=1554.8
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
[04:03:49] tick balance=$311.88
  diag: trend=bullish skip=ema_overextended price=77088.9 ema20_h4=75369.4 dist=1719.5 max_dist=1544.7
[04:04:51] tick balance=$311.88
  diag: trend=bullish skip=ema_overextended price=77122.3 ema20_h4=75372.6 dist=1749.7 max_dist=1544.7
[04:05:53] tick balance=$311.88
  diag: trend=bullish skip=ema_overextended price=77151.6 ema20_h4=75375.4 dist=1776.2 max_dist=1544.7
[04:06:56] tick balance=$311.88
  diag: trend=bullish skip=ema_overextended price=77130.3 ema20_h4=75373.3 dist=1757.0 max_dist=1544.7
[04:07:58] tick balance=$311.88
  diag: trend=bullish skip=ema_overextended price=77149.6 ema20_h4=75375.7 dist=1773.9 max_dist=1544.7
[04:08:59] tick balance=$311.88
  diag: trend=bullish skip=ema_overextended price=77214.1 ema20_h4=75381.3 dist=1832.8 max_dist=1544.7
[04:10:01] tick balance=$311.88
  diag: trend=bullish skip=ema_overextended price=77196.4 ema20_h4=75378.9 dist=1817.5 max_dist=1544.7
[04:11:03] tick balance=$311.88
  diag: trend=bullish skip=ema_overextended price=77199.1 ema20_h4=75381.0 dist=1818.1 max_dist=1544.7
[04:12:06] tick balance=$311.88
  diag: trend=bullish skip=ema_overextended price=77194.5 ema20_h4=75379.4 dist=1815.1 max_dist=1544.7
[04:13:08] tick balance=$311.88
  diag: trend=bullish skip=ema_overextended price=77196.1 ema20_h4=75379.6 dist=1816.5 max_dist=1544.7
[04:14:10] tick balance=$311.88
  diag: trend=bullish skip=ema_overextended price=77197.3 ema20_h4=75379.7 dist=1817.6 max_dist=1544.7
[04:15:12] tick balance=$311.88
  diag: trend=bullish skip=ema_overextended price=77246.4 ema20_h4=75384.8 dist=1861.6 max_dist=1544.7
[04:16:15] tick balance=$311.88
  diag: trend=bullish skip=ema_overextended price=77320.1 ema20_h4=75390.6 dist=1929.5 max_dist=1549.0
[04:17:17] tick balance=$311.88
  diag: trend=bullish skip=ema_overextended price=77317.6 ema20_h4=75391.0 dist=1926.6 max_dist=1549.0
[04:18:19] tick balance=$311.88
  diag: trend=bullish skip=ema_overextended price=77310.1 ema20_h4=75390.4 dist=1919.7 max_dist=1549.0
[04:19:21] tick balance=$311.88
  diag: trend=bullish skip=ema_overextended price=77315.7 ema20_h4=75391.0 dist=1924.7 max_dist=1549.1
[04:20:23] tick balance=$311.88
  diag: trend=bullish skip=ema_overextended price=77324.1 ema20_h4=75391.0 dist=1933.1 max_dist=1549.1
[04:21:25] tick balance=$311.88
  diag: trend=bullish skip=ema_overextended price=77288.0 ema20_h4=75388.5 dist=1899.5 max_dist=1549.1
[04:22:28] tick balance=$311.88
  diag: trend=bullish skip=ema_overextended price=77329.4 ema20_h4=75392.3 dist=1937.1 max_dist=1549.2
[04:23:30] tick balance=$311.88
  diag: trend=bullish skip=ema_overextended price=77343.6 ema20_h4=75393.6 dist=1950.0 max_dist=1551.4
[04:24:32] tick balance=$311.88
  diag: trend=bullish skip=ema_overextended price=77295.0 ema20_h4=75389.0 dist=1906.0 max_dist=1554.8
[04:25:35] tick balance=$311.88
  diag: trend=bullish skip=ema_overextended price=77293.9 ema20_h4=75388.9 dist=1905.0 max_dist=1554.8
[04:26:37] tick balance=$311.88
  diag: trend=bullish skip=ema_overextended price=77286.4 ema20_h4=75388.7 dist=1897.7 max_dist=1554.8
[04:27:39] tick balance=$311.88
  diag: trend=bullish skip=ema_overextended price=77314.6 ema20_h4=75390.8 dist=1923.8 max_dist=1554.8
[04:28:41] tick balance=$311.88
  diag: trend=bullish skip=ema_overextended price=77293.0 ema20_h4=75388.8 dist=1904.2 max_dist=1554.8
[04:29:43] tick balance=$311.88
  diag: trend=bullish skip=ema_overextended price=77277.2 ema20_h4=75387.3 dist=1889.9 max_dist=1554.8
[04:30:45] tick balance=$311.88
  diag: trend=bullish skip=ema_overextended price=77250.0 ema20_h4=75385.2 dist=1864.8 max_dist=1554.8
[04:31:46] tick balance=$311.88
  diag: trend=bullish skip=ema_overextended price=77233.5 ema20_h4=75383.2 dist=1850.3 max_dist=1554.8
[04:32:49] tick balance=$311.88
  diag: trend=bullish skip=ema_overextended price=77225.9 ema20_h4=75382.8 dist=1843.1 max_dist=1554.8
[04:33:52] tick balance=$311.88
  diag: trend=bullish skip=ema_overextended price=77252.8 ema20_h4=75384.9 dist=1867.9 max_dist=1554.8
[04:34:54] tick balance=$311.88
  diag: trend=bullish skip=ema_overextended price=77234.1 ema20_h4=75383.2 dist=1850.9 max_dist=1554.8
[04:35:57] tick balance=$311.88
  diag: trend=bullish skip=ema_overextended price=77221.0 ema20_h4=75382.0 dist=1839.0 max_dist=1554.8
[04:36:59] tick balance=$311.88
  diag: trend=bullish skip=ema_overextended price=77236.0 ema20_h4=75383.4 dist=1852.6 max_dist=1554.8
[04:38:02] tick balance=$311.88
  diag: trend=bullish skip=ema_overextended price=77316.0 ema20_h4=75390.9 dist=1925.1 max_dist=1554.8
[04:39:04] tick balance=$311.88
  diag: trend=bullish skip=ema_overextended price=77325.3 ema20_h4=75391.7 dist=1933.6 max_dist=1554.8
[04:40:06] tick balance=$311.88
  diag: trend=bullish skip=ema_overextended price=77315.1 ema20_h4=75390.9 dist=1924.2 max_dist=1554.8
[04:41:09] tick balance=$311.88
  diag: trend=bullish skip=ema_overextended price=77299.1 ema20_h4=75389.4 dist=1909.7 max_dist=1554.8
[04:42:11] tick balance=$311.88
  diag: trend=bullish skip=ema_overextended price=77332.1 ema20_h4=75392.6 dist=1939.5 max_dist=1554.8
[04:43:13] tick balance=$311.88
  diag: trend=bullish skip=ema_overextended price=77340.4 ema20_h4=75392.8 dist=1947.6 max_dist=1554.8
[04:44:15] tick balance=$311.88
  diag: trend=bullish skip=ema_overextended price=77259.5 ema20_h4=75385.6 dist=1873.9 max_dist=1554.8
[04:45:17] tick balance=$311.88
  diag: trend=bullish skip=ema_overextended price=77272.7 ema20_h4=75386.9 dist=1885.8 max_dist=1554.8
[04:46:20] tick balance=$311.88
  diag: trend=bullish skip=ema_overextended price=77273.5 ema20_h4=75387.0 dist=1886.5 max_dist=1554.8
[04:47:22] tick balance=$311.88
  diag: trend=bullish skip=ema_overextended price=77287.5 ema20_h4=75388.3 dist=1899.2 max_dist=1554.8
[04:48:24] tick balance=$311.88
  diag: trend=bullish skip=ema_overextended price=77294.6 ema20_h4=75389.0 dist=1905.6 max_dist=1554.8
[04:49:27] tick balance=$311.88
  diag: trend=bullish skip=ema_overextended price=77258.1 ema20_h4=75385.5 dist=1872.6 max_dist=1554.8
[04:50:29] tick balance=$311.88
  diag: trend=bullish skip=ema_overextended price=77250.1 ema20_h4=75384.7 dist=1865.4 max_dist=1554.8
[04:51:31] tick balance=$311.88
  diag: trend=bullish skip=ema_overextended price=77252.9 ema20_h4=75385.0 dist=1867.9 max_dist=1554.8
[04:52:33] tick balance=$311.88
  diag: trend=bullish skip=ema_overextended price=77238.0 ema20_h4=75383.6 dist=1854.4 max_dist=1554.8
[04:53:35] tick balance=$311.88
  diag: trend=bullish skip=ema_overextended price=77243.2 ema20_h4=75384.1 dist=1859.1 max_dist=1554.8
[04:54:37] tick balance=$311.88
  diag: trend=bullish skip=ema_overextended price=77243.3 ema20_h4=75384.1 dist=1859.2 max_dist=1554.8
```
