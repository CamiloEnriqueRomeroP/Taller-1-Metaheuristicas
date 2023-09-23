import numpy as np

# http://www.sfu.ca/~ssurjano/spheref.html
class sphere:
    def __init__(self, lb: float = -5.12, ub: float = 5.12):
        self.lower_bound = lb
        self.upper_bound = ub
        self.optimum = 0.0

    @staticmethod
    def evaluate(cells):
        # sphere = x[0]^2 + x[1]^2 + x[2]^2 + ... + x[n-1]^2
        summa = (np.power(cells,2)).sum()
        return summa

    def __str__(self):
        return "Sphere-lb:" + str(self.lower_bound) + '-up:' + str(self.upper_bound)