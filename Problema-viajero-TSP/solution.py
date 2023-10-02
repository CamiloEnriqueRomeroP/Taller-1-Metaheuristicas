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
                C_sorted = sorted(C_prima, key=lambda x: x[last_location+1], reverse=False)
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
        acum_fitness = []
        Part_1 = self.cells[0:int(len(self.cells)/3)+1]   
        Part_2 = self.cells[int(len(self.cells)/3)+1:int(len(self.cells)*2/3)+1] 
        Part_3 = self.cells[int(len(self.cells)*2/3)+1:int(len(self.cells))] 
        
        partial_solucion = [Part_1, Part_2, Part_3]
       
        x0, x1, x2, x3 = self.construct_partial_solution(partial_solucion, 0)
        y0, y1, y2, y3 = self.construct_partial_solution(partial_solucion, 1)
        z0, z1, z2, z3 = self.construct_partial_solution(partial_solucion, 2)
        
        copy_cells = np.copy(self.cells)
                        
        # A, B, C
        fitness_ABC = self.fitness
        solution_ABC = np.copy(self.cells)
        
        # A', B, C
        fitness_ApBC = self.fitness-self.new_fitness(x0, x1, x2, x3)  
        solution_ApBC = self.swapPositions(copy_cells, x1, x2) 
        copy_cells = np.copy(self.cells)
        # A, B', C        
        fitness_ABpC = self.fitness-self.new_fitness(y0, y1, y2, y3)  
        solution_ABpC = self.swapPositions(copy_cells, y1, y2) 
        copy_cells = np.copy(self.cells)
        # A, B, C'
        fitness_ABCp = self.fitness-self.new_fitness(z0, z1, z2, z3)  
        solution_ABCp = self.swapPositions(copy_cells, z1, z2) 
        copy_cells = np.copy(self.cells)
        # A', B', C
        fitness_ApBpC = self.fitness-self.new_fitness(x0, x1, x2, x3)-self.new_fitness(y0, y1, y2, y3)   
        solution_ApBpC = self.swapPositions(copy_cells, x1, x2) 
        solution_ApBpC = self.swapPositions(copy_cells, y1, y2) 
        copy_cells = np.copy(self.cells)
        # A, B', C'
        fitness_ABpCp = self.fitness-self.new_fitness(y0, y1, y2, y3)-self.new_fitness(z0, z1, z2, z3)    
        solution_ABpCp = self.swapPositions(copy_cells, y1, y2)   
        solution_ABpCp = self.swapPositions(copy_cells, z1, z2) 
        copy_cells = np.copy(self.cells)
        # A', B, C'
        fitness_ApBCp = self.fitness-self.new_fitness(x0, x1, x2, x3)-self.new_fitness(z0, z1, z2, z3)  
        solution_ApBCp = self.swapPositions(copy_cells, x1, x2) 
        solution_ApBCp = self.swapPositions(copy_cells, z1, z2) 
        copy_cells = np.copy(self.cells)
        # A', B', C'
        fitness_ApBpCp = self.fitness-self.new_fitness(x0, x1, x2, x3)-self.new_fitness(y0, y1, y2, y3)-self.new_fitness(z0, z1, z2, z3)     
        solution_ApBpCp = self.swapPositions(copy_cells, x1, x2) 
        solution_ApBpCp = self.swapPositions(copy_cells, y1, y2) 
        solution_ApBpCp = self.swapPositions(copy_cells, z1, z2) 
        copy_cells = np.copy(self.cells)
        
        acum_fitness = [[fitness_ABC,solution_ABC],
                        [fitness_ApBC,solution_ApBC],
                        [fitness_ABpC,solution_ABpC],
                        [fitness_ABCp,solution_ABCp],
                        [fitness_ApBpC,solution_ApBpC],
                        [fitness_ABpCp,solution_ABpCp],
                        [fitness_ApBCp,solution_ApBCp],
                        [fitness_ApBpCp,solution_ApBpCp]]
        
        est_fitness = acum_fitness.max(axis=0)

    def construct_partial_solution(self, partial_solucion, count):
        local_part = partial_solucion[count]
        i = np.random.randint(len(local_part)-1)
        pos_1 = local_part[i]
        pos_2 = local_part[i+1]       
        if i == 0:
            if count == 0:
                previous_part = partial_solucion[2]
                pos_0 = previous_part[-1]
            else:
                previous_part = partial_solucion[count-1]
                pos_0 = previous_part[-1]
        else:
            pos_0 = local_part[i-1]            
        if i == len(local_part)-2:
            if count == 2:
                next_part = partial_solucion[0]
                pos_3 = next_part[0]
            else:
                next_part = partial_solucion[count+1]
                pos_3 = next_part[0]
        else:              
            pos_3 = local_part[i+2]             
        return pos_0, pos_1, pos_2, pos_3

    def new_fitness(self, Previous_Start, Start, End, Post_End):
        subtraction = self.problem.distance(Previous_Start, Start)+self.problem.distance(End, Post_End)
        addition = self.problem.distance(Previous_Start, End)+self.problem.distance(Start, Post_End)
        return addition - subtraction
    
    def swapPositions(self, copy_cells, start, end):
        for i in range(len(copy_cells)):
            if copy_cells[i] == start:
                pos1 = i                
                break
        for j in range(len(copy_cells)):
            if copy_cells[j] == end:
                pos2 = j                
                break                
        copy_cells[pos1], copy_cells[pos2] = copy_cells[pos2], copy_cells[pos1]
        return copy_cells

    def __str__(self):
        return "cells:" + str(self.cells) + \
               "-fit:" + str(self.fitness)
