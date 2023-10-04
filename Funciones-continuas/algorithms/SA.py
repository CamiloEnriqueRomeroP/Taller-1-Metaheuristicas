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
        stop_optimal = self.function.optimum + 0.00001
        stop = False
        for iteration in range(1, self.max_efos):
            R = solution(S.size, S.function)
            R.from_solution(S) # R is a full copy of S
            #R.tweakSegment(self.bandwidth, iteration)
            R.tweak(self.bandwidth)
            t = t - to/(self.max_efos + 1)
            ale = np.random.uniform()            
            try: 
                prob = math.exp((S.fitness - R.fitness) / t) # Minimizing
            except:
                prob = 1
            if R.fitness < S.fitness or ale < prob: # Minimizing
                S.from_solution(R)
            if S.fitness < self.best.fitness: # Minimizing
                self.best.from_solution(S)
            best_fitness_history[iteration] = self.best.fitness
            if S.fitness <= stop_optimal:
                best_fitness_history[iteration:self.max_efos] = self.best.fitness
                stop = True
                iteration = self.max_efos
                break
        return best_fitness_history, stop

    def __str__(self):
        result = "SA-bandwidth:" + str(self.bandwidth)
        return result