import numpy as np
from solution import solution
import math

class SA:
    def __init__(self, max_efos: int, bandwidth: float):
        self.max_efos = max_efos
        self.bandwidth = bandwidth

    def evolve(self, seed: int, d: int, f):
        to = 100
        self.function = f
        np.random.seed (seed)
        best_fitness_history = np.zeros(self.max_efos, float)
        S = solution(d, f) # S is a new Solution
        S.Initialization()
        best_fitness_history[0] = S.fitness
        self.best = solution(d, f)
        self.best.from_solution(S) # self.best is a full copy of S
        t= to
        optimal = self.function.optimum
        stop_optimal = optimal + 0.00001
        for iteration in range(1, self.max_efos):
            R = solution(S.size, S.function)
            R.from_solution(S) # R is a full copy of S
            R.tweak(self.bandwidth)
            t = t - to/(self.max_efos + 1)
            ale = np.random.uniform()
            prob = np.exp((S.fitness - R.fitness) / t) # Minimizing
            if R.fitness < S.fitness or ale < prob: # Minimizing
                S.from_solution(R)
            if S.fitness < self.best.fitness: # Minimizing
                self.best.from_solution(S)
            best_fitness_history[iteration] = self.best.fitness
            if S.fitness <= stop_optimal:
                best_fitness_history[iteration:self.max_efos] = self.best.fitness
                iteration = self.max_efos
                break
        return best_fitness_history

    def __str__(self):
        result = "SA:-bandwidth:" + str(self.bandwidth)
        return result