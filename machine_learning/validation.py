'''
validation data, which sits between 
training and testing and helps us decide
 when to stop training before overfitting starts.

 eg: 1000 samples

700 → Train
150 → Validation
150 → Test
'''

# it is only use to check the performance during training
#code

import tensorflow as tf
import numpy as np

x = np.random.rand(100,4)
y = (x.sum(axis=1)>2).astype(int)

model = tf.keras.Sequential([
    tf.keras.layers.Dense(8, activation="relu",input_shape=(4,)),
    tf.keras.layers.Dense(1,activation="sigmoid")
])
model.compile(
   optimizer = "adam",
   loss = "binary_crossentropy",
   metrics =["accuracy"]

)

history = model.fit(
    x,
    y,
    epochs = 50,
    validation_split = 0.2
)