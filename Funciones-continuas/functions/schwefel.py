import numpy as np

# https://goker.dev/iom/benchmarks/schwefel-1.2
class schwefel:
    def __init__(self, lb: float = -100, ub: float = 100):
        self.lower_bound = lb
        self.upper_bound = ub
        self.optimum = 0.0

    @staticmethod
    def evaluate(cells):
        summa = 0
        for i in range(len(cells) + 1):
            summa = summa + np.power(cells[:i].sum(), 2)
        return summa

    def __str__(self):
        return "Schwefel-1.2-lb:" + str(self.lower_bound) + '-up:' + str(self.upper_bound)
