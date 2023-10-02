import numpy as np
from pathlib import Path

# Download problems at https://people.sc.fsu.edu/~jburkardt/datasets/tsp/tsp.html
# Download problems at TSPLIb -> http://comopt.ifi.uni-heidelberg.de/software/TSPLIB95/tsp/

class tsp:
    size: int

    def __init__(self, filename):
        file1 = open(filename, 'r')
        lines = file1.readlines()

        self.file_name = Path(filename).stem
        self.size = int(lines[0])

        # Coordinate of cities
        x = np.zeros(self.size, float)
        y = np.zeros(self.size, float)
        positionLine = 1
        for i in range(0, self.size):
            lines[positionLine] = lines[positionLine].rstrip() # remove \n
            line = lines[positionLine].split('\t')
            if line[0] != '?':
                x[positionLine - 1] = float(line[0])
                y[positionLine - 1] = float(line[1])
            positionLine = positionLine + 1

        # Distance matrix
        self.distances = np.zeros((self.size, self.size), dtype=float)
        for i in range(0, self.size):
            lines[positionLine] = lines[positionLine].rstrip()  # remove \n
            line = lines[positionLine].split('\t')
            for j in range(0, self.size):
                dis = float(line[j])
                self.distances[i][j] = self.distances[j][i] = dis
            positionLine = positionLine + 1

        # Best known solution (convert to zero based index required)
        self.bestKnown = np.zeros(self.size, dtype=int)
        for i in range(0, self.size):
            lines[positionLine] = lines[positionLine].rstrip()  # remove \n
            line = lines[positionLine].split('\n')
            if line[0] != '?':
                self.bestKnown[i] = int(line[0]) - 1
            positionLine = positionLine + 1

        # Tour length
        line = lines[positionLine].split('\n')
        self.bestFitness = 0
        if line[0] != '?':
            self.bestFitness = float(line[0])

    def distance(self, cityA: int, cityB: int):
        return self.distances[cityA][cityB]  # This problem is symmetric

    def evaluate(self, cells):
        fitness = 0
        for i in range(len(cells)):
            j = i + 1
            if j >= len(cells):
                j = 0
            fitness = fitness + self.distances[cells[i]][cells[j]]
        return fitness

    def __str__(self):
        return self.file_name + ' ' + str(self.bestFitness)