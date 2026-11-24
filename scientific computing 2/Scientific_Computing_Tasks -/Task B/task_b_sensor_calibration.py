import numpy as np
import timeit

# ==========================================
# REQUIREMENT E: Real-World IoT Sensor Batch Processing
# ==========================================

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