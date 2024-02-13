import pandas as pd
import os
import streamlit as st
from ydata_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

from pycaret.classification import setup as classification_setup, compare_models as classification_compare_models, pull as classification_pull, save_model as classification_save_model
from pycaret.regression import setup as regression_setup, compare_models as regression_compare_models, pull as regression_pull, save_model as regression_save_model


with st.sidebar:
    st.image(
        "https://i.etsystatic.com/41369585/r/il/9099ae/4698309797/il_1080xN.4698309797_m5ov.jpg"
    )
    st.title("AutoLearn")
    choice = st.radio("Navigation", ["Upload", "Profiling", "ML", "Download"])
    st.info(
        "This application allows you to build an automated machine learning pipeline using Streamlit, Pandas Profiling, and Pycaret. And it is damnright magic!"
    )
if os.path.exists("sourcedata.csv"):
    df = pd.read_csv("sourcedata.csv", index_col=False)


if choice == "Upload":
    st.title("Upload Your Data for Modeling")
    file = st.file_uploader("Upload a CSV file", type=["csv"])
    if file:
        df = pd.read_csv(file, index_col=False)
        df.to_csv("sourcedata.csv", index=False)
elif choice == "Profiling":
    st.title("Automated Exploratory Data Analysis")
    profile_report = ProfileReport(df)
    st_profile_report(profile_report)
elif choice == "ML":
    st.write("ML")
    target = st.selectbox("Select Target Variable", df.columns)
    analysis_type = st.radio("Select Analysis Type", ["Regression", "Classification"])
    if st.button("Run Model"):
        if analysis_type == "Regression":
            regression_setup(df, target=target)
            setup_df = regression_pull()
            st.info("This is the ML Experiment Settings")
            st.dataframe(setup_df)
            best_model = regression_compare_models()
            compare_df = regression_pull()
            st.info("This is the Model Comparison")
            st.dataframe(compare_df)
            regression_save_model(best_model, "best_model")
        elif analysis_type == "Classification":

elif choice == "Download":
    with open("best_model.pkl", "rb") as f:
        st.download_button("Download the Model", f, "trained_model.pkl")
