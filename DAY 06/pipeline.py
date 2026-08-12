# Composition
from dataset import Dataset
from cleaner import DataCleaner
from models import RandomForestModel

class Pipeline:
    def __init__(self, model):
        self.dataset = Dataset("data/train.csv", 1000)
        self.cleaner = DataCleaner([])
        self.model = model 

    def run(self):
        self.dataset.load()
        self.dataset.show_info()

        self.dataset.remove_duplicates()
        self.dataset.train_test_split()

        self.cleaner.clean()
        self.cleaner.remove_nulls()
        self.cleaner.normalize()
        self.cleaner.encode_labels()

        self.model.train()
        self.model.predict()
        self.model.evaluate() 
        self.model.save_model()


