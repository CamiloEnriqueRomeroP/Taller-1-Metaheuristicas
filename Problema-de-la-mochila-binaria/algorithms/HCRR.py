import numpy as np
from solution import solution

class HCRR:
    def __init__(self, max_efos: int, max_local: int):
        self.max_efos = max_efos
        self.max_local = max_local

    def evolve(self, seed: int, problem):
        self.problem = problem
        np.random.seed(seed)
        best_fitness_history = np.zeros(self.max_efos, float)
        efos = 0
        stop_optimal = self.problem.OptimalKnown
        stop = False
        while efos < self.max_efos:
            S = solution(problem)  # S is a new Solution
            S.Initialization()  # Random initialization and calculating fitness
            if efos == 0:
                self.best = solution(problem)
                self.best.from_solution(S)  # self.best is a full copy of S
            else:
                if S.fitness > self.best.fitness:
                    self.best.from_solution(S)  # self.best is a full copy of S                              
            best_fitness_history[efos] = self.best.fitness
            efos += 1
            # Perform the hill climbig optimization (local)
            for opt in range(1, self.max_local):
                R = solution(S.problem)
                R.from_solution(S)  # R is a full copy of S
                R.tweak()
                #R.tweakUpperDensity()
                if R.fitness > S.fitness:
                    S.from_solution(R)
                if S.fitness > self.best.fitness:
                    self.best.from_solution(S)  # self.best is a full copy of S
                best_fitness_history[efos] = self.best.fitness
                efos += 1
                if S.fitness >= stop_optimal:
                    best_fitness_history[efos:self.max_efos] = self.best.fitness
                    stop = True
                    efos = self.max_efos
                    break
                if efos >= self.max_efos:
                    break
        return best_fitness_history, stop

    def __str__(self):
        result = "HCRR-maxlocal:" + str(self.max_local)
        return result
