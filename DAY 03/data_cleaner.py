class DataCleaner:

    def clean(self):
        print("Cleaning Data...")

    def remove_nulls(self):
        print("Removing null values...")

    def normalize(self):
        print("Normalizing data...")

    def encode_labels(self):
        print("Encoding labels")

cleaner = DataCleaner()
cleaner.clean()
cleaner.remove_nulls()
cleaner.normalize()
cleaner.encode_labels() 