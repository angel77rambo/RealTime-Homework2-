import csv
from datetime import datetime
from models import MarketDataPoint

def load_market_data(file_path: str) -> list:
    """
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    data = []

    with open(file_path, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            point = MarketDataPoint(
                timestamp=datetime.fromisoformat(row["timestamp"]),
                symbol=row["symbol"],
                price=float(row["price"])
            )
            data.append(point)

    return data
