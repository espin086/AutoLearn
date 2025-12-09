"""
ML Trainer module for AutoLearn.
Handles model training operations for regression, classification, and clustering.
"""
import logging
from typing import Any, Dict, Optional, Tuple

import pandas as pd
from pycaret.classification import (
    compare_models as classification_compare_models,
    pull as classification_pull,
    save_model as classification_save_model,
    setup as classification_setup,
    tune_model,
)
from pycaret.clustering import (
    create_model as clustering_create_model,
    pull as clustering_pull,
    save_model as clustering_save_model,
    setup as clustering_setup,
)
from pycaret.regression import (
    compare_models as regression_compare_models,
    pull as regression_pull,
    save_model as regression_save_model,
    setup as regression_setup,
)

from config import BEST_MODEL_PATH, CLUSTERING_MODELS

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class MLTrainer:
    """Manages machine learning model training operations."""

    @staticmethod
    def train_regression_model(
        df: pd.DataFrame, target: str
    ) -> Tuple[Optional[Any], Optional[pd.DataFrame], Optional[pd.DataFrame]]:
        """
        Train a regression model using PyCaret.

        Args:
            df: Training DataFrame.
            target: Target column name.

        Returns:
            Tuple of (best_model, setup_df, compare_df).
        """
        try:
            logger.info(f"Setting up regression experiment with target: {target}")
            regression_setup(df, target=target)
            setup_df = regression_pull()

            logger.info("Comparing regression models...")
            best_model = regression_compare_models()
            compare_df = regression_pull()

            logger.info("Saving best regression model...")
            model_path = str(BEST_MODEL_PATH.with_suffix(""))
            regression_save_model(best_model, model_path)

            return best_model, setup_df, compare_df
        except Exception as e:
            logger.error(f"Error training regression model: {e}")
            return None, None, None

    @staticmethod
    def train_classification_model(
        df: pd.DataFrame, target: str
    ) -> Tuple[Optional[Any], Optional[pd.DataFrame], Optional[pd.DataFrame]]:
        """
        Train a classification model using PyCaret.

        Args:
            df: Training DataFrame.
            target: Target column name.

        Returns:
            Tuple of (tuned_model, setup_df, compare_df).
        """
        try:
            logger.info(f"Setting up classification experiment with target: {target}")
            classification_setup(df, target=target)
            setup_df = classification_pull()

            logger.info("Comparing classification models...")
            best_model = classification_compare_models(sort="AUC")
            compare_df = classification_pull()

            logger.info("Tuning best classification model...")
            tuned_model = tune_model(best_model)

            logger.info("Saving best classification model...")
            model_path = str(BEST_MODEL_PATH.with_suffix(""))
            classification_save_model(tuned_model, model_path)

            return tuned_model, setup_df, compare_df
        except Exception as e:
            logger.error(f"Error training classification model: {e}")
            return None, None, None

    @staticmethod
    def train_clustering_model(
        df: pd.DataFrame,
    ) -> Tuple[Optional[Any], Optional[pd.DataFrame], Optional[pd.DataFrame]]:
        """
        Train a clustering model using PyCaret.

        Args:
            df: Training DataFrame.

        Returns:
            Tuple of (best_model, setup_df, all_metrics_df).
        """
        try:
            logger.info("Setting up clustering experiment...")
            clustering_setup(data=df, normalize=True, remove_multicollinearity=True)
            setup_df = clustering_pull()

            best_model_name = None
            best_silhouette = -1
            all_metrics_df = pd.DataFrame()

            logger.info("Comparing clustering models...")
            for model_name in CLUSTERING_MODELS:
                logger.info(f"Training clustering model: {model_name}")
                model = clustering_create_model(model_name)
                metrics_df = clustering_pull()
                metrics_df["model_name"] = model_name
                all_metrics_df = pd.concat([all_metrics_df, metrics_df], ignore_index=True)

                current_silhouette = all_metrics_df.loc[
                    all_metrics_df["model_name"] == model_name, "Silhouette"
                ].values[0]

                if current_silhouette > best_silhouette:
                    best_silhouette = current_silhouette
                    best_model_name = model_name

            all_metrics_df.reset_index(drop=True, inplace=True)
            all_metrics_df.set_index("model_name", inplace=True)

            logger.info(f"Best clustering model: {best_model_name}")
            best_model = clustering_create_model(best_model_name)

            logger.info("Saving best clustering model...")
            model_path = str(BEST_MODEL_PATH.with_suffix(""))
            clustering_save_model(best_model, model_path)

            return best_model, setup_df, all_metrics_df
        except Exception as e:
            logger.error(f"Error training clustering model: {e}")
            return None, None, None
