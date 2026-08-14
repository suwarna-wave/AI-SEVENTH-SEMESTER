"""Genetic Algorithm for bounded numerical-function optimization."""

from __future__ import annotations

import math
import random
from collections.abc import Callable, Sequence

Vector = list[float]


class GeneticAlgorithm:
    """Optimize a real-valued function without requiring external libraries."""

    def __init__(
        self,
        objective: Callable[[Sequence[float]], float],
        bounds: Sequence[tuple[float, float]],
        *,
        population_size: int = 80,
        generations: int = 150,
        crossover_rate: float = 0.9,
        mutation_rate: float | None = None,
        mutation_scale: float = 0.1,
        elite_size: int = 2,
        tournament_size: int = 3,
        maximize: bool = False,
        seed: int | None = None,
    ) -> None:
        if not bounds or any(low >= high for low, high in bounds):
            raise ValueError("Each bound must be a (low, high) pair with low < high.")
        if population_size < 2 or not 0 <= elite_size < population_size:
            raise ValueError("Use population_size >= 2 and 0 <= elite_size < population_size.")
        if generations < 1 or tournament_size < 2:
            raise ValueError("generations must be positive and tournament_size >= 2.")
        if not 0 <= crossover_rate <= 1 or mutation_scale < 0:
            raise ValueError("Invalid crossover_rate or mutation_scale.")

        self.objective = objective
        self.bounds = list(bounds)
        self.population_size = population_size
        self.generations = generations
        self.crossover_rate = crossover_rate
        self.mutation_rate = mutation_rate if mutation_rate is not None else 1 / len(bounds)
        if not 0 <= self.mutation_rate <= 1:
            raise ValueError("mutation_rate must be between 0 and 1.")
        self.mutation_scale = mutation_scale
        self.elite_size = elite_size
        self.tournament_size = tournament_size
        self.maximize = maximize
        self.rng = random.Random(seed)
        self.history: list[float] = []

    def _random_individual(self) -> Vector:
        return [self.rng.uniform(low, high) for low, high in self.bounds]

    def _ranked(self, population: list[Vector]) -> list[tuple[float, Vector]]:
        scored = [(float(self.objective(x)), x) for x in population]
        if any(not math.isfinite(score) for score, _ in scored):
            raise ValueError("The objective function must return finite numbers.")
        return sorted(scored, key=lambda item: item[0], reverse=self.maximize)

    def _select(self, ranked: list[tuple[float, Vector]]) -> Vector:
        candidates = self.rng.sample(ranked, min(self.tournament_size, len(ranked)))
        winner = max(candidates, key=lambda item: item[0]) if self.maximize else min(
            candidates, key=lambda item: item[0]
        )
        return winner[1]

    def _crossover(self, first: Vector, second: Vector) -> tuple[Vector, Vector]:
        if self.rng.random() >= self.crossover_rate:
            return first.copy(), second.copy()
        child1, child2 = [], []
        for a, b, (low, high) in zip(first, second, self.bounds):
            alpha = self.rng.random()
            child1.append(min(high, max(low, alpha * a + (1 - alpha) * b)))
            child2.append(min(high, max(low, alpha * b + (1 - alpha) * a)))
        return child1, child2

    def _mutate(self, individual: Vector) -> Vector:
        for i, (low, high) in enumerate(self.bounds):
            if self.rng.random() < self.mutation_rate:
                step = self.rng.gauss(0, self.mutation_scale * (high - low))
                individual[i] = min(high, max(low, individual[i] + step))
        return individual

    def run(self) -> tuple[Vector, float]:
        """Return (best_variables, best_objective_value)."""
        population = [self._random_individual() for _ in range(self.population_size)]
        self.history.clear()

        for _ in range(self.generations):
            ranked = self._ranked(population)
            self.history.append(ranked[0][0])
            next_population = [x.copy() for _, x in ranked[: self.elite_size]]

            while len(next_population) < self.population_size:
                children = self._crossover(self._select(ranked), self._select(ranked))
                for child in children:
                    if len(next_population) < self.population_size:
                        next_population.append(self._mutate(child))
            population = next_population

        best_value, best_vector = self._ranked(population)[0]
        self.history.append(best_value)
        return best_vector.copy(), best_value


if __name__ == "__main__":
    # Example: the Sphere function has its global minimum f(0, 0) = 0.
    def sphere(x: Sequence[float]) -> float:
        return sum(value**2 for value in x)

    ga = GeneticAlgorithm(sphere, bounds=[(-5.12, 5.12)] * 2, seed=42)
    solution, value = ga.run()
    print("Best solution:", [round(x, 6) for x in solution])
    print("Objective value:", f"{value:.10f}")
