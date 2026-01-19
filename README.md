Capacitated Vehicle Routing Problem (CVRP) – Last-Mile Logistics Optimization
This project addresses a practical variant of the Capacitated Vehicle Routing Problem (CVRP), inspired by last-mile distribution challenges. It incorporates the management of two distinct vehicle types:

**Long-term vehicles**: fixed in number and specifications, capable of completing full daily routes.

**Short-term vehicles**: rented on-demand at higher costs, designed for single round trips.

The focus is on optimizing route planning while balancing operational constraints and cost efficiency, providing actionable insights for logistics and distribution management.

## Problem 
Describe the prb

## Project Workflow

1. **Mathematical Modeling**
   - Formulation of the CVRP variant with additional vehicle constraints.
   - Definition of variables, constraints, and objective function.

2. **Exact Implementation (IBM CPLEX)**
   - Model solved exactly on small to medium instances.
   - Provides baseline solutions and validation.

3. **Metaheuristic Approach (Tabu Search)**
   - Applied to larger instances where exact methods become computationally expensive.
   - Focus on solution quality and computation time trade-off.

<div align="center">
  <img src="assets/CVRP.png" alt="CVRP" width="500" height="300">
</div>



