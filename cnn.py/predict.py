import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.models import load_model
from tensorflow.keras.datasets import mnist

model = load_model("digit_model.keras")
(X_train, y_train), (X_test, y_test) = mnist.load_data()

index = np.random.randint(0, 10000)
image = X_test[index]
actual = y_test[index]
image_normalized = image / 255.0
image_normalized = image_normalized.reshape(1, 28, 28, 1)

prediction = model.predict(image_normalized)

predicted_digit = np.argmax(prediction)
confidence = np.max(prediction)
print("Predicted Digit:", predicted_digit)
print("Actual Digit:", actual)
print(f"Confidence: {confidence*100:.2f}%")

plt.imshow(image, cmap="gray")
plt.title(f"Predicted: {predicted_digit} | Actual: {actual}")
plt.axis("off")
plt.show()