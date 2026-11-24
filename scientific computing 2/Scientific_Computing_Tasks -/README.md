
# BIT 2118: Scientific Computing — Repository Index

## 1. Course & Submission Guidelines
* **Course:** BIT 2118: Scientific Computing[cite: 2]
* **Group Work & Individual Submission:** Discussions are conducted as group work, while each student maintains and submits their own individual GitHub repository (group repositories should not be used)[cite: 2].
* **VLMS Submission:** Upload your GitHub repository link and documentation via VLMS[cite: 2].
* **Standard Task Requirements (A–E):** Each task addresses identifying inputs and mathematical operations, modifying at least one input/parameter and explaining how results change, explaining outputs and interpreting graphs where applicable, and modifying the program for a related real-world case with documented assumptions, input data, output, and interpretation[cite: 2].

---

## 2. Core Python Libraries & SciPy Submodules

### Python Libraries Used
| Library / Module | Purpose in Coursework | Common Functions Used |
| :--- | :--- | :--- |
| **NumPy** (`import numpy as np`) | Stores numerical data in arrays and performs fast vectorized calculations, matrix operations, and linear algebra[cite: 5]. | `np.array()`, `np.mean()`, `np.linalg.solve()`, `np.linalg.eig()`[cite: 5] |
| **SciPy** (`from scipy...`) | Provides scientific algorithms for equation solving, interpolation, curve fitting, integration, ODEs, and optimization[cite: 5]. | `root_scalar()`, `root()`, `curve_fit()`, `simpson()`, `solve_ivp()`, `minimize()`[cite: 5] |
| **Matplotlib** (`import matplotlib.pyplot as plt`) | Creates graphs for interpreting convergence, fitted curves, ODE behavior, interpolation, and simulation results[cite: 5]. | `plt.plot()`, `plt.scatter()`, `plt.xlabel()`, `plt.legend()`, `plt.show()`[cite: 5] |
| **timeit** (`import timeit`) | Measures execution time to compare Python loops against vectorized NumPy code[cite: 5]. | `timeit.timeit(function, number=1)`[cite: 5] |

### SciPy Submodules Referenced
| Submodule | Purpose | Key Functions | Related Task(s) |
| :--- | :--- | :--- | :--- |
| `scipy.linalg` | LU decomposition and repeated solutions of linear systems[cite: 5] | `lu_factor()`, `lu_solve()`[cite: 5] | Task 7 (in `Task A and F`)[cite: 3, 5] |
| `scipy.optimize` | Root finding, nonlinear systems, curve fitting, and optimization[cite: 5] | `root_scalar()`, `root()`, `curve_fit()`, `minimize()`[cite: 5] | Tasks 10–12, 14, 19[cite: 3, 4, 5] |
| `scipy.interpolate` | Estimation of values between measured data points[cite: 5] | `interp1d()`, `CubicSpline()`[cite: 5] | Task 13 (in `Task L and O`)[cite: 4, 5] |
| `scipy.integrate` | Numerical integration and numerical solution of differential equations[cite: 5] | `simpson()`, `solve_ivp()`[cite: 5] | Tasks 16, 18[cite: 4, 5] |

---

## 3. Detailed Task Directory & Index

### [Task A and F](./Task%20A%20and%20F/)
* **Task A (Task 2) — NumPy Arrays and Numerical Computation:** Covers 1-D vectors, 2-D matrices, and element-wise array operations (such as mean, min, max, and vectorized temperature unit conversion on IoT/weather readings)[cite: 3, 6].
  * *Example Applications:* Sensor readings from IoT devices, image pixels, network traffic measurements, scientific measurements, machine-learning feature matrices, and financial time-series[cite: 6].
* **Task F (Task 7) — Gaussian Elimination and LU Decomposition:** Covers transforming $Ax = b$ via elimination/back-substitution and factoring $A = LU$ (or $PA = LU$) so a single factored matrix can efficiently solve multiple right-hand-side vectors[cite: 3, 5, 13].
  * *Example Applications:* Engineering simulations, repeated linear-system solutions, finite-element methods, economic models, and scientific models with many equations[cite: 3, 13].

### [Task B](./Task%20B/)
* **Task B (Task 3) — Mathematical Functions and Vectorization:** Covers applying operations across entire arrays in a single vectorized expression instead of explicit Python loops, benchmarking runtime speed-ups on large datasets (such as latency measurements)[cite: 3, 5, 7].
  * *Example Applications:* Large datasets, simulations, signal processing, image processing, numerical models, and machine learning with repeated arithmetic operations[cite: 3, 7].

### [Task C and I](./Task%20C%20and%20I/)
* **Task C (Task 4) — Floating-Point Arithmetic and Numerical Errors:** Covers binary floating-point representation limits, absolute vs. relative error, truncation vs. round-off error, tolerance-based comparisons (`np.isclose()`), and numerically stable vs. unstable expressions[cite: 3, 8, 9].
  * *Example Applications:* Scientific simulations, banking calculations, GPS/navigation, engineering design, iterative algorithms, and systems sensitive to accumulated numerical error[cite: 3, 8].
* **Task I (Task 10) — Root Finding: Bisection and Fixed-Point Methods:** Covers bracketing sign changes on $[a, b]$ and halving intervals (bisection) alongside rearranging $f(x) = 0$ into $x = g(x)$ (fixed-point iteration) to find roots such as equilibrium temperatures[cite: 3, 17, 18].
  * *Example Applications:* Break-even points, engineering equations, interest rates, calibration, physical equilibrium, and threshold values[cite: 3, 17].

### [Task D and  J](./Task%20D%20and%20%20J/)
* **Task D (Task 5) — Matrix Algebra and Matrix Operations:** Covers row/column organization, matrix addition and multiplication, determinants, and inverses ($AA^{-1} = I$) applied to 2-D geometric transformations (rotation and scaling)[cite: 3, 10].
  * *Example Applications:* Computer graphics transformations, machine learning, cryptography, network models, robotics, electrical circuits, and solving systems of equations[cite: 3, 10].
* **Task J (Task 11) — Root Finding: Newton-Raphson and Secant Methods:** Covers tangent-line updates using derivatives (Newton-Raphson) and slope approximations from two recent points (secant method), applied to nonlinear financial/physical equations such as Internal Rate of Return (IRR)[cite: 3, 19, 20].
  * *Example Applications:* Circuit equations, optimization subproblems, financial rate calculations, nonlinear models, calibration, and solving physical equations[cite: 3, 19].

### [TASK E AND Q](./TASK%20E%20AND%20Q/)
* **Task E (Task 6) — Solution of Systems of Linear Equations:** Covers formulating and solving linear systems $Ax = b$ (`np.linalg.solve()`) and checking residuals/verification ($A\hat{x} \approx b$), such as server resource allocation[cite: 3, 5, 11, 12].
  * *Example Applications:* Electrical circuit analysis, resource allocation, traffic-flow models, balancing chemical equations, computer graphics, and parameter estimation[cite: 3, 11].
* **Task Q (Task 18) — Numerical Solution of ODEs Using SciPy:** Covers using `scipy.integrate.solve_ivp` with adaptive step control and tolerances to solve initial-value ODEs $\frac{dy}{dt} = f(t, y)$, such as RC circuit capacitor charging[cite: 4, 5, 27, 28].
  * *Example Applications:* Control systems, epidemiology, robotics, chemical reactions, electrical circuits, mechanical systems, and dynamic simulations[cite: 4, 27].

### [Task G](./Task%20G/)
* **Task G (Task 8) — Iterative Methods for Linear Systems:** Covers Jacobi and Gauss-Seidel iterative solvers starting from an initial guess and tracking iteration error until convergence within a tolerance, applied to sparse grid/temperature models[cite: 4, 14, 15].
  * *Example Applications:* Large sparse systems from heat transfer, electrical networks, structural models, image reconstruction, and scientific simulations where direct factorization may be expensive[cite: 4, 14].

### [Task H and R](./Task%20H%20and%20R/)
* **Task H (Task 9) — Eigenvalues and Eigenvectors:** Covers solving $Av = \lambda v$ (`np.linalg.eig()`) to analyze scaling/stretching along invariant directions and compute dominant eigenvector centrality on network adjacency matrices[cite: 3, 5, 16, 17].
  * *Example Applications:* PageRank concepts, vibration analysis, stability of dynamical systems, principal component analysis (PCA), image compression, quantum models, and network centrality[cite: 3, 4, 16].
* **Task R (Task 19) — Numerical Optimization:** Covers minimizing or maximizing objective functions subject to bounds and inequality/equality constraints (`scipy.optimize.minimize`), including checking discrete/integer alternatives such as server capacity allocation[cite: 4, 5, 29, 30].
  * *Example Applications:* Cloud resource allocation, network routing, machine-learning training, scheduling, engineering design, cost reduction, and parameter tuning[cite: 4, 29].

### [Task L and O](./Task%20L%20and%20O/)
* **Task L (Task 13) — Interpolation:** Covers estimating intermediate values between known measurements using linear interpolation (`interp1d`) and smooth cubic splines (`CubicSpline`), such as hourly-to-10-minute temperature resampling[cite: 4, 5, 21, 22].
  * *Example Applications:* Sensor calibration, missing measurement estimation, animation, geographic data, lookup tables, engineering tables, and resampling signals[cite: 4, 21].
* **Task O (Task 16) — Numerical Integration:** Covers approximating definite integrals/accumulated quantities from discrete samples using the trapezoidal rule (`np.trapezoid`) and Simpson's rule (`scipy.integrate.simpson`), such as electrical energy from power readings[cite: 4, 5, 25].
  * *Example Applications:* Energy consumption, distance from velocity data, probability calculations, signal energy, total flow, area, and accumulated quantities[cite: 4, 25].

### [Task M](./Task%20M/)
* **Task M (Task 14) — Curve Fitting and Approximation:** Covers least-squares parameter estimation (`scipy.optimize.curve_fit`) to fit a model curve to noisy empirical observations, evaluate RMSE/predictions, and plot observed vs. fitted curves (such as server response time vs. user load)[cite: 4, 5, 22, 23].
  * *Example Applications:* Trend estimation, calibration, performance modelling, growth curves, sensor models, demand forecasting, and experimental science[cite: 4, 22].

### [Task N](./Task%20N/)
* **Task N (Task 15) — Numerical Differentiation:** Covers estimating derivatives from discrete data using forward differences at the start, central differences in the interior, and backward differences at the end, such as estimating vehicle speed from GPS position samples[cite: 4, 23, 24].
  * *Example Applications:* Estimating speed from position data, acceleration from velocity, gradients in optimization, rates of change in sensors, and sensitivity analysis[cite: 4, 23].

### [Task P](./Task%20P/)
* **Task P (Task 17) — Ordinary Differential Equations — Euler Method:** Covers stepping forward from an initial condition via $y_{n+1} = y_n + h\,f(t_n, y_n)$ and comparing step sizes ($h$) against analytical solutions, applied to cooling curves and RC charging[cite: 4, 26, 27].
  * *Example Applications:* Population growth, cooling, charging capacitors, motion, epidemic models, and other systems that evolve over time[cite: 4, 26].

### [Task S](./Task%20S/)
* **Task S (Task 20) — Random Numbers and Monte Carlo Methods:** Covers estimating probabilities and quantities via repeated random sampling (`np.random.default_rng`) and tracking running convergence across simulation counts $N$, such as server overload risk[cite: 4, 31, 32].
  * *Example Applications:* Risk analysis, reliability, queue simulation, finance, uncertainty analysis, computer graphics, physical simulations, and estimating difficult integrals[cite: 4, 31].

### [Task_K](./Task_K/)
* **Task_K (Task 12) — Polynomial and Nonlinear Equation Solving:** Covers solving systems of polynomial and nonlinear equations (`scipy.optimize.root`) from multiple initial guesses and verifying near-zero residuals, such as intersections between a circle and a parabola[cite: 4, 5, 20, 21].
  * *Example Applications:* Kinematics, chemical equilibrium, geometric intersection, control systems, calibration, and finding operating points in nonlinear models[cite: 4, 20].

```

