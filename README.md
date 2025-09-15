# AQA Python Project

A modern test automation framework built with Python 3.9+ and Playwright for end-to-end testing of web applications. This project demonstrates best practices in test automation including the Page Object Model pattern, test reporting with Allure, and CI/CD integration with GitHub Actions.

[![GitHub Actions](https://github.com/vitaliiyz/aqa_python/actions/workflows/github-actions.yml/badge.svg?branch=main)](https://github.com/vitaliiyz/aqa_python/actions/workflows/github-actions.yml)
[![Python Version](https://img.shields.io/badge/python-3.9%2B-blue.svg)](https://python.org)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## 🎯 Project Overview

This test automation project provides a robust framework for testing web applications with focus on:
- **Scalable Architecture**: Built using the Page Object Model pattern for maintainable test code
- **Modern Tools**: Leveraging Playwright for reliable cross-browser testing
- **Comprehensive Reporting**: Automated Allure reports published via GitHub Pages
- **CI/CD Integration**: Automated testing and deployment with GitHub Actions
- **Code Quality**: Enforced code style and linting with Black and Flake8

## 🛠 Technologies

- **Python 3.9+** - Programming language  
- **Poetry** - Dependency management and packaging
- **Playwright** - Cross-browser automation framework
- **Pytest** - Testing framework with fixtures and parameterization
- **Allure** - Test reporting and documentation
- **Black** - Code formatting
- **Flake8** - Code linting and style checking

## 📊 Test Reporting

Allure HTML reports are automatically generated and published via GitHub Pages after each successful test run on `main` or `dev` branches.

🔗 **View latest report:** [Allure Report on GitHub Pages](https://vitaliiyz.github.io/aqa_python/)  
*(Report may not exist until the first successful CI run on `main` or `dev`.)*

## 🚀 Getting Started

### Prerequisites

Ensure you have the following installed on your system:
- Python 3.9 or higher
- Poetry (for dependency management)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/vitaliiyz/aqa_python.git
   cd aqa_python
   ```

2. **Install Poetry** (if not already installed):
   ```bash
   # Using pip
   pip install poetry
   
   # Or using the official installer
   curl -sSL https://install.python-poetry.org | python3 -
   
   # Or using pipx (recommended)
   pipx install poetry
   ```

3. **Install project dependencies:**
   ```bash
   # Install all dependencies including dev tools
   poetry install
   
   # Install Playwright browsers
   poetry run playwright install
   ```

4. **Verify installation:**
   ```bash
   # Run a quick test to verify everything works
   poetry run pytest tests/main_page_test.py -v
   ```

## 🧪 Running Tests

### Quick Start

Run all tests in headless mode (default):
```bash
poetry run pytest
```

### Test Execution Options

**Run specific test files:**
```bash
# Run tests for main page functionality
poetry run pytest tests/main_page_test.py

# Run tests for cart functionality  
poetry run pytest tests/cart_page_test.py
```

**Run specific test cases:**
```bash
# Run a specific test by name
poetry run pytest tests/main_page_test.py::test_accept_privacy_popup_closed

# Run tests with specific product parameter
poetry run pytest tests/cart_page_test.py::test_add_and_remove_product_from_cart -k "iphone"
```

**Browser and UI Options:**
```bash
# Show browser UI (headed mode)
poetry run pytest --headed

# Slow down actions for debugging
poetry run pytest --slowmo=1000

# Use specific browser
poetry run pytest --browser chromium  # default
poetry run pytest --browser firefox
poetry run pytest --browser webkit

# Combine options
poetry run pytest --headed --browser firefox --slowmo=500
```

**Test Reporting:**
```bash
# Generate Allure report locally
poetry run pytest --alluredir=allure-results
poetry run allure serve allure-results

# Run with verbose output
poetry run pytest -v

# Run with test coverage
poetry run pytest --cov=pages --cov=utils
```

## 🛠 Development

### Code Quality Tools

This project uses automated code quality tools to ensure consistent code style:

```bash
# Format code with Black
poetry run black .

# Check code style with Flake8
poetry run flake8 .

# Run both formatting and linting
poetry run black . && poetry run flake8 .
```

### Development Environment

```bash
# Activate the Poetry virtual environment
poetry shell

# Install development dependencies
poetry install --with dev

# Run tests in watch mode during development
poetry run pytest-watch  # Note: requires pytest-watch installation
```

### Adding New Tests

1. **Create page objects** in the `pages/` directory following the existing pattern
2. **Write test cases** in the `tests/` directory using pytest fixtures
3. **Use Allure decorators** for better test reporting:
   ```python
   import allure
   
   @allure.step("Verify element is visible")
   def test_element_visibility(page_object):
       page_object.expect_to_be_visible(page_object.element())
   ```

## 📁 Project Structure

```
├── .github/
│   └── workflows/
│       └── github-actions.yml    # CI/CD pipeline configuration
├── pages/                        # Page Object Model classes
│   ├── __init__.py
│   ├── base_page.py             # Base page with common functionality
│   ├── main_page.py             # Main/home page elements and actions
│   ├── search_page.py           # Search results page
│   ├── product_page.py          # Individual product page
│   └── cart_page.py             # Shopping cart page
├── tests/                        # Test cases and fixtures
│   ├── __init__.py
│   ├── conftest.py              # Pytest fixtures and configuration
│   ├── main_page_test.py        # Tests for main page functionality
│   └── cart_page_test.py        # Tests for cart operations
├── utils/                        # Utility functions and helpers
│   ├── __init__.py
│   └── helpers.py               # Common helper functions
├── config.py                     # Configuration settings
├── pyproject.toml               # Poetry dependencies and project config
├── poetry.lock                  # Lock file for reproducible builds
└── README.md                    # Project documentation
```

## 🤝 Contributing

We welcome contributions! Please follow these guidelines:

### Getting Started with Contributions

1. **Fork the repository** and create a feature branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes** following the project conventions:
   - Follow the existing code style (enforced by Black and Flake8)
   - Add appropriate tests for new functionality
   - Update documentation as needed
   - Use meaningful commit messages

3. **Test your changes:**
   ```bash
   # Run all tests
   poetry run pytest
   
   # Check code style
   poetry run black . --check
   poetry run flake8 .
   ```

4. **Submit a pull request** with:
   - Clear description of changes
   - Reference to related issues
   - Test results and screenshots if applicable

### Code Style Guidelines

- **Python Code**: Follow PEP 8 standards (enforced by Flake8)
- **Formatting**: Use Black for automatic code formatting
- **Line Length**: Maximum 88 characters per line
- **Imports**: Group imports according to PEP 8 (standard, third-party, local)
- **Docstrings**: Use Google-style docstrings for classes and functions
- **Naming**: Use descriptive names for variables, functions, and classes

### Reporting Issues

Please use the GitHub issue tracker to report bugs or request features:
- **Bug reports**: Include steps to reproduce, expected vs actual behavior
- **Feature requests**: Describe the use case and proposed solution
- **Questions**: Tag with 'question' label for general inquiries

## 📄 License

This project is created for educational and practice purposes. Please ensure you comply with the terms of service of any websites you test against.

## 🙏 Acknowledgments

- Built with [Playwright](https://playwright.dev/) for reliable web testing
- Test reporting powered by [Allure Framework](https://allurereport.org/)
- Dependency management with [Poetry](https://python-poetry.org/)
- Code quality ensured by [Black](https://black.readthedocs.io/) and [Flake8](https://flake8.pycqa.org/)