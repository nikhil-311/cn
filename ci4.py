import random

from deap import base, creator, tools, algorithms

# Evaluation function
def eval_func(individual):

    # Minimize quadratic function
    return sum(x ** 2 for x in individual),

# DEAP setup
creator.create("FitnessMin",
               base.Fitness,
               weights=(-1.0,))

creator.create("Individual",
               list,
               fitness=creator.FitnessMin)

toolbox = base.Toolbox()

# Attribute generator
toolbox.register(
    "attr_float",
    random.uniform,
    -5.0,
    5.0
)

# Individual generator
toolbox.register(
    "individual",
    tools.initRepeat,
    creator.Individual,
    toolbox.attr_float,
    n=3
)

# Population generator
toolbox.register(
    "population",
    tools.initRepeat,
    list,
    toolbox.individual
)

# Evaluation function
toolbox.register("evaluate", eval_func)

# Crossover operator
toolbox.register(
    "mate",
    tools.cxBlend,
    alpha=0.5
)

# Mutation operator
toolbox.register(
    "mutate",
    tools.mutGaussian,
    mu=0,
    sigma=1,
    indpb=0.2
)

# Selection operator
toolbox.register(
    "select",
    tools.selTournament,
    tournsize=3
)

# Create population
population = toolbox.population(n=50)

# Number of generations
generations = 20

# Run Genetic Algorithm
for gen in range(generations):

    offspring = algorithms.varAnd(
        population,
        toolbox,
        cxpb=0.5,
        mutpb=0.1
    )

    fits = toolbox.map(
        toolbox.evaluate,
        offspring
    )

    for fit, ind in zip(fits, offspring):

        ind.fitness.values = fit

    population = toolbox.select(
        offspring,
        k=len(population)
    )

# Best individual
best_ind = tools.selBest(population, k=1)[0]

best_fitness = best_ind.fitness.values[0]

print("Best individual:", best_ind)

print("Best fitness:", best_fitness)