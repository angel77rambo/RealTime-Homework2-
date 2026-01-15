import matplotlib.pyplot as plt


def plot_runtime(sizes, naive_times, optimized_times):
    plt.figure()
    plt.plot(sizes, naive_times, label="Naive Strategy")
    plt.plot(sizes, optimized_times, label="Optimized Strategy")
    plt.xlabel("Input Size")
    plt.ylabel("Runtime (seconds)")
    plt.title("Runtime Scaling")
    plt.legend()
    plt.show()


def plot_memory(sizes, naive_memory, optimized_memory):
    plt.figure()
    plt.plot(sizes, naive_memory, label="Naive Strategy")
    plt.plot(sizes, optimized_memory, label="Optimized Strategy")
    plt.xlabel("Input Size")
    plt.ylabel("Peak Memory Usage (MB)")
    plt.title("Memory Usage Scaling")
    plt.legend()
    plt.show()
