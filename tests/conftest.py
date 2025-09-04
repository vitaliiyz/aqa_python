import pytest
from playwright.sync_api import Page
from pages.main_page import MainPage
from pages.search_page import SearchPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from utils.helpers import close_popup_if_visible

# --- Global timeout defaults in milliseconds ---
GLOBAL_DEFAULT_TIMEOUT = 10000          # 10 sec for all locators
GLOBAL_NAVIGATION_TIMEOUT = 20000       # 20 sec for navigation

@pytest.fixture
def main_page(page: Page) -> MainPage:
    """Fixture to initialize the MainPage with global timeouts and ensure it's open."""
    # Set global flexible timeouts
    page.set_default_timeout(GLOBAL_DEFAULT_TIMEOUT)
    page.set_default_navigation_timeout(GLOBAL_NAVIGATION_TIMEOUT)

    page_model = MainPage(page)
    if page.url != page_model.url:
        page_model.open_page()

    # Close cookies popup if visible
    close_popup_if_visible(page_model)

    return page_model

@pytest.fixture
def search_page(page: Page) -> SearchPage:
    """Fixture to initialize the SearchPage with global timeouts."""
    page.set_default_timeout(GLOBAL_DEFAULT_TIMEOUT)
    page.set_default_navigation_timeout(GLOBAL_NAVIGATION_TIMEOUT)

    page_model = SearchPage(page)
    return page_model

@pytest.fixture
def product_page(page: Page) -> ProductPage:
    """Fixture to initialize the ProductPage with global timeouts."""
    page.set_default_timeout(GLOBAL_DEFAULT_TIMEOUT)
    page.set_default_navigation_timeout(GLOBAL_NAVIGATION_TIMEOUT)

    page_model = ProductPage(page)
    return page_model

@pytest.fixture
def cart_page(page: Page) -> CartPage:
    """Fixture to initialize the CartPage with global timeouts."""
    page.set_default_timeout(GLOBAL_DEFAULT_TIMEOUT)
    page.set_default_navigation_timeout(GLOBAL_NAVIGATION_TIMEOUT)

    page_model = CartPage(page)
    return page_model