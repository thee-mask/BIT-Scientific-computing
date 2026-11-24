Here is the complete **Task B** documentation in a single copy-paste block for `task-b/README.md`, including everything from Requirements B, C, D, and E along with the full Python code blocks:

```markdown
# BIT 2118: Scientific Computing - Task B: Mathematical Functions and Vectorization

## Table of Contents
1. [Overview & Concept](#1-overview--concept)
2. [Requirement B: Identification of Inputs and Mathematical Operations](#2-requirement-b-identification-of-inputs-and-mathematical-operations)
3. [Requirement C: Parameter Modification & Result Analysis](#3-requirement-c-parameter-modification--result-analysis)
4. [Requirement D: Output Interpretation & Graphical Analysis](#4-requirement-d-output-interpretation--graphical-analysis)
5. [Requirement E: Real-World Modification (IoT Sensor Calibration)](#5-requirement-e-real-world-modification-iot-sensor-calibration)

---

## 1. Overview & Concept

Vectorization applies a mathematical operation to many values at once instead of stepping through elements one by one in a Python loop[cite: 12]. Using NumPy array operations executes element-wise calculations efficiently across large datasets[cite: 10, 12].

---

## 2. Requirement B: Identification of Inputs and Mathematical Operations

### 2.1 Inputs and Mathematical Operations
* **Input:** `latency_ms`, an array of $1{,}000{,}000$ simulated network latency readings in $[5, 250]\,\text{ms}$ generated using NumPy's `default_rng(42)`[cite: 12].
* **Mathematical Operations:**
  1. Convert each latency reading from milliseconds to seconds: $s_i = \frac{L_i}{1000.0}$[cite: 12]
  2. Square each converted value for error calculation: $y_i = s_i^2$[cite: 12]

### 2.2 Baseline Implementation Code (`code/Task_03_vectorization.py`)
```python
import numpy as np
import timeit
import matplotlib.pyplot as plt

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

```

---

## 3. Requirement C: Parameter Modification & Result Analysis

### 3.1 Parameter Modification

We vary the sample count $N$ across $[10{,}000,\; 100{,}000,\; 500{,}000,\; 1{,}000{,}000]$ to compare how execution time and speed-up scale with dataset size.

### 3.2 Parameter Modification Code

```python
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

```

* **Effect of Changing $N$:** Increasing $N$ increases total runtime for both approaches, but the explicit Python loop grows much faster than the vectorized NumPy operation, producing a clear speed-up advantage on larger arrays.



---

## 4. Requirement D: Output Interpretation & Graphical Analysis

### 4.1 Output & Plotting Code

```python
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

```

* **Meaning of Output & Graph:** Both functions produce the same squared latency values in $\text{s}^2$, while the graph shows the vectorized execution line staying near zero seconds compared to the rising runtime of the Python loop as $N$ grows.



> **Runtime Comparison Plot:**
> 

---

## 5. Requirement E: Real-World Modification (IoT Sensor Calibration)

### 5.1 Assumptions and Input Data

* **Assumptions:** An IoT temperature sensor produces readings in $[500, 1500]\,\text{mV}$ across $500{,}000$ samples, converted via $T = \frac{V - 500.0}{10.0}$ ($^\circ\text{C}$), and evaluated by squared deviation $(T - 25.0)^2$ from a $25.0\,^\circ\text{C}$ nominal reference.


* **Input Data:** `voltage_mv = rng.uniform(500.0, 1500.0, 500_000)` generated with seed `101`.



### 5.2 Real-World Modification Code (`code/task_b_sensor_calibration.py`)

```python
import numpy as np
import timeit

# Assumptions:
# 1. IoT analog temperature sensor outputs voltage in millivolts (mV) in [500 mV, 1500 mV].
# 2. Linear calibration equation: T_celsius = (voltage_mv - 500.0) / 10.0.
# 3. Squared deviation from nominal 25.0 C setpoint is computed for anomaly monitoring.

rng = np.random.default_rng(101)
voltage_mv = rng.uniform(500.0, 1500.0, 500_000)
nominal_temp_c = 25.0


def calibrate_loop(voltages):
    sq_deviations = []
    for v in voltages:
        temp_c = (v - 500.0) / 10.0
        sq_deviations.append((temp_c - nominal_temp_c) ** 2)
    return np.array(sq_deviations)


def calibrate_vectorized(voltages):
    temp_c = (voltages - 500.0) / 10.0
    return (temp_c - nominal_temp_c) ** 2


t_loop = timeit.timeit(lambda: calibrate_loop(voltage_mv), number=1)
t_vec = timeit.timeit(lambda: calibrate_vectorized(voltage_mv), number=3) / 3
deviations = calibrate_vectorized(voltage_mv)

print(f"First 5 calibrated squared deviations: {deviations[:5]}")
print(f"Mean squared deviation from 25 C: {np.mean(deviations):.2f}")
print(f"Loop execution time: {t_loop:.4f} s")
print(f"Vectorized execution time: {t_vec:.4f} s")
print(f"Speed-up factor: {t_loop / t_vec:.1f}x")

```

### 5.3 Output and Interpretation

Vectorized expressions compute calibrated sensor values and squared deviations across $500{,}000$ samples significantly faster than an explicit loop, supporting faster processing of high-volume IoT telemetry.

```

```