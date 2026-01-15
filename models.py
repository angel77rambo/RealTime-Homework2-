from dataclasses import dataclass
from datetime import datetime
from abc import ABC, abstractmethod

@dataclass(frozen=True)
class MarketDataPoint:
    """
    Immutable market data structure.
    """
    timestamp: datetime
    symbol: str
    price: float


class Strategy(ABC):
    """
    Abstract base class for trading strategies.
    """

    @abstractmethod
    def generate_signals(self, tick: MarketDataPoint) -> list:
        pass

