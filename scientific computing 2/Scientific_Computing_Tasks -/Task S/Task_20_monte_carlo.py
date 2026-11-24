import numpy as np
import matplotlib.pyplot as plt

# ==========================================
# REQUIREMENT B: Baseline Monte Carlo Task
# ==========================================

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

# ==========================================
# REQUIREMENT C: Parameter Modification (Higher Demand Volatility)
# ==========================================

std_demand_high = 180.0
demand_high = rng.normal(mean_demand, std_demand_high, N)
overloaded_high = demand_high > capacity
overload_prob_high = overloaded_high.mean()

print(f"Modified std={std_demand_high} overload probability: {overload_prob_high:.4%}")
print(f"Overload cases under higher volatility: {overloaded_high.sum()} out of {N}")

# ==========================================
# REQUIREMENT D: Graphical Convergence Plot
# ==========================================

plt.figure(figsize=(8, 5))
plt.semilogx(indices + 1, running_probability[indices], label=f"Baseline (std={std_demand})")
plt.xlabel("Number of simulations")
plt.ylabel("Estimated overload probability")
plt.title("Monte Carlo estimate of server-overload risk")
plt.legend()
plt.grid(True)
plt.savefig("images/task_s_overload_convergence.png", dpi=300, bbox_inches="tight")
plt.show()