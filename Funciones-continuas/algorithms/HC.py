from solution import solution
import numpy as np


class HC:
    def __init__(self, max_efos: int, bandwidth: float):
        self.max_efos = max_efos
        self.bandwidth = bandwidth

    def evolve(self, seed: int, d: int, f):
        self.function = f
        np.random.seed(seed)
        best_fitness_history = np.zeros(self.max_efos, float)
        self.best = solution(d, f)
        self.best.Initialization()
        best_fitness_history[0] = self.best.fitness
        S = self.best  # S is a pointer to self.best, not a full copy
        stop_optimal = self.function.optimum + 0.00001
        stop = False
        for iteration in range(1, self.max_efos):
            R = solution(S.size, S.function)
            R.from_solution(S)  # R is a full copy of S
            #R.tweakSegment(self.bandwidth,iteration)
            R.tweak(self.bandwidth)
            if R.fitness < S.fitness:
                S.from_solution(R)
            best_fitness_history[iteration] = self.best.fitness
            if S.fitness <= stop_optimal:
                best_fitness_history[iteration:self.max_efos] = self.best.fitness
                stop = True
                iteration = self.max_efos
                break
        return best_fitness_history, stop

    def __str__(self):
        result = "HC-bandwidth:" + str(self.bandwidth)
        return result
