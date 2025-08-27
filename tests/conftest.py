import pytest
from playwright.sync_api import Page
from pages.main_page import MainPage
from pages.search_page import SearchPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from utils.helpers import close_popup_if_visible


@pytest.fixture
def main_page(page: Page) -> MainPage:
    """Fixture to initialize the MainPage and ensure it's open."""
    page_model = MainPage(page)
    if page.url != page_model.url:
        page_model.open_page()

    # Close cookies popup when it is visible on page
    close_popup_if_visible(page_model)

    return page_model


@pytest.fixture
def search_page(page: Page) -> SearchPage:
    """Fixture to initialize the SearchPage and ensure it's open."""
    page_model = SearchPage(page)
    return page_model


@pytest.fixture
def product_page(page: Page) -> ProductPage:
    """Fixture to initialize the ProductPage and ensure it's open."""
    page_model = ProductPage(page)
    return page_model


@pytest.fixture
def cart_page(page: Page) -> CartPage:
    """Fixture to initialize the CartPage and ensure it's open."""
    page_model = CartPage(page)
    return page_model
