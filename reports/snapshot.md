# Bot Snapshot — 2026-04-15 13:56 UTC

## Service: active
balance=$394.09

## Config
POST_CLOSE_COOLDOWN: int = 1800 # 30 мин после закрытия
RISK_PCT: float = 0.05 # 5% от баланса на сделку
ADX_MIN: float = 20.0 # ADX < 20 → choppy market, skip entry

## Trades (last 20)
```
13|BUY|74275.5||open|2026-04-15 13:30:37|
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
2026-04-15|363.1|30.99|0
2026-04-14|413.74|-50.64|0
2026-04-13|413.74|0.0|0
2026-04-12|423.86|-10.12|0
2026-04-11|457.33|-130.15|0
```

## Open Positions
```
13|BUY|74275.5|open
```

## Diag Summary (last ~4h)
```
    184 trend_htf=ranging trend_mid=ranging skip=trend_mismatch
      2 trend=bearish atr_ratio=1.15 obs=7 obs_fresh=7 fvgs=19 bos=21 sigs=0 wrong_side=5 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=2 near_gap_pct=0.066
      2 trend=bearish atr_ratio=1.09 obs=7 obs_fresh=7 fvgs=17 bos=23 sigs=0 wrong_side=5 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=2 near_gap_pct=0.072
      1 trend=bullish atr_ratio=1.08 obs=7 obs_fresh=6 fvgs=13 bos=22 sigs=1 wrong_side=1 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=2 near_gap_pct=-0.08 skip=side_busy open_sides=['BUY']
      1 trend=bullish atr_ratio=0.99 obs=7 obs_fresh=7 fvgs=13 bos=21 sigs=1 wrong_side=0 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=1 near_gap_pct=0.019
      1 trend=bearish atr_ratio=1.18 obs=7 obs_fresh=7 fvgs=18 bos=22 sigs=0 wrong_side=5 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=2 near_gap_pct=0.108
      1 trend=bearish atr_ratio=1.17 obs=7 obs_fresh=7 fvgs=18 bos=23 sigs=0 wrong_side=5 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=2 near_gap_pct=0.153
      1 trend=bearish atr_ratio=1.17 obs=7 obs_fresh=7 fvgs=18 bos=23 sigs=0 wrong_side=5 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=2 near_gap_pct=0.146
      1 trend=bearish atr_ratio=1.17 obs=7 obs_fresh=7 fvgs=18 bos=22 sigs=0 wrong_side=5 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=2 near_gap_pct=0.198
      1 trend=bearish atr_ratio=1.17 obs=7 obs_fresh=7 fvgs=18 bos=22 sigs=0 wrong_side=5 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=2 near_gap_pct=0.161
      1 trend=bearish atr_ratio=1.17 obs=7 obs_fresh=7 fvgs=18 bos=22 sigs=0 wrong_side=5 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=2 near_gap_pct=0.149
      1 trend=bearish atr_ratio=1.16 obs=7 obs_fresh=7 fvgs=19 bos=21 sigs=0 wrong_side=5 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=2 near_gap_pct=0.042
      1 trend=bearish atr_ratio=1.16 obs=7 obs_fresh=7 fvgs=19 bos=21 sigs=0 wrong_side=5 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=2 near_gap_pct=0.028
      1 trend=bearish atr_ratio=1.16 obs=7 obs_fresh=7 fvgs=18 bos=23 sigs=0 wrong_side=5 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=2 near_gap_pct=0.131
      1 trend=bearish atr_ratio=1.15 obs=7 obs_fresh=7 fvgs=19 bos=21 sigs=0 wrong_side=5 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=2 near_gap_pct=0.088
      1 trend=bearish atr_ratio=1.15 obs=7 obs_fresh=7 fvgs=19 bos=21 sigs=0 wrong_side=5 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=2 near_gap_pct=0.068
      1 trend=bearish atr_ratio=1.15 obs=7 obs_fresh=7 fvgs=19 bos=20 sigs=0 wrong_side=5 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=2 near_gap_pct=0.054
      1 trend=bearish atr_ratio=1.15 obs=7 obs_fresh=7 fvgs=19 bos=20 sigs=0 wrong_side=5 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=2 near_gap_pct=0.032
      1 trend=bearish atr_ratio=1.15 obs=7 obs_fresh=7 fvgs=18 bos=22 sigs=0 wrong_side=5 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=2 near_gap_pct=0.15
      1 trend=bearish atr_ratio=1.15 obs=7 obs_fresh=7 fvgs=17 bos=23 sigs=0 wrong_side=5 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=2 near_gap_pct=0.256
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
[15:24:17] tick balance=$408.86
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[15:25:19] tick balance=$408.86
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[15:26:23] tick balance=$408.86
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[15:27:25] tick balance=$408.86
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[15:28:28] tick balance=$408.86
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[15:29:31] tick balance=$408.86
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[15:30:35] tick balance=$408.86
✅ <b>LONG Opened</b>
Entry: <b>$74,275.5</b>
SL: <b>$73,706.8</b>
TP: <b>$75,780.5</b>
Vol: <b>345</b> contracts
Risk: <b>$20.44</b>
Daily PnL: <b>$+45.76</b>
Reason: Long: OB+FVG confluence + BOS
  diag: trend=bullish atr_ratio=0.99 obs=7 obs_fresh=7 fvgs=13 bos=21 sigs=1 wrong_side=0 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=1 near_gap_pct=0.019
[15:31:41] tick balance=$404.68
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[15:32:44] tick balance=$403.59
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[15:33:47] tick balance=$407.10
  diag: trend=bullish atr_ratio=1.08 obs=7 obs_fresh=6 fvgs=13 bos=22 sigs=1 wrong_side=1 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=2 near_gap_pct=-0.08 skip=side_busy open_sides=['BUY']
[15:34:50] tick balance=$404.98
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[15:35:55] tick balance=$403.05
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
🤖 <b>SMC Bot Started</b> — ▶️ ACTIVE
Balance: <b>$404.07</b>
BTC Price: <b>$74,136.30</b>
Leverage: <b>x30</b>
Risk: <b>5.0%</b> ($20.20)
R:R min: <b>2.5</b>
Max positions: <b>2</b>
Daily limits: <b>+$90.78</b> / <b>-$72.62</b>
Max trades/day: <b>10</b>
Breakeven: at <b>50%</b> to TP
Commands: /start /stop /status /help
[*] Scanning every 60s...
[TG poll] drained backlog, starting offset=0
[15:36:07] tick balance=$402.98
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[15:37:09] tick balance=$401.67
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[15:38:14] tick balance=$398.18
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[15:39:17] tick balance=$400.92
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
🤖 <b>SMC Bot Started</b> — ▶️ ACTIVE
Balance: <b>$402.47</b>
BTC Price: <b>$74,090.50</b>
Leverage: <b>x30</b>
Risk: <b>5.0%</b> ($20.12)
R:R min: <b>2.5</b>
Max positions: <b>2</b>
Daily limits: <b>+$90.78</b> / <b>-$72.62</b>
Max trades/day: <b>10</b>
Breakeven: at <b>50%</b> to TP
Commands: /start /stop /status /help
[*] Scanning every 60s...
[TG poll] drained backlog, starting offset=0
[15:39:35] tick balance=$402.41
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[15:40:38] tick balance=$400.42
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[15:41:41] tick balance=$399.36
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[15:42:45] tick balance=$397.51
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[15:43:49] tick balance=$394.05
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[15:44:53] tick balance=$393.22
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[15:45:57] tick balance=$396.23
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[15:47:01] tick balance=$395.95
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[15:48:04] tick balance=$397.85
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[15:49:07] tick balance=$394.97
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[15:50:11] tick balance=$395.90
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[15:51:14] tick balance=$395.22
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[15:52:17] tick balance=$392.28
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[15:53:20] tick balance=$393.42
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[15:54:23] tick balance=$394.43
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[15:55:27] tick balance=$393.95
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[15:56:30] tick balance=$394.09
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
```
