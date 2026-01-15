from data_loader import load_market_data
from strategies import NaiveMovingAverageStrategy, WindowedMovingAverageStrategy
from profiler import measure_runtime, measure_memory
from reporting import plot_runtime, plot_memory

DATA_PATH = "data/market_data.csv"
WINDOW_SIZE = 50

data = load_market_data(DATA_PATH)

input_sizes = [1000, 10000, 100000]

naive_times = []
optimized_times = []
naive_memory = []
optimized_memory = []

for size in input_sizes:
    subset = data[:size]

    naive = NaiveMovingAverageStrategy()
    optimized = WindowedMovingAverageStrategy(WINDOW_SIZE)

    naive_times.append(measure_runtime(naive, subset))
    optimized_times.append(measure_runtime(optimized, subset))

    naive_memory.append(measure_memory(naive, subset))
    optimized_memory.append(measure_memory(optimized, subset))

plot_runtime(input_sizes, naive_times, optimized_times)
plot_memory(input_sizes, naive_memory, optimized_memory)
