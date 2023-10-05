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
            constructing_solution.append(S_rand[i][0])
        constructing_solution_np = np.array(constructing_solution)
        self.cells = constructing_solution_np.astype(int)
        self.fitness = self.problem.evaluate(self.cells)

    # Original Tweak
    def tweak(self):
        pos = np.random.choice(
            np.arange(1, self.problem.size), 2, replace=False)
        pos.sort()
        i = pos[0]
        k = pos[1]
        self.cells[i:k] = self.cells[k - 1:i - 1:-1]
        print(self.cells)
        self.fitness = self.problem.evaluate(self.cells)

    def tweak_3opt(self):

        part1, part2, part3 = self.segment_solution()
        x2, y1, y2, z1, z2, x1 = 0, part1[-1], part2[0], part2[-1], part3[0], part3[-1]

        # A, B, C
        fitness_ABC = self.fitness
        solution_ABC = np.concatenate((part1, part2, part3))
        # A', B, C
        fitness_ApBC = self.fitness+self.new_fitness(x1, x2, y1, y2)
        A_prima = self.swapPositions(part1)
        solution_ApBC = np.concatenate((A_prima, part2, part3))
        # A, B', C
        fitness_ABpC = self.fitness+self.new_fitness(y1, y2, z1, z2)
        B_prima = self.swapPositions(part2)
        solution_ABpC = np.concatenate((part1, B_prima, part3))
        # A, B, C'
        fitness_ABCp = self.fitness+self.new_fitness(z1, z2, x1, x2)
        C_prima = self.swapPositions(part3)
        solution_ABCp = np.concatenate((part1, part2, C_prima))
        # A', B', C
        fitness_ApBpC = self.fitness + \
            self.new_fitness(x1, x2, y1, y2)+self.new_fitness(y1, y2, z1, z2)
        solution_ApBpC = np.concatenate((A_prima, B_prima, part3))
        # A, B', C'
        fitness_ABpCp = self.fitness + \
            self.new_fitness(y1, y2, z1, z2)+self.new_fitness(z1, z2, x1, x2)
        solution_ABpCp = np.concatenate((part1, B_prima, C_prima))
        # A', B, C'
        fitness_ApBCp = self.fitness + \
            self.new_fitness(x1, x2, y1, y2)+self.new_fitness(z1, z2, x1, x2)
        solution_ApBCp = np.concatenate((A_prima, part2, C_prima))
        # A', B', C'
        fitness_ApBpCp = self.fitness+self.new_fitness(x1, x2, y1, y2)+self.new_fitness(
            y1, y2, z1, z2)+self.new_fitness(z1, z2, x1, x2)
        solution_ApBpCp = np.concatenate((A_prima, B_prima, C_prima))

        acum_fitness = [[fitness_ABC, solution_ABC],
                        [fitness_ApBC, solution_ApBC],
                        [fitness_ABpC, solution_ABpC],
                        [fitness_ABCp, solution_ABCp],
                        [fitness_ApBpC, solution_ApBpC],
                        [fitness_ABpCp, solution_ABpCp],
                        [fitness_ApBCp, solution_ApBCp],
                        [fitness_ApBpCp, solution_ApBpCp]]

        best_acum_fitness = sorted(
            acum_fitness, key=lambda x: x[0], reverse=False)[0][0]
        best_solution = sorted(
            acum_fitness, key=lambda x: x[0], reverse=False)[0][1]
        self.cells = np.copy(best_solution)
        self.fitness = self.problem.evaluate(self.cells)

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
        subtraction = self.problem.distance(
            Previous_Start, Start)+self.problem.distance(End, Post_End)
        addition = self.problem.distance(
            Previous_Start, End)+self.problem.distance(Start, Post_End)
        return addition - subtraction

    def swapPositions(self, part):
        reversed_part = part[::-1]
        return reversed_part

    def __str__(self):
        return "cells:" + str(self.cells) + \
               "-fit:" + str(self.fitness)

    def segment_solution(self):
        copy_solution = np.copy(self.cells)

        n = np.random.randint(0, self.cells.size)

        # Aseguramos que n esté dentro del rango del tamaño del vector
        n = n % len(copy_solution)
        copy_solution[:] = np.concatenate(
            (copy_solution[-n:], copy_solution[:-n]))

        # Calculamos el tamaño objetivo para cada parte
        size_objetive = self.problem.size // 3

        # Verificamos si la longitud del vector es un múltiplo de 3
        if self.problem.size % 3 == 0:
            # Si es un múltiplo de 3, dividimos el vector en tres partes de igual tamaño
            part1 = copy_solution[:size_objetive]
            part2 = copy_solution[size_objetive:2 * size_objetive]
            part3 = copy_solution[2 * size_objetive:]
        else:
            # Si no es un múltiplo de 3, aplicamos la lógica de ajuste para minimizar la diferencia
            # Calculamos el tamaño máximo permitido para la diferencia entre las partes
            max_diference = 1

            # Inicializamos las variables de corte
            section1, section2 = 0, 0

            # Intentamos encontrar los puntos de corte que cumplan con las condiciones
            while True:
                section1 = np.random.randint(
                    size_objetive - max_diference, size_objetive + 1)
                section2 = np.random.randint(
                    2 * size_objetive - max_diference, 2 * size_objetive + 1)

                # Verificamos si los cortes cumplen con las condiciones
                if 0 < section1 < section2 < self.problem.size:
                    break

            # Segmentamos el vector en tres partes
            part1 = copy_solution[:section1]
            part2 = copy_solution[section1:section2]
            part3 = copy_solution[section2:]
            part1 = np.array(part1)
            part2 = np.array(part2)
            part3 = np.array(part3)
        return part1, part2, part3
