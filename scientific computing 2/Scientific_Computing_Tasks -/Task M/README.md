### 3. Complete `README.md` for Task M (`task-m/README.md`)

```markdown
# BIT 2118: Scientific Computing - Task M: Curve Fitting and Approximation

## Table of Contents
1. [Overview & Concept](#1-overview--concept)
2. [Requirement B: Identification of Inputs and Mathematical Operations](#2-requirement-b-identification-of-inputs-and-mathematical-operations)
3. [Requirement C: Parameter Modification & Result Analysis](#3-requirement-c-parameter-modification--result-analysis)
4. [Requirement D: Output Interpretation & Graphical Analysis](#4-requirement-d-output-interpretation--graphical-analysis)
5. [Requirement E: Real-World Modification (Electricity Demand vs. Temperature)](#5-requirement-e-real-world-modification-electricity-demand-vs-temperature)

---

## 1. Overview & Concept

Curve fitting estimates parameters of a mathematical model so a function closely follows observed data, typically by minimizing the sum of squared residuals $\sum (y_i - \hat{y}_i)^2$ using least squares (`scipy.optimize.curve_fit`)[cite: 20].

---

## 2. Requirement B: Identification of Inputs and Mathematical Operations

### 2.1 Inputs and Mathematical Operations
* **Inputs:** Concurrent user counts `users = [50, 100, 150, 200, 250, 300, 350]` and measured server response times `response_ms = [82, 95, 115, 145, 185, 238, 305]` ($\text{ms}$)[cite: 20, 21].
* **Mathematical Operations:** Fits the quadratic model $y = ax^2 + bx + c$ via least squares, computes fitted predictions $\hat{y}_i$, evaluates Root Mean Square Error $\text{RMSE} = \sqrt{\frac{1}{n}\sum (y_i - \hat{y}_i)^2}$, and predicts response time at $400$ concurrent users[cite: 20, 21].

### 2.2 Baseline Implementation Code (`code/Task_14_curve_fitting.py`)
```python
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# Concurrent users and measured server response time (milliseconds)
users = np.array([50, 100, 150, 200, 250, 300, 350], dtype=float)
response_ms = np.array([82, 95, 115, 145, 185, 238, 305], dtype=float)


def model(x, a, b, c):
    return a * x ** 2 + b * x + c


parameters, covariance = curve_fit(model, users, response_ms)
a, b, c = parameters
predicted = model(users, a, b, c)
rmse = np.sqrt(np.mean((response_ms - predicted) ** 2))

print(f"Fitted model: y = {a:.6f}x^2 + {b:.4f}x + {c:.2f}")
print(f"RMSE: {rmse:.2f} ms")
print(f"Predicted response at 400 users: {model(400, a, b, c):.2f} ms")

```

---

## 3. Requirement C: Parameter Modification & Result Analysis

### 3.1 Parameter Modification

We increase the prediction load from $400$ users to `target_users = 500` to examine projected latency under higher concurrency.

### 3.2 Parameter Modification Code

```python
target_users = 500
print(f"Predicted response at {target_users} users (extrapolated): {model(target_users, a, b, c):.2f} ms")

```

* **Effect of Changing Target Users:** Because the quadratic term $ax^2$ grows faster than linearly at higher loads, extending the prediction to $500$ users yields a markedly steeper increase in predicted response time than at lower user counts, while extrapolating beyond $350$ users adds modeling uncertainty.



---

## 4. Requirement D: Output Interpretation & Graphical Analysis

### 4.1 Output & Plotting Code

```python
x_plot = np.linspace(users.min(), target_users, 300)
plt.figure(figsize=(8, 5))
plt.scatter(users, response_ms, label="Measurements")
plt.plot(x_plot, model(x_plot, a, b, c), label="Fitted curve")
plt.xlabel("Concurrent users")
plt.ylabel("Response time (ms)")
plt.title("Server response-time curve fitting")
plt.legend()
plt.grid(True)
plt.savefig("images/task_m_curve_fit.png", dpi=300, bbox_inches="tight")
plt.show()

```

* **Meaning of Output & Graph:** The small RMSE shows that the quadratic curve aligns closely with the measured latency points, illustrating accelerating response times as concurrent traffic increases.



> **Curve Fitting Plot:**
> 

---

## 5. Requirement E: Real-World Modification (Electricity Demand vs. Temperature)

### 5.1 Assumptions and Input Data

* **Assumptions:** Peak daily electricity demand ($\text{MW}$) increases quadratically with higher ambient temperatures ($^\circ\text{C}$) due to cooling loads.


* **Input Data:** `ambient_temp_c = [18.0, 21.0, 24.0, 27.0, 30.0, 33.0, 36.0]` and `peak_demand_mw = [120.0, 128.0, 141.0, 160.0, 185.0, 216.0, 253.0]`.

### 5.2 Real-World Modification Code (`code/task_m_energy_demand.py`)

```python
import numpy as np
from scipy.optimize import curve_fit

# Assumptions:
# 1. Daily peak electricity demand (MW) increases quadratically at higher ambient temperatures
#    due to cooling/HVAC loads.
# 2. Model form: D(T) = a * T^2 + b * T + c.

ambient_temp_c = np.array([18.0, 21.0, 24.0, 27.0, 30.0, 33.0, 36.0], dtype=float)
peak_demand_mw = np.array([120.0, 128.0, 141.0, 160.0, 185.0, 216.0, 253.0], dtype=float)


def demand_model(temp, a, b, c):
    return a * temp ** 2 + b * temp + c


params, _ = curve_fit(demand_model, ambient_temp_c, peak_demand_mw)
a_fit, b_fit, c_fit = params
pred_mw = demand_model(ambient_temp_c, a_fit, b_fit, c_fit)
rmse_mw = np.sqrt(np.mean((peak_demand_mw - pred_mw) ** 2))

print(f"Fitted demand model: D(T) = {a_fit:.4f}T^2 + {b_fit:.4f}T + {c_fit:.2f}")
print(f"Fit RMSE: {rmse_mw:.2f} MW")
print(f"Estimated peak demand at 38 C: {demand_model(38.0, a_fit, b_fit, c_fit):.2f} MW")

```

### 5.3 Output and Interpretation

The fitted quadratic curve models rising peak electricity demand during warmer conditions and estimates expected peak load at 38 degree celcius for capacity planning.

```

---



```