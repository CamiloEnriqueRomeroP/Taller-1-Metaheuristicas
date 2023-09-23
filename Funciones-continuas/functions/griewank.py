import numpy as np

# http://www.sfu.ca/~ssurjano/griewank.html
class griewank:
    def __init__(self, lb: float = -600, ub: float = 600):
        self.lower_bound = lb
        self.upper_bound = ub
        self.optimum = 0.0

    @staticmethod
    def evaluate(cells):
        i = np.arange(1, len(cells) + 1)
        t1 = (np.power(cells, 2)).sum() / 4000
        t2 = - np.prod(np.cos(cells / np.sqrt(i)))
        return t1 + t2 + 1

    def __str__(self):
        return "Griewank-lb:" + str(self.lower_bound) + '-up:' + str(self.upper_bound)