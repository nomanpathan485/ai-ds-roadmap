import tensorflow as tf

(x_train,y_train), (x_test,y_test) = tf.keras.datasets.mnist.load_data()

#we only normalise x cause y is a label data it shows which label does the image belong to so converting it doesnt really make sense

x_train = x_train/255.0
x_test = x_test/255.0

model = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=(28,28)),
    tf.keras.layers.Dense(128, activation="relu"),
    tf.keras.layers.Dense(10,activation="softmax")
])

model.compile(
    optimizer = "adam",
    loss = "sparse_categorical_crossentropy",
    metrics = ["accuracy"]
)

model.fit(
    x_train,
    y_train,
    epochs = 5,
    validation_split = 0.2
)

test_loss, test_accuracy = model.evaluate(
    x_test,
    y_test
)

print(f"print accuracy: {test_accuracy}")
