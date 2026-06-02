import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split

X = np.array([
    [0.2, 0.5],
    [0.4, 0.6],
    [0.5, 0.7],
    [0.8, 0.9],
    [1.0, 0.95],
    [0.3, 0.55],
    [0.6, 0.8],
    [0.9, 0.92],
    [0.1, 0.4],
    [0.7, 0.85]
],dtype=np.float32)

y = np.array([
    0, 0, 1, 1, 1,
    0, 1, 1, 0, 1
],dtype=np.float32)

#split the data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = tf.keras.Sequential([
    tf.keras.layers.Dense(
        1,
        activation="sigmoid",
        input_shape =(2,)
    )
])
#model.summary()

#compile
'''
compile() is basically telling TensorFlow:

How do we measure mistakes?
How do we improve?
What should we report?
'''

model.compile(
    optimizer = "adam",
    loss = "binary_crossentropy",
    metrics =["accuracy"]
)
#train_model
model.fit(
    X_train,
    y_train,
    epochs = 50, #How many times the model sees the entire training dataset.
    verbose = 1  #How much information TensorFlow prints while training.
)

weights_before = model.layers[0].get_weights()
print(weights_before)
model.fit(
    X_train,
    y_train,
    epochs=50,
    verbose=0
)
weights_after = model.layers[0].get_weights()
print(weights_after)

#evalute on test data
loss, accuracy = model.evaluate(
    X_test,
    y_test,
    verbose = 0
)

print("test accuracy:", accuracy)