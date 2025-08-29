# AQA Python Project

This is a test automation project written in Python 3.9. It is currently in the early stages of development.

[![GitHub Actions](https://github.com/vitaliiyz/aqa_python/actions/workflows/github-actions.yml/badge.svg?branch=main)](https://github.com/vitaliiyz/aqa_python/actions/workflows/github-actions.yml)

## 🛠 Technologies

- Python 3.9+  
- Poetry (dependency management)
- Playwright

## 📊 Allure Report

Allure HTML reports are automatically generated and published via GitHub Pages after each successful test run on `main` or `dev` branches.

🔗 **View latest report:** [Allure Report on GitHub Pages](https://vitaliiyz.github.io/aqa_python/)  
*(Report may not exist until the first successful CI run on `main` or `dev`.)*

## 📝 Description

The project is being created for practice and learning purposes. Structure and goals are still being defined.

## ▶️ Running Tests

#### Prerequisites

This project uses Poetry for dependency management. Make sure you have Poetry installed:

```bash
# Install Poetry (if not already installed)
curl -sSL https://install.python-poetry.org | python3 -

# Or using pipx (recommended)
pipx install poetry
```

Then install dependencies:

```bash
# Install all dependencies including dev tools
poetry install --extras dev

# Install Playwright browsers
poetry run playwright install
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

#### Development tools:

```bash
# Run code formatting
poetry run black .

# Run linting
poetry run flake8 .

# Activate the virtual environment (optional, for manual use)
poetry shell
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