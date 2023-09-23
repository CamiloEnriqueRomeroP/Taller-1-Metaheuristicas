from solution import solution
from tsp import tsp
import numpy as np

class HC:
    def __init__(self, max_efos: int):
        self.max_efos = max_efos

    def evolve(self, seed: int, problem: tsp):
        self.problem = problem
        np.random.seed (seed)
        best_fitness_history = np.zeros(self.max_efos, float)

        self.best = solution(self.problem)
        self.best.Initialization()
        best_fitness_history[0] = self.best.fitness

        S = self.best # S is a pointer to self.best, not a full copy
        for iteration in range(1, self.max_efos):
            R = solution(S.problem)
            R.from_solution(S) # R is a full copy of S
            R.tweak()
            if R.fitness < S.fitness: # Minimizing
                S.from_solution(R)
            best_fitness_history[iteration] = self.best.fitness
        return best_fitness_history

    def __str__(self):
        result = "HC:"
        return result