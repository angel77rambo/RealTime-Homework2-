from typing import List, Optional, Deque
import collections
from models import Strategy, MarketDataPoint

class NaiveMovingAverageStrategy(Strategy):
    """
    Naive Implementation.
    Time Complexity: O(N) total (O(k) per tick due to list slicing).
    Space Complexity: O(N) (Stores entire history).
    """
    def __init__(self, window_size: int = 50):
        self.window_size = window_size
        self.history: List[float] = []

    def name(self) -> str:
        return "Naive (O(N) Space)"

    def generate_signals(self, tick: MarketDataPoint) -> Optional[str]:
        self.history.append(tick.price)
        
        if len(self.history) < self.window_size:
            return None
        
        # INEFFICIENCY: Creates a copy of the slice and iterates to sum every tick
        window_slice = self.history[-self.window_size:]
        avg_price = sum(window_slice) / self.window_size
        
        if tick.price > avg_price: return "BUY"
        elif tick.price < avg_price: return "SELL"
        return "HOLD"

class WindowedMovingAverageStrategy(Strategy):
    """
    Optimized Implementation.
    Time Complexity: O(1) per tick (Incremental update).
    Space Complexity: O(k) (Stores only window size).
    """
    def __init__(self, window_size: int = 50):
        self.window_size = window_size
        # Deque with maxlen automatically handles eviction
        self.window: Deque[float] = collections.deque(maxlen=window_size)
        self.current_sum = 0.0

    def name(self) -> str:
        return "Optimized (O(1) Time)"

    def generate_signals(self, tick: MarketDataPoint) -> Optional[str]:
        # If the window is full, subtract the outgoing element from sum
        if len(self.window) == self.window_size:
            self.current_sum -= self.window[0]
            
        self.window.append(tick.price)
        self.current_sum += tick.price
        
        if len(self.window) < self.window_size:
            return None
            
        avg_price = self.current_sum / self.window_size
        
        if tick.price > avg_price: return "BUY"
        elif tick.price < avg_price: return "SELL"
        return "HOLD"
