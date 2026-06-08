class model:
    def __init__(self, model_name):
        self.model_name = model_name

    def train(self):
        print(f"training {self.model_name}")

#objects

cnn = model("cnn")
mnist = model("mnist")
cnn.train()
mnist.train()