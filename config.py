"""
Configuration file for AutoLearn application.
Centralized configuration for paths, settings, and constants.
"""
import os
from pathlib import Path

# Base directories
BASE_DIR = Path(__file__).parent
DATA_DIR = BASE_DIR / "data"
MODELS_DIR = BASE_DIR / "models"

# Ensure directories exist
DATA_DIR.mkdir(exist_ok=True)
MODELS_DIR.mkdir(exist_ok=True)

# File paths
SOURCE_DATA_PATH = DATA_DIR / "sourcedata.csv"
PREDICTIONS_PATH = DATA_DIR / "predictions.csv"
BEST_MODEL_PATH = MODELS_DIR / "best_model.pkl"

# Application settings
APP_TITLE = "AutoLearn"
APP_IMAGE_URL = (
    "https://i.etsystatic.com/41369585/r/il/9099ae/4698309797/il_1080xN.4698309797_m5ov.jpg"
)
APP_INFO = (
    "This application allows you to build an automated machine learning pipeline "
    "using Streamlit, Pandas Profiling, and Pycaret. And it is damnright magic!"
)

# Navigation options
NAVIGATION_OPTIONS = ["Upload", "ML", "Download", "Model Inference"]

# ML analysis types
ANALYSIS_TYPES = ["Regression", "Classification", "Clustering"]

# Clustering models that support predict_model
CLUSTERING_MODELS = ["kmeans", "ap", "birch"]
