import sys
from data_loader import load_from_df, load_from_csv
from strategies import NaiveMovingAverageStrategy, WindowedMovingAverageStrategy
from profiler import benchmark_strategy
from reporting import plot_scaling, generate_markdown

def main(dataframe=None, csv_file=None):
    # 1. Load Data
    full_data = []
    if dataframe is not None:
        full_data = load_from_df(dataframe)
    elif csv_file is not None:
        full_data = load_from_csv(csv_file)
    else:
        print("Error: No data source provided.")
        return

    # 2. Define Test Sizes (1k, 10k, 100k)
    target_sizes = [1000, 10000, 100000]
    
    # Filter sizes that are too large for the dataset
    valid_sizes = [s for s in target_sizes if s <= len(full_data)]
    if not valid_sizes:
        print("Data too small for benchmarking.")
        return

    results = {
        "sizes": valid_sizes,
        "naive_times": [], "opt_times": [],
        "naive_mems": [], "opt_mems": []
    }

    print(f"\n--- Starting Benchmark (Total Data: {len(full_data)} ticks) ---")
    
    for size in valid_sizes:
        print(f"Processing input size: {size}...")
        
        # Test Naive
        res_naive = benchmark_strategy(NaiveMovingAverageStrategy, full_data, size)
        results["naive_times"].append(res_naive["runtime"])
        results["naive_mems"].append(res_naive["memory_mb"])
        
        # Test Optimized
        res_opt = benchmark_strategy(WindowedMovingAverageStrategy, full_data, size)
        results["opt_times"].append(res_opt["runtime"])
        results["opt_mems"].append(res_opt["memory_mb"])

    # 3. Report & Visualize
    generate_markdown(results)
    plot_scaling(results)

if __name__ == "__main__":
    # If run as script from command line, expects a file 'market_data.csv'
    main(csv_file='market_data.csv')
