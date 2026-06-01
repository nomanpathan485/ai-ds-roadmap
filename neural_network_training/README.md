Imagine you're standing on a mountain in complete fog.

Your goal:

Reach the lowest point of the valley

You can't see the whole mountain.

So you:

Take a small step.
Check if you're going downhill.
Take another step.
Repeat.

This is exactly what Gradient Descent does.

Bad Weights
     ↓
Calculate Loss
     ↓
Adjust Weights Slightly
     ↓
Calculate New Loss
     ↓
Keep Moving Toward Lower Loss
A Simple Example

Suppose our model is:

prediction = weight * input

Input:

input = 5

Actual answer:

actual = 50

Start with a random weight:

weight = 2

Prediction:

5 × 2 = 10

Loss:

(50 - 10)² = 1600

Terrible prediction.

So Gradient Descent asks:

Should I increase the weight or decrease it?

If we try:

weight = 3

Prediction:

15

Closer to 50.

Loss becomes smaller.

Therefore:

Increase the weight

This process repeats automatically thousands of times.