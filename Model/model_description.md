# CVRP Mathematical Model

The `model/` folder contains the **mathematical formulation** of our Capacitated Vehicle Routing Problem (CVRP) variant as a **Mixed Integer Linear Program (MILP / PLNE)**.  
The objective is to **minimize total cost**, including fixed vehicle costs and penalties for exceeding time and distance limits.

---

## Sets and Parameters

- **C** – set of clients, (C = {1,2, ...,n})  
- **VL** – set of long-term vehicles  
- **VS** – set of short-term vehicles  
- **N** – set of nodes, (N = {0} UNION C), where 0 is the depot  
- **dj** – demand of client (j in C)  
- **capk** – capacity of vehicle (k in VL)  
- **disti,j** – distance between nodes ((i,j) in N)  
- **Spk** – speed of vehicle (k in VL)  
- **Fck** – fixed cost for vehicle (k in VL UNION VS)  
- **over_timek** – cost per unit of time exceeded for vehicle (k in VL)  
- **over_distancek** – cost per unit of distance exceeded for vehicle (k in VL)  
- **soft_timek** – soft time limit for vehicle (k in VL)  
- **hard_timek** – hard time limit for vehicle (k in VL)  
- **max_distancek** – maximum distance allowed for vehicle (k in VL)  

---

## Decision Variables

- x_{i,j,k} in {0,1} – 1 if long-term vehicle k in **VL** travels arc (i,j)  
- y_{j,k} in {0,1} – 1 if short-term vehicle k in **VS** serves client (j)  
- u_{i,k} in R^+ – continuous variable for **subtour elimination (MTZ)** for client i in **C** and vehicle k in **VL**  
- over_time_long_k in R^+ – time exceeded by long-term vehicle k  
- over_distance_long_k in R^+ – distance exceeded by long-term vehicle k  

---

## Objective Function

<div align="center">
  <img src="https://github.com/lamkadmiamine/Capacitated-Vehicle-Routing-Problem/blob/main/assets/FonctionObjectif.png" alt="CVRP" width="700" height="500">
</div>

---

## Constraints

<div align="center">
  <img src="https://github.com/lamkadmiamine/Capacitated-Vehicle-Routing-Problem/blob/main/assets/contraintes.png" alt="CVRP" width="550" height="500">
</div>


## Notes

- Constraints (1)–(4) guarantee that **all clients are served exactly once** and that **long-term vehicle routes are feasible and continuous**.  
- Constraints (5)–(7) ensure **time and distance limits** are respected for long-term vehicles.  
- Constraint (8) restricts the **distance traveled by short-term vehicles**.  
- This formulation serves as the basis for exact solution methods (e.g., IBM CPLEX) and is also the foundation for the metaheuristic approach (Tabu Search) for larger instances.

