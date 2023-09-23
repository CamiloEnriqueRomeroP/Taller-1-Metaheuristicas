import numpy as np
from solution import solution
import math


class SA:
    def __init__(self, max_efos: int):
        self.max_efos = max_efos

    def evolve(self, seed: int, problem):
        to = 100
        self.problem = problem
        np.random.seed (seed)
        best_fitness_history = np.zeros(self.max_efos, float)

        S = solution(self.problem)
        S.Initialization()
        best_fitness_history[0] = S.fitness
        self.best = solution(self.problem)
        self.best.from_solution(S) # self.best is a full copy of S
        t= to
        for iteration in range(1, self.max_efos):
            R = solution(S.problem)
            R.from_solution(S) # R is a full copy of S
            R.tweak()
            t = t - to/(self.max_efos + 1)
            ale = np.random.uniform()
            prob = math.exp((R.fitness - S.fitness) / t)
            if R.fitness > S.fitness or ale < prob:
                S.from_solution(R)
            if S.fitness > self.best.fitness:
                self.best.from_solution(S)
            best_fitness_history[iteration] = self.best.fitness
        return best_fitness_history

    def __str__(self):
        result = "SA"
        return result