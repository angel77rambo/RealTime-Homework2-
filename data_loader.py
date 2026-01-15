import csv
from datetime import datetime
from models import MarketDataPoint

def load_market_data(file_path: str) -> list:
    """
    Reads market data from a CSV file.

    Time Complexity: O(n)
    Space Complexity: O(n)
    Each row is parsed into a MarketDataPoint and stored in memory.
    """
    data = []

    with open(file_path, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            data_point = MarketDataPoint(
                timestamp=datetime.fromisoformat(row["timestamp"]),
                symbol=row["symbol"],
                price=float(row["price"])
            )
            data.append(data_point)

    return data
