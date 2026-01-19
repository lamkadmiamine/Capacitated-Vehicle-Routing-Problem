# CVRP Mathematical Model

The `model/` folder contains the **mathematical formulation** of our Capacitated Vehicle Routing Problem (CVRP) variant as a **Mixed Integer Linear Program (MILP / PLNE)**.  
The objective is to **minimize total cost**, including fixed vehicle costs and penalties for exceeding time and distance limits.

---

## Sets and Parameters

- **C** – set of clients, \(C = \{1,2,\dots,n\}\)  
- **VL** – set of long-term vehicles  
- **VS** – set of short-term vehicles  
- **N** – set of nodes, \(N = \{0\} \cup C\), where 0 is the depot  
- **dj** – demand of client \(j \in C\)  
- **capk** – capacity of vehicle \(k \in VL\)  
- **disti,j** – distance between nodes \(i,j \in N\)  
- **Spk** – speed of vehicle \(k \in VL\)  
- **Fck** – fixed cost for vehicle \(k \in VL \cup VS\)  
- **over_timek** – cost per unit of time exceeded for vehicle \(k \in VL\)  
- **over_distancek** – cost per unit of distance exceeded for vehicle \(k \in VL\)  
- **soft_timek** – soft time limit for vehicle \(k \in VL\)  
- **hard_timek** – hard time limit for vehicle \(k \in VL\)  
- **max_distancek** – maximum distance allowed for vehicle \(k \in VL\)  

---

## Decision Variables

- \(x_{i,j,k} \in \{0,1\}\) – 1 if long-term vehicle \(k \in VL\) travels arc \((i,j)\)  
- \(y_{j,k} \in \{0,1\}\) – 1 if short-term vehicle \(k \in VS\) serves client \(j\)  
- \(u_{i,k} \in \mathbb{R}^+\) – continuous variable for **subtour elimination (MTZ)** for client \(i \in C\) and vehicle \(k \in VL\)  
- \(over\_time\_long_k \in \mathbb{R}^+\) – time exceeded by long-term vehicle \(k\)  
- \(over\_distance\_long_k \in \mathbb{R}^+\) – distance exceeded by long-term vehicle \(k\)  

---

## Objective Function

Minimize total cost:  

\[
\min \sum_{k \in VL} \sum_{j \in C} F_{c,k} \, x_{0,j,k} +
\sum_{k \in VS} \sum_{j \in C} F_{c,k} \, y_{j,k} +
\sum_{k \in VL} over\_time_k \cdot over\_time\_long_k +
\sum_{k \in VL} over\_distance_k \cdot over\_distance\_long_k
\]

---

## Constraints

1. **Service constraint** – every client is visited exactly once:  

\[
\sum_{i \in N, i \neq j} x_{i,j,k} + \sum_{k \in VS} y_{j,k} = 1, \quad \forall j \in C
\]

2. **Vehicle capacity** – long-term vehicle does not exceed capacity:  

\[
\sum_{i \in N, i \neq j} d_j \, x_{i,j,k} \le cap_k, \quad \forall k \in VL
\]

3. **Flow conservation** – vehicle leaves each client it visits:  

\[
\sum_{i \in N, i \neq j} x_{i,j,k} = \sum_{i \in N, i \neq j} x_{j,i,k}, \quad \forall k \in VL, \forall j \in C
\]

4. **Subtour elimination (MTZ)** – ensures continuous tours:  

\[
u_{i,k} - u_{j,k} + (|C| - 1) x_{i,j,k} \le |C| - 2, \quad \forall k \in VL, \forall i,j \in C, i \neq j
\]

5. **Time constraints** – long-term vehicle respects soft and hard time limits:  

\[
\sum_{i,j \in N, i \neq j} \frac{dist_{i,j}}{speed_k} x_{i,j,k} \le soft\_time_k + over\_time\_long_k
\]

\[
\sum_{i,j \in N, i \neq j} \frac{dist_{i,j}}{speed_k} x_{i,j,k} \le hard\_time_k
\]

6. **Distance constraints** – maximum distance for long- and short-term vehicles:  

\[
\sum_{i,j \in N, i \neq j} dist_{i,j} x_{i,j,k} \le max\_distance_k + over\_distance\_long_k, \quad \forall k \in VL
\]

\[
\sum_{i,j \in N, i \neq j} dist_{i,j} x_{i,j,k} \le max\_distance_k, \quad \forall k \in VS
\]

---

## Notes

- Constraints (1)–(4) guarantee that **all clients are served exactly once** and that **long-term vehicle routes are feasible and continuous**.  
- Constraints (5)–(7) ensure **time and distance limits** are respected for long-term vehicles.  
- Constraint (8) restricts the **distance traveled by short-term vehicles**.  
- This formulation serves as the basis for exact solution methods (e.g., IBM CPLEX) and is also the foundation for the metaheuristic approach (Tabu Search) for larger instances.

