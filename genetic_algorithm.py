"""Real-coded Genetic Algorithm for maximizing x*sin(10*pi*x) + 1."""

import math
import random

# Parameters given in the experiment
LOWER_BOUND, UPPER_BOUND = 0.0, 1.0
POPULATION_SIZE = 60
GENERATIONS = 100
CROSSOVER_RATE = 0.90
MUTATION_RATE = 0.15
MUTATION_STD = 0.08
ELITE_COUNT = 2
TOURNAMENT_SIZE = 3
RANDOM_SEED = 42


def fitness(x: float) -> float:
    """Objective function to maximize."""
    return x * math.sin(10 * math.pi * x) + 1


def tournament_selection(population: list[float]) -> float:
    """Return the fittest chromosome from a random tournament."""
    competitors = random.sample(population, TOURNAMENT_SIZE)
    return max(competitors, key=fitness)


def crossover(parent1: float, parent2: float) -> tuple[float, float]:
    """Create two children using arithmetic crossover."""
    if random.random() >= CROSSOVER_RATE:
        return parent1, parent2

    alpha = random.random()
    child1 = alpha * parent1 + (1 - alpha) * parent2
    child2 = alpha * parent2 + (1 - alpha) * parent1
    return child1, child2


def mutate(chromosome: float) -> float:
    """Apply Gaussian mutation and keep the chromosome inside [0, 1]."""
    if random.random() < MUTATION_RATE:
        chromosome += random.gauss(0, MUTATION_STD)
    return max(LOWER_BOUND, min(UPPER_BOUND, chromosome))


def genetic_algorithm() -> tuple[float, float]:
    """Run the GA and return the best chromosome and its fitness."""
    random.seed(RANDOM_SEED)
    population = [
        random.uniform(LOWER_BOUND, UPPER_BOUND)
        for _ in range(POPULATION_SIZE)
    ]

    for generation in range(GENERATIONS + 1):
        population.sort(key=fitness, reverse=True)

        if generation % 10 == 0:
            print(
                f"Generation {generation:3d}: x = {population[0]:.8f}, "
                f"fitness = {fitness(population[0]):.8f}"
            )
        if generation == GENERATIONS:
            break

        # Elitism: carry the two best chromosomes to the next generation.
        next_population = population[:ELITE_COUNT]
        while len(next_population) < POPULATION_SIZE:
            parent1 = tournament_selection(population)
            parent2 = tournament_selection(population)
            child1, child2 = crossover(parent1, parent2)
            next_population.extend([mutate(child1), mutate(child2)])

        population = next_population[:POPULATION_SIZE]

    best_x = population[0]
    return best_x, fitness(best_x)


if __name__ == "__main__":
    best_x, best_fitness = genetic_algorithm()
    print(f"\nBest solution\nx = {best_x:.10f}\nf(x) = {best_fitness:.10f}")
