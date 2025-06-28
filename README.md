# AQA Python Project

This is a test automation project written in Python 3.9. It is currently in the early stages of development.

## 🛠 Technologies

- Python 3.9  
- Playwright

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
```