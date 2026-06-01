
import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

numbers = [-10, -5, 0, 5, 10]

for num in numbers:
    print(f"Input: {num}, Output: {sigmoid(num):.4f}")


