import numpy as np

# http://www.sfu.ca/~ssurjano/rastr.html
class rastrigin:
    def __init__(self, lb: float = -5.12, ub: float = 5.12):
        self.lower_bound = lb
        self.upper_bound = ub
        self.optimum = 0.0

    @staticmethod
    def evaluate(cells):
        d = len(cells)
        summa = 10 * d + (np.power(cells, 2) - 10 * np.cos(2 * np.pi * cells)).sum()
        return summa

    def __str__(self):
        return "Rastrigin-lb:" + str(self.lower_bound) + '-up:' + str(self.upper_bound)