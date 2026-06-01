import tensorflow as tf

model = tf.keras.Sequential([
    tf.keras.layers.Dense(
        2,
        activation="relu",
        input_shape =(4,)
    ),
    
    tf.keras.layers.Dense(
        5,
        activation="relu",
    ),

    tf.keras.layers.Dense(
        1,
        activation="sigmoid"
    )
])

model.summary()

