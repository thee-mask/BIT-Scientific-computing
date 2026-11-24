import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import root

# ------------------------------------------------------------
# Modified case: where does a curved road enter and leave the
# coverage area of a mobile network tower?
# Tower at the origin (0, 0), coverage radius R km (circle):
#     x^2 + y^2 = R^2
# Road shaped like a parabola (km):
#     y = a*x^2 + c
# ------------------------------------------------------------

R = 5.0     # coverage radius in km (assumed)
a = 0.2     # how sharply the road curves (assumed)
c = -3.0    # road height at x = 0, in km (assumed)

def equations(z):
    x, y = z
    return [
        x**2 + y**2 - R**2,
        y - (a * x**2 + c)
    ]

found = []
for guess in ([4.0, 1.0], [-4.0, 1.0], [0.0, -5.0]):
    sol = root(equations, guess)
    print("Initial guess:", guess)
    print("Point found:", np.round(sol.x, 4))
    print("Residuals:", np.round(equations(sol.x), 10))
    print("Converged:", sol.success)
    print()
    # keep only true solutions, and avoid listing the same point twice
    if sol.success and not any(np.allclose(sol.x, p, atol=1e-6) for p in found):
        found.append(sol.x)

print("Coverage boundary crossings (x, y) in km:")
for p in found:
    print(f"  ({p[0]:.3f}, {p[1]:.3f})")

if len(found) == 2:
    length = abs(found[0][0] - found[1][0])
    print(f"Horizontal distance between the two crossings: {length:.3f} km")

# Graph
theta = np.linspace(0, 2 * np.pi, 400)
xs = np.linspace(-6, 6, 400)

plt.figure(figsize=(6, 6))
plt.plot(R * np.cos(theta), R * np.sin(theta), label="Tower coverage (circle)")
plt.plot(xs, a * xs**2 + c, label="Road (parabola)")
for p in found:
    plt.plot(p[0], p[1], "ro")
    plt.annotate(f"({p[0]:.2f}, {p[1]:.2f})", p, textcoords="offset points", xytext=(6, 6))
plt.plot(0, 0, "k^", label="Tower")
plt.axis("equal")
plt.xlim(-6, 6)
plt.ylim(-6, 6)
plt.xlabel("x (km)")
plt.ylabel("y (km)")
plt.title("Road crossing the tower's coverage area")
plt.grid(True)
plt.legend(loc="lower right")

# Save BEFORE show(), otherwise the saved image is blank
plt.savefig("outputs/task12_modified_graph.png", dpi=150)
plt.show()
