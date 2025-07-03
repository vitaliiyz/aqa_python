import pytest
import allure, os
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


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed and "page" in item.funcargs:
        screenshot = item.funcargs["page"].screenshot()
        allure.attach(screenshot, name="failure-screenshot", attachment_type=allure.attachment_type.PNG)
