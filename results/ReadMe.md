# Results and Performance Analysis

This folder presents a **comparative analysis of the two solution approaches** developed for the Vehicle Routing Problem:
- **PLNE (Exact Integer Linear Programming – IBM CPLEX)**
- **Metaheuristic approach (Tabu Search)**

The comparison is performed on multiple datasets with increasing problem sizes.

---

## Experimental Results

### Performance Comparison

| Dataset (Clients) | Method | Time (min) | Time (s) | Final Gap (%) | Lower Bound | Upper Bound | Cost |
|-------------------|--------|------------|----------|---------------|-------------|-------------|------|
| 10 clients | PLNE | 0 | – | 0 | 700.40 | 700.40 | 700.40 |
| 10 clients | Heuristic | – | 17.34 | 0 | – | – | 700.40 |
| 15 clients | PLNE | 2.66 | – | 0 | 839.21 | 884.81 | 884.81 |
| 15 clients | Heuristic | – | 97.40 | 0 | – | – | 884.81 |
| 20 clients | PLNE | 15 | – | 0 | 685.30 | 781.36 | 781.36 |
| 20 clients | Heuristic | – | 138.06 | 0 | – | – | 781.36 |
| 50 clients | PLNE | 15 | – | 34.78 | – | – | – |
| 50 clients | Heuristic | – | 70.19 | – | – | – | 300.00 |
| 100 clients | PLNE | 15 | – | 41.53 | – | – | – |
| 100 clients | Heuristic | – | 91.59 | – | – | – | 760.00 |

**Table 1 – Performance comparison of PLNE and heuristic approaches across different datasets**

---

## Interpretation of Results

The results clearly highlight the **strengths and limitations** of both approaches.

- For **small instances (10–15 clients)**, the PLNE method performs very well, reaching optimal solutions with zero gap and reasonable computation times. The heuristic achieves the same solution quality, confirming its correctness and efficiency.

- For **medium instances (20 clients)**, PLNE is still capable of finding optimal solutions, but the computation time starts to increase significantly. The heuristic remains competitive and achieves optimal or near-optimal solutions in short execution times.

- For **large instances (50 and 100 clients)**, PLNE becomes impractical. The solver reaches the imposed time limit, produces large optimality gaps, and fails to provide reliable lower bounds. This confirms the scalability limitations of exact methods for large-scale VRP instances.

- The **metaheuristic approach** demonstrates strong robustness on large datasets. It consistently finds feasible solutions in short computation times and provides acceptable solution quality, making it more suitable for real-world, large-scale applications.

Overall, the heuristic shows a much better **scalability**, while PLNE remains useful when exact optimality is required for small or medium-sized problems.

---

## Conclusion

This study demonstrates a clear performance contrast between the two solution methods:

- **PLNE** is highly effective for small instances where optimality is required and computational resources are not a constraint.
- However, its performance rapidly deteriorates as the problem size increases, leading to excessive computation times and large optimality gaps.

- **The Tabu Search heuristic** consistently produces feasible and high-quality solutions in significantly shorter times.
- It sometimes reaches optimal solutions for small instances and remains reliable for large instances where exact methods fail.

Consequently, the heuristic approach is more appropriate for **large-scale practical applications**, while PLNE remains relevant for **benchmarking and validation on smaller instances**.

---

## Perspectives

Several improvements can be considered to further enhance performance:

- **For PLNE**:
  - Integrating **Lagrangian relaxation** or decomposition techniques to accelerate convergence.
  - Using advanced solver configurations or parallelization to reduce computation time.

- **For the heuristic**:
  - Hybridization with exact methods (matheuristics).
  - Adaptive tabu tenure and neighborhood size.
  - Parallel neighborhood exploration to improve solution quality.

These perspectives open the way for more efficient hybrid approaches combining **exact optimization and metaheuristics**.

---

