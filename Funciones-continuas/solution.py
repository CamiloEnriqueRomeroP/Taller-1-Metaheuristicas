import numpy as np

class solution:

    def __init__(self, d: int, f):
        self.size = d
        self.cells = np.zeros(self.size, float)
        self.fitness = 0.0
        self.function = f

    def from_solution(self, origin):
        self.size = origin.size
        self.cells = np.copy(origin.cells)
        self.fitness = origin.fitness
        self.function = origin.function

    def Initialization(self):
        self.cells = np.random.uniform(low=self.function.lower_bound, high=self.function.upper_bound,
                                       size=(self.size,))
        self.fitness = self.function.evaluate(self.cells)

    def tweak(self, bandwidth: float):
        bandwidths = np.random.uniform(low=-bandwidth, high=bandwidth, size=(self.size,))
        self.cells = self.cells + bandwidths
        self.cells[self.cells < self.function.lower_bound] = self.function.lower_bound
        self.cells[self.cells > self.function.upper_bound] = self.function.upper_bound
        self.fitness = self.function.evaluate(self.cells)

    def __str__(self):
        return "cells:" + str(self.cells) + \
               "-fit:" + str(self.fitness)