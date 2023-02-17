import matplotlib.pyplot as plt
import pandas as pd

# Membaca file CSV
data = pd.read_csv('nama_file.csv')

# Membuat plot
plt.plot(data['kolom_x'], data['kolom_y'])

# Menampilkan plot
plt.show()
