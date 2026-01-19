/*********************************************
 * OPL Model for CVRP
 * Author: amine
 *********************************************/

// === Data declaration ===
int numClients = ...;
int numVehiclesLongTerm = ...;
int numVehiclesShortTerm = ...;

range Clients = 1..numClients;
range VehiclesLongTerm = 1..numVehiclesLongTerm;
range VehiclesShortTerm = 1..numVehiclesShortTerm;

// === Parameters ===
float distances[0..numClients, 0..numClients] = ...;
float demands[Clients]= ...;
float vehicleCapacityLong[VehiclesLongTerm]= ...;
float vehicleSpeedLong[VehiclesLongTerm]= ...;
float maxSoftTimeLong[VehiclesLongTerm]= ...;
float maxHardTimeLong[VehiclesLongTerm]= ...;
float maxDistanceLong[VehiclesLongTerm]= ...;
float maxDistanceShort[VehiclesShortTerm]= ...;
float fixedCostLong[VehiclesLongTerm]= ...;
float fixedCostShort[VehiclesShortTerm]= ...;
float overTimeCostLong[VehiclesLongTerm]= ...;
float overDistanceCostLong[VehiclesLongTerm]= ...;

// === Decision variables ===
dvar boolean x[0..numClients, 0..numClients, VehiclesLongTerm];
dvar boolean y[Clients, VehiclesShortTerm];
dvar float+ u[Clients, VehiclesLongTerm];
dvar float+ over_time_long[VehiclesLongTerm];
dvar float+ over_distance_long[VehiclesLongTerm];

// === Objective function ===
minimize
  sum(k in VehiclesLongTerm, j in Clients) fixedCostLong[k] * x[0, j, k] +
  sum(k in VehiclesShortTerm, j in Clients) fixedCostShort[k] * y[j, k] +
  sum(k in VehiclesLongTerm) overTimeCostLong[k] * over_time_long[k] +
  sum(k in VehiclesLongTerm) overDistanceCostLong[k] * over_distance_long[k];

// === Constraints ===
subject to {
  // Each client must be served exactly once
  forall(j in Clients)
    sum(i in 0..numClients: i != j, k in VehiclesLongTerm) x[i, j, k] + sum(k in VehiclesShortTerm) y[j, k] == 1;

  // Long-term vehicle capacity limits
  forall(k in VehiclesLongTerm)
    sum(j in Clients, i in 0..numClients: i != j) demands[j] * x[i, j, k] <= vehicleCapacityLong[k];

  // Flow conservation for long-term vehicles
  forall(k in VehiclesLongTerm, j in Clients)
    sum(i in 0..numClients: i != j) x[i, j, k] == sum(i in 0..numClients: i != j) x[j, i, k];

  // MTZ: Subtour elimination
  forall(k in VehiclesLongTerm, i in Clients, j in Clients: i != j)
    u[i, k] - u[j, k] + (numClients - 1) * x[i, j, k] <= numClients - 2;

  // Short-term vehicle distance limits
  forall(k in VehiclesShortTerm) {
    sum(j in Clients) 2 * distances[0, j] * y[j, k] <= maxDistanceShort[k];
  }

  // Long-term vehicle time and distance overruns
  forall(k in VehiclesLongTerm) {
    sum(i in 0..numClients, j in 0..numClients: i != j) distances[i, j] / vehicleSpeedLong[k] * x[i, j, k] <= maxSoftTimeLong[k] + over_time_long[k];
    sum(i in 0..numClients, j in 0..numClients: i != j) distances[i, j] / vehicleSpeedLong[k] * x[i, j, k] <= maxHardTimeLong[k];
    sum(i in 0..numClients, j in 0..numClients: i != j) distances[i, j] * x[i, j, k] <= maxDistanceLong[k] + over_distance_long[k];
  }
}

// === Execution ===
execute {
  writeln("Starting CVRP optimization...");
}

// === Output ===
execute OUTPUT {
  writeln("Solution status: ", cplex.status);
  writeln("Objective value: ", cplex.getObjValue());
}

