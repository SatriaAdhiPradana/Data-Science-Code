import matplotlib.pyplot as plt

# Membuat plot
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
plt.plot(x, y)

# Menambahkan label pada sumbu x dan y
plt.xlabel('Nilai x')
plt.ylabel('Nilai y')

# Menambahkan judul plot
plt.title('Grafik nilai x dan y')

# Menampilkan plot
plt.show()
