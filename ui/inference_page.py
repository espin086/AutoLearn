"""
Inference page UI component for AutoLearn.
Handles model inference interface.
"""
import streamlit as st
import pandas as pd

from backend.data_handler import DataHandler
from backend.ml_predictor import MLPredictor


def render_inference_page() -> None:
    """Render the model inference page."""
    st.title("Upload Your Data for Predictions")

    if not st.session_state.get("analysis_type"):
        st.warning(
            "No trained model found. Please train a model first using the ML page."
        )
        st.stop()

    file = st.file_uploader("Upload a CSV file", type=["csv"])

    if file:
        df_inference = pd.read_csv(file, index_col=False)
        st.success("CSV file uploaded successfully for predictions!")

        predictor = MLPredictor()
        predictions = None

        if st.session_state.analysis_type == "Regression":
            predictions = _predict_regression(predictor, df_inference)

        elif st.session_state.analysis_type == "Classification":
            predictions = _predict_classification(predictor, df_inference)

        elif st.session_state.analysis_type == "Clustering":
            predictions = _predict_clustering(predictor, df_inference)

        if predictions is not None:
            st.subheader("Predictions:")
            st.write(predictions)

            if DataHandler.save_predictions(predictions):
                st.success("Predictions saved to data/predictions.csv")
            else:
                st.error("Failed to save predictions.")


def _predict_regression(
    predictor: MLPredictor, df: pd.DataFrame
) -> pd.DataFrame:
    """Make regression predictions."""
    st.success("Regression Best Model loaded successfully for predictions!")
    predictions = predictor.predict_regression(df)

    if predictions is None:
        st.error("Failed to make regression predictions. Check logs for details.")

    return predictions


def _predict_classification(
    predictor: MLPredictor, df: pd.DataFrame
) -> pd.DataFrame:
    """Make classification predictions."""
    st.success("Classification Best Model loaded successfully for predictions!")
    predictions = predictor.predict_classification(df)

    if predictions is None:
        st.error("Failed to make classification predictions. Check logs for details.")

    return predictions


def _predict_clustering(
    predictor: MLPredictor, df: pd.DataFrame
) -> pd.DataFrame:
    """Make clustering predictions."""
    st.success("Clustering Best Model loaded successfully for predictions!")
    predictions = predictor.predict_clustering(df)

    if predictions is None:
        st.error("Failed to make clustering predictions. Check logs for details.")

    return predictions
