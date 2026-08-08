class DataCleaner:

    def __init__(self, data ):
        self.data = data 

    def clean(self):
        print("Cleaning Data...")

    def remove_nulls(self):
        print("Removing null values...")

    def normalize(self):
        print("Normalizing data...")

    def encode_labels(self):
        print("Encoding labels")

data = [10, 20, None, 50, 40]
cleaner = DataCleaner(data)
cleaner.clean()
cleaner.remove_nulls()
cleaner.normalize()
cleaner.encode_labels() 