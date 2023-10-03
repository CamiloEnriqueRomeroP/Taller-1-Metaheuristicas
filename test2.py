import numpy as np


def evaluate(cells):
    summa = 0
    for i in range(len(cells) + 1):
        summa = summa + np.power(cells[:i].sum(), 2)
    return summa


S = np.random.uniform(low=-5, high=5, size=(5,))
print(S[0:1])
Result = evaluate(S[0:1])
print(Result)
