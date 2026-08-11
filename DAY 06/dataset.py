class Dataset:
    def __init__(self, filename: str, rows: int):
        self.filename = filename 
        self.rows = rows 

    def load(self):
        print(f"{self.filename} Loaded")

    def show_info(self):
        print(f"Rows: {self.rows}")

    def remove_duplicates(self):
        self.rows -= 100 
        print("Duplicates Removed")

    def train_test_split(self):
        train = self.rows * 0.8
        test = self.rows - train 

        print(f"Train Size: {train}")
        print(f"Test Size: {test}")

