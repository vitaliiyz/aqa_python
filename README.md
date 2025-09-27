# AQA Python - Test Automation Learning Project

[![GitHub Actions](https://github.com/vitaliiyz/aqa_python/actions/workflows/github-actions.yml/badge.svg?branch=main)](https://github.com/vitaliiyz/aqa_python/actions/workflows/github-actions.yml)
[![Python Version](https://img.shields.io/badge/python-3.9%2B-blue.svg)](https://python.org)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

A Python test automation project built with Playwright for learning web testing fundamentals.

## 🛠 Technologies Used
- **Python 3.9+** - Programming language
- **Playwright** - Web automation framework
- **Pytest** - Testing framework
- **Poetry** - Dependency management
- **Allure** - Test reporting

## 🚀 Setup

1. **Clone the project:**
   ```bash
   git clone <your-repo-url>
   cd aqa_python
   ```

2. **Install Poetry and dependencies:**
   ```bash
   # Install Poetry if needed
   pip install poetry
   
   # Install project dependencies
   poetry install
   
   # Install browsers
   poetry run playwright install
   ```

## 🧪 Running Tests

**Basic test execution:**
```bash
# Run all tests
poetry run pytest

# Run specific test file
poetry run pytest tests/main_page_test.py

# Run with browser UI visible
poetry run pytest --headed

# Generate test report
poetry run pytest --alluredir=allure-results
poetry run allure serve allure-results
```

## 📁 Project Structure

```
├── pages/              # Page Object Model classes
│   ├── base_page.py   # Common page functionality
│   ├── main_page.py   # Main page elements and actions
│   └── ...
├── tests/             # Test cases
│   ├── conftest.py    # Test fixtures
│   └── *_test.py      # Individual test files
├── utils/             # Helper functions
├── config.py          # Configuration settings
└── pyproject.toml     # Dependencies and settings
```

## 🎯 Learning Goals

This project demonstrates:
- Page Object Model pattern
- Pytest fixtures and parameterization
- Web element interaction with Playwright
- Test reporting with Allure
- Basic CI/CD concepts

---
*This is a learning project for educational purposes.*
