import pandas as pd

# Membaca file CSV
data = pd.read_csv('nama_file.csv')

# Menampilkan statistik deskriptif
print(data.describe())
