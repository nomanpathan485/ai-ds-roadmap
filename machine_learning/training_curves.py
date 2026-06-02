import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

x = np.random.rand(1000, 4)
y = (x.sum(axis=1)>2).astype(int)

model = tf.keras.Sequential([
    tf.keras.layers.Dense(8, activation="relu",input_shape=(4,)),
    tf.keras.layers.Dense(1,activation="sigmoid")
])

model.compile(
    optimizer = "adam",
    loss = "binary_crossentropy",
    metrics=["accuracy"]
)

history = model.fit(
    x,
    y,
    epochs = 50,
    validation_split = 0.2,
    verbose = 0
)

plt.plot(history.history["loss"],label="loss")
plt.plot(history.history["val_loss"],label="val_loss")
plt.legend()
plt.show()

