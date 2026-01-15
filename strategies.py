from collections import deque
from models import Strategy, MarketDataPoint

class NaiveMovingAverageStrategy(Strategy):

    def __init__(self):
        self.prices = []

    def generate_signals(self, tick: MarketDataPoint) -> list:
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        self.prices.append(tick.price)
        avg_price = sum(self.prices) / len(self.prices)

        if tick.price > avg_price:
            return ["BUY"]
        elif tick.price < avg_price:
            return ["SELL"]
        else:
            return []


class WindowedMovingAverageStrategy(Strategy):

    def __init__(self, window_size: int):
        self.window_size = window_size
        self.window = deque(maxlen=window_size)
        self.running_sum = 0.0

    def generate_signals(self, tick: MarketDataPoint) -> list:
        """
        Time Complexity: O(1)
        Space Complexity: O(k)
        """
        if len(self.window) == self.window_size:
            self.running_sum -= self.window[0]

        self.window.append(tick.price)
        self.running_sum += tick.price

        avg_price = self.running_sum / len(self.window)

        if tick.price > avg_price:
            return ["BUY"]
        elif tick.price < avg_price:
            return ["SELL"]
        else:
            return []
