Multiple Neurons

Suppose we have 3 neurons.

Each neuron has its own weights.

inputs = np.array([5, 90])
weights = np.array([
    [0.8, 0.2],
    [0.4, 0.6],
    [0.9, 0.1]
])

Visualize it:

Neuron 1 → [0.8, 0.2]
Neuron 2 → [0.4, 0.6]
Neuron 3 → [0.9, 0.1]
Magic of NumPy: Dot Product

What Just Happened?

NumPy computed:

Neuron 1:

(5 × 0.8) + (90 × 0.2)

Neuron 2:

(5 × 0.4) + (90 × 0.6)

Neuron 3:

(5 × 0.9) + (90 × 0.1)

All at once.

This is the foundation of deep learning.

Every layer in a neural network is basically:

Inputs
 ↓
Weights
 ↓
Matrix Multiplication
 ↓
Activation Function
 ↓
Next Layer