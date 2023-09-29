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
        optimal = self.problem.OptimalKnown
        stop_optimal = optimal - optimal*0.00001
        while efos < self.max_efos:
            C = solution(problem)                 
            S_rand = []
            self.best = solution(problem)                 
            S = solution(problem)  
            S_copy = solution(S.problem)
            C_prima = []
            C_2_prima = []
            # S.Initialization()  # Random initialization and calculating fitness
            # Perform the hill climbig optimization (local)
            if efos == 0:
                self.best.from_solution(S)  # self.best is a full copy of S
                best_fitness_history[0] = self.best.fitness
            C_prima = C.problem.items
            for var in range(C.cells.size):
                #print("Entra al ciclo")
                #if S:
                if not bool(C_prima):
                    #print("C_prima Is empty")
                    break
                else:
                    #print("C_prima Is not empty")
                    C_Ordernado = sorted(C_prima, key=lambda x: x[3], reverse=True)
                    C_dos_prima = C_Ordernado[0:int(len(C_Ordernado)*0.5)+1]
                    i = np.random.randint(len(C_dos_prima))
                    s_random_component = C_dos_prima[i]                    
                    S_copy.cells = np.copy(S.cells)
                    S_copy.cells[s_random_component[0]]=1
                    S_copy.evaluate()
                    #S.cells[s_random_component[0]]=1
                    #S.evaluate()
                    weight = S_copy.weight
                    if weight < problem.capacity: 
                        if not bool(S_rand):
                            S_rand.append(s_random_component)
                            continue     
                        S_rand.append(s_random_component)      
                        S_set = {tuple(sublista) for sublista in S_rand}
                        C_sin_repeticiones = [sublista for sublista in C.problem.items if tuple(sublista) not in S_set]
                        C_prima = C_sin_repeticiones  
                        S.cells[s_random_component[0]]=1                      
                        print(S)
                    else:
                        print("No es factible")
                        S.evaluate()
                        weight = S.weight
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
                    break
                if efos >= self.max_efos:
                    break        
        return best_fitness_history

    def __str__(self):
        result = "GRASP-maxlocal:" + str(self.max_local)
        return result
