
### 3. Complete `README.md` for Task S (`task-s/README.md`)

```markdown
# BIT 2118: Scientific Computing - Task S: Random Numbers and Monte Carlo Methods

## Table of Contents
1. [Overview & Concept](#1-overview--concept)
2. [Requirement B: Identification of Inputs and Mathematical Operations](#2-requirement-b-identification-of-inputs-and-mathematical-operations)
3. [Requirement C: Parameter Modification & Result Analysis](#3-requirement-c-parameter-modification--result-analysis)
4. [Requirement D: Output Interpretation & Graphical Analysis](#4-requirement-d-output-interpretation--graphical-analysis)
5. [Requirement E: Real-World Modification (Delivery SLA Breach Probability)](#5-requirement-e-real-world-modification-delivery-sla-breach-probability)

---

## 1. Overview & Concept

Monte Carlo methods estimate probabilities and numerical quantities through repeated random sampling. As the number of simulated scenarios $N$ increases, the sample proportion converges toward the true underlying probability.

---

## 2. Requirement B: Identification of Inputs and Mathematical Operations

### 2.1 Inputs and Mathematical Operations
* **Inputs:** Server capacity $= 1000.0$, normal demand mean $\mu = 850.0$, standard deviation $\sigma = 120.0$, $N = 100{,}000$ trials, and generator seed `42`.
* **Mathematical Operations:** Generates $N$ random demand samples $D_i \sim \mathcal{N}(\mu, \sigma^2)$, checks overload conditions $D_i > 1000.0$, calculates overload probability as the mean of overload indicators, and computes cumulative running probability across trials.

### 2.2 Baseline Implementation Code (`code/Task_20_monte_carlo.py`)
```python
import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(42)
capacity = 1000.0
mean_demand = 850.0
std_demand = 120.0
N = 100_000

# Random demand scenarios
demand = rng.normal(mean_demand, std_demand, N)
overloaded = demand > capacity
overload_probability = overloaded.mean()

print(f"Estimated overload probability: {overload_probability:.4%}")
print(f"Number of overload cases: {overloaded.sum()} out of {N}")

# Running probability to show convergence
running_probability = np.cumsum(overloaded) / np.arange(1, N + 1)
indices = np.unique(np.logspace(1, np.log10(N), 200).astype(int)) - 1

```

---

## 3. Requirement C: Parameter Modification & Result Analysis

### 3.1 Parameter Modification

We increase demand variability from `std_demand = 120.0` to `std_demand_high = 180.0` while keeping server capacity at $1000.0$ and mean demand at $850.0$.

### 3.2 Parameter Modification Code

```python
std_demand_high = 180.0
demand_high = rng.normal(mean_demand, std_demand_high, N)
overloaded_high = demand_high > capacity
overload_prob_high = overloaded_high.mean()

print(f"Modified std={std_demand_high} overload probability: {overload_prob_high:.4%}")
print(f"Overload cases under higher volatility: {overloaded_high.sum()} out of {N}")

```

* **Effect of Changing Standard Deviation:** Raising $\sigma$ spreads demand further into the upper tail above $1000.0$, increasing both the number of overload scenarios and the estimated overload probability.

---

## 4. Requirement D: Output Interpretation & Graphical Analysis

### 4.1 Output & Plotting Code

```python
plt.figure(figsize=(8, 5))
plt.semilogx(indices + 1, running_probability[indices], label=f"Baseline (std={std_demand})")
plt.xlabel("Number of simulations")
plt.ylabel("Estimated overload probability")
plt.title("Monte Carlo estimate of server-overload risk")
plt.legend()
plt.grid(True)
plt.savefig("images/task_s_overload_convergence.png", dpi=300, bbox_inches="tight")
plt.show()

```

* **Meaning of Output & Graph:** The running probability fluctuates noticeably with small sample sizes and settles around a steady estimate as the simulation count increases on the logarithmic horizontal axis.

> **Monte Carlo Convergence Plot:**
> 

---

## 5. Requirement E: Real-World Modification (Delivery SLA Breach Probability)

### 5.1 Assumptions and Input Data

* **Assumptions:** Parcel transit times follow a normal distribution with mean $40.0\,\text{hours}$ and standard deviation $6.0\,\text{hours}$, and a delivery breaches the SLA if transit time exceeds $48.0\,\text{hours}$.


* **Input Data:** $100{,}000$ simulated transit times drawn with seed `2026`.

### 5.2 Real-World Modification Code (`code/task_s_delivery_delay.py`)

```python
import numpy as np

# Assumptions:
# 1. Total delivery transit time (hours) follows a normal distribution with mean 40.0 h
#    and standard deviation 6.0 h across independent shipments.
# 2. Service Level Agreement (SLA) threshold is 48.0 hours.
# 3. Simulation uses 100,000 simulated shipments with seed 2026.

rng = np.random.default_rng(2026)
sla_hours = 48.0
mean_transit_h = 40.0
std_transit_h = 6.0
num_shipments = 100_000

transit_times = rng.normal(mean_transit_h, std_transit_h, num_shipments)
late_shipments = transit_times > sla_hours
breach_probability = late_shipments.mean()

print(f"Estimated SLA breach probability (> {sla_hours}h): {breach_probability:.4%}")
print(f"Late shipments: {late_shipments.sum()} out of {num_shipments}")

```

### 5.3 Output and Interpretation

The estimated breach probability quantifies how often deliveries exceed the $48$-hour SLA threshold under normal transit variability, helping operations teams assess delay risk.

```

---



```