import time
from memory_profiler import memory_usage


def measure_runtime(strategy, data):
    """
    Measures total execution time for a strategy.
    """
    start = time.time()
    for tick in data:
        strategy.generate_signals(tick)
    end = time.time()
    return end - start


def measure_memory(strategy, data):
    """
    Measures peak memory usage for a strategy.
    """

    def run():
        for tick in data:
            strategy.generate_signals(tick)

    mem_usage = memory_usage(run, max_usage=True)
    return mem_usage
