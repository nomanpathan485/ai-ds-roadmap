Sequential
tf.keras.Sequential()
Means:

Layer 1
 ↓
Layer 2
 ↓
Layer 3

stacked one after another.

Dense Layer
tf.keras.layers.Dense(1)

means:

1 neuron

Exactly like the neuron we built manually.

Optimizer
optimizer='sgd'

SGD = Stochastic Gradient Descent

This is the algorithm that updates weights automatically.

Loss
loss='mse'

MSE = Mean Squared Error

It's basically the loss function we were calculating manually, but averaged across many examples.