import math

def nearest_neighbor_tsp(graph):
    num_cities = len(graph)
    unvisited = set(range(num_cities))
    tour = []
    start_city = 0  # Start from city 0

    while unvisited:
        nearest_city = min(unvisited, key=lambda city: graph[start_city][city])
        tour.append(nearest_city)
        unvisited.remove(nearest_city)
        start_city = nearest_city

    tour.append(tour[0])  # Return to the starting city to complete the tour

    total_distance = sum(graph[tour[i]][tour[i + 1]] for i in range(num_cities))

    return tour, total_distance

# Example usage
graph = [
    [0, 29, 20, 21],
    [29, 0, 15, 28],
    [20, 15, 0, 30],
    [21, 28, 30, 0]
]

tour, total_distance = nearest_neighbor_tsp(graph)
print("Optimal Tour:", tour)
print("Total Distance:", total_distance)
