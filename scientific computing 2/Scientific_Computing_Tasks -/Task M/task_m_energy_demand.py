import numpy as np
from scipy.optimize import curve_fit

# ==========================================
# REQUIREMENT E: Real-World Electricity Demand Model
# ==========================================

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