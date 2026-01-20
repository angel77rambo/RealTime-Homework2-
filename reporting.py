import matplotlib.pyplot as plt
import numpy as np

def plot_scaling(results: dict, filename: str = "complexity_analysis.png"):
    """
    Generates a side-by-side bar chart for Runtime and Memory.
    """
    sizes = results["sizes"]
    x = np.arange(len(sizes))
    width = 0.35
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
    
    # 1. Runtime Plot
    ax1.bar(x - width/2, results["naive_times"], width, label='Naive (O(N) Space)', color='#ff9999')
    ax1.bar(x + width/2, results["opt_times"], width, label='Windowed (O(1) Time)', color='#66b3ff')
    ax1.set_title('Runtime Scaling Analysis', fontsize=14)
    ax1.set_xlabel('Input Size (Ticks)', fontsize=12)
    ax1.set_ylabel('Execution Time (seconds)', fontsize=12)
    ax1.set_xticks(x)
    ax1.set_xticklabels(sizes)
    ax1.legend()
    ax1.grid(axis='y', linestyle='--', alpha=0.5)
    
    # 2. Memory Plot
    ax2.bar(x - width/2, results["naive_mems"], width, label='Naive (Full History)', color='#ff9999')
    ax2.bar(x + width/2, results["opt_mems"], width, label='Windowed (Fixed Buffer)', color='#66b3ff')
    ax2.set_title('Memory Usage Analysis', fontsize=14)
    ax2.set_xlabel('Input Size (Ticks)', fontsize=12)
    ax2.set_ylabel('Peak Memory Increase (MB)', fontsize=12)
    ax2.set_xticks(x)
    ax2.set_xticklabels(sizes)
    ax2.legend()
    ax2.grid(axis='y', linestyle='--', alpha=0.5)
    
    plt.tight_layout()
    plt.savefig(filename)
    print(f"Visualization saved as '{filename}'")

def generate_markdown(results: dict, filename: str = "complexity_report.md"):
    """
    Writes a comprehensive complexity report to markdown.
    """
    # Calculate speedup for the largest dataset
    last_idx = -1
    t_naive = results["naive_times"][last_idx]
    t_opt = results["opt_times"][last_idx]
    # Prevent division by zero
    speedup = t_naive / t_opt if t_opt > 1e-9 else 0
    
    md_content = f"""# Financial Signal Processing: Complexity Analysis Report

## 1. Executive Summary

This report analyzes the computational performance of two Moving Average trading strategies. The benchmarking results demonstrate that algorithmic choices significantly impact system scalability. Specifically, the **Windowed Strategy** outperforms the **Naive Strategy** by approximately **{speedup:.2f}x** in execution speed on large datasets while maintaining a near-zero memory footprint growth.

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
"""
    
    for i, size in enumerate(results["sizes"]):
        tn = results["naive_times"][i]
        to = results["opt_times"][i]
        # Avoid division by zero
        su = tn / to if to > 1e-9 else 0.0
        md_content += f"| {size:,} | {tn:.6f} | {to:.6f} | {su:.2f}x |\n"

    md_content += """
### Peak Memory Usage (MB)

*Note: The Windowed Strategy typically shows near 0.00 MB growth because it recycles a small, fixed amount of memory.*

| Input Size (Ticks) | Naive Strategy (MB) | Windowed Strategy (MB) |
| :--- | :--- | :--- |
"""

    for i, size in enumerate(results["sizes"]):
        mn = results["naive_mems"][i]
        mo = results["opt_mems"][i]
        # Format optimized memory to show <0.001 if very small
        mo_str = f"{mo:.4f}" if mo > 0.001 else "< 0.001"
        md_content += f"| {size:,} | {mn:.4f} | {mo_str} |\n"

    md_content += """
## 4. Conclusion

The **WindowedMovingAverageStrategy** is the superior choice for production trading systems. By restricting memory usage to a fixed window $k$ and using constant-time updates, it ensures the system remains stable and responsive even when processing millions of ticks (e.g., high-frequency trading data). The Naive approach, while functionally correct, incurs technical debt through linear memory growth and redundant calculations.
"""

    with open(filename, "w") as f:
        f.write(md_content)
    
    print(f"Report saved as '{filename}'")
