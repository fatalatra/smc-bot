# Bot Snapshot — 2026-04-17 22:55 UTC

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
2026-04-17|328.7|-16.81|0
2026-04-16|381.29|-52.59|0
2026-04-15|363.1|17.9|0
2026-04-14|413.74|-50.64|0
2026-04-13|413.74|0.0|0
2026-04-12|423.86|-10.12|0
2026-04-11|457.33|-130.15|0
```

## Open Positions
```
none
```

## Diag Summary (last ~4h)
```
      2 trend=bullish skip=trend_immature trend_age_s=871 need_s=900
      2 trend=bullish skip=trend_immature trend_age_s=746 need_s=900
      2 trend=bullish skip=trend_immature trend_age_s=621 need_s=900
      2 trend=bullish skip=trend_immature trend_age_s=61 need_s=900
      2 trend=bullish skip=trend_immature trend_age_s=559 need_s=900
      2 trend=bullish skip=trend_immature trend_age_s=496 need_s=900
      2 trend=bullish skip=trend_immature trend_age_s=434 need_s=900
      2 trend=bullish skip=trend_immature trend_age_s=310 need_s=900
      2 trend=bullish skip=trend_immature trend_age_s=248 need_s=900
      2 trend=bullish skip=trend_immature trend_age_s=0 need_s=900
      2 trend=bullish skip=ema_overextended price=77330.6 ema20_h4=75217.0 dist=2113.6 max_dist=1643.0
      1 trend=bullish skip=trend_immature trend_age_s=809 need_s=900
      1 trend=bullish skip=trend_immature trend_age_s=808 need_s=900
      1 trend=bullish skip=trend_immature trend_age_s=684 need_s=900
      1 trend=bullish skip=trend_immature trend_age_s=683 need_s=900
      1 trend=bullish skip=trend_immature trend_age_s=372 need_s=900
      1 trend=bullish skip=trend_immature trend_age_s=371 need_s=900
      1 trend=bullish skip=trend_immature trend_age_s=186 need_s=900
      1 trend=bullish skip=trend_immature trend_age_s=185 need_s=900
      1 trend=bullish skip=trend_immature trend_age_s=124 need_s=900
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
[00:03:26] tick balance=$311.88
  diag: trend=bullish skip=ema_overextended price=77390.5 ema20_h4=75222.7 dist=2167.8 max_dist=1643.0
[00:04:29] tick balance=$311.88
  diag: trend=bullish skip=ema_overextended price=77440.0 ema20_h4=75227.9 dist=2212.1 max_dist=1643.0
[00:05:31] tick balance=$311.88
  diag: trend=bullish skip=ema_overextended price=77445.0 ema20_h4=75227.8 dist=2217.2 max_dist=1643.0
[00:06:32] tick balance=$311.88
  diag: trend=bullish skip=ema_overextended price=77449.9 ema20_h4=75228.3 dist=2221.6 max_dist=1643.0
[00:07:34] tick balance=$311.88
  diag: trend=bullish skip=ema_overextended price=77431.8 ema20_h4=75226.6 dist=2205.2 max_dist=1643.0
[00:08:36] tick balance=$311.88
  diag: trend=bullish skip=ema_overextended price=77452.5 ema20_h4=75228.6 dist=2223.9 max_dist=1643.0
[00:09:38] tick balance=$311.88
  diag: trend=bullish skip=ema_overextended price=77449.8 ema20_h4=75228.3 dist=2221.5 max_dist=1643.0
[00:10:41] tick balance=$311.88
  diag: trend=bullish skip=ema_overextended price=77451.5 ema20_h4=75228.5 dist=2223.0 max_dist=1643.0
[00:11:43] tick balance=$311.88
  diag: trend=bullish skip=ema_overextended price=77428.3 ema20_h4=75226.3 dist=2202.0 max_dist=1643.0
[00:12:46] tick balance=$311.88
  diag: trend=bullish skip=ema_overextended price=77471.8 ema20_h4=75230.4 dist=2241.4 max_dist=1643.0
[00:13:48] tick balance=$311.88
  diag: trend=bullish skip=ema_overextended price=77458.0 ema20_h4=75229.1 dist=2228.9 max_dist=1643.0
[00:14:51] tick balance=$311.88
  diag: trend=bullish skip=ema_overextended price=77457.1 ema20_h4=75222.1 dist=2235.0 max_dist=1643.0
[00:15:53] tick balance=$311.88
  diag: trend=bullish skip=ema_overextended price=77309.1 ema20_h4=75216.1 dist=2093.0 max_dist=1643.0
[00:16:55] tick balance=$311.88
  diag: trend=bullish skip=ema_overextended price=77352.0 ema20_h4=75219.0 dist=2133.0 max_dist=1643.0
[00:17:58] tick balance=$311.88
  diag: trend=bullish skip=ema_overextended price=77324.9 ema20_h4=75216.7 dist=2108.2 max_dist=1643.0
[00:19:00] tick balance=$311.88
  diag: trend=bullish skip=ema_overextended price=77304.2 ema20_h4=75214.4 dist=2089.8 max_dist=1643.0
[00:20:02] tick balance=$311.88
  diag: trend=bullish skip=ema_overextended price=77316.9 ema20_h4=75215.6 dist=2101.3 max_dist=1643.0
[00:21:05] tick balance=$311.88
  diag: trend=bullish skip=ema_overextended price=77343.0 ema20_h4=75218.1 dist=2124.9 max_dist=1643.0
[00:22:07] tick balance=$311.88
  diag: trend=bullish skip=ema_overextended price=77324.9 ema20_h4=75217.4 dist=2107.5 max_dist=1643.0
[00:23:09] tick balance=$311.88
  diag: trend=bullish skip=ema_overextended price=77364.7 ema20_h4=75220.2 dist=2144.5 max_dist=1643.0
[00:24:12] tick balance=$311.88
  diag: trend=bullish skip=ema_overextended price=77364.1 ema20_h4=75220.1 dist=2144.0 max_dist=1643.0
[00:25:14] tick balance=$311.88
  diag: trend=bullish skip=ema_overextended price=77337.7 ema20_h4=75217.4 dist=2120.3 max_dist=1643.0
[00:26:16] tick balance=$311.88
  diag: trend=bullish skip=ema_overextended price=77343.6 ema20_h4=75218.2 dist=2125.4 max_dist=1643.0
[00:27:19] tick balance=$311.88
  diag: trend=bullish skip=ema_overextended price=77363.1 ema20_h4=75220.1 dist=2143.0 max_dist=1643.0
[00:28:21] tick balance=$311.88
  diag: trend=bullish skip=ema_overextended price=77383.0 ema20_h4=75222.1 dist=2160.9 max_dist=1643.0
[00:29:23] tick balance=$311.88
  diag: trend=bullish skip=ema_overextended price=77355.6 ema20_h4=75219.4 dist=2136.2 max_dist=1643.0
[00:30:25] tick balance=$311.88
  diag: trend=bullish skip=ema_overextended price=77326.0 ema20_h4=75216.4 dist=2109.6 max_dist=1643.0
[00:31:27] tick balance=$311.88
  diag: trend=bullish skip=ema_overextended price=77350.1 ema20_h4=75217.7 dist=2132.4 max_dist=1643.0
[00:32:30] tick balance=$311.88
  diag: trend=bullish skip=ema_overextended price=77344.8 ema20_h4=75218.3 dist=2126.5 max_dist=1643.0
[00:33:32] tick balance=$311.88
  diag: trend=bullish skip=ema_overextended price=77388.3 ema20_h4=75223.6 dist=2164.7 max_dist=1643.0
[00:34:35] tick balance=$311.88
  diag: trend=bullish skip=ema_overextended price=77428.6 ema20_h4=75226.3 dist=2202.3 max_dist=1643.0
[00:35:37] tick balance=$311.88
  diag: trend=bullish skip=ema_overextended price=77424.8 ema20_h4=75225.2 dist=2199.6 max_dist=1643.0
[00:36:38] tick balance=$311.88
  diag: trend=bullish skip=ema_overextended price=77401.4 ema20_h4=75223.9 dist=2177.5 max_dist=1643.0
[00:37:41] tick balance=$311.88
  diag: trend=bullish skip=ema_overextended price=77379.4 ema20_h4=75222.1 dist=2157.3 max_dist=1643.0
[00:38:43] tick balance=$311.88
  diag: trend=bullish skip=ema_overextended price=77339.8 ema20_h4=75218.0 dist=2121.8 max_dist=1643.0
[00:39:46] tick balance=$311.88
  diag: trend=bullish skip=ema_overextended price=77336.0 ema20_h4=75217.5 dist=2118.5 max_dist=1643.0
[00:40:48] tick balance=$311.88
  diag: trend=bullish skip=ema_overextended price=77351.5 ema20_h4=75219.3 dist=2132.2 max_dist=1643.0
[00:41:50] tick balance=$311.88
  diag: trend=bullish skip=ema_overextended price=77387.6 ema20_h4=75223.5 dist=2164.1 max_dist=1643.0
[00:42:52] tick balance=$311.88
  diag: trend=bullish skip=ema_overextended price=77406.9 ema20_h4=75223.6 dist=2183.3 max_dist=1643.0
[00:43:54] tick balance=$311.88
  diag: trend=bullish skip=ema_overextended price=77371.2 ema20_h4=75221.9 dist=2149.3 max_dist=1643.0
[00:44:57] tick balance=$311.88
  diag: trend=bullish skip=ema_overextended price=77373.6 ema20_h4=75221.1 dist=2152.5 max_dist=1643.0
[00:46:00] tick balance=$311.88
  diag: trend=bullish skip=ema_overextended price=77344.7 ema20_h4=75218.3 dist=2126.4 max_dist=1643.0
[00:47:02] tick balance=$311.88
  diag: trend=bullish skip=ema_overextended price=77330.6 ema20_h4=75217.0 dist=2113.6 max_dist=1643.0
[00:48:04] tick balance=$311.88
  diag: trend=bullish skip=ema_overextended price=77313.4 ema20_h4=75216.3 dist=2097.1 max_dist=1643.0
[00:49:07] tick balance=$311.88
  diag: trend=bullish skip=ema_overextended price=77319.0 ema20_h4=75215.9 dist=2103.1 max_dist=1643.0
[00:50:09] tick balance=$311.88
  diag: trend=bullish skip=ema_overextended price=77315.0 ema20_h4=75215.4 dist=2099.6 max_dist=1643.0
[00:51:11] tick balance=$311.88
  diag: trend=bullish skip=ema_overextended price=77317.3 ema20_h4=75215.7 dist=2101.6 max_dist=1643.0
[00:52:13] tick balance=$311.88
  diag: trend=bullish skip=ema_overextended price=77381.2 ema20_h4=75221.8 dist=2159.4 max_dist=1643.0
[00:53:15] tick balance=$311.88
  diag: trend=bullish skip=ema_overextended price=77333.4 ema20_h4=75217.2 dist=2116.2 max_dist=1643.0
[00:54:17] tick balance=$311.88
  diag: trend=bullish skip=ema_overextended price=77344.1 ema20_h4=75218.6 dist=2125.5 max_dist=1643.0
```
