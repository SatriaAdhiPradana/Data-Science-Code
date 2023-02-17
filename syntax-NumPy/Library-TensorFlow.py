import tensorflow as tf

# Membuat model neural network sederhana
model = tf.keras.models.Sequential([
  tf.keras.layers.Dense(64, activation='relu', input_shape=(10,)),
  tf.keras.layers.Dense(64, activation='relu'),
  tf.keras.layers.Dense(1)
])

# Mengompilasi model
model.compile(optimizer=tf.keras.optimizers.Adam(0.001),
              loss='mse',
              metrics=['mae'])

# Melatih model menggunakan data latih
model.fit(X_train, y_train, epochs=100, validation_split=0.2)

# Memprediksi data uji menggunakan model
y_pred = model.predict(X_test)
