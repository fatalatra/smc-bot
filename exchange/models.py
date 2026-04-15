from dataclasses import dataclass
from enum import Enum
from typing import Optional

class Side(str, Enum):
    BUY = 'BUY'       # long open
    SELL = 'SELL'      # short open

class OrderType(str, Enum):
    LIMIT = 'LIMIT'
    MARKET = 'MARKET'

@dataclass
class Candle:
    ts: int
    open: float
    high: float
    low: float
    close: float
    volume: float

@dataclass
class OrderBlock:
    side: Side
    high: float
    low: float
    tf: str
    ts: int
    mitigated: bool = False

@dataclass
class FVG:
    side: Side
    high: float
    low: float
    tf: str
    ts: int
    filled: bool = False

@dataclass
class Signal:
    side: Side
    entry: float
    sl: float
    tp: float
    ob: Optional[OrderBlock] = None
    fvg: Optional[FVG] = None
    score: float = 0.0
    reason: str = ''
