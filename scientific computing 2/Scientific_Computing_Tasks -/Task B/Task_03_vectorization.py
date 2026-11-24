import numpy as np
import timeit
import matplotlib.pyplot as plt

# ==========================================
# REQUIREMENT B: Baseline Vectorization Task
# ==========================================

# Simulated network latency readings in milliseconds (1,000,000 samples)
rng = np.random.default_rng(42)
latency_ms = rng.uniform(5, 250, 1_000_000)


def loop_version(data_ms):
    squared = []
    for value in data_ms:
        seconds = value / 1000.0
        squared.append(seconds ** 2)
    return np.array(squared)


def vectorized_version(data_ms):
    seconds = data_ms / 1000.0
    return seconds ** 2


loop_time = timeit.timeit(lambda: loop_version(latency_ms), number=1)
vector_time = timeit.timeit(lambda: vectorized_version(latency_ms), number=3) / 3
result = vectorized_version(latency_ms)

print("First five squared latency values:", result[:5])
print(f"Loop time: {loop_time:.4f} s")
print(f"Vectorized time: {vector_time:.4f} s")
print(f"Approximate speed-up: {loop_time / vector_time:.1f}x")

# ==========================================
# REQUIREMENT C: Parameter Modification (Sample Size N)
# ==========================================

sample_sizes = [10_000, 100_000, 500_000, 1_000_000]
loop_times = []
vec_times = []

for n in sample_sizes:
    sample_data = rng.uniform(5, 250, n)
    t_loop = timeit.timeit(lambda: loop_version(sample_data), number=1)
    t_vec = timeit.timeit(lambda: vectorized_version(sample_data), number=3) / 3
    loop_times.append(t_loop)
    vec_times.append(t_vec)
    print(f"N={n}: Loop={t_loop:.4f}s, Vectorized={t_vec:.4f}s, Speed-up={t_loop / t_vec:.1f}x")

# ==========================================
# REQUIREMENT D: Graphical Comparison Plot
# ==========================================

plt.figure(figsize=(8, 5))
plt.plot(sample_sizes, loop_times, marker="o", label="Python Loop")
plt.plot(sample_sizes, vec_times, marker="s", label="NumPy Vectorized")
plt.xlabel("Number of Latency Samples (N)")
plt.ylabel("Execution Time (seconds)")
plt.title("Loop vs. Vectorized Execution Time (Task B)")
plt.legend()
plt.grid(True)
plt.savefig("images/task_b_runtime_comparison.png", dpi=300, bbox_inches="tight")
plt.show()