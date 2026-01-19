import copy
from cost import CostEvaluator
from neighborhood import NeighborhoodGenerator


class TabuSearch:

    def __init__(self, tabu_tenure, max_iterations, neighborhood_size=10):
        self.tabu_tenure = tabu_tenure
        self.max_iterations = max_iterations
        self.neighborhood_size = neighborhood_size

    def run(self, initial_solution, data):
        current = initial_solution.copy()
        best = current.copy()

        best_cost = CostEvaluator.compute(best, data)
        tabu_list = []

        history_best = []
        history_neighbors = []

        for it in range(self.max_iterations):
            neighbors = [
                NeighborhoodGenerator.generate(current, data)
                for _ in range(self.neighborhood_size)
            ]

            admissible = [
                s for s in neighbors
                if s not in tabu_list or
                CostEvaluator.compute(s, data) < best_cost
            ]

            if not admissible:
                break

            candidate = min(
                admissible,
                key=lambda s: CostEvaluator.compute(s, data)
            )

            candidate_cost = CostEvaluator.compute(candidate, data)
            history_neighbors.append((it, candidate_cost))

            if candidate_cost < best_cost:
                best = candidate.copy()
                best_cost = candidate_cost
                history_best.append((it, best_cost))

            current = candidate.copy()
            tabu_list.append(current)

            if len(tabu_list) > self.tabu_tenure:
                tabu_list.pop(0)

        return best, best_cost, history_best, history_neighbors

