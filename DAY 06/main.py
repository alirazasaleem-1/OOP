from pipeline import Pipeline
from models import RandomForestModel

pipeline = Pipeline(RandomForestModel())
pipeline.run()