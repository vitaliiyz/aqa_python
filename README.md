# AQA Python Project

This is a test automation project written in Python 3.9. It is currently in the early stages of development.

[![CI/CD Pipeline](https://github.com/vitaliiyz/aqa_python/actions/workflows/github-actions.yml/badge.svg?branch=main)](https://github.com/vitaliiyz/aqa_python/actions/workflows/github-actions.yml)

## 🛠 Technologies

- Python 3.11  
- Playwright
- Poetry (dependency management)
- pytest (testing framework)
- Allure (test reporting)

## 📊 Allure Report

Allure HTML reports are automatically generated and published via GitHub Pages after each successful test run on `main` or `dev` branches.

🔗 **View latest report:** [Allure Report on GitHub Pages](https://vitaliiyz.github.io/aqa_python/)  
*(Report may not exist until the first successful CI run on `main` or `dev`.)*

## 📝 Description

The project is being created for practice and learning purposes. Structure and goals are still being defined.

## ▶️ Running Tests

#### Prerequisites

First, make sure you have Poetry installed. If not, install it:
```bash
curl -sSL https://install.python-poetry.org | python3 -
```

**Note**: If Poetry isn't available in your PATH after installation, you can:
1. Add it to your PATH: `export PATH="$HOME/.local/bin:$PATH"`
2. Or restart your terminal and try again

Then install project dependencies:
```bash
poetry install
playwright install
```

#### All possible ways to run tests:

By default, tests run in Headless mode:
- `poetry run pytest                               # Run all tests`
- `poetry run pytest tests/main_page_test.py       # Run all tests in specific file`
- `poetry run pytest tests/main_page_test.py::test_accept_privacy_popup_visible # Run specific test`

To run tests in headed mode (with browser UI):
- `poetry run pytest --headed                      # Show browser UI`
- `poetry run pytest --slowmo                      # Slow down actions by 500ms`
- `poetry run pytest --browser chromium            # Use Chromium browser (default)`
- `poetry run pytest --headed --browser firefox    # Use Firefox browser`
- `poetry run pytest tests/main_page_test.py::test_accept_privacy_popup_visible --headed --browser firefox`

#### Code formatting and linting:
- `poetry run black .                              # Format code with Black`
- `poetry run flake8 .                             # Lint code with Flake8`

#### Generate Allure reports:
- `poetry run pytest --alluredir=allure-results    # Run tests and generate Allure data`
- `allure serve allure-results                     # View Allure report (requires Allure CLI)`

Alternatively, you can activate the Poetry shell and run commands directly:
```bash
# Activate Poetry's managed virtual environment
poetry shell

# Then run commands directly:
pytest                                             # Run all tests
pytest --headed --browser firefox                 # Run with browser UI
black .                                            # Format code
flake8 .                                           # Lint code
```

**Troubleshooting: If Poetry command is not found**

If you get "poetry: command not found", try:
```bash
# Option 1: Add Poetry to PATH (permanent solution)
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc

# Option 2: Use Python module (temporary solution)
python -m poetry --version
python -m poetry install
python -m poetry run pytest
```

## 📁 Project Structure
```
├── pages/
│   ├── __init__.py
│   ├── base_page.py
│   └── main_page.py
├── tests/
│   ├── __init__.py
│   ├── test_main_page.py
│   └── conftest.py
├── utils/
│   ├── __init__.py
│   └── helpers.py
```