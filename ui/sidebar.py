"""
Sidebar UI component for AutoLearn.
"""
import streamlit as st

from config import APP_TITLE, APP_IMAGE_URL, APP_INFO, NAVIGATION_OPTIONS


def render_sidebar() -> str:
    """
    Render the sidebar with navigation options.

    Returns:
        Selected navigation choice.
    """
    with st.sidebar:
        st.image(APP_IMAGE_URL)
        st.title(APP_TITLE)
        choice = st.radio("Navigation", NAVIGATION_OPTIONS)
        st.info(APP_INFO)

    return choice
