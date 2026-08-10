# Composition

class Dataset:
    def load(self):
        print("Loading Dataset...")

class DataCleaner:
    def clean(self):
        print("Cleaning Dataset...")

class Model:
    def train(self):
        print("Training...")

class Evaluator:
    def evaluate(self):
        print("Evaluating....")


class Pipeline:
    def __init__(self):
        self.dataset = Dataset()
        self.cleaner = DataCleaner()
        self.model = Model()
        self.evaluator = Evaluator()

    def run(self):
        self.dataset.load()
        self.cleaner.clean()
        self.model.train()
        self.evaluator.evaluate()

pipeline = Pipeline()
pipeline.run()