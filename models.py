import abc
from dataclasses import dataclass
from datetime import datetime
from typing import Optional
import pandas as pd

@dataclass(frozen=True)
class MarketDataPoint:
    """
    Immutable data point representing a single market tick.
    """
    timestamp: datetime
    symbol: str
    price: float

class Strategy(abc.ABC):
    """
    Abstract Base Class for all trading strategies.
    """
    @abc.abstractmethod
    def generate_signals(self, tick: MarketDataPoint) -> Optional[str]:
        pass

    @abc.abstractmethod
    def name(self) -> str:
        pass
