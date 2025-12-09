# Installing the software

## Prerequisites

This project uses [uv](https://docs.astral.sh/uv/) for fast, reliable Python package management.

### Install uv

**macOS and Linux:**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows:**
```powershell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**With pip:**
```bash
pip install uv
```

For more installation options, visit: https://docs.astral.sh/uv/getting-started/installation/

## Setup

### Clone the Repository

```bash
git clone https://github.com/espin086/AutoLearn.git
cd AutoLearn
```

### Install Dependencies

With uv, you don't need to manually create or activate a virtual environment. uv handles this automatically!

```bash
uv sync
```

This command will:
- Create a virtual environment (`.venv`) if it doesn't exist
- Install Python 3.11 if needed
- Install all project dependencies
- Lock dependencies for reproducibility

### Run Program

```bash
make run
```

Or alternatively:

```bash
uv run streamlit run app.py
```

The application will be available at http://localhost:8501

## Additional Commands

### Add a new dependency

```bash
uv add <package-name>
```

### Add a development dependency

```bash
uv add --dev <package-name>
```

### Update dependencies

```bash
uv sync --upgrade
```

### Run tests

```bash
uv run pytest
```

### Activate the virtual environment manually (optional)

If you prefer to activate the environment manually:

```bash
source .venv/bin/activate  # macOS/Linux
# or
.venv\Scripts\activate  # Windows
```

## Why uv?

- **Fast**: 10-100x faster than pip
- **Reliable**: Built-in dependency resolver
- **Easy**: Automatic virtual environment management
- **Modern**: Uses the latest Python packaging standards (pyproject.toml)

# 
