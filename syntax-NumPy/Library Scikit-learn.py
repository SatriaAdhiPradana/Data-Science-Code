from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Memuat dataset
from sklearn.datasets import load_boston
boston = load_boston()

# Membagi dataset menjadi data latih dan data uji
X_train, X_test, y_train, y_test = train_test_split(boston.data, boston.target, test_size=0.2, random_state=0)

# Membuat model regresi linear
model = LinearRegression()

# Melatih model menggunakan data latih
model.fit(X_train, y_train)

# Memprediksi data uji menggunakan model
y_pred = model.predict(X_test)
