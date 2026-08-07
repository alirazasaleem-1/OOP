# A Configure Class is used to store the settings of the model.

class Config:
    def __init__(self):
        # Dataset
        self.dataset_path = "data/train.csv"

        # Training
        self.learning_rate = 0.001
        self.epochs = 20 
        self.batch_size = 32 

        # Model
        self.hidden_size = 128
        self.num_classes = 10

        # Device 
        self.device = "cpu"

        # Saving 
        self.model_path = "models/model.pth"

    def __str__(self):
        return (
            f"Dataset: {self.dataset_path}\n"
            f"Learning Rate: {self.learning_rate}\n"
            f"Epochs: {self.epochs}\n"
            f"Hidden Size: {self.hidden_size}\n"
            f"Classes: {self.num_classes}\n"
            f"Device: {self.device}\n"
            f"Model Path: {self.model_path}"
        )

config = Config()
print(config)