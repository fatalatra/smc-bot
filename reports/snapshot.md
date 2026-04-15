# Bot Snapshot — 2026-04-15 18:55 UTC

## Service: active
balance=$388.15

## Config
POST_CLOSE_COOLDOWN: int = 180 # 3 мин техническая пауза после закрытия
RISK_PCT: float = 0.05 # 5% от баланса на сделку
ADX_MIN: float = 20.0 # ADX < 20 → choppy market, skip entry

## Trades (last 20)
```
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
2|SELL|73451.8|13.15|closed|2026-04-11 20:18:03|2026-04-12 08:14:54
1|SELL|73575.9|13.15|closed|2026-04-11 20:01:37|2026-04-12 08:14:54
```

## Daily PnL
```
2026-04-15|363.1|25.05|0
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
    208 trend_htf=ranging trend_mid=ranging skip=trend_mismatch
      1 trend=bullish atr_ratio=1.35 obs=9 obs_fresh=8 fvgs=11 bos=27 sigs=0 wrong_side=3 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=5 near_gap_pct=-0.09
      1 trend=bullish atr_ratio=1.33 obs=9 obs_fresh=8 fvgs=11 bos=27 sigs=0 wrong_side=3 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=5 near_gap_pct=0.05
      1 trend=bullish atr_ratio=1.32 obs=10 obs_fresh=9 fvgs=11 bos=26 sigs=0 wrong_side=3 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=6 near_gap_pct=0.048
      1 skip=post_close_cooldown wait_s=987
      1 skip=post_close_cooldown wait_s=924
      1 skip=post_close_cooldown wait_s=862
      1 skip=post_close_cooldown wait_s=800
      1 skip=post_close_cooldown wait_s=737
      1 skip=post_close_cooldown wait_s=675
      1 skip=post_close_cooldown wait_s=613
      1 skip=post_close_cooldown wait_s=550
      1 skip=post_close_cooldown wait_s=487
      1 skip=post_close_cooldown wait_s=47
      1 skip=post_close_cooldown wait_s=424
      1 skip=post_close_cooldown wait_s=361
      1 skip=post_close_cooldown wait_s=299
      1 skip=post_close_cooldown wait_s=236
      1 skip=post_close_cooldown wait_s=1797
      1 skip=post_close_cooldown wait_s=1735
```

## Errors
```
The above exception was the direct cause of the following exception:
Traceback (most recent call last):
    with map_httpcore_exceptions():
    self.gen.throw(typ, value, traceback)
  File "/root/smc-bot/venv/lib/python3.11/site-packages/httpx/_transports/default.py", line 118, in map_httpcore_exceptions
httpx.ConnectError: [SSL: TLSV1_ALERT_INTERNAL_ERROR] tlsv1 alert internal error (_ssl.c:992)
[sol watch err] [SSL: TLSV1_ALERT_INTERNAL_ERROR] tlsv1 alert internal error (_ssl.c:992)
[ERROR] [SSL: TLSV1_ALERT_INTERNAL_ERROR] tlsv1 alert internal error (_ssl.c:992)
Traceback (most recent call last):
  File "/root/smc-bot/venv/lib/python3.11/site-packages/httpx/_transports/default.py", line 101, in map_httpcore_exceptions
    with map_exceptions(exc_map):
    self.gen.throw(typ, value, traceback)
  File "/root/smc-bot/venv/lib/python3.11/site-packages/httpcore/_exceptions.py", line 14, in map_exceptions
httpcore.ConnectError: [SSL: TLSV1_ALERT_INTERNAL_ERROR] tlsv1 alert internal error (_ssl.c:992)
The above exception was the direct cause of the following exception:
Traceback (most recent call last):
    with map_httpcore_exceptions():
    self.gen.throw(typ, value, traceback)
  File "/root/smc-bot/venv/lib/python3.11/site-packages/httpx/_transports/default.py", line 118, in map_httpcore_exceptions
httpx.ConnectError: [SSL: TLSV1_ALERT_INTERNAL_ERROR] tlsv1 alert internal error (_ssl.c:992)
```

## Last 100 Log Lines
```
[20:03:39] tick balance=$388.15
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:04:45] tick balance=$388.15
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:05:48] tick balance=$388.15
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:06:49] tick balance=$388.15
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:07:50] tick balance=$388.15
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:08:56] tick balance=$388.15
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:09:59] tick balance=$388.15
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:11:01] tick balance=$388.15
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:12:05] tick balance=$388.15
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:13:08] tick balance=$388.15
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:14:11] tick balance=$388.15
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:15:13] tick balance=$388.15
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:16:15] tick balance=$388.15
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:17:17] tick balance=$388.15
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:18:19] tick balance=$388.15
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:19:21] tick balance=$388.15
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:20:27] tick balance=$388.15
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:21:29] tick balance=$388.15
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:22:34] tick balance=$388.15
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:23:36] tick balance=$388.15
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:24:39] tick balance=$388.15
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:25:46] tick balance=$388.15
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:26:48] tick balance=$388.15
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:27:51] tick balance=$388.15
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:28:54] tick balance=$388.15
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:29:56] tick balance=$388.15
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:30:58] tick balance=$388.15
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:32:00] tick balance=$388.15
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:33:02] tick balance=$388.15
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:34:04] tick balance=$388.15
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:35:06] tick balance=$388.15
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:36:09] tick balance=$388.15
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:37:10] tick balance=$388.15
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:38:11] tick balance=$388.15
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:39:14] tick balance=$388.15
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:40:15] tick balance=$388.15
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:41:17] tick balance=$388.15
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:42:20] tick balance=$388.15
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:43:22] tick balance=$388.15
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:44:24] tick balance=$388.15
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:45:25] tick balance=$388.15
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:46:27] tick balance=$388.15
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:47:29] tick balance=$388.15
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:48:31] tick balance=$388.15
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:49:32] tick balance=$388.15
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:50:34] tick balance=$388.15
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:51:37] tick balance=$388.15
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:52:38] tick balance=$388.15
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:53:40] tick balance=$388.15
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[20:54:41] tick balance=$388.15
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
```
