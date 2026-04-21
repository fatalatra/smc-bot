# Bot Snapshot — 2026-04-21 10:55 UTC

## Service: active
balance=$296.96

## Config
POST_CLOSE_COOLDOWN: int = 180 # 3 мин техническая пауза после закрытия
RISK_PCT: float = 0.01 # 1% для старта на HYPE (вернём к 5% после 5+ сделок)
ADX_MIN: float = 20.0 # ADX < 20 → choppy market, skip entry

## Trades (last 20)
```
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
9|BUY|74842.7|-22.95|closed|2026-04-14 15:24:35|2026-04-14 17:34:53
```

## Daily PnL
```
2026-04-21|296.96|0.0|0
2026-04-20|312.71|-15.75|0
2026-04-19|354.45|-41.74|0
2026-04-18|311.88|42.12|0
2026-04-17|328.7|-16.81|0
2026-04-16|381.29|-52.59|0
2026-04-15|363.1|17.9|0
```

## Open Positions
```
none
```

## Diag Summary (last ~4h)
```
     33 trend_htf=ranging trend_mid=ranging skip=trend_mismatch
     16 trend=bearish skip=adx_low adx=13.9 min=20.0
     15 trend=bearish skip=adx_low adx=13.8 min=20.0
     14 trend=bearish skip=adx_low adx=13.5 min=20.0
     14 trend=bearish skip=adx_low adx=13.4 min=20.0
     13 trend=bearish skip=adx_low adx=14.3 min=20.0
     13 trend=bearish skip=adx_low adx=12.9 min=20.0
     13 trend=bearish skip=adx_low adx=12.3 min=20.0
     12 trend=bearish skip=adx_low adx=12.7 min=20.0
     11 trend=bearish skip=adx_low adx=14.0 min=20.0
     10 trend=bearish skip=adx_low adx=13.2 min=20.0
      9 trend=bearish skip=adx_low adx=11.4 min=20.0
      7 trend=bearish skip=adx_low adx=15.3 min=20.0
      5 trend=bearish skip=adx_low adx=12.4 min=20.0
      4 trend=bearish skip=adx_low adx=14.5 min=20.0
      4 trend=bearish skip=adx_low adx=13.1 min=20.0
      3 trend=bearish skip=adx_low adx=14.6 min=20.0
      3 trend=bearish skip=adx_low adx=14.4 min=20.0
      3 trend=bearish skip=adx_low adx=12.1 min=20.0
      3 trend=bearish skip=adx_low adx=11.7 min=20.0
```

## Errors
```
  File "/root/smc-bot/venv/lib/python3.11/site-packages/httpx/_transports/default.py", line 101, in map_httpcore_exceptions
    with map_exceptions(exc_map):
    self.gen.throw(typ, value, traceback)
  File "/root/smc-bot/venv/lib/python3.11/site-packages/httpcore/_exceptions.py", line 14, in map_exceptions
The above exception was the direct cause of the following exception:
Traceback (most recent call last):
    with map_httpcore_exceptions():
    self.gen.throw(typ, value, traceback)
  File "/root/smc-bot/venv/lib/python3.11/site-packages/httpx/_transports/default.py", line 118, in map_httpcore_exceptions
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
[12:11:08] tick balance=$296.96
  diag: trend=bearish skip=adx_low adx=13.9 min=20.0
[12:12:09] tick balance=$296.96
  diag: trend=bearish skip=adx_low adx=13.9 min=20.0
[12:13:12] tick balance=$296.96
  diag: trend=bearish skip=adx_low adx=13.9 min=20.0
[12:14:14] tick balance=$296.96
  diag: trend=bearish skip=adx_low adx=13.9 min=20.0
[12:15:16] tick balance=$296.96
  diag: trend=bearish skip=adx_low adx=14.3 min=20.0
[12:16:19] tick balance=$296.96
  diag: trend=bearish skip=adx_low adx=14.3 min=20.0
[12:17:21] tick balance=$296.96
  diag: trend=bearish skip=adx_low adx=14.3 min=20.0
[12:18:23] tick balance=$296.96
  diag: trend=bearish skip=adx_low adx=14.0 min=20.0
[12:19:26] tick balance=$296.96
  diag: trend=bearish skip=adx_low adx=13.9 min=20.0
[12:20:28] tick balance=$296.96
  diag: trend=bearish skip=adx_low adx=13.8 min=20.0
[12:21:30] tick balance=$296.96
  diag: trend=bearish skip=adx_low adx=13.7 min=20.0
[12:22:33] tick balance=$296.96
  diag: trend=bearish skip=adx_low adx=13.6 min=20.0
[12:23:36] tick balance=$296.96
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[12:24:41] tick balance=$296.96
  diag: trend=bearish skip=adx_low adx=13.1 min=20.0
🤖 <b>SMC Bot Started</b> — ▶️ ACTIVE
Balance: <b>$296.96</b>
HYPE_USDT Price: <b>$40.988</b>
Leverage: <b>x10</b>
Risk: <b>1.0%</b> ($2.97)
R:R min: <b>2.5</b>
Max positions: <b>2</b>
Daily limits: <b>+$74.24</b> / <b>-$59.39</b>
Max trades/day: <b>10</b>
Breakeven: at <b>50%</b> to TP
Commands: /start /stop /status /help
[*] Scanning every 60s...
[TG poll] drained backlog, starting offset=0
[12:25:22] tick balance=$296.96
  diag: trend=bearish skip=trend_immature trend_age_s=0 need_s=900
[12:26:24] tick balance=$296.96
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[12:27:26] tick balance=$296.96
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[12:28:28] tick balance=$296.96
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[12:29:31] tick balance=$296.96
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[12:30:33] tick balance=$296.96
  diag: trend=bearish skip=trend_immature trend_age_s=311 need_s=900
[TG poll] err: 
[12:31:35] tick balance=$296.96
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[12:32:37] tick balance=$296.96
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[12:33:39] tick balance=$296.96
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[12:34:41] tick balance=$296.96
  diag: trend=bearish skip=trend_immature trend_age_s=559 need_s=900
[12:35:44] tick balance=$296.96
  diag: trend=bearish skip=trend_immature trend_age_s=621 need_s=900
[12:36:46] tick balance=$296.96
  diag: trend=bearish skip=trend_immature trend_age_s=683 need_s=900
[12:37:49] tick balance=$296.96
  diag: trend=bearish skip=trend_immature trend_age_s=746 need_s=900
[12:38:50] tick balance=$296.96
  diag: trend=bearish skip=trend_immature trend_age_s=808 need_s=900
[12:39:52] tick balance=$296.96
  diag: trend=bearish skip=trend_immature trend_age_s=870 need_s=900
[12:40:55] tick balance=$296.96
  diag: trend=bearish skip=adx_low adx=12.4 min=20.0
[12:41:57] tick balance=$296.96
  diag: trend=bearish skip=adx_low adx=12.4 min=20.0
[12:42:59] tick balance=$296.96
  diag: trend=bearish skip=adx_low adx=12.4 min=20.0
[12:44:01] tick balance=$296.96
  diag: trend=bearish skip=adx_low adx=12.4 min=20.0
[12:45:03] tick balance=$296.96
  diag: trend=bearish skip=adx_low adx=11.9 min=20.0
[12:46:06] tick balance=$296.96
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[12:47:08] tick balance=$296.96
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[12:48:10] tick balance=$296.96
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[12:49:12] tick balance=$296.96
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[12:50:15] tick balance=$296.96
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[12:51:17] tick balance=$296.96
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[12:52:19] tick balance=$296.96
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[12:53:21] tick balance=$296.96
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[12:54:24] tick balance=$296.96
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
```
