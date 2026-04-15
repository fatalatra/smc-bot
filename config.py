from dataclasses import dataclass

@dataclass
class Config:
    SYMBOL: str = "BTC_USDT"
    WATCH_SYMBOL: str = "SOL_USDT"  # shadow watcher (без реальных сделок)
    WATCH_ENABLED: bool = True
    LEVERAGE: int = 30
    RISK_PCT: float = 0.05          # 5% от баланса на сделку
    MIN_RR: float = 2.5             # минимальный Risk:Reward
    MAX_POSITIONS: int = 2
    MARGIN_TYPE: str = "isolated"   # isolated / cross

    # Таймфреймы SMC
    TF_HTF: str = "Min60"           # 4H — старший фильтр тренда
    TF_TREND: str = "Min15"         # 1H — основной тренд
    TF_ZONES: str = "Min5"         # 15M — зоны OB/FVG
    TF_ENTRY: str = "Min1"          # 5M — точка входа

    # Интервал сканирования (сек)
    SCAN_INTERVAL: int = 60

    # Дедупликация сигналов (сек)
    SIGNAL_COOLDOWN: int = 900       # 15 мин между одинаковыми сигналами
    POST_CLOSE_COOLDOWN: int = 1800   # 30 мин после закрытия

    # ATR фильтр волатильности (15M свечи)
    ATR_PERIOD: int = 14
    ATR_LONG_PERIOD: int = 50
    ATR_RATIO_MIN: float = 0.8       # ATR(14) >= ATR(50) * 0.8 — текущая волатильность не сильно ниже среднего
    ADX_PERIOD: int = 14
    ADX_MIN: float = 20.0             # ADX < 20 → choppy market, skip entry
    SL_ATR_MULT: float = 0.5         # SL буфер от края OB = ATR(14) * 0.5

    # Сессионный фильтр (UTC часы) — Лондон + NY
    SESSION_START_UTC: int = 0
    SESSION_END_UTC: int = 24

    # Дневные лимиты — динамические, в % от баланса на старте дня
    DAILY_PROFIT_PCT: float = 0.25  # +25% от баланса дня → стоп
    DAILY_LOSS_PCT: float = 0.20    # -20% от баланса дня → стоп (2026-04-14 manual override)
    MAX_DAILY_TRADES: int = 10      # макс открытий в сутки
    
    # Breakeven — 2026-04-14 починен (stoporder/change_plan_price).
    # При progress_pct >= BREAKEVEN_PCT бот двигает SL на entry+BREAKEVEN_OFFSET.
    # 2026-04-14 вечером: partial TP стал первичной защитой, breakeven - вторичная страховка
    BREAKEVEN_PCT: float = 0.5      # 50% пути к TP — страховка от разворотов
    BREAKEVEN_OFFSET: float = 5.0   # $5 над entry (для LONG) или под (для SHORT)

    # Liquidity-aware SL filter — 2026-04-14.
    # Перед эмиссией сигнала проверяем: не стоит ли планируемый SL в "stop-hunt зоне"
    # над недавним 1h swing low (для LONG) или под swing high (для SHORT).
    # Если SL находится в LIQUIDITY_THRESHOLD_PCT от ликвидности — сетап пропускается.
    # Это THE главный защитный фильтр против "цена сняла наш SL и развернулась" — самого
    # частого паттерна поражений 2026-04-14 (trades #8, #9, #10).
    LIQUIDITY_CHECK_ENABLED: bool = True
    LIQUIDITY_THRESHOLD_PCT: float = 0.003   # 0.3% — дистанция "SL слишком близко к liquidity pool"
    LIQUIDITY_SWINGS_LOOKBACK: int = 10      # проверяем последние N 1h свингов

    # Partial TP — закрывает PARTIAL_TP_FRACTION от позиции на PARTIAL_TP_R × risk_dist.
    # После partial close SL на остатке автоматически едет на entry+BREAKEVEN_OFFSET.
    # Это ключевая защита: большинство SMC-ретестов доходят до 1R но не до 2.5R —
    # partial TP на 1R превращает эти "почти-winner"-сделки из полных SL в +0.5R.
    PARTIAL_TP_ENABLED: bool = True
    PARTIAL_TP_R: float = 1.0        # срабатывает при цене = entry ± risk_distance × 1.0
    PARTIAL_TP_FRACTION: float = 0.5 # доля позиции к закрытию (0.5 = половина)

config = Config()
