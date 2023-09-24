import numpy as np

arr = np.arange(15)
# Use fill() function
arr[9:len(arr)] = 1
print(arr)
