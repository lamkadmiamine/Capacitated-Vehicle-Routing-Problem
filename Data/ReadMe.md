# Dataset 
The **/Data** folder contains the problem instances used in this project. It includes four Excel files corresponding to different numbers of clients:
  - 15Clients.xlsx
  - 20Clients.xlsx
  - 50Clients.xlsx
  - 100Clients.xlsx

Each file provides the following parameters for the CVRP variant:
  - Distance Matrix – distances between all customer locations
  - Number of Vehicles – total available vehicles
  - Capacity – vehicle load capacity
  - Average Speed – average travel speed
  - Fixed Cost – fixed cost per vehicle
  - Soft Time Limit – preferred maximum route duration
  - Hard Time Limit – absolute maximum route duration
  - Soft Distance Limit – preferred maximum travel distance
  - Hard Distance Limit – absolute maximum travel distance
  - Distance Penalty Cost – cost per unit of distance exceeded
  - Time Penalty Cost – cost per unit of time exceeded

Note: The larger instances (50Clients and 100Clients) are primarily used in the metaheuristic (Tabu Search) due to the computational complexity of solving large CVRP instances exactly (NP-hard problem).
