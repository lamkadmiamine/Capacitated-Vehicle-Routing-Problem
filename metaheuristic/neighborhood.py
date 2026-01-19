import random


class NeighborhoodGenerator:

    @staticmethod
    def generate(solution, data):
        neighbor = solution.copy()

        while True:
            container = random.choice([neighbor.long_term, neighbor.short_term])
            idx = random.randint(0, len(container) - 1)

            route = container[idx]
            if len(route) <= 2:
                continue

            client = random.choice(route[1:-1])
            route.remove(client)

            container2 = random.choice([neighbor.long_term, neighbor.short_term])
            idx2 = random.randint(0, len(container2) - 1)

            pos = random.randint(1, len(container2[idx2]) - 1)
            container2[idx2].insert(pos, client)

            if neighbor.is_valid(data):
                return neighbor

