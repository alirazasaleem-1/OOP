from pipeline import Pipeline
from models import LinearRegressionModel

pipeline = Pipeline(LinearRegressionModel())
pipeline.run()