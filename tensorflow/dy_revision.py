import numpy as np
import tensorflow as tf

x = np.array([
    [2, 50],
    [4, 60],
    [5, 70],
    [8, 90],
    [10, 95],
    [3, 55],
    [6, 80],
    [9, 92],
    [1, 40],
    [7, 85]
],dtype=np.float32)

y = np.array([
    0,0,1,1,1,
    0,1,1,0,1
],dtype=np.float32)

model = tf.keras.Sequential([
    tf.keras.layers.Dense(
        4,
        activation = "relu",
        input_shape = (3,)
    ),
    tf.keras.layers.Dense(
        1,
        activation="sigmoid"
    )
])

model.compile(
    optimizer = "adam",
    loss = "binary crossentropy",
    metrics = ["accuracy"]
)

model.summary()