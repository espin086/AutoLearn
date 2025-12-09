"""
Upload page UI component for AutoLearn.
Handles data upload and profiling display.
"""
import streamlit as st
import pandas as pd

from backend.data_handler import DataHandler
from backend.profiling import DataProfiler


def render_upload_page(df: pd.DataFrame) -> pd.DataFrame:
    """
    Render the upload page with file upload and profiling.

    Args:
        df: Current DataFrame (if any).

    Returns:
        Updated DataFrame after upload (or existing df).
    """
    st.title("Upload Your Data for Modeling")

    file = st.file_uploader("Upload a CSV file", type=["csv"])

    if file:
        df = pd.read_csv(file, index_col=False)
        if DataHandler.save_source_data(df):
            st.success("Data uploaded successfully. Generating profiling report...")
        # Invalidate cached profile when new data is uploaded
        st.session_state.profile_report_html = None

    if df is not None:
        # Generate the profile report only once per dataset version
        if st.session_state.profile_report_html is None:
            profiler = DataProfiler()
            profile_report = profiler.generate_profile_report(df)
            if profile_report:
                st.session_state.profile_report_html = profiler.profile_to_html(
                    profile_report
                )

        if st.session_state.profile_report_html:
            st.components.v1.html(
                st.session_state.profile_report_html, height=800, scrolling=True
            )
    else:
        st.info("Upload a CSV file to automatically generate a profile report.")

    return df
