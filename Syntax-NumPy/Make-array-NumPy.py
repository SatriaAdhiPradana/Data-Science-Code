import numpy as np

# Membuat array dari list
arr = np.array([1, 2, 3, 4, 5])

# Membuat array kosong dengan 5 elemen
arr = np.empty(5)

# Membuat array dengan nilai 0, dengan dimensi 2x3
arr = np.zeros((2, 3))

# Membuat array dengan nilai 1, dengan dimensi 2x3
arr = np.ones((2, 3))

# Membuat array dengan nilai acak antara 0 dan 1, dengan dimensi 2x3
arr = np.random.rand(2, 3)

# Membuat array dengan nilai acak dari distribusi normal, dengan dimensi 2x3
arr = np.random.randn(2, 3)
