class CVRPSolution:
    """
    Represents a CVRP solution.
    """

    def __init__(self, long_term_routes, short_term_routes):
        self.long_term = long_term_routes
        self.short_term = short_term_routes

    def copy(self):
        return CVRPSolution(
            [r.copy() for r in self.long_term],
            [r.copy() for r in self.short_term]
        )

    def is_valid(self, data):
        all_clients = set(range(1, data.numClients + 1))
        visited_long = set()
        visited_short = set()

        # Long-term vehicles
        for k, route in enumerate(self.long_term):
            if route[0] != 0 or route[-1] != 0:
                return False

            clients = route[1:-1]
            if visited_long.intersection(clients):
                return False
            visited_long.update(clients)

            demand = sum(data.demands[c - 1] for c in clients)
            if demand > data.vehicleCapacityLong[k]:
                return False

            distance = sum(
                data.distances[route[i], route[i + 1]]
                for i in range(len(route) - 1)
            )

            time_spent = distance / data.vehicleSpeedLong[k]
            if time_spent > data.maxHardTimeLong[k]:
                return False

        # Short-term vehicles
        for k, route in enumerate(self.short_term):
            if route == [0, 0]:
                continue
            if len(route) != 3:
                return False

            client = route[1]
            if client in visited_long or client in visited_short:
                return False
            visited_short.add(client)

            dist = (
                data.distances[0, client]
                + data.distances[client, 0]
            )
            if dist > data.maxDistanceShort[k]:
                return False

        return visited_long.union(visited_short) == all_clients

