Think of an activation function as a decision maker.

Neuron Output
      ↓
Activation Function
      ↓
Final Decision

Sigmoid Function is a most famous activation function.

It squeezes any number between:

0 and 1
sigma(x)= 1/1+e^-x

Examples:
Input: -10 → Output ≈ 0

Input: 0 → Output = 0.5

Input: 10 → Output ≈ 1

Useful for:

Binary Classification
Yes/No
Pass/Fail
Spam/Not Spam

The Problem with Sigmoid:

For many years, people used sigmoid everywhere.

Then researchers discovered a problem:

Very Negative → Gradient ≈ 0
Very Positive → Gradient ≈ 0

When gradients become very small:

Learning slows down

This is called the Vanishing Gradient Problem.

Because of this, modern deep learning rarely uses sigmoid in hidden layers.