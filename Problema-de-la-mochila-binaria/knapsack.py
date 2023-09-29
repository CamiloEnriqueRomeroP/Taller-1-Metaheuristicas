import numpy as np
import os

class knapsack:
    def __init__(self, filename):
        self.name = os.path.basename(filename)
        self.name = os.path.splitext(self.name)[0]
        file1 = open(filename, 'r')
        lines = file1.readlines()

        firstline = lines[0].split(' ')

        self.size = int(firstline[0])
        self.capacity = float(firstline[1].strip())
        self.profits = np.zeros(self.size, dtype=float)
        self.weights = np.zeros(self.size, dtype=float)

        positionLine = 1
        for i in range(0, self.size):
            line = lines[positionLine].split(' ')
            self.profits[positionLine - 1] = float(line[0].replace(',', '.'))
            self.weights[positionLine - 1] = float(line[1].replace(',', '.'))
            positionLine = positionLine + 1
        self.OptimalKnown = float(lines[positionLine].replace(',', '.'))

        self.items = []
        for i in range(0, self.size):
            self.items.append([i, self.weights[i], self.profits[i],
                          self.profits[i] / self.weights[i]])

    def table_of_items(self):
        copy_of_items = self.items.copy()
        return copy_of_items

    def evaluate(self, cells):
        weight = (cells * self.weights).sum()
        fitness = -1
        if weight <= self.capacity:
            fitness = (cells * self.profits).sum()
        #else:
            #print("Error")
        return fitness, weight

    def __str__(self):
        return "file:" + str(self.name) + \
               "-size:" + str(self.size) + \
               "-opt:" + str(self.OptimalKnown)