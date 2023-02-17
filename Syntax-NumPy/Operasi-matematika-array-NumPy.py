import numpy as np

# Operasi matematika dasar
arr = np.array([1, 2, 3, 4, 5])
arr += 2
arr *= 2
arr /= 2
arr -= 2

# Operasi matematika pada array dengan dimensi berbeda
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
arr3 = arr1 + arr2
arr4 = np.dot(arr1, arr2)
