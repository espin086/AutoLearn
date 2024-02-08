# 🤖 AutoLearn


This is a simple Streamlit app that utilizes PyCaret and Pandas Data Profiler to perform automated exploratory data analysis (EDA) and train machine learning models. The app provides various features for data profiling, model training, and model evaluation.

## 🔌 Installation

To run this app, please follow the installation instructions provided in the [INSTALLATION](INSTALLATION.md) file.

## 🛣 Getting Started

1. Download the Iris dataset from the following link: [Iris Dataset](https://archive.ics.uci.edu/dataset/53/iris)

2. Load the dataset into the app by clicking on the "Upload Data" button.

![Upload Data](images/demo_upload_data.png)

## 🔍 Data Profiling Features

### Data Overview

The app provides an overview of the loaded dataset, including the number of rows, columns, and data types.

![Data Overview](images/demo_profile_overview.png)

### Data Alerts

The app identifies potential issues in the dataset, such as missing values, high cardinality, and data type inconsistencies.

![Data Alerts](images/demo_profile_alerts.png)

### Rich Column Level Statistics & Visuals

The app generates various statistics and visualizations for each column in the dataset, including histograms, tables, and descriptive statistics.

![Variable Histogram](images/demo_variable_hist.png)

![Variable Table](images/demo_variable_table.png)

![Variable Statistics](images/demo_variable_statistics.png)

### Identify Correlations Between Variables

The app identifies correlations between variables and visualizes them using interaction plots and heatmaps.

![Interactions](images/demo_interactions.png)

![Heatmap](images/demo_heatmap.png)

### Visualize Missing Values

The app provides a visualization of missing values in the dataset.

![Missing Values](images/demo_missing_values.png)

### View Data Samples

The app allows you to view a sample of the loaded dataset.

![Sample Data](images/demo_sample_data.png)

### Find Duplicate Rows

The app identifies and displays duplicate rows in the dataset.

![Duplicates](images/demo_duplicates.png)

## 🤖 Automated Machine Learning

### Automated ML Experiment Settings

The app provides settings for running an automated machine learning experiment, including target variable selection, feature engineering, and model selection.

![Model Experiment](images/demo_model_experiment.png)

### Model Leaderboard

The app displays a leaderboard of trained machine learning models, ranked by their performance metrics.

![Model Leaderboard](images/demo_model_leaderboard.png)

### Download Best Model

The app allows you to download the best-performing machine learning model for further use.

![Download Model](images/demo_download_model.png)

## Conclusion

This Streamlit app provides a user-friendly interface for performing automated exploratory data analysis and machine learning model training. It leverages the power of PyCaret and Pandas Data Profiler to simplify the data analysis and model building process.