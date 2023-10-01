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
        self.cells = np.random.choice(
            self.problem.size, self.problem.size, replace=False)
        self.fitness = self.problem.evaluate(self.cells)

    def Initialization_GRASP(self):
        S_rand = []
        last_location = 0
        number_size = np.arange(0, self.cells.size)
        constructing_solution = []
        new_d_list = np.c_[number_size, self.problem.distances]
        C_prima = np.c_[number_size, self.problem.distances]
        for var in range(self.cells.size):
            if len(C_prima) == 0:
                break
            else:
                C_sorted = sorted(
                    C_prima, key=lambda x: x[last_location+1], reverse=False)
                C_two_prima = int(len(C_sorted)*0.33)+1
                pos = np.random.randint(C_two_prima)
                s_random_component = C_sorted[pos]
                S_rand.append(s_random_component)
                S_set = {tuple(sublist) for sublist in S_rand}
                C_prima = [sublist for sublist in new_d_list if tuple(
                    sublist) not in S_set]
                last_location = int(s_random_component[0])

        for i in range(0, self.cells.size):
            constructing_solution = np.append(
                constructing_solution, S_rand[i][0])
        self.cells = constructing_solution.astype(int)
        self.fitness = self.problem.evaluate(self.cells)

    # Original Tweak
    def tweak(self):
        pos = np.random.choice(
            np.arange(1, self.problem.size), 2, replace=False)
        pos.sort()
        i = pos[0]
        k = pos[1]
        self.cells[i:k] = self.cells[k - 1:i - 1:-1]
        self.fitness = self.problem.evaluate(self.cells)

    def tweak_3opt(self):
        Inicial_Solution = self.cells
        Part_1 = Inicial_Solution[0:int(len(Inicial_Solution)/3)+1]   
        Part_2 = Inicial_Solution[int(len(Inicial_Solution)/3)+1:int(len(Inicial_Solution)*2/3)+1] 
        Part_3 = Inicial_Solution[int(len(Inicial_Solution)*2/3)+1:int(len(Inicial_Solution))] 
        X1 = np.random.choice(Part_1[0:len(Part_1)-1], 1)
        X2 = Part_1[X1+1]
        if X1 == Part_1[0]:
            X0 = Part_3[-1]
        else:
            X0 = Part_1[X1-1]
            
            
            
        self.fitness = self.problem.evaluate(self.cells)
        # falta definir las seis ciudades a modificar
        C_1 = 0
        C_2 = 1
        C_3 = 2
        C_4 = 3
        C_5 = 4
        X1 = C_2
        X2 = C_2+1
        Y1 = C_3
        Y2 = C_3+1
        Z1 = C_4
        Z2 = C_4+1
        self.fitness = self.new_fitness(X1, X2)  
        self.cells = self.swapPositions(self.cells, X1, X2)
             

        self.fitness = self.new_fitness(Y1, Y2) 
        self.cells = self.swapPositions(self.cells, Y1, Y2)
        print(self.cells)
        print(self.fitness)
        self.fitness = self.new_fitness(Z1, Z2) 
        self.cells = self.swapPositions(self.cells, Z1, Z2)
        print(self.cells)
        print(self.fitness)

    def new_fitness(self, Start, End):
        subtraction = self.problem.distance(self.cells[Start-1], self.cells[Start])+self.problem.distance(self.cells[End], self.cells[End+1])
        addition = self.problem.distance(self.cells[Start-1], self.cells[End])+self.problem.distance(self.cells[Start], self.cells[End+1])
        return self.fitness-subtraction+addition
    
    def swapPositions(self, cells, pos1, pos2):
        cells[pos1], cells[pos2] = cells[pos2], cells[pos1]
        return self.cells

    def __str__(self):
        return "cells:" + str(self.cells) + \
               "-fit:" + str(self.fitness)
