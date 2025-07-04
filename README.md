# AQA Python Project

This is a test automation project written in Python 3.9. It is currently in the early stages of development.

[![GitHub Actions](https://github.com/vitaliiyz/aqa_python/actions/workflows/github-actions.yml/badge.svg?branch=main)](https://github.com/vitaliiyz/aqa_python/actions/workflows/github-actions.yml)

## 🛠 Technologies

- Python 3.11  
- Playwright

## 📊 Allure Report

Allure HTML reports are automatically generated and published via GitHub Pages after each successful test run on `main` or `dev` branches.

🔗 **View latest report:** [Allure Report on GitHub Pages](https://vitaliiyz.github.io/aqa_python/)  
*(Report may not exist until the first successful CI run on `main` or `dev`.)*

## 📝 Description

The project is being created for practice and learning purposes. Structure and goals are still being defined.

## ▶️ Running Tests
#### Prerequisites

- `$ pip install pytest playwright`
- `$ playwright install`

#### All possible ways to run tests:

By default, tests run in Headless mode:
- `$ pytest                               # Run all tests`
- `$ pytest tests/main_page_test.py       # Run all tests in specific file`
- `$ pytest tests/main_page_test.py::test_accept_privacy_popup_visible # Run specific test`

To run tests in headed mode (with browser UI):
- `$ pytest --headed                      # Show browser UI`
- `$ pytest --slowmo                      # Slow down actions by 500ms`
- `$ pytest --browser chromium            # Use Chromium browser (default)`
- `$ pytest --headed --browser firefox    # Use Firefox browser`
- `$ pytest tests/main_page_test.py::test_accept_privacy_popup_visible --headed --browser firefox`

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