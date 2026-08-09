class BaseModel:
    def train(self):
        print("Training Model...")

    def predict(self):
        print("Making Predictions...")

    def evaluate(self):
        print("Evaluating model...")

    def save_model(self):
        print("Saving model..")

class CNNModel(BaseModel):

    def train(self):
        print("Training CNN using images...")

class LinearRegressionModel(BaseModel):
    pass 

class RandomForestModel(BaseModel):
    pass 

model = BaseModel()
model.train()

cnn = CNNModel()
cnn.train()
cnn.predict()
cnn.evaluate()
cnn.save_model()