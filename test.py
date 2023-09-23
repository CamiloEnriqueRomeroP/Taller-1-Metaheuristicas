import numpy as np


arr = np.zeros(10)
arr[4:len(arr)] = 1
print(arr)