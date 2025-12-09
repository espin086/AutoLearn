# Tests

Unit tests for the AutoLearn application.

## Running Tests

```bash
# Run all tests
pytest tests/

# Run with verbose output
pytest tests/ -v

# Run with coverage
pytest tests/ --cov=backend --cov=ui --cov-report=html
```

## Test Structure

- `test_data_handler.py` - Tests for data I/O operations

## Requirements

```bash
pip install pytest pytest-cov
```

## Adding Tests

Create new test files following the pattern `test_<module_name>.py`

Example:
```python
import pytest
from backend.module import MyClass

class TestMyClass:
    def test_method(self):
        result = MyClass.method()
        assert result == expected
```
