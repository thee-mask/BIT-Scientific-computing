import numpy as np

# ==========================================
# REQUIREMENT E: Real-World Delivery SLA Risk
# ==========================================

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