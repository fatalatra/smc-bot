"""
Risk Management
- Размер позиции на основе % риска от баланса
- Валидация R:R
- Конвертация в контракты MEXC (1 контракт = 0.0001 BTC)
"""
from config import config
from exchange.models import Signal


def calculate_position_size(balance: float, signal: Signal, price: float) -> int:
    """
    Возвращает кол-во контрактов.
    1 контракт = 0.0001 BTC
    """
    risk_amount = balance * config.RISK_PCT  # $ которыми рискуем
    sl_distance = abs(signal.entry - signal.sl)
    
    if sl_distance == 0:
        return 0
    
    # Размер позиции в BTC
    btc_size = risk_amount / sl_distance
    
    # Конвертация в контракты
    contracts = int(btc_size / 0.0001)
    
    # Минимум 1 контракт
    return max(contracts, 1) if contracts > 0 else 0


def validate_rr(signal: Signal) -> bool:
    """Проверяет что R:R >= минимального"""
    risk = abs(signal.entry - signal.sl)
    reward = abs(signal.tp - signal.entry)
    if risk == 0:
        return False
    rr = reward / risk
    return rr >= config.MIN_RR


def max_positions_reached(open_positions: int) -> bool:
    return open_positions >= config.MAX_POSITIONS
