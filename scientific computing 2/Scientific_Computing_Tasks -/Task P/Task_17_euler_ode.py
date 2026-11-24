import numpy as np
import matplotlib.pyplot as plt

# ==========================================
# REQUIREMENT B: Baseline Euler ODE Cooling Task
# ==========================================

# Newton's law of cooling: dT/dt = -k * (T - T_ambient)
T_ambient = 25.0
T_initial = 90.0
k = 0.12
h = 1.0       # step size in minutes
end_time = 30.0


def cooling_rate(T):
    return -k * (T - T_ambient)


time = np.arange(0, end_time + h, h)
temperature = np.zeros_like(time)
temperature[0] = T_initial

for i in range(len(time) - 1):
    temperature[i + 1] = temperature[i] + h * cooling_rate(temperature[i])

# Exact analytical solution for validation
exact = T_ambient + (T_initial - T_ambient) * np.exp(-k * time)

print(f"Euler temperature after 30 min: {temperature[-1]:.2f} C")
print(f"Exact temperature after 30 min: {exact[-1]:.2f} C")
print(f"Final absolute error: {abs(temperature[-1] - exact[-1]):.4f} C")

# ==========================================
# REQUIREMENT C: Parameter Modification (Step Size h = 0.25 min)
# ==========================================

h_fine = 0.25
time_fine = np.arange(0, end_time + h_fine, h_fine)
temp_fine = np.zeros_like(time_fine)
temp_fine[0] = T_initial

for i in range(len(time_fine) - 1):
    temp_fine[i + 1] = temp_fine[i] + h_fine * cooling_rate(temp_fine[i])

exact_fine = T_ambient + (T_initial - T_ambient) * np.exp(-k * time_fine)
print(f"Fine step (h={h_fine}) Euler temp at 30 min: {temp_fine[-1]:.2f} C")
print(f"Fine step final absolute error: {abs(temp_fine[-1] - exact_fine[-1]):.4f} C")

# ==========================================
# REQUIREMENT D: Graphical Comparison Plot
# ==========================================

plt.figure(figsize=(8, 5))
plt.plot(time, temperature, marker="o", label=f"Euler (h={h} min)")
plt.plot(time_fine, temp_fine, linestyle="-.", label=f"Euler (h={h_fine} min)")
plt.plot(time, exact, linestyle="--", label="Exact solution")
plt.xlabel("Time (minutes)")
plt.ylabel("Temperature (C)")
plt.title("Cooling of a hot object (Task P)")
plt.legend()
plt.grid(True)
plt.savefig("images/task_p_cooling_curve.png", dpi=300, bbox_inches="tight")
plt.show()