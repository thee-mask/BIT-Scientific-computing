import numpy as np

# ==========================================
# REQUIREMENT E: Real-World RC Circuit Charging
# ==========================================

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