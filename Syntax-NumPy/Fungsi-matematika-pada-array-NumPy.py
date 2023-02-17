import numpy as np

# Menghitung rata-rata
arr = np.array([1, 2, 3, 4, 5])
mean = np.mean(arr)

# Menghitung standar deviasi
std = np.std(arr)

# Menghitung korelasi antara dua array
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([5, 4, 3, 2, 1])
corr = np.corrcoef(arr1, arr2)
