import numpy as np

inputs = np.array([5, 90])

weights = np.array([
    [0.8, 0.2],
    [0.4, 0.6],
    [0.9, 0.1]
])

biases = np.array([1, 2, 3])
#Think of bias as:
#A learnable offset that gives the neuron flexibility.

output = np.dot(weights, inputs) + biases

print(output)