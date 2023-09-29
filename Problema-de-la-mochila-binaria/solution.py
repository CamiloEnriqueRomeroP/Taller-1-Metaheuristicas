import numpy as np
import knapsack


class solution:
    def __init__(self, p: knapsack):
        self.problem = p
        self.cells = np.zeros(self.problem.size, int)
        self.fitness = 0.0
        self.weight = 0.0

    def from_solution(self, origin):
        self.problem = origin.problem
        self.cells = np.copy(origin.cells)
        self.fitness = origin.fitness
        self.weight = origin.weight

    def evaluate(self):
        self.fitness, self.weight = self.problem.evaluate(self.cells)

    # Original code
    # def Initialization(self):
    #     positions = np.random.choice(self.problem.size, self.problem.size, replace=False)
    #     self.cells = np.zeros(self.problem.size, int)
    #     self.add_items_while_keep_capacity(positions, 0)
    #     self.evaluate()

    # def add_items_while_keep_capacity(self, positions, weight):
    #     self.weight = weight
    #     for p in positions:
    #         if self.weight + self.problem.weights[p] < self.problem.capacity:
    #             self.cells[p] = 1
    #             self.weight += self.problem.weights[p]

    # def tweak(self):
    #     selectedPositions = np.where(self.cells == 1)[0]
    #     unselectedPositions = np.where(self.cells == 0)[0]
    #     x = np.random.randint(len(selectedPositions), size=1)
    #     elementToRemove = selectedPositions[x[0]]
    #     self.cells[elementToRemove] = 0
    #     self.weight = self.weight - self.problem.weights[elementToRemove]
    #     self.fitness = self.fitness - self.problem.profits[elementToRemove]
    #     self.complete(unselectedPositions, False)

    def Initialization(self):
        positions = np.random.choice(
            self.problem.size, self.problem.size, replace=False)
        self.cells = np.zeros(self.problem.size, int)
        self.add_items_while_keep_capacity(positions, 0)
        self.evaluate()    
    
    # def Initialization_GRASP(self,Solution):
    #     C_Ordernado = sorted(C_prima, key=lambda x: x[3], reverse=True)
    #     C_dos_prima = int(len(C_Ordernado)*0.33)+1
    #     i = np.random.randint(C_dos_prima)
    #     s_random_component = C_Ordernado[i]   
    #     Solution.cells = np.copy(S.cells)
    #     Solution.cells[s_random_component[0]] = 1
    #     Solution.evaluate()
    #     weight = Solution.weight
    #     if weight < problem.capacity:
    #         if not bool(S_rand):
    #             S_rand.append(s_random_component)
    #         S_rand.append(s_random_component)
    #         S_set = {tuple(sublista) for sublista in S_rand}
    #         C_sin_repeticiones = [
    #             sublista for sublista in C.problem.items if tuple(sublista) not in S_set]
    #         C_prima = C_sin_repeticiones
    #         S.cells[s_random_component[0]] = 1
    #     else:
    #         # print("No es factible")
    #         S.evaluate()
    #         weight = S.weight
    #         break

    def add_items_while_keep_capacity(self, positions, weight):
        self.weight = weight
        for p in positions:
            if self.weight + self.problem.weights[p] < self.problem.capacity:
                self.cells[p] = 1
                self.weight += self.problem.weights[p]

    def tweak(self):
        selectedPositions = np.where(self.cells == 1)[0]
        unselectedPositions = np.where(self.cells == 0)[0]
        x = np.random.randint(len(selectedPositions), size=1)
        elementToRemove = selectedPositions[x[0]]
        self.cells[elementToRemove] = 0
        self.weight = self.weight - self.problem.weights[elementToRemove]
        self.fitness = self.fitness - self.problem.profits[elementToRemove]
        self.complete(unselectedPositions, False)

    def complete(self, unselectedPositions, calculatePositions):
        if calculatePositions:
            unselectedPositions = np.where(self.cells == 0)[0]

        empty = self.problem.capacity - self.weight
        while empty > 0 and len(unselectedPositions) > 0:
            fitUnselected = np.array(
                [unselectedPositions, self.problem.weights[unselectedPositions]])
            fitUnselected = fitUnselected[:, np.where(
                fitUnselected[1, :] < empty)][0]
            unselectedPositions = np.copy(fitUnselected[0])
            if len(fitUnselected[0]) == 0:
                break
            elementToAdd = int(
                fitUnselected[0][np.random.randint(len(fitUnselected[0]))])
            self.cells[elementToAdd] = 1
            self.weight = self.weight + self.problem.weights[elementToAdd]
            self.fitness = self.fitness + self.problem.profits[elementToAdd]
            unselectedPositions = np.array(unselectedPositions[np.where(unselectedPositions != elementToAdd)],
                                           dtype=int)
            empty = self.problem.capacity - self.weight

    def __str__(self):
        result = "Cells:" + str(self.cells) + \
                 "-fitness:" + str(self.fitness)
        return result
