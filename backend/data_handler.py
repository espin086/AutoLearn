"""
Data handler module for AutoLearn.
Handles all data I/O operations including loading, saving, and managing datasets.
"""
import logging
from pathlib import Path
from typing import Optional

import pandas as pd

from config import SOURCE_DATA_PATH, PREDICTIONS_PATH

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class DataHandler:
    """Manages data loading, saving, and validation operations."""

    @staticmethod
    def load_source_data() -> Optional[pd.DataFrame]:
        """
        Load source data from the configured path.

        Returns:
            DataFrame if data exists, None otherwise.
        """
        try:
            if SOURCE_DATA_PATH.exists():
                logger.info(f"Loading data from {SOURCE_DATA_PATH}")
                df = pd.read_csv(SOURCE_DATA_PATH, index_col=False)
                logger.info(f"Loaded {len(df)} rows and {len(df.columns)} columns")
                return df
            else:
                logger.warning(f"Source data not found at {SOURCE_DATA_PATH}")
                return None
        except Exception as e:
            logger.error(f"Error loading source data: {e}")
            return None

    @staticmethod
    def save_source_data(df: pd.DataFrame) -> bool:
        """
        Save DataFrame as source data.

        Args:
            df: DataFrame to save.

        Returns:
            True if successful, False otherwise.
        """
        try:
            df.to_csv(SOURCE_DATA_PATH, index=False)
            logger.info(f"Saved source data to {SOURCE_DATA_PATH}")
            return True
        except Exception as e:
            logger.error(f"Error saving source data: {e}")
            return False

    @staticmethod
    def save_predictions(predictions: pd.DataFrame) -> bool:
        """
        Save predictions DataFrame.

        Args:
            predictions: Predictions DataFrame to save.

        Returns:
            True if successful, False otherwise.
        """
        try:
            predictions.to_csv(PREDICTIONS_PATH, index=False)
            logger.info(f"Saved predictions to {PREDICTIONS_PATH}")
            return True
        except Exception as e:
            logger.error(f"Error saving predictions: {e}")
            return False

    @staticmethod
    def validate_dataframe(df: pd.DataFrame) -> bool:
        """
        Validate that a DataFrame is suitable for ML operations.

        Args:
            df: DataFrame to validate.

        Returns:
            True if valid, False otherwise.
        """
        if df is None or df.empty:
            logger.warning("DataFrame is None or empty")
            return False

        if len(df) < 2:
            logger.warning("DataFrame has fewer than 2 rows")
            return False

        logger.info("DataFrame validation passed")
        return True
