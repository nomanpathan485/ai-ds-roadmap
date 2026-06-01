actuall = 50
input = 5
learning_rate = 0.5
weight = 1

for epoch in range(20):
    prediction = weight * input
    error = actuall - prediction
    weight = learning_rate* error + weight

    print(
        f"Epoch {epoch+1}",
        f"Weight={weight:.4f}",
        f"Prediction={prediction:.4f}",
        f"Error={error:.4f}"
    )
