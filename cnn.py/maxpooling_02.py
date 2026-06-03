import tensorflow as tf
import matplotlib.pyplot as plt
(x_train,y_train),(x_test,y_test)= tf.keras.datasets.mnist.load_data()
# normalise
x_train = x_train/255.0
x_test = x_test/255.0
#cnn need channel
x_train = x_train.reshape(-1,28,28,1)
x_test = x_test.reshape(-1,28,28,1)
#model
model = tf.keras.Sequential([
    tf.keras.layers.Conv2D(
        32,
        (3,3),
        activation="relu",
        input_shape=(28,28,1)
    ),
    tf.keras.layers.MaxPooling2D((2,2)),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(
        10,
        activation = "softmax"
    )
])
model.compile(
    optimizer = "adam",
    loss="sparse_categorical_crossentropy",
    metrics = ["accuracy"]
)
model.summary()

history = model.fit(
    x_train,
    y_train,
    epochs = 5,
    validation_split = 0.2
)

test_loss, test_accuracy = model.evaluate(
    x_test,
    y_test,
    
)
print(f"test accuracy:{test_accuracy}")