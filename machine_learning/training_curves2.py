import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

# Create dataset
X = np.random.rand(1000, 4)

# Rule:
# If sum of 4 numbers > 2 => class 1
# Else => class 0
y = (X.sum(axis=1) > 2).astype(int)

# Build model
model = tf.keras.Sequential([
    tf.keras.layers.Dense(
        8,
        activation="relu",
        input_shape=(4,)
    ),

    tf.keras.layers.Dense(
        1,
        activation="sigmoid"
    )
])

# Compile model
model.compile(
    optimizer="adam",
    loss="binary_crossentropy",
    metrics=["accuracy"]
)

# Train model
history = model.fit(
    X,
    y,
    epochs=50,
    validation_split=0.2,
    verbose=1
)

# Show what TensorFlow stored
print("\nStored metrics:")
print(history.history.keys())

# -------------------------
# LOSS GRAPH
# -------------------------
plt.figure(figsize=(8, 5))

plt.plot(history.history["loss"])
plt.plot(history.history["val_loss"])

plt.title("Training Loss vs Validation Loss")
plt.xlabel("Epoch")
plt.ylabel("Loss")

plt.legend([
    "Training Loss",
    "Validation Loss"
])

plt.grid(True)
plt.show()

# -------------------------
# ACCURACY GRAPH
# -------------------------
plt.figure(figsize=(8, 5))

plt.plot(history.history["accuracy"])
plt.plot(history.history["val_accuracy"])

plt.title("Training Accuracy vs Validation Accuracy")
plt.xlabel("Epoch")
plt.ylabel("Accuracy")

plt.legend([
    "Training Accuracy",
    "Validation Accuracy"
])

plt.grid(True)
plt.show()