import numpy as np
from solution import solution


class GRASP:
    def __init__(self, max_efos: int, max_local: int):
        self.max_efos = max_efos
        self.max_local = max_local

    def evolve(self, seed: int, problem):
        self.problem = problem
        np.random.seed(seed)
        best_fitness_history = np.zeros(self.max_efos, float)
        efos = 0
        stop_optimal = self.problem.OptimalKnown
        stop = False
        self.best = solution(problem)          
        while efos < self.max_efos:
            C = solution(problem)                 
            S_rand = []               
            S = solution(problem)  
            S_copy = solution(S.problem)
            C_prima = []
            total_weight = 0
            if efos == 0:
                self.best.from_solution(S)  # self.best is a full copy of S
                best_fitness_history[0] = self.best.fitness
            C_prima = C.problem.items
            for var in range(C.cells.size):
                if not bool(C_prima):
                    #print("C_prima Is empty")
                    break
                else:
                    #print("C_prima Is not empty")
                    C_Ordernado = sorted(C_prima, key=lambda x: x[3], reverse=True)                    
                    C_dos_prima = int(len(C_Ordernado)*0.33)+1
                    i = np.random.randint(C_dos_prima)
                    s_random_component = C_Ordernado[i]
                    S_copy.cells = np.copy(S.cells)
                    S_copy.cells[s_random_component[0]]=1
                    S_copy.evaluate()
                    
                    weight_test = s_random_component[1]
                    total_weight = total_weight + weight_test
                    weight = S_copy.weight                    
                    if weight <= problem.capacity: 
                        if not bool(S_rand):
                            S_rand.append(s_random_component)
                            S.cells[s_random_component[0]]=1     
                            continue     
                        S_rand.append(s_random_component)      
                        S_set = {tuple(sublista) for sublista in S_rand}
                        C_sin_repeticiones = [sublista for sublista in C.problem.items if tuple(sublista) not in S_set]
                        C_prima = C_sin_repeticiones  
                        S.cells[s_random_component[0]]=1      
                    else:
                        #print("No es factible")
                        S.cells[s_random_component[0]]=0  
                        #S.evaluate() 
                        break                    

            for opt in range(1, self.max_local):
                R = solution(S.problem)
                R.from_solution(S)  # R is a full copy of S
                R.tweak()  # Tweeking and calculating fitness
                if R.fitness > S.fitness:
                    S.from_solution(R)
                if S.fitness > self.best.fitness:
                    self.best.from_solution(S)  # self.best is a full copy of S
                best_fitness_history[efos] = self.best.fitness
                efos += 1
                if S.fitness >= stop_optimal:
                    best_fitness_history[efos:self.max_efos] = self.best.fitness
                    efos = self.max_efos
                    stop = True
                    break
                if efos >= self.max_efos:
                    break        
        return best_fitness_history, stop

    def __str__(self):
        result = "GRASP-maxlocal:" + str(self.max_local)
        return result
