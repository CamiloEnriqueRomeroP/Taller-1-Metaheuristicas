import numpy as np
from tsp import tsp

class solution:
    def __init__(self, p: tsp):
        self.problem = p
        self.cells = np.zeros(self.problem.size, int)
        self.fitness = 0.0

    def from_solution(self, origin):
        self.problem = origin.problem
        self.cells = np.copy(origin.cells)
        self.fitness = origin.fitness

    def Initialization(self):
        self.cells = np.random.choice(self.problem.size, self.problem.size, replace=False)
        self.fitness = self.problem.evaluate(self.cells)

    def tweak(self):
        pos = np.random.choice(np.arange(1, self.problem.size), 2, replace=False)
        pos.sort()
        i = pos[0]
        k = pos[1]
        self.cells[i:k] = self.cells[k - 1:i - 1:-1]
        self.fitness = self.problem.evaluate(self.cells)

    def __str__(self):
        return "cells:" + str(self.cells) + \
               "-fit:" + str(self.fitness)