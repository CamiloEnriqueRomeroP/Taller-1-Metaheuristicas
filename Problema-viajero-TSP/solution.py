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
        self.cells = np.random.choice(self.problem.size, self.problem.size, replace=False)
        self.fitness = self.problem.evaluate(self.cells)
        
        S_rand = [] 
        total_weight = 0 
        C_prima = self.problem.distances
        for var in range(self.cells.size):
            if not bool(C_prima.size):
                break
            else:
                # Hay que encontrar una manera de evaluar si una solucion es factible
                C_Ordernado = sorted(C_prima, key=lambda x: x[0], reverse=True)                    
                C_dos_prima = int(len(C_Ordernado)*0.33)+1
                i = np.random.randint(C_dos_prima)
                s_random_component = C_Ordernado[i]
                # hasta aqui tiene sentido
                weight_test = s_random_component[1]
                total_weight = total_weight + weight_test           
                if total_weight <= self.problem.capacity: 
                    S_rand.append(s_random_component)      
                    S_set = {tuple(sublista) for sublista in S_rand}
                    C_prima = [sublista for sublista in self.problem.items if tuple(sublista) not in S_set]  
                    self.cells[s_random_component[0]]=1      
                else:
                    self.evaluate()  
                    break    
        
        
        

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