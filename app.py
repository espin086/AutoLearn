import os

import pandas as pd
import streamlit as st
from ydata_profiling import ProfileReport

from pycaret.classification import (
    compare_models as classification_compare_models,
    load_model as classification_load_model,
    predict_model as classification_predict_model,
    pull as classification_pull,
    save_model as classification_save_model,
    setup as classification_setup,
    tune_model,
)
from pycaret.clustering import (
    assign_model as clustering_assign_model,
    create_model as clustering_create_model,
    load_model as clustering_load_model,
    predict_model as clustering_predict_model,
    pull as clustering_pull,
    save_model as clustering_save_model,
    setup as clustering_setup,
)
from pycaret.regression import (
    compare_models as regression_compare_models,
    load_model as regression_load_model,
    predict_model as regression_predict_model,
    pull as regression_pull,
    save_model as regression_save_model,
    setup as regression_setup,
)


def generate_profile(data: pd.DataFrame) -> ProfileReport:
    """Generate a profiling report for the provided dataframe."""
    return ProfileReport(data)


df = None
if os.path.exists("sourcedata.csv"):
    df = pd.read_csv("sourcedata.csv", index_col=False)


with st.sidebar:
    st.image(
        "https://i.etsystatic.com/41369585/r/il/9099ae/4698309797/il_1080xN.4698309797_m5ov.jpg"
    )
    st.title("AutoLearn")
    choice = st.radio("Navigation", ["Upload", "ML", "Download", "Model Inference"])
    st.info(
        "This application allows you to build an automated machine learning pipeline using Streamlit, Pandas Profiling, and Pycaret. And it is damnright magic!"
    )

# Initialize session state
if "analysis_type" not in st.session_state:
    st.session_state.analysis_type = None
if "profile_report_html" not in st.session_state:
    st.session_state.profile_report_html = None

if choice == "Upload":
    st.title("Upload Your Data for Modeling")
    file = st.file_uploader("Upload a CSV file", type=["csv"])
    if file:
        df = pd.read_csv(file, index_col=False)
        df.to_csv("sourcedata.csv", index=False)
        # Invalidate cached profile when new data is uploaded
        st.session_state.profile_report_html = None
        st.success("Data uploaded successfully. Generating profiling report...")
    if df is not None:
        # Generate the profile report only once per dataset version to avoid
        # expensive recomputation on every rerun.
        if st.session_state.profile_report_html is None:
            profile_report = generate_profile(df)
            st.session_state.profile_report_html = profile_report.to_html()
        st.components.v1.html(
            st.session_state.profile_report_html, height=800, scrolling=True
        )
    else:
        st.info("Upload a CSV file to automatically generate a profile report.")

elif choice == "ML":
    if df is None:
        st.warning("Please upload data first to run ML experiments.")
        st.stop()

    st.write("ML")
    target = st.selectbox(
        "Select Target Variable (Only for Regression and Classification)", df.columns
    )
    st.session_state.analysis_type = st.radio(
        "Select Analysis Type", ["Regression", "Classification", "Clustering"]
    )
    if st.button("Run Model"):
        if st.session_state.analysis_type == "Regression":
            regression_setup(df, target=target)
            setup_df = regression_pull()
            st.info("This is the ML Experiment Settings")
            st.dataframe(setup_df)
            best_model = regression_compare_models()
            compare_df = regression_pull()
            st.info("This is the Model Comparison")
            st.dataframe(compare_df)
            regression_save_model(best_model, "best_model")
        elif st.session_state.analysis_type == "Classification":
            classification_setup(df, target=target)
            setup_df = classification_pull()
            st.info("This is the ML Experiment Settings")
            st.dataframe(setup_df)
            best_model = classification_compare_models(sort="AUC")
            compare_df = classification_pull()
            st.info("This is the Model Comparison")
            st.dataframe(compare_df)
            tuned_model = tune_model(best_model)
            st.info("Fine tuned the best model...")
            st.write(tuned_model)
            classification_save_model(tuned_model, "best_model")
        elif st.session_state.analysis_type == "Clustering":
            best_model_name = None
            best_silhouette = -1

            clustering_setup(data=df, normalize=True, remove_multicollinearity=True)
            setup_df = clustering_pull()
            st.info("This is the Clustering Experiment Settings")
            st.dataframe(setup_df)
            # Clustering Models: ['kmeans', 'hclust', 'ap', 'meanshift', 'sc', 'dbscan', 'optics', 'birch']
            # Models has predict_model functionality: ['kmeans', 'ap', 'birch']
            # Models does not has predict_model functionality: ['hclust', 'meanshift','sc','dbscan', 'optics']
            models = ["kmeans", "ap", "birch"]
            all_metrics_df = pd.DataFrame()
            for model_name in models:
                # Train the clustering model using PyCaret
                model = clustering_create_model(model_name)
                print(model)
                metrics_df = clustering_pull()

                # Add the 'model_name' column to the metrics DataFrame
                metrics_df["model_name"] = model_name

                # Concatenate the current metrics DataFrame to the overall DataFrame
                all_metrics_df = pd.concat(
                    [all_metrics_df, metrics_df], ignore_index=True
                )

                # Check if the silhouette score for the current model is better than the best so far
                current_silhouette = all_metrics_df.loc[
                    all_metrics_df["model_name"] == model_name, "Silhouette"
                ].values[0]
                if current_silhouette > best_silhouette:
                    best_silhouette = current_silhouette
                    best_model_name = model_name

            all_metrics_df.reset_index(drop=True, inplace=True)
            print(best_model_name)

            all_metrics_df.set_index("model_name", inplace=True)
            # Display the DataFrame
            st.info("This is the Model Comparison")
            st.dataframe(all_metrics_df)
            model = clustering_create_model(best_model_name)
            print(model)
            clustering_save_model(model, "best_model")

elif choice == "Download":
    with open("best_model.pkl", "rb") as f:
        st.download_button("Download the Model", f, "trained_model.pkl")

elif choice == "Model Inference":
    st.title("Upload Your Data for Predictions")
    file = st.file_uploader("Upload a CSV file", type=["csv"])
    if file and st.session_state.analysis_type:
        df_inference = pd.read_csv(file, index_col=False)
        # Display a message about the successful upload
        st.success("CSV file uploaded successfully for predictions!")
        # Load the best model saved in a .pkl file
        if st.session_state.analysis_type == "Regression":
            regression_model = regression_load_model("best_model")
            st.success("Regression Best Model loaded successfully for predictions!")
            predictions = regression_predict_model(regression_model, data=df_inference)
            st.subheader("Predictions:")
            st.write(predictions)
            predictions.to_csv("predictions.csv", index=False)
            st.success("Predictions saved to predictions.csv")
        elif st.session_state.analysis_type == "Classification":
            classification_model = classification_load_model("best_model")
            st.success("Classification Best Model loaded successfully for predictions!")
            predictions = classification_predict_model(
                classification_model, data=df_inference
            )
            st.subheader("Predictions:")
            st.write(predictions)
            predictions.to_csv("predictions.csv", index=False)
            st.success("Predictions saved to predictions.csv")
        elif st.session_state.analysis_type == "Clustering":
            clustering_model = clustering_load_model("best_model")
            print(clustering_model)
            st.success("Clustering Best Model loaded successfully for predictions!")
            predictions = clustering_predict_model(
                model=clustering_model, data=df_inference
            )
            st.subheader("Predictions:")
            st.write(predictions)
            predictions.to_csv("predictions.csv", index=False)
            st.success("Predictions saved to predictions.csv")
