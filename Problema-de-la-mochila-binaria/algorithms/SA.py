import numpy as np
from solution import solution
import math


class SA:
    def __init__(self, max_efos: int):
        self.max_efos = max_efos

    def evolve(self, seed: int, problem):
        to = 100
        self.problem = problem
        np.random.seed(seed)
        best_fitness_history = np.zeros(self.max_efos, float)        
        stop_optimal = self.problem.OptimalKnown
        S = solution(self.problem)
        S.Initialization()
        best_fitness_history[0] = S.fitness
        self.best = solution(self.problem)
        self.best.from_solution(S)  # self.best is a full copy of S
        t = to
        stop = False
        for iteration in range(1, self.max_efos):
            R = solution(S.problem)
            R.from_solution(S)  # R is a full copy of S
            R.tweakUpperDensity()
            #R.tweak()
            t = t - to/(self.max_efos + 1)
            ale = np.random.uniform()            
            try: 
                prob = math.exp((R.fitness - S.fitness) / t) # Minimizing
            except:
                prob = 1
            if R.fitness > S.fitness or ale < prob:
                S.from_solution(R)
            if S.fitness > self.best.fitness:
                self.best.from_solution(S)
            best_fitness_history[iteration] = self.best.fitness
            if S.fitness >= stop_optimal:
                best_fitness_history[iteration:self.max_efos] = self.best.fitness
                iteration = self.max_efos
                stop = True
                break
        return best_fitness_history, stop

    def __str__(self):
        result = "SA"
        return result
