# BIT 2118: Scientific Computing — Group Work Documentation (Tasks H & R)

**Course:** BIT 2118 — Scientific Computing  
**Submission Components:** Tasks H (Eigenvalues and Eigenvectors) and R (Numerical Optimization)  
**Repository Structure:** Individual GitHub repository ready (`Task_H_Eigenvalues/`, `Task_R_Optimization/`, `README.md`)

---

## Folder Structure

```text
H R/
├── README.md
├── Task_H_Eigenvalues/
│   ├── task_h_base.py
│   ├── task_h_base_plot.png
│   ├── task_h_param_modified.py
│   ├── task_h_param_plot.png
│   ├── task_h_realworld_pagerank.py
│   └── task_h_realworld_plot.png
└── Task_R_Optimization/
    ├── task_r_base.py
    ├── task_r_base_plot.png
    ├── task_r_param_modified.py
    ├── task_r_param_plot.png
    ├── task_r_realworld_fertilizer.py
    └── task_r_realworld_plot.png
```

---

## Task H: Eigenvalues and Eigenvectors (Network Centrality)

### 1. Requirement B: Input Values & Mathematical Operations
* **Input Values:** A $4 \times 4$ symmetric binary adjacency matrix $A$ representing an undirected network of nodes $A, B, C, D$:
  $$A = \begin{bmatrix} 0 & 1 & 1 & 0 \\ 1 & 0 & 1 & 1 \\ 1 & 1 & 0 & 1 \\ 0 & 1 & 1 & 0 \end{bmatrix}$$
  where $A_{ij} = 1$ indicates a direct link between node $i$ and node $j$, and $0$ otherwise.
* **Mathematical Operations Performed:**
  1. **Eigenvalue Decomposition:** Solves the characteristic equation $\det(A - \lambda I) = 0$ and the eigenvector equation $A\mathbf{v} = \lambda \mathbf{v}$ using `np.linalg.eig(A)`.
  2. **Dominant Eigenpair Selection:** Extracts the largest real eigenvalue $\lambda_{\max} = 2.5616$ (by the Perron-Frobenius theorem, guaranteed positive and unique for connected non-negative matrices) and its corresponding eigenvector $\mathbf{v}_{\max}$.
  3. **L1 Normalization:** Computes normalized eigenvector centrality scores $c_i = \frac{|v_i|}{\sum_j |v_j|}$ so all importance scores sum to $1.0$ ($100\%$).
  4. **Residual Verification:** Computes the Euclidean norm $\|A\mathbf{v} - \lambda_{\max}\mathbf{v}\|_2 = 2.69 \times 10^{-15}$ to confirm machine-precision accuracy.

### 2. Requirement C: Parameter Modification & Impact Analysis
* **Modification Made:** Added a direct connection between Node A and Node D ($A_{0,3} = 1$ and $A_{3,0} = 1$), transforming the diamond network into a complete graph ($K_4$) where every node has degree $3$.
* **How the Result Changes:**
  * **Dominant Eigenvalue:** Increases from $\lambda_{\max} = 2.5616$ to $\lambda_{\max} = 3.0000$ (reflecting higher overall network connectivity and spectral radius).
  * **Eigenvector Centrality:** Shifts from an unequal distribution (`A: 0.2192, B: 0.2808, C: 0.2808, D: 0.2192`) to an exact uniform distribution (`A: 0.2500, B: 0.2500, C: 0.2500, D: 0.2500`). Because all four nodes now share identical structural symmetry, no single node holds superior hub influence.

### 3. Requirement D: Meaning of Output & Graph Interpretation
* **Output Meaning:** In the base network, Nodes **B** and **C** each score **0.2808 (28.08%)**, while Nodes **A** and **D** score **0.2192 (21.92%)**. Eigenvector centrality measures not just how many connections a node has, but whether it connects to other well-connected nodes. Nodes B and C act as central hubs (degree 3) bridging the network, whereas A and D sit on the periphery (degree 2).
* **Graph Interpretation:**
  * `task_h_base_plot.png`: Visually highlights the two-tier hierarchy where central bars B and C rise higher than peripheral bars A and D.
  * `task_h_param_plot.png`: Side-by-side comparison bars show A and D rising from `0.2192` to `0.2500` while B and C drop from `0.2808` to `0.2500`, illustrating structural equalization.

### 4. Requirement E: Real-World Case Modification — Research Paper Citation Authority (PageRank)
* **Problem & Assumptions:** Models a directed academic citation network of 5 research papers (`P1` to `P5`). Unlike an undirected network, citations flow in one direction ($C_{ij} = 1$ if Paper $j$ cites Paper $i$). To prevent dangling-node rank sinks and ensure a unique dominant eigenvector, we construct a column-stochastic transition matrix $H$ and apply Google's PageRank damping factor $d = 0.85$:
  $$G = dH + \frac{1 - d}{N}\mathbf{1}\mathbf{1}^T$$
* **Input Data:** $5 \times 5$ directed citation matrix $C$ across `P1 (AI Survey)`, `P2 (Core Algo)`, `P3 (Dataset)`, `P4 (App Study)`, and `P5 (Hardware)`, with $d = 0.85$.
* **Output & Interpretation (`task_h_realworld_plot.png`):**
  * Dominant eigenvalue $\lambda_{\max} = 1.0000$ (a fundamental property of column-stochastic Markov matrices), verified to error $6.40 \times 10^{-16}$.
  * **Ranking:** `#1 P2 (Core Algo): 0.2862 (28.62%)`, `#2 P1 (AI Survey): 0.2460 (24.60%)`, `#3 P3 (Dataset): 0.1917 (19.17%)`, `#4 P4 (App Study): 0.1415 (14.15%)`, `#5 P5 (Hardware): 0.1346 (13.46%)`. Even though `P1` is cited by 3 papers, `P2` achieves higher authority because it is cited by 4 papers including high-influence `P1`.

---

## Task R: Numerical Optimization (Constrained Cost Minimization)

### 1. Requirement B: Input Values & Mathematical Operations
* **Input Values:**
  * Decision variables: $x$ (Type A server units), $y$ (Type B server units), initial guess $\mathbf{x}_0 = [5, 3]$.
  * Unit costs: $c_A = \$12$, $c_B = \$18$.
  * Unit capacities: $k_A = 100$, $k_B = 170$; minimum required capacity $K_{\min} = 1000$.
  * Non-negativity bounds: $x \ge 0, y \ge 0$.
* **Mathematical Operations Performed:**
  1. **Constrained Linear/Nonlinear Programming (SLSQP):** Uses Sequential Least Squares Programming (`scipy.optimize.minimize(..., method="SLSQP")`) to minimize the linear objective function $f(x, y) = 12x + 18y$ subject to the inequality constraint $g(x, y) = 100x + 170y - 1000 \ge 0$.
  2. **Integer Grid Search:** Evaluates discrete combinations $(a, b) \in \{0, \dots, 19\}^2$ satisfying $100a + 170b \ge 1000$ to find the lowest-cost whole-server deployment.

### 2. Requirement C: Parameter Modification & Impact Analysis
* **Modifications Made:**
  1. Reduced Type A server unit cost from **$\$12$ to $\$9$** (simulating a vendor bulk discount).
  2. Increased minimum required capacity from **$1000$ to $1500$** units.
* **How the Result Changes:**
  * In the base case, Type B offers a better cost-per-capacity ratio ($\$18 / 170 = \$0.1059$/unit vs. Type A's $\$12 / 100 = \$0.1200$/unit), so the optimizer allocates **100% Type B** ($x = 0, y = 5.882$).
  * After the price drop, Type A becomes more cost-efficient ($\$9 / 100 = \$0.0900$/unit vs. Type B's $\$0.1059$/unit). Consequently, the optimal solution flips completely from Type B to **100% Type A**: $x = 15.000, y = 0.000$, achieving exact capacity $1500$ at minimum cost **$\$135.00$** (matching the integer optimum exactly).

### 3. Requirement D: Meaning of Output & Graph Interpretation
* **Output Meaning:**
  * **Continuous Optimum:** $x = 0.000, y = 5.882$ gives the theoretical minimum planning cost of **$\$105.88$** at exact capacity $1000.00$. Because fractional servers cannot be purchased in reality, rounding up to whole servers gives the **Best Integer Solution**: $0$ Type A and $6$ Type B servers, yielding $1020$ capacity (a $20$-unit safety buffer) for **$\$108.00$**.
* **Graph Interpretation:**
  * `task_r_base_plot.png`: The shaded blue area shows all feasible $(x, y)$ pairs meeting capacity $\ge 1000$. Because both the objective and constraint are linear, the continuous optimum (red dot) sits at the y-intercept corner $(0, 5.88)$ of the boundary line, while the feasible integer optimum (green square) sits just above it at $(0, 6)$.
  * `task_r_param_plot.png`: Shows the feasible boundary shifted outward to $100x + 170y = 1500$ and the optimum jumping to the x-intercept corner $(15, 0)$.

### 4. Requirement E: Real-World Case Modification — Agricultural Fertilizer Blend Optimization
* **Problem & Assumptions:** A commercial farm in Kiambu County needs to blend three fertilizers—**Urea (46-0-0)** at KES 75/kg, **DAP (18-46-0)** at KES 95/kg, and **NPK (17-17-17)** at KES 88/kg—to supply at least **90 kg Nitrogen (N)**, **60 kg Phosphorus (P)**, and **30 kg Potassium (K)** per hectare while keeping total application weight $\le 450$ kg/ha.
* **Formulation:**
  $$\min_{x_1, x_2, x_3 \ge 0} 75x_1 + 95x_2 + 88x_3$$
  subject to:
  * $0.46x_1 + 0.18x_2 + 0.17x_3 \ge 90$ (Nitrogen)
  * $0.46x_2 + 0.17x_3 \ge 60$ (Phosphorus)
  * $0.17x_3 \ge 30$ (Potassium)
  * $x_1 + x_2 + x_3 \le 450$ (Spreader weight limit)
* **Output & Interpretation (`task_r_realworld_plot.png`):**
  * **Optimal Mix:** `104.91 kg Urea` (KES 7,868.62) + `65.22 kg DAP` (KES 6,195.65) + `176.47 kg NPK 17:17:17` (KES 15,529.41).
  * **Total Weight & Cost:** `346.60 kg/ha` (well within the 450 kg limit) at a minimum cost of **KES 29,593.68 per hectare**.
  * **Nutrient Verification:** Supplies exactly `90.00 kg N`, `60.00 kg P`, and `30.00 kg K` with zero wasteful nutrient over-application, as confirmed by the equal-height paired bars in `task_r_realworld_plot.png`.
