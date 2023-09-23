from solution import solution
from tsp import tsp
import numpy as np

class HCRR:
    def __init__(self, max_efos: int, max_local: int):
        self.max_efos = max_efos
        self.max_local = max_local

    def evolve(self, seed: int, problem: tsp):
        self.problem = problem
        np.random.seed (seed)
        best_fitness_history = np.zeros(self.max_efos, float)
        efos = 0
        while efos < self.max_efos:
          S = solution(problem) # S is a new Solution
          S.Initialization() # Random initialization and calculating fitness
          if efos == 0:
            self.best = solution(problem)
            self.best.from_solution(S) # self.best is a full copy of S
            best_fitness_history[0] = self.best.fitness
          # Perform the hill climbig optimization (local)
          for opt in range(1, self.max_local):
              R = solution(S.problem)
              R.from_solution(S) # R is a full copy of S
              R.tweak() # Tweeking and calculating fitness
              if R.fitness < S.fitness: # Minimizing
                  S.from_solution(R)
              if S.fitness < self.best.fitness: # Minimizing
                  self.best.from_solution(S) # self.best is a full copy of S
              best_fitness_history[efos] = self.best.fitness
              efos+=1
              if efos >= self.max_efos:
                break
        return best_fitness_history

    def __str__(self):
        result = "HCRR-maxlocal:" + str(self.max_local)
        return result