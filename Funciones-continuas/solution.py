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

    # Original code
    def Initialization(self):
        self.cells = np.random.uniform(
            low=self.function.lower_bound, high=self.function.upper_bound, size=(self.size,))
        self.fitness = self.function.evaluate(self.cells)
        
    def Initialization_GRASP(self):
        dimensions = 0
        S_rand = []
        fitnessComponent = []
        randomSolutions = []
        for i  in range (0, int(self.size*0.5)):
            components = np.random.uniform(low=self.function.lower_bound, high=self.function.upper_bound, size=(self.size,))
            randomSolutions.append(components)
            fitnessComponent.append(self.function.evaluate(components))
        population = np.c_[fitnessComponent, randomSolutions]
        C_prima = np.copy(population)
        constructing_solution = []
        for var in range(10):
            if len(C_prima) == 0:
                break
            else:
                C_sorted = sorted(C_prima, key=lambda x: x[0], reverse=False)
                C_two_prima = int(len(C_sorted)*0.33)+1
                for i in range (0, 5):
                    pos = np.random.randint(C_two_prima)
                    s_random_component = C_sorted[pos]
                    dimensions = dimensions + 1
                    S_rand.append(s_random_component[dimensions])
                    if dimensions == 50:
                        break
                
        self.cells = np.copy(S_rand)
        self.fitness = self.function.evaluate(self.cells)
                
    def tweak(self, bandwidth: float):
        bandwidths = np.random.uniform(low=-bandwidth, high=bandwidth, size=(self.size,))
        self.cells = self.cells + bandwidths
        self.cells[self.cells <self.function.lower_bound] = self.function.lower_bound
        self.cells[self.cells >self.function.upper_bound] = self.function.upper_bound
        self.fitness = self.function.evaluate(self.cells)   
                     
    def tweakSegment(self, bandwidth: float, efos):
        bandwidth = bandwidth - 0.0001*efos
        bandwidths = np.random.uniform(low=-bandwidth, high=bandwidth, size=(self.size,))        
        self.cells = self.cells + bandwidths
        self.cells[self.cells <self.function.lower_bound] = self.function.lower_bound
        self.cells[self.cells >self.function.upper_bound] = self.function.upper_bound
        self.fitness = self.function.evaluate(self.cells)   
        
    def __str__(self):
        return "cells:" + str(self.cells) + \
               "-fit:" + str(self.fitness)
