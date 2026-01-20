import time
import tracemalloc
import gc
from typing import List, Type
from models import Strategy, MarketDataPoint

def benchmark_strategy(strategy_cls: Type[Strategy], data: List[MarketDataPoint], input_size: int) -> dict:
    """
    Runs a strategy on a subset of data and measures time and memory.
    """
    # Create subset outside of measurement to focus only on strategy execution
    subset = data[:input_size]
    
    # Force Garbage Collection before starting to clear previous noise
    gc.collect()
    
    # Instantiate strategy
    strategy = strategy_cls(window_size=100)
    
    # --- Start Memory Tracing ---
    tracemalloc.start()
    
    # --- Start Timer ---
    start_time = time.perf_counter()
    
    # Run Simulation
    for tick in subset:
        strategy.generate_signals(tick)
        
    end_time = time.perf_counter()
    
    # --- Capture Memory ---
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    # Calculate usage in MB
    peak_mb = peak / (1024 * 1024)
    
    # Logic: Since O(1) memory is tiny (~0.0008 MB), we want to avoid raw 0 if possible,
    # but strictly speaking, the delta might be 0 if Python reuses memory blocks.
    return {
        "size": input_size,
        "runtime": end_time - start_time,
        "memory_mb": peak_mb
    }
