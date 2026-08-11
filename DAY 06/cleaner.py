class DataCleaner:

    def __init__(self, data ):
        self.__data = data 

    @property
    def data(self):
        return self.__data 

    @data.setter
    def data(self, new_data):
        if isinstance(new_data, list):
            self.__data = new_data
        else:
            print("Data must be a list!")

    def clean(self):
        print("Cleaning Data...")

    def remove_nulls(self):
        print("Removing null values...")

    def normalize(self):
        print("Normalizing data...")

    def encode_labels(self):
        print("Encoding labels")