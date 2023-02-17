import pandas as pd

# Membaca file CSV
df = pd.read_csv('data.csv')

# Menampilkan data awal
print(df.head())

# Menampilkan statistik deskriptif
print(df.describe())

# Mengambil kolom tertentu
col = df['kolom']

# Mengambil baris tertentu berdasarkan kondisi
baris = df.loc[df['kolom'] == 'nilai']

# Membuat kolom baru
df['kolom_baru'] = df['kolom_x'] + df['kolom_y']

# Menyimpan data ke file CSV
df.to_csv('data_baru.csv', index=False)
