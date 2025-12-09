"""
AutoLearn - Automated Machine Learning Application
Main entry point for the Streamlit application.
"""
import streamlit as st

from backend.data_handler import DataHandler
from ui.sidebar import render_sidebar
from ui.upload_page import render_upload_page
from ui.ml_page import render_ml_page
from ui.download_page import render_download_page
from ui.inference_page import render_inference_page


def initialize_session_state() -> None:
    """Initialize Streamlit session state variables."""
    if "analysis_type" not in st.session_state:
        st.session_state.analysis_type = None
    if "profile_report_html" not in st.session_state:
        st.session_state.profile_report_html = None


def main() -> None:
    """Main application entry point."""
    # Initialize session state
    initialize_session_state()

    # Load existing data if available
    data_handler = DataHandler()
    df = data_handler.load_source_data()

    # Render sidebar and get navigation choice
    choice = render_sidebar()

    # Route to appropriate page based on user choice
    if choice == "Upload":
        df = render_upload_page(df)

    elif choice == "ML":
        render_ml_page(df)

    elif choice == "Download":
        render_download_page()

    elif choice == "Model Inference":
        render_inference_page()


if __name__ == "__main__":
    main()
