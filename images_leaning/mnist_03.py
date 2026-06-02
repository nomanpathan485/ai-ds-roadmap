import tensorflow as tf
import matplotlib.pyplot as plt

(X_train, y_train), (X_test, y_test) = tf.keras.datasets.mnist.load_data()

plt.imshow(X_train[0], cmap="gray")
plt.title(f"Label: {y_train[0]}")
plt.show()

print("Image shape:", X_train[0].shape)
print("Label:", y_train[0])

print("\nFirst 5 pixels of first row:")
print(X_train[0][0][:5])