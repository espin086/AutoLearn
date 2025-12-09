"""
Download page UI component for AutoLearn.
Handles model download interface.
"""
import streamlit as st

from config import BEST_MODEL_PATH


def render_download_page() -> None:
    """Render the model download page."""
    st.title("Download Trained Model")

    if not BEST_MODEL_PATH.exists():
        st.warning(
            "No trained model found. Please train a model first using the ML page."
        )
        st.stop()

    try:
        with open(BEST_MODEL_PATH, "rb") as f:
            st.download_button("Download the Model", f, "trained_model.pkl")
        st.success("Model is ready for download!")
    except Exception as e:
        st.error(f"Error loading model for download: {e}")
