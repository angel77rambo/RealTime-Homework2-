# Financial Signal Processing Complexity Analysis

## Overview
This project explores the impact of algorithmic design on the performance of financial trading systems. It implements and benchmarks two versions of a Moving Average strategy: a "Naive" implementation with $O(N)$ space complexity and an "Optimized" implementation using `collections.deque` with $O(1)$ time complexity.

## Structure

* `data_loader.py`: Handles ingestion of CSV market data into immutable `MarketDataPoint` objects.
* `models.py`: Defines the `MarketDataPoint` dataclass and the abstract `Strategy` base class.
* `strategies.py`: Contains the implementation of:
    * `NaiveMovingAverageStrategy`: Recomputes sums from full history.
    * `WindowedMovingAverageStrategy`: Uses a sliding window buffer (deque) for efficient calculation.
* `profiler.py`: A benchmarking tool using `tracemalloc` and `time` to record performance metrics.
* `reporting.py`: Generates the Markdown report and visualization plots.
* `main.py`: The entry point script that orchestrates the data loading and analysis pipeline.

## Installation & Setup

1.  Ensure you have Python 3.7+ installed.
2.  Install dependencies:
    ```bash
    pip install pandas matplotlib numpy
    ```

## Usage

You can run the analysis using the main script. If you have a `market_data.csv` file in the root directory:

```bash
python main.py
