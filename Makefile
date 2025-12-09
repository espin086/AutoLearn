# Run the application
run: 
	uv run streamlit run app.py

# Install dependencies
install:
	uv sync

# Update dependencies
update:
	uv sync --upgrade

# Run tests
test:
	uv run pytest

# Add a new dependency
add:
	@echo "Usage: make add-dep PACKAGE=<package-name>"

add-dep:
	uv add $(PACKAGE)

# Add a dev dependency
add-dev:
	uv add --dev $(PACKAGE)

# Clean up cache and temporary files
clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type d -name ".pytest_cache" -exec rm -rf {} +

# Show help
help:
	@echo "Available commands:"
	@echo "  make run        - Run the Streamlit application"
	@echo "  make install    - Install project dependencies"
	@echo "  make update     - Update dependencies to latest versions"
	@echo "  make test       - Run tests"
	@echo "  make add-dep    - Add a dependency (use: make add-dep PACKAGE=package-name)"
	@echo "  make add-dev    - Add a dev dependency (use: make add-dev PACKAGE=package-name)"
	@echo "  make clean      - Clean up cache and temporary files"
	@echo "  make help       - Show this help message"
