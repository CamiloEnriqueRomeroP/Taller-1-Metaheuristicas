from solution import solution
import numpy as np

class GRASP:
    def __init__(self, max_efos: int, max_local: int, bandwidth: float):
        self.max_efos = max_efos
        self.max_local = max_local
        self.bandwidth = bandwidth

    def evolve(self, seed: int, d: int, f):
        self.function = f
        np.random.seed(seed)
        best_fitness_history = np.zeros(self.max_efos, float)
        efos = 0
        stop_optimal = self.function.optimum + 0.00001
        stop = False
        while efos < self.max_efos:
            S = solution(d, f)  # S is a new Solution
            S.Initialization_GRASP()
            if efos == 0:
                self.best = solution(d, f)
                self.best.from_solution(S)  # self.best is a full copy of S
                best_fitness_history[0] = self.best.fitness
            # Perform the hill climbig optimization (local)
            for opt in range(1, self.max_local):
                R = solution(S.size, S.function)
                R.from_solution(S)  # R is a full copy of S
                R.tweak(self.bandwidth)  # Tweeking and calculating fitness
                if R.fitness < S.fitness:
                    S.from_solution(R)
                if S.fitness < self.best.fitness:
                    self.best.from_solution(S)  # self.best is a full copy of S
                best_fitness_history[efos] = self.best.fitness
                efos += 1
                if S.fitness <= stop_optimal:
                    best_fitness_history[efos:self.max_efos] = self.best.fitness
                    stop = True
                    efos = self.max_efos
                    break
                if efos >= self.max_efos:
                    break
        return best_fitness_history, stop

    def __str__(self):
        result = "GRASP-bandwidth:" + str(self.bandwidth)
        result += "-maxlocal:" + str(self.max_local)
        return result
