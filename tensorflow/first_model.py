import tensorflow as tf
import numpy as np

# Training data
X = np.array([
    [2, 50],
    [4, 60],
    [5, 70],
    [8, 90],
    [10, 95]
], dtype=np.float32)

y = np.array([
    0,
    0,
    1,
    1,
    1
], dtype=np.float32)

# Build model
model = tf.keras.Sequential([
    tf.keras.layers.Dense(1, input_shape=(2,))
])

# Compile model
model.compile(
    optimizer='sgd',
    loss='mse'
)

# Train model
model.fit(X, y, epochs=50, verbose=1)

# Test prediction
prediction = model.predict(
    np.array([[6, 80]], dtype=np.float32)
)

print("Prediction:", prediction)