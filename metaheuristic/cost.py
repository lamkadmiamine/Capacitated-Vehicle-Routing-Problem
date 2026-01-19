class CostEvaluator:

    @staticmethod
    def compute(solution, data):
        total_cost = 0

        # Long-term vehicles
        for k, route in enumerate(solution.long_term):
            if len(route) > 2:
                total_cost += data.fixedCostLong[k]

                distance = sum(
                    data.distances[route[i], route[i + 1]]
                    for i in range(len(route) - 1)
                )

                time_spent = distance / data.vehicleSpeedLong[k]

                over_time = max(0, time_spent - data.maxHardTimeLong[k])
                over_distance = max(0, distance - data.maxDistanceLong[k])

                total_cost += data.overTimeCostLong[k] * over_time
                total_cost += data.overDistanceCostLong[k] * over_distance

        # Short-term vehicles
        for k, route in enumerate(solution.short_term):
            if len(route) > 2:
                total_cost += data.fixedCostShort[k]

        return total_cost

