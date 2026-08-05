class Dataset:
    def __init__(self, filename):
        self.filename = filename 

    def load(self):
        print("Dataset Loaded")

    def show_info(self):
        print("Rows: 5000")

    def remove_duplicates(self):
        print("Duplicates Removed")

    def train_test_split(self):
        print("Train Size: 4000")
        print("Test Size: 1000")

dataset: Dataset = Dataset("spam.csv")
dataset.load()
dataset.show_info()
dataset.remove_duplicates()
dataset.train_test_split()