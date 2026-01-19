import time
from data_loader import CVRPData
from solution import CVRPSolution
from tabu_search import TabuSearch
from initial_solution import generate_initial_solution  # si séparée


data = CVRPData(
    file_path="data/50Clients.xlsx",
    num_clients=50,
    num_long=6,
    num_short=20
)

initial_solution = generate_initial_solution(data)

tabu = TabuSearch(
    tabu_tenure=20,
    max_iterations=25000
)

start = time.time()
best_solution, best_cost, hist_best, hist_neighbors = tabu.run(initial_solution, data)
end = time.time()

print("Best cost:", best_cost)
print(f"Execution time: {end - start:.2f}s")

