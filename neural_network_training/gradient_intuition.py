actual = 50
input_value = 5

for weight in [1, 2, 4, 6, 8, 10]:
    prediction = weight * input_value
    loss = (actual - prediction) ** 2

    print(
        f"Weight={weight}, "
        f"Prediction={prediction}, "
        f"Loss={loss}"
    )