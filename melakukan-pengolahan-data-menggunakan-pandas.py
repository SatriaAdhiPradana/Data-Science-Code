import pandas as pd

# Membaca file CSV
data = pd.read_csv('nama_file.csv')

# Menghitung rata-rata dari kolom tertentu
rata_rata = data['kolom_x'].mean()

# Membuat kolom baru dengan menggabungkan dua kolom
data['kolom_baru'] = data['kolom_x'] + data['kolom_y']

# Menampilkan data yang sudah diolah
print(data.head())
