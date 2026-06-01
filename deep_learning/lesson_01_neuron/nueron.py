import numpy as np

hours_studied = 5
attendance = 90

w1 = 0.8
w2 = 0.2
bias = 1

output = (hours_studied * w1) + (attendance * w2) + bias

print("Neuron Output:", output)