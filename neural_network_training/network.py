import numpy as np

# Inputs
X = np.array([5, 90])

# Hidden layer weights
W1 = np.array([
    [0.8, 0.2],
    [0.4, 0.6],
    [0.9, 0.1]
])

# Hidden layer bias
b1 = np.array([1, 2, 3])

# Hidden layer output
hidden = np.dot(W1, X) + b1

print("Hidden Layer:")
print(hidden)

# Output layer weights
W2 = np.array([0.5, 0.3, 0.2])

# Output bias
b2 = 1

output = np.dot(W2, hidden) + b2

print("\nFinal Output:")
print(output)