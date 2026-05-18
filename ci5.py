import numpy as np
import random

# Distance matrix
distance_matrix = np.array([
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
])

# ACO Parameters
num_ants = 10
num_iterations = 50
evaporation_rate = 0.5
pheromone_constant = 1.0
heuristic_constant = 1.0

# Number of cities
num_cities = len(distance_matrix)

# Initialize pheromone matrix
pheromone = np.ones((num_cities, num_cities))

# Visibility matrix
visibility = 1 / distance_matrix

# Avoid divide-by-zero warning
visibility[visibility == np.inf] = 0

# ACO Algorithm
for iteration in range(num_iterations):

    ant_routes = []

    for ant in range(num_ants):

        # Random starting city
        current_city = random.randint(0, num_cities - 1)

        visited_cities = [current_city]

        route = [current_city]

        # Build complete route
        while len(visited_cities) < num_cities:

            probabilities = []

            for city in range(num_cities):

                if city not in visited_cities:

                    pheromone_value = pheromone[current_city][city]

                    visibility_value = visibility[current_city][city]

                    probability = (
                        pheromone_value ** pheromone_constant
                    ) * (
                        visibility_value ** heuristic_constant
                    )

                    probabilities.append((city, probability))

            # Select best probability city
            probabilities = sorted(
                probabilities,
                key=lambda x: x[1],
                reverse=True
            )

            selected_city = probabilities[0][0]

            route.append(selected_city)

            visited_cities.append(selected_city)

            current_city = selected_city

        ant_routes.append(route)

    # Update pheromone
    delta_pheromone = np.zeros((num_cities, num_cities))

    for route in ant_routes:

        for i in range(len(route) - 1):

            city_a = route[i]

            city_b = route[i + 1]

            delta_pheromone[city_a][city_b] += (
                1 / distance_matrix[city_a][city_b]
            )

            delta_pheromone[city_b][city_a] += (
                1 / distance_matrix[city_a][city_b]
            )

    # Evaporation + update
    pheromone = (
        (1 - evaporation_rate) * pheromone
    ) + delta_pheromone

# Find best route
best_route = min(
    ant_routes,
    key=lambda route: sum(
        distance_matrix[route[i]][route[(i + 1) % num_cities]]
        for i in range(num_cities)
    )
)

# Shortest distance
shortest_distance = sum(
    distance_matrix[best_route[i]][best_route[(i + 1) % num_cities]]
    for i in range(num_cities)
)

# Output
print("Best route:", best_route)

print("Shortest distance:", shortest_distance)