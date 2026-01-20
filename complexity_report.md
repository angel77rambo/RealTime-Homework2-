# Financial Signal Processing: Complexity Analysis Report

## 1. Executive Summary

This report analyzes the computational performance of two Moving Average trading strategies. The benchmarking results demonstrate that algorithmic choices significantly impact system scalability. Specifically, the **Windowed Strategy** outperforms the **Naive Strategy** by approximately **2.05x** in execution speed on large datasets while maintaining a near-zero memory footprint growth.

## 2. Algorithm Complexity Analysis

### NaiveMovingAverageStrategy
* **Theoretical Time Complexity**: $O(N \cdot k)$ total. For every new tick, the algorithm slices a list of size $N$ to get the last $k$ elements, which is computationally expensive.
* **Theoretical Space Complexity**: $O(N)$. The strategy stores the entire price history in a list, causing memory usage to grow linearly with input size.
* **Bottleneck**: The `self.history[-self.window_size:]` slicing operation creates a new copy of the list segment every single tick.

### WindowedMovingAverageStrategy (Optimized)
* **Theoretical Time Complexity**: $O(N)$ total ($O(1)$ per tick).
* **Theoretical Space Complexity**: $O(k)$, where $k$ is the window size (fixed).
* **Optimization Techniques**:
    * **Data Structure**: Uses `collections.deque` with a `maxlen` attribute to automatically handle the sliding window eviction in $O(1)$ time.
    * **Incremental Math**: Maintains a running `current_sum`. When a tick enters, we add it; when a tick leaves, we subtract it. No re-summing required.

## 3. Benchmark Results

### Runtime Performance (Seconds)

| Input Size (Ticks) | Naive Strategy (s) | Windowed Strategy (s) | Speedup Factor |
| :--- | :--- | :--- | :--- |
| 1,000 | 0.005384 | 0.001988 | 2.71x |
| 10,000 | 0.071911 | 0.007680 | 9.36x |
| 100,000 | 0.545964 | 0.266400 | 2.05x |

### Peak Memory Usage (MB)

*Note: The Windowed Strategy typically shows near 0.00 MB growth because it recycles a small, fixed amount of memory.*

| Input Size (Ticks) | Naive Strategy (MB) | Windowed Strategy (MB) |
| :--- | :--- | :--- |
| 1,000 | 0.1501 | 0.0011 |
| 10,000 | 0.2240 | 0.0011 |
| 100,000 | 0.9072 | 0.0011 |

## 4. Conclusion

The **WindowedMovingAverageStrategy** is the superior choice for production trading systems. By restricting memory usage to a fixed window $k$ and using constant-time updates, it ensures the system remains stable and responsive even when processing millions of ticks (e.g., high-frequency trading data). The Naive approach, while functionally correct, incurs technical debt through linear memory growth and redundant calculations.
