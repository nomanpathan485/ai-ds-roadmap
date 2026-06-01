import numpy as np

def relu(x):
    return np.maximum(0, x)

numbers = [-5, -2, 0, 2, 5]

for num in numbers:
    print(f"input:{num}, output:{relu(num):.4f}")