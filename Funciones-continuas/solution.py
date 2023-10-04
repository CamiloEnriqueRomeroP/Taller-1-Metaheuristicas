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
        S_rand = []
        param = []
        fitness_component = []
        components = np.random.uniform(low=self.function.lower_bound, high=self.function.upper_bound, size=(self.size,))
        for d in range (0, self.size):
            fitness_component.append(self.function.evaluate(components[d:d+1]))
        new_d_list = np.c_[fitness_component, components]
        C_prima = np.copy(new_d_list)
        constructing_solution = []
        for var in range(self.cells.size):
            if len(C_prima) == 0:
                break
            else:
                C_sorted = sorted(C_prima, key=lambda x: x[0], reverse=False)
                C_two_prima = int(len(C_sorted)*0.33)+1
                pos = np.random.randint(C_two_prima)
                s_random_component = C_sorted[pos]
                S_rand.append(s_random_component)
                S_set = {tuple(sublist) for sublist in S_rand}
                C_prima = [sublist for sublist in new_d_list if tuple(
                    sublist) not in S_set]
        
        for i in range(0, self.cells.size):
            constructing_solution.append(S_rand[i][1])        
        constructing_solution_np = np.array(constructing_solution)
        self.cells = constructing_solution_np.astype(int)
        self.fitness = self.function.evaluate(self.cells)        
                
    def tweak(self, bandwidth: float):
        bandwidths = np.random.uniform(
            low=-bandwidth, high=bandwidth, size=(self.size,))
        self.cells = self.cells + bandwidths
        self.cells[self.cells <
                   self.function.lower_bound] = self.function.lower_bound
        self.cells[self.cells >
                   self.function.upper_bound] = self.function.upper_bound
        self.fitness = self.function.evaluate(self.cells)   

    def __str__(self):
        return "cells:" + str(self.cells) + \
               "-fit:" + str(self.fitness)
