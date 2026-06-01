import tensorflow as tf
import numpy as np

# Dataset
X = np.array([
    [0.2, 0.5],
    [0.4, 0.6],
    [0.5, 0.7],
    [0.8, 0.9],
    [1.0, 0.95]
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
    tf.keras.layers.Dense(
        3,
        activation="sigmoid",
        input_shape=(2,)
    )
])

# Compile model
model.compile(
    optimizer="adam",
    loss="binary_crossentropy",
    metrics=["accuracy"]
)

# Train model
model.fit(
    X,
    y,
    epochs=50
)

# Predict
prediction = model.predict(
    np.array([[0.6, 0.8]], dtype=np.float32)
)

print(prediction)

print("\nWeights and Bias:")

weights, bias = model.layers[0].get_weights()

print("Weights:")
print(weights)

print("\nBias:")
print(bias)
