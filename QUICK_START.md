# 🚀 Quick Start Guide

## ✅ What is AutoLearn?

AutoLearn is a powerful Streamlit application that automates machine learning workflows using PyCaret and YData Profiling. It features a clean, modular architecture with separated UI and backend logic.

## 📁 Project Structure

```
AutoLearn/
├── app.py                    # Main application entry point
├── config.py                 # Centralized configuration
├── data/                     # Data storage (gitignored)
│   ├── sourcedata.csv       # Uploaded source data
│   └── predictions.csv      # Model predictions
├── models/                   # Model storage (gitignored)
│   └── best_model.pkl       # Trained model
├── backend/                  # Backend business logic
│   ├── data_handler.py      # Data I/O operations
│   ├── profiling.py         # Data profiling
│   ├── ml_trainer.py        # Model training
│   └── ml_predictor.py      # Model inference
└── ui/                       # UI components (Streamlit)
    ├── sidebar.py           # Sidebar navigation
    ├── upload_page.py       # Upload and profiling page
    ├── ml_page.py           # ML training page
    ├── download_page.py     # Model download page
    └── inference_page.py    # Inference page
```

## 🏃 Running the App

```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

## 🎯 Key Features

### 1. Modular Architecture
- **UI Layer** (`ui/`): Pure Streamlit components
- **Backend Layer** (`backend/`): Pure business logic
- **Configuration** (`config.py`): Centralized settings

### 2. Organized Data Storage
- **Data files**: Stored in `data/` directory
- **Model files**: Stored in `models/` directory
- Both directories are gitignored

### 3. Separation of Concerns
- Each module has a single, clear purpose
- UI code never contains business logic
- Backend code is testable independently

## 🔧 Common Tasks

### Add a New ML Type
1. Add training method to `backend/ml_trainer.py`
2. Add prediction method to `backend/ml_predictor.py`
3. Update UI in `ui/ml_page.py`
4. Add type to `config.py`

### Add a New Page
1. Create `ui/new_page.py` with `render_new_page()` function
2. Update `ui/sidebar.py` navigation
3. Import and call in `app.py`

### Modify Paths or Settings
Edit `config.py` - all paths and settings are centralized

## 🔍 Module Guide

| Module | Purpose |
|--------|---------|
| `config.py` | All configuration and paths |
| `backend/data_handler.py` | Data loading, saving, validation |
| `backend/profiling.py` | YData profiling reports |
| `backend/ml_trainer.py` | Model training (regression, classification, clustering) |
| `backend/ml_predictor.py` | Model inference and predictions |
| `ui/sidebar.py` | Navigation menu |
| `ui/upload_page.py` | Data upload and profiling display |
| `ui/ml_page.py` | Model training interface |
| `ui/download_page.py` | Model download interface |
| `ui/inference_page.py` | Prediction interface |

## 🧪 Testing

```bash
# Install test dependencies
pip install pytest pytest-cov

# Run tests
pytest tests/

# Run with coverage
pytest tests/ --cov=backend --cov=ui
```

## 📚 Documentation

- **README.md**: Full feature documentation with screenshots
- **INSTALLATION.md**: Installation instructions
- **QUICK_START.md**: This file - quick reference guide
- **tests/README.md**: Testing guide

## 💡 Design Principles

1. **Single Responsibility**: Each module does one thing well
2. **Separation of Concerns**: UI separate from business logic
3. **DRY (Don't Repeat Yourself)**: Reusable components
4. **Maintainability**: Files < 200 lines, clear structure
5. **Testability**: Backend logic independent of UI

## 🛠️ Code Quality

- ✅ PEP8 compliant
- ✅ Type hints throughout
- ✅ Docstrings for all functions
- ✅ Comprehensive logging (INFO, WARNING, ERROR)
- ✅ Error handling with try-except blocks

## 🚦 Workflow

### Data Upload → Profile
1. User uploads CSV via Upload page
2. `DataHandler` saves to `data/sourcedata.csv`
3. `DataProfiler` generates profiling report
4. UI displays interactive profile

### Train Model
1. User selects target and analysis type
2. `MLTrainer` trains appropriate model
3. Model saved to `models/best_model.pkl`
4. Results displayed in UI

### Make Predictions
1. User uploads prediction data
2. `MLPredictor` loads model and predicts
3. `DataHandler` saves to `data/predictions.csv`
4. Results displayed in UI

## 🎓 Best Practices

- **Before modifying**: Understand which module to change
- **Keep it modular**: Don't mix UI and backend logic
- **Use configuration**: Add new settings to `config.py`
- **Write tests**: Test backend modules independently
- **Check logs**: Backend modules log important events

## 🎉 Benefits

- 🧩 **Modular**: Easy to extend and modify
- 🧪 **Testable**: Backend can be unit tested
- 📚 **Maintainable**: Clear structure, easy to navigate
- 🚀 **Scalable**: Simple to add new features
- 🗂️ **Organized**: Logical file structure

---

**Ready to use!** Run `streamlit run app.py` and start building ML models! 🚀
