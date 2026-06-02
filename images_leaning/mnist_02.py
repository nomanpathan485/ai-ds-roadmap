import tensorflow as tf
import matplotlib.pyplot as plt

(x_train, y_train), (x_test,Y_test) = tf.keras.datasets.mnist.load_data()

plt.imshow(x_train[0], cmap="gray")
plt.title(f"label: {y_train[0]}")
plt.show()

print("Image shape:", x_train[0].shape)
print("Label:", y_train[0])