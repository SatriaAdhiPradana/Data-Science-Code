import numpy as np
import pandas as pd

# Membaca file CSV
data = pd.read_csv('nama_file.csv')

# Mengubah data ke dalam bentuk array NumPy
data_array = np.array(data)

# Melakukan operasi matematika pada array
data_array *= 2

# Menampilkan array yang sudah diolah
print(data_array)
