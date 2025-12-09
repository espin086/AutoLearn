"""
ML page UI component for AutoLearn.
Handles ML model training interface.
"""
import streamlit as st
import pandas as pd

from backend.ml_trainer import MLTrainer
from config import ANALYSIS_TYPES


def render_ml_page(df: pd.DataFrame) -> None:
    """
    Render the ML training page.

    Args:
        df: DataFrame to train on.
    """
    if df is None:
        st.warning("Please upload data first to run ML experiments.")
        st.stop()

    st.write("ML")

    target = st.selectbox(
        "Select Target Variable (Only for Regression and Classification)", df.columns
    )

    st.session_state.analysis_type = st.radio("Select Analysis Type", ANALYSIS_TYPES)

    if st.button("Run Model"):
        trainer = MLTrainer()

        if st.session_state.analysis_type == "Regression":
            _train_regression(trainer, df, target)

        elif st.session_state.analysis_type == "Classification":
            _train_classification(trainer, df, target)

        elif st.session_state.analysis_type == "Clustering":
            _train_clustering(trainer, df)


def _train_regression(trainer: MLTrainer, df: pd.DataFrame, target: str) -> None:
    """Train regression model and display results."""
    best_model, setup_df, compare_df = trainer.train_regression_model(df, target)

    if best_model and setup_df is not None and compare_df is not None:
        st.info("This is the ML Experiment Settings")
        st.dataframe(setup_df)

        st.info("This is the Model Comparison")
        st.dataframe(compare_df)

        st.success("Regression model trained and saved successfully!")
    else:
        st.error("Failed to train regression model. Check logs for details.")


def _train_classification(trainer: MLTrainer, df: pd.DataFrame, target: str) -> None:
    """Train classification model and display results."""
    tuned_model, setup_df, compare_df = trainer.train_classification_model(df, target)

    if tuned_model and setup_df is not None and compare_df is not None:
        st.info("This is the ML Experiment Settings")
        st.dataframe(setup_df)

        st.info("This is the Model Comparison")
        st.dataframe(compare_df)

        st.info("Fine tuned the best model...")
        st.write(tuned_model)

        st.success("Classification model trained and saved successfully!")
    else:
        st.error("Failed to train classification model. Check logs for details.")


def _train_clustering(trainer: MLTrainer, df: pd.DataFrame) -> None:
    """Train clustering model and display results."""
    best_model, setup_df, all_metrics_df = trainer.train_clustering_model(df)

    if best_model and setup_df is not None and all_metrics_df is not None:
        st.info("This is the Clustering Experiment Settings")
        st.dataframe(setup_df)

        st.info("This is the Model Comparison")
        st.dataframe(all_metrics_df)

        st.success("Clustering model trained and saved successfully!")
    else:
        st.error("Failed to train clustering model. Check logs for details.")
