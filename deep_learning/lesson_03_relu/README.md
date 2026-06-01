The Most Important Activation Function: ReLU

Formula:

f(x)=max(0,x)

Meaning:

If x < 0 → Output = 0

If x > 0 → Output = x

Examples:

Input: -5 → 0
Input: -1 → 0
Input: 0  → 0
Input: 4  → 4
Input: 10 → 10

Sigmoid squashes everything between 0 and 1.
ReLU keeps positive values large.
ReLU trains much faster.

That's why most modern networks use ReLU in hidden layers.