import numpy as np
import math

# http://www.sfu.ca/~ssurjano/ackley.html
class ackley:
    def __init__(self, lb: float = -32.768, ub: float = 32.768):
        self.lower_bound = lb
        self.upper_bound = ub
        self.optimum = 0.0

    @staticmethod
    def evaluate(cells):
        a = 20
        b = 0.2
        c = 2 * np.pi
        d = len(cells)
        t1 = - a * math.exp( - b * math.sqrt((1 / d) * (np.power(cells, 2)).sum()))
        t2 = - math.exp((1 / d) * (np.cos(c * cells)).sum())
        return t1 + t2 + a + math.exp(1)

    def __str__(self):
        return "Ackley-lb:" + str(self.lower_bound) + '-up:' + str(self.upper_bound)