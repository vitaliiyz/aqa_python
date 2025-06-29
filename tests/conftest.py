import pytest
from playwright.sync_api import Page
from pages.main_page import MainPage


@pytest.fixture
def main_page(page: Page) -> MainPage:
    """Fixture to initialize the MainPage and ensure it's open."""
    page_model = MainPage(page)
    if page.url != page_model.url:
        page_model.open_page()
    return page_model
