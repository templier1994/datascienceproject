import os
from src.datascience import logger
from sklearn.model_selection import train_test_split
import pandas as pd

from src.datascience.entity.config_entity import DataTransformationConfig


class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    ## Note: you can add different data transformation techniques such as Scaler, PCA and all. You can perform all kinds of EDA in ML cycle before passing this data to the model

    # in this case data are clean, just split it.
    def train_test_splitting(self):
        data = pd.read_csv(self.config.data_path)
        train, test = train_test_split(data)  # split 0.75-0.25
        train.to_csv(os.path.join(self.config.root_dir, "train.csv"), index=False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"), index=False)

        logger.info("Splited data into training and test sets")
        logger.info(f"train shape : {train.shape}")
        logger.info(f"test shape : {test.shape}")
