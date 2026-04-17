# Bot Snapshot — 2026-04-17 10:55 UTC

## Service: active
balance=$292.43

## Config
POST_CLOSE_COOLDOWN: int = 180 # 3 мин техническая пауза после закрытия
RISK_PCT: float = 0.05 # 5% от баланса на сделку
ADX_MIN: float = 20.0 # ADX < 20 → choppy market, skip entry

## Trades (last 20)
```
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
2|SELL|73451.8|13.15|closed|2026-04-11 20:18:03|2026-04-12 08:14:54
1|SELL|73575.9|13.15|closed|2026-04-11 20:01:37|2026-04-12 08:14:54
```

## Daily PnL
```
2026-04-17|328.7|-36.27|0
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
     78 trend_htf=ranging trend_mid=ranging skip=trend_mismatch
      2 trend=bullish atr_ratio=1.57 obs=8 obs_fresh=5 fvgs=9 bos=26 sigs=0 wrong_side=4 price_out=1 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=0.792
      1 trend=bullish skip=trend_immature trend_age_s=866 need_s=900
      1 trend=bullish skip=trend_immature trend_age_s=804 need_s=900
      1 trend=bullish skip=trend_immature trend_age_s=742 need_s=900
      1 trend=bullish skip=trend_immature trend_age_s=681 need_s=900
      1 trend=bullish skip=trend_immature trend_age_s=61 need_s=900
      1 trend=bullish skip=trend_immature trend_age_s=618 need_s=900
      1 trend=bullish skip=trend_immature trend_age_s=557 need_s=900
      1 trend=bullish skip=trend_immature trend_age_s=494 need_s=900
      1 trend=bullish skip=trend_immature trend_age_s=433 need_s=900
      1 trend=bullish skip=trend_immature trend_age_s=370 need_s=900
      1 trend=bullish skip=trend_immature trend_age_s=308 need_s=900
      1 trend=bullish skip=trend_immature trend_age_s=247 need_s=900
      1 trend=bullish skip=trend_immature trend_age_s=185 need_s=900
      1 trend=bullish skip=trend_immature trend_age_s=123 need_s=900
      1 trend=bullish skip=trend_immature trend_age_s=0 need_s=900
      1 trend=bullish atr_ratio=2.11 obs=7 obs_fresh=4 fvgs=8 bos=30 sigs=0 wrong_side=3 price_out=1 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=0.808
      1 trend=bullish atr_ratio=2.11 obs=7 obs_fresh=4 fvgs=8 bos=30 sigs=0 wrong_side=3 price_out=1 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=0.769
      1 trend=bullish atr_ratio=2.0 obs=7 obs_fresh=4 fvgs=8 bos=29 sigs=0 wrong_side=3 price_out=1 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=0.954
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
[12:04:23] tick balance=$313.79
  diag: trend=bullish atr_ratio=1.67 obs=7 obs_fresh=4 fvgs=8 bos=27 sigs=0 wrong_side=3 price_out=1 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=1.005
[12:05:25] tick balance=$314.13
  diag: trend=bullish atr_ratio=1.6 obs=7 obs_fresh=4 fvgs=8 bos=27 sigs=0 wrong_side=3 price_out=1 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=1.019
[12:06:29] tick balance=$315.37
  diag: trend=bullish atr_ratio=1.61 obs=7 obs_fresh=4 fvgs=8 bos=27 sigs=0 wrong_side=3 price_out=1 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=1.055
[12:07:31] tick balance=$313.97
  diag: trend=bullish atr_ratio=1.61 obs=7 obs_fresh=4 fvgs=8 bos=27 sigs=0 wrong_side=3 price_out=1 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=1.012
[12:08:33] tick balance=$314.61
  diag: trend=bullish atr_ratio=1.61 obs=7 obs_fresh=4 fvgs=8 bos=27 sigs=0 wrong_side=3 price_out=1 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=1.034
[12:09:35] tick balance=$312.13
  diag: trend=bullish atr_ratio=1.62 obs=7 obs_fresh=4 fvgs=8 bos=27 sigs=0 wrong_side=3 price_out=1 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=0.947
[12:10:38] tick balance=$308.70
  diag: trend=bullish atr_ratio=1.59 obs=8 obs_fresh=5 fvgs=8 bos=26 sigs=0 wrong_side=4 price_out=1 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=0.85
[12:11:40] tick balance=$308.25
  diag: trend=bullish atr_ratio=1.59 obs=8 obs_fresh=5 fvgs=8 bos=25 sigs=0 wrong_side=4 price_out=1 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=0.831
[12:12:43] tick balance=$306.59
  diag: trend=bullish atr_ratio=1.6 obs=8 obs_fresh=5 fvgs=8 bos=25 sigs=0 wrong_side=4 price_out=1 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=0.778
[12:13:46] tick balance=$307.93
  diag: trend=bullish atr_ratio=1.6 obs=8 obs_fresh=5 fvgs=8 bos=25 sigs=0 wrong_side=4 price_out=1 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=0.821
[12:14:48] tick balance=$306.68
  diag: trend=bullish atr_ratio=1.6 obs=8 obs_fresh=5 fvgs=8 bos=26 sigs=0 wrong_side=4 price_out=1 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=0.781
[12:15:51] tick balance=$307.46
  diag: trend=bullish atr_ratio=1.57 obs=8 obs_fresh=5 fvgs=9 bos=26 sigs=0 wrong_side=4 price_out=1 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=0.806
[12:16:53] tick balance=$307.06
  diag: trend=bullish atr_ratio=1.57 obs=8 obs_fresh=5 fvgs=9 bos=26 sigs=0 wrong_side=4 price_out=1 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=0.792
[12:17:56] tick balance=$307.06
  diag: trend=bullish atr_ratio=1.57 obs=8 obs_fresh=5 fvgs=9 bos=26 sigs=0 wrong_side=4 price_out=1 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=0.792
[12:18:59] tick balance=$308.88
  diag: trend=bullish atr_ratio=1.59 obs=8 obs_fresh=5 fvgs=9 bos=26 sigs=0 wrong_side=4 price_out=1 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=0.851
[12:20:03] tick balance=$308.47
  diag: trend=bullish atr_ratio=1.51 obs=8 obs_fresh=5 fvgs=9 bos=26 sigs=0 wrong_side=4 price_out=1 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=0.829
[12:21:06] tick balance=$309.35
  diag: trend=bullish atr_ratio=1.53 obs=8 obs_fresh=5 fvgs=9 bos=26 sigs=0 wrong_side=4 price_out=1 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=0.863
[12:22:08] tick balance=$310.50
  diag: trend=bullish atr_ratio=1.53 obs=8 obs_fresh=5 fvgs=9 bos=26 sigs=0 wrong_side=4 price_out=1 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=0.903
[12:23:10] tick balance=$309.81
  diag: trend=bullish atr_ratio=1.53 obs=8 obs_fresh=5 fvgs=9 bos=25 sigs=0 wrong_side=4 price_out=1 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=0.878
[12:24:14] tick balance=$309.54
  diag: trend=bullish atr_ratio=1.53 obs=8 obs_fresh=5 fvgs=9 bos=25 sigs=0 wrong_side=4 price_out=1 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=0.872
[12:25:17] tick balance=$310.62
  diag: trend=bullish atr_ratio=1.42 obs=8 obs_fresh=5 fvgs=10 bos=25 sigs=0 wrong_side=4 price_out=1 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=0.903
[12:26:20] tick balance=$308.23
  diag: trend=bullish atr_ratio=1.44 obs=8 obs_fresh=5 fvgs=9 bos=25 sigs=0 wrong_side=4 price_out=1 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=0.82
[12:27:24] tick balance=$306.84
  diag: trend=bullish atr_ratio=1.45 obs=8 obs_fresh=5 fvgs=9 bos=26 sigs=0 wrong_side=4 price_out=1 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=0.786
[12:28:27] tick balance=$304.52
  diag: trend=bullish atr_ratio=1.47 obs=9 obs_fresh=6 fvgs=9 bos=26 sigs=0 wrong_side=5 price_out=1 bos_miss=0 risk_neg=0 liquidity_trap=0 near_gap_pct=0.713
[12:29:29] tick balance=$292.43
[sync] trade #19 BUY entry=75720.1 closed (sl) at price=75335.1
[real_pnl] trade #19: profit=-19.66 open_fee=0.00 close_fee=0.00 => net=-19.66
  diag: skip=post_close_cooldown wait_s=177
[12:30:33] tick balance=$292.43
  diag: skip=post_close_cooldown wait_s=115
[12:31:36] tick balance=$292.43
  diag: skip=post_close_cooldown wait_s=52
[12:32:38] tick balance=$292.43
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[12:33:40] tick balance=$292.43
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[12:34:42] tick balance=$292.43
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[12:35:46] tick balance=$292.43
  diag: trend=bullish atr_ratio=1.35 obs=9 obs_fresh=6 fvgs=10 bos=27 sigs=0 wrong_side=5 price_out=0 bos_miss=0 risk_neg=0 liquidity_trap=1 near_gap_pct=0.388
[12:36:48] tick balance=$292.43
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[12:37:49] tick balance=$292.43
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[12:38:51] tick balance=$292.43
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[12:39:53] tick balance=$292.43
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[12:40:55] tick balance=$292.43
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[12:41:57] tick balance=$292.43
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[12:42:59] tick balance=$292.43
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[12:44:03] tick balance=$292.43
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[12:45:05] tick balance=$292.43
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[12:46:08] tick balance=$292.43
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[12:47:10] tick balance=$292.43
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[12:48:12] tick balance=$292.43
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[12:49:14] tick balance=$292.43
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[12:50:17] tick balance=$292.43
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[12:51:19] tick balance=$292.43
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[12:52:21] tick balance=$292.43
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[12:53:23] tick balance=$292.43
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
[12:54:26] tick balance=$292.43
  diag: trend_htf=ranging trend_mid=ranging skip=trend_mismatch
```
