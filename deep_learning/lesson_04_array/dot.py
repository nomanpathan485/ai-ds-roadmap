import numpy as np

inputs = np.array([5, 90])

weights = np.array([
    [0.8, 0.2],
    [0.4, 0.6],
    [0.9, 0.1]
])

output = np.dot(weights, inputs)

print(output)