# Bot Snapshot — 2026-04-15 13:28 UTC

## Service: active
balance=$408.86

## Config
POST_CLOSE_COOLDOWN: int = 1800 # 30 мин после закрытия
RISK_PCT: float = 0.05 # 5% от баланса на сделку
ADX_MIN: float = 20.0 # ADX < 20 → choppy market, skip entry

## Trades (last 20)
```
err
```

## Daily PnL
```
2026-04-15|363.1|45.76|0
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
    178 trend_htf=ranging trend_mid=ranging skip=trend_mismatch
      2 trend=bearish atr_ratio=1.15 obs=7 obs_fresh=7 fvgs=19 bos=21 sigs=0 wrong_side=5 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=2 near_gap_pct=0.066
      2 trend=bearish atr_ratio=1.09 obs=7 obs_fresh=7 fvgs=17 bos=23 sigs=0 wrong_side=5 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=2 near_gap_pct=0.072
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
      1 trend=bearish atr_ratio=1.14 obs=7 obs_fresh=7 fvgs=19 bos=21 sigs=0 wrong_side=5 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=2 near_gap_pct=0.103
      1 trend=bearish atr_ratio=1.14 obs=7 obs_fresh=7 fvgs=18 bos=23 sigs=0 wrong_side=5 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=2 near_gap_pct=0.205
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
[14:36:13] tick balance=$408.86
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[14:37:15] tick balance=$408.86
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[14:38:18] tick balance=$408.86
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[14:39:20] tick balance=$408.86
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[14:40:23] tick balance=$408.86
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[14:41:26] tick balance=$408.86
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[14:42:29] tick balance=$408.86
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[14:43:31] tick balance=$408.86
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[14:44:33] tick balance=$408.86
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[14:45:36] tick balance=$408.86
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[14:46:39] tick balance=$408.86
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[14:47:41] tick balance=$408.86
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[14:48:44] tick balance=$408.86
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[14:49:46] tick balance=$408.86
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[14:50:49] tick balance=$408.86
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[14:51:51] tick balance=$408.86
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[14:52:54] tick balance=$408.86
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[14:53:56] tick balance=$408.86
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[14:54:59] tick balance=$408.86
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[14:56:02] tick balance=$408.86
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[14:57:06] tick balance=$408.86
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[14:58:08] tick balance=$408.86
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[14:59:11] tick balance=$408.86
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[15:00:13] tick balance=$408.86
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[15:01:16] tick balance=$408.86
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[15:02:19] tick balance=$408.86
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[15:03:21] tick balance=$408.86
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[15:04:24] tick balance=$408.86
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[15:05:27] tick balance=$408.86
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[15:06:30] tick balance=$408.86
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[15:07:32] tick balance=$408.86
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[15:08:36] tick balance=$408.86
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[15:09:39] tick balance=$408.86
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[15:10:41] tick balance=$408.86
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[15:11:44] tick balance=$408.86
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[15:12:47] tick balance=$408.86
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[15:13:49] tick balance=$408.86
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[15:14:52] tick balance=$408.86
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[15:15:55] tick balance=$408.86
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[15:16:57] tick balance=$408.86
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[15:18:00] tick balance=$408.86
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[15:19:04] tick balance=$408.86
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[15:20:06] tick balance=$408.86
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[15:21:09] tick balance=$408.86
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[15:22:11] tick balance=$408.86
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[15:23:14] tick balance=$408.86
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[15:24:17] tick balance=$408.86
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[15:25:19] tick balance=$408.86
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[15:26:23] tick balance=$408.86
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[15:27:25] tick balance=$408.86
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
```
