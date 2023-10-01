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
        
    def Initialization_GRASP(self):
        S_rand = [] 
        last_location = 0
        number_size = np.arange(0, self.cells.size)
        constructing_solution = []
        new_d_list = np.c_[number_size,self.problem.distances]
        C_prima = np.c_[number_size,self.problem.distances]
        for var in range(self.cells.size):
            if len(C_prima) == 0:
                break
            else:
                C_Ordernado = sorted(C_prima, key=lambda x: x[last_location+1], reverse=False)                    
                C_dos_prima = int(len(C_Ordernado)*0.33)+1
                pos = np.random.randint(C_dos_prima)
                s_random_component = C_Ordernado[pos]
                S_rand.append(s_random_component)    
                S_set = {tuple(sublista) for sublista in S_rand}
                C_prima = [sublista for sublista in new_d_list if tuple(sublista) not in S_set] 
                last_location = int(s_random_component[0])
        
        for i in range(0, self.cells.size):
            constructing_solution = np.append(constructing_solution, S_rand[i][0])
        self.cells = constructing_solution.astype(int)   
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