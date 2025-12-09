"""
ML Predictor module for AutoLearn.
Handles model inference and prediction operations.
"""
import logging
from typing import Optional

import pandas as pd
from pycaret.classification import (
    load_model as classification_load_model,
    predict_model as classification_predict_model,
)
from pycaret.clustering import (
    load_model as clustering_load_model,
    predict_model as clustering_predict_model,
)
from pycaret.regression import (
    load_model as regression_load_model,
    predict_model as regression_predict_model,
)

from config import BEST_MODEL_PATH

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class MLPredictor:
    """Manages machine learning model inference operations."""

    @staticmethod
    def predict_regression(df: pd.DataFrame) -> Optional[pd.DataFrame]:
        """
        Make predictions using trained regression model.

        Args:
            df: DataFrame to make predictions on.

        Returns:
            DataFrame with predictions if successful, None otherwise.
        """
        try:
            model_path = str(BEST_MODEL_PATH.with_suffix(""))
            logger.info(f"Loading regression model from {model_path}")
            model = regression_load_model(model_path)

            logger.info("Making regression predictions...")
            predictions = regression_predict_model(model, data=df)
            logger.info("Regression predictions completed")
            return predictions
        except Exception as e:
            logger.error(f"Error making regression predictions: {e}")
            return None

    @staticmethod
    def predict_classification(df: pd.DataFrame) -> Optional[pd.DataFrame]:
        """
        Make predictions using trained classification model.

        Args:
            df: DataFrame to make predictions on.

        Returns:
            DataFrame with predictions if successful, None otherwise.
        """
        try:
            model_path = str(BEST_MODEL_PATH.with_suffix(""))
            logger.info(f"Loading classification model from {model_path}")
            model = classification_load_model(model_path)

            logger.info("Making classification predictions...")
            predictions = classification_predict_model(model, data=df)
            logger.info("Classification predictions completed")
            return predictions
        except Exception as e:
            logger.error(f"Error making classification predictions: {e}")
            return None

    @staticmethod
    def predict_clustering(df: pd.DataFrame) -> Optional[pd.DataFrame]:
        """
        Make predictions using trained clustering model.

        Args:
            df: DataFrame to make predictions on.

        Returns:
            DataFrame with predictions if successful, None otherwise.
        """
        try:
            model_path = str(BEST_MODEL_PATH.with_suffix(""))
            logger.info(f"Loading clustering model from {model_path}")
            model = clustering_load_model(model_path)

            logger.info("Making clustering predictions...")
            predictions = clustering_predict_model(model=model, data=df)
            logger.info("Clustering predictions completed")
            return predictions
        except Exception as e:
            logger.error(f"Error making clustering predictions: {e}")
            return None
