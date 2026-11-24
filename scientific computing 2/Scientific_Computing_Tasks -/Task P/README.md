

```markdown
# BIT 2118: Scientific Computing - Task P: Ordinary Differential Equations - Euler Method

## Table of Contents
1. [Overview & Concept](#1-overview--concept)
2. [Requirement B: Identification of Inputs and Mathematical Operations](#2-requirement-b-identification-of-inputs-and-mathematical-operations)
3. [Requirement C: Parameter Modification & Result Analysis](#3-requirement-c-parameter-modification--result-analysis)
4. [Requirement D: Output Interpretation & Graphical Analysis](#4-requirement-d-output-interpretation--graphical-analysis)
5. [Requirement E: Real-World Modification (RC Circuit Charging)](#5-requirement-e-real-world-modification-rc-circuit-charging)

---

## 1. Overview & Concept

Euler's method approximates the solution of an ordinary differential equation $\frac{dy}{dt} = f(t, y)$ with initial value $y(t_0) = y_0$ by stepping forward in time using discrete increments $h$[cite: 25]:

$$y_{n+1} = y_n + h \, f(t_n, y_n)$$

---

## 2. Requirement B: Identification of Inputs and Mathematical Operations

### 2.1 Inputs and Mathematical Operations
* **Inputs:** Ambient temperature $T_{\text{ambient}} = 25.0\,^\circ\text{C}$, initial temperature $T_{\text{initial}} = 90.0\,^\circ\text{C}$, cooling constant $k = 0.12\,\text{min}^{-1}$, step size $h = 1.0\,\text{min}$, and time range $0$ to $30\,\text{min}$[cite: 25].
* **Mathematical Operations:** Evaluates $\frac{dT}{dt} = -k(T - T_{\text{ambient}})$, updates temperature via $T_{i+1} = T_i + h\left[-k(T_i - T_{\text{ambient}})\right]$, and compares against the exact solution $T_{\text{exact}}(t) = T_{\text{ambient}} + (T_0 - T_{\text{ambient}})e^{-kt}$[cite: 25].

### 2.2 Baseline Implementation Code (`code/Task_17_euler_ode.py`)
```python
import numpy as np
import matplotlib.pyplot as plt

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

```

---

## 3. Requirement C: Parameter Modification & Result Analysis

### 3.1 Parameter Modification

We reduce the time step from $h = 1.0\,\text{min}$ to `h_fine = 0.25` min across the same $30$-minute period.

### 3.2 Parameter Modification Code

```python
h_fine = 0.25
time_fine = np.arange(0, end_time + h_fine, h_fine)
temp_fine = np.zeros_like(time_fine)
temp_fine[0] = T_initial

for i in range(len(time_fine) - 1):
    temp_fine[i + 1] = temp_fine[i] + h_fine * cooling_rate(temp_fine[i])

exact_fine = T_ambient + (T_initial - T_ambient) * np.exp(-k * time_fine)
print(f"Fine step (h={h_fine}) Euler temp at 30 min: {temp_fine[-1]:.2f} C")
print(f"Fine step final absolute error: {abs(temp_fine[-1] - exact_fine[-1]):.4f} C")

```

* **Effect of Changing Step Size $h$:** Smaller step sizes reduce truncation error and move the Euler approximation closer to the exact cooling curve, at the cost of more iterations.



---

## 4. Requirement D: Output Interpretation & Graphical Analysis

### 4.1 Output & Plotting Code

```python
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

```

* **Meaning of Output & Graph:** Temperature cools exponentially from $90.0\,^\circ\text{C}$ toward the $25.0\,^\circ\text{C}$ ambient temperature, with the finer step curve following the exact solution more closely.



> **Cooling Curve Plot:**
> 

---

## 5. Requirement E: Real-World Modification (RC Circuit Charging)

### 5.1 Assumptions and Input Data

* **Assumptions:** A capacitor starting at $0.0\,\text{V}$ charges through a $2000\,\Omega$ resistor from a $12.0\,\text{V}$ source with capacitance $C = 0.001\,\text{F}$ over $10.0\,\text{s}$ using $\Delta t = 0.1\,\text{s}$.


* **Input Data:** $\frac{dV}{dt} = \frac{V_s - V}{RC}$ with $V_s = 12.0$, $R = 2000.0$, and $C = 0.001$.



### 5.2 Real-World Modification Code (`code/task_p_capacitor_charge.py`)

```python
import numpy as np

# Assumptions:
# 1. Series RC circuit charged by a constant source V_s = 12.0 V.
# 2. Resistance R = 2000 ohms, Capacitance C = 0.001 F (time constant tau = R*C = 2.0 s).
# 3. Differential equation: dV/dt = (V_s - V) / (R * C), starting at V(0) = 0.0 V.

V_source = 12.0
resistance = 2000.0
capacitance = 0.001
dt = 0.1
t_end = 10.0

t_vals = np.arange(0.0, t_end + dt, dt)
v_euler = np.zeros_like(t_vals)
v_euler[0] = 0.0

for i in range(len(t_vals) - 1):
    dv_dt = (V_source - v_euler[i]) / (resistance * capacitance)
    v_euler[i + 1] = v_euler[i] + dt * dv_dt

v_exact = V_source * (1.0 - np.exp(-t_vals / (resistance * capacitance)))

print(f"Capacitor voltage at t={t_end}s (Euler): {v_euler[-1]:.4f} V")
print(f"Capacitor voltage at t={t_end}s (Exact): {v_exact[-1]:.4f} V")
print(f"Final absolute error: {abs(v_euler[-1] - v_exact[-1]):.4f} V")

```

### 5.3 Output and Interpretation

The capacitor voltage rises smoothly over time and approaches the $12.0\,\text{V}$ supply voltage as $t$ spans multiple time constants ($\tau = 2.0\,\text{s}$).

```

```