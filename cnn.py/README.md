CNN Idea

Instead of looking at the whole image at once:

[ Entire Image ]

CNN looks at small regions:

[■■■]
[■■■]
[■■■]

like a tiny window.

This window is called a:

Filter (Kernel)
Example

Suppose image:

1 1 1 0
1 1 1 0
1 1 1 0
0 0 0 0

And filter:

1 1
1 1

The filter slides across the image:

⬜⬜
⬜⬜

checking for patterns.

What CNN Learns

Early layers learn:

Edges
Lines
Corners

Later layers learn:

Eyes
Nose
Shapes
Digits
Faces

maxpooling:
Suppose Conv2D Produced
8  2  4  1
5  9  3  2
7  1  6  0
2  4  8  5

Shape:

(4,4)
MaxPooling(2,2)

Take a 2×2 box:

8 2
5 9

Pick the maximum:

9

Next box:

4 1
3 2

Maximum:

4

Bottom-left:

7 1
2 4

Maximum:

7

Bottom-right:

6 0
8 5

Maximum:

8

Result:

9 4
7 8

Shape changed:

(4,4)
↓
(2,2)
Why Do This?

Because we want to:

Keep important information
9
4
7
8

and remove less useful details.

Benefits

Smaller image:

Less memory
Less computation
Faster training

and often:

Better generalization
Visual Intuition

Imagine a photo of a cat.

You don't need every single pixel.

You need:

Ear
Eye
Whiskers
Shape

MaxPooling helps keep strong features and discard tiny details.

Quiz

If MaxPooling is:

MaxPooling2D((2,2))

and the input shape is:

(26,26,32)

What do you think the output shape becomes?

Hint:

Height gets divided by 2
Width gets divided by 2
Number of feature maps stays the same

Take a guess. 🔥