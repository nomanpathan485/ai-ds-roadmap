'''
What is Train/Test Split?
Suppose we have 1000 samples.
Instead of training on all of them:
1000 samples
we divide them:
800 → Training Set
200 → Test Set

Visual:

Dataset
   ↓
 ┌──────────┬─────────┐
 │ Train    │ Test    │
 │ 80%      │ 20%     │
 └──────────┴─────────┘
Why Do We Need a Test Set?

Imagine I tell you:
My model got 99% accuracy.
Your first question should be:

On training data or test data?

Because:
99% Training Accuracy
might be useless.
But:
99% Test Accuracy
is impressive.
'''
#code:

from sklearn.model_selection import train_test_split
import numpy as np

x = np.array([
    [2, 50],
    [4, 60],
    [5, 70],
    [8, 90],
    [10, 95],
    [3, 55],
    [6, 80],
    [9, 92],
    [1, 40],
    [7, 85]

])
y = np.array([
    0,0,1,1,1,
    0,1,1,0,1
])

x_train, x_test, y_train,y_test = train_test_split(
    x,
    y,
    test_size=0.2,
    random_state = 42
)
print("Training samples:", len(x_train))
print("Testing samples:", len(x_test))

print("\nX_train:")
print(x_train)

print("\nX_test:")
print(x_test)
