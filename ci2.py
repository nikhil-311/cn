import numpy as np
import matplotlib.pyplot as plt

# Objective function
def objective_function(x):
    return np.sum(x**2)

# Initialize random population
def initialize_population(pop_size, dim, lower_bound, upper_bound):
    return np.random.uniform(lower_bound, upper_bound, (pop_size, dim))

# Evaluate fitness of population
def evaluate_population(population):
    return np.array([objective_function(ind) for ind in population])

# Clone selected antibodies
def clone_population(selected, clone_factor):
    clones = []
    
    for i, antibody in enumerate(selected):
        num_clones = int(clone_factor / (i + 1))
        clones.extend([antibody.copy() for _ in range(num_clones)])
    
    return np.array(clones)

# Hypermutation
def hypermutation(clones, beta, lower_bound, upper_bound):
    mutated = []
    
    for clone in clones:
        mutation_rate = beta * np.exp(-objective_function(clone))
        
        new_clone = clone + mutation_rate * np.random.randn(*clone.shape)
        
        new_clone = np.clip(new_clone, lower_bound, upper_bound)
        
        mutated.append(new_clone)
    
    return np.array(mutated)

# Replace weak population members
def replace_population(population, new_cells, pop_size):
    combined = np.vstack((population, new_cells))
    
    fitness = evaluate_population(combined)
    
    sorted_indices = np.argsort(fitness)
    
    return combined[sorted_indices[:pop_size]]

# Main CLONALG algorithm
def clonalg(pop_size=50,
            dim=5,
            generations=100,
            lower_bound=-5,
            upper_bound=5,
            selection_size=10,
            clone_factor=20,
            beta=1.0):

    # Initialize population
    population = initialize_population(
        pop_size,
        dim,
        lower_bound,
        upper_bound
    )

    best_fitness_history = []

    for gen in range(generations):

        # Evaluate fitness
        fitness = evaluate_population(population)

        # Sort population by fitness
        sorted_indices = np.argsort(fitness)
        population = population[sorted_indices]

        # Select best antibodies
        selected = population[:selection_size]

        # Clone selected antibodies
        clones = clone_population(selected, clone_factor)

        # Hypermutation
        mutated_clones = hypermutation(
            clones,
            beta,
            lower_bound,
            upper_bound
        )

        # Replace population
        population = replace_population(
            population,
            mutated_clones,
            pop_size
        )

        # Best fitness
        best_fitness = objective_function(population[0])

        best_fitness_history.append(best_fitness)

        # Print progress
        if gen % 10 == 0:
            print(f"Generation {gen}: Best Fitness = {best_fitness:.6f}")

    return population[0], best_fitness_history

# Run algorithm
best_solution, history = clonalg()

# Print final results
print("\nBest Solution:", best_solution)
print("Best Fitness:", objective_function(best_solution))

# Plot convergence graph
plt.plot(history)

plt.title("CLONALG Convergence")
plt.xlabel("Generation")
plt.ylabel("Best Fitness")

plt.grid()

plt.show()