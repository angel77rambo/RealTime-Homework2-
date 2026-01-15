from datetime import datetime
from models import MarketDataPoint
from strategies import NaiveMovingAverageStrategy, WindowedMovingAverageStrategy


def test_strategies_execute():
    tick = MarketDataPoint(datetime.now(), "AAPL", 100.0)

    naive = NaiveMovingAverageStrategy()
    optimized = WindowedMovingAverageStrategy(5)

    assert naive.generate_signals(tick) is not None
    assert optimized.generate_signals(tick) is not None
