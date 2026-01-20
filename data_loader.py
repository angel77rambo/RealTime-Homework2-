import csv
import pandas as pd
from datetime import datetime
from typing import List
from models import MarketDataPoint

def load_from_csv(filename: str) -> List[MarketDataPoint]:
    """Reads a CSV file and converts it to a list of MarketDataPoints."""
    data = []
    try:
        with open(filename, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                data.append(MarketDataPoint(
                    timestamp=datetime.fromisoformat(row['timestamp']),
                    symbol=row['symbol'],
                    price=float(row['price'])
                ))
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
    return data

def load_from_df(df: pd.DataFrame) -> List[MarketDataPoint]:
    """
    Ingests a pandas DataFrame and converts it to MarketDataPoints.
    Assumes columns: 'timestamp', 'symbol', 'price'.
    """
    print(f"Ingesting DataFrame with {len(df)} rows...")
    data = []
    # itertuples is significantly faster than iterrows
    for row in df.itertuples(index=False):
        # Handle timestamp conversion if necessary
        ts = row.timestamp
        if not isinstance(ts, datetime):
            ts = pd.to_datetime(ts)
            
        data.append(MarketDataPoint(
            timestamp=ts,
            symbol=str(row.symbol),
            price=float(row.price)
        ))
    return data
