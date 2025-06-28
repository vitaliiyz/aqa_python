import pytest
from playwright.sync_api import Page, expect
from pages.main_page import MainPage
from utils.helpers import close_popup_if_visible


@pytest.fixture(scope="function")
def main_page(page: Page) -> MainPage:
    main_page = MainPage(page, expect)
    if page.url != main_page.url:
        main_page.open_page()
    return main_page


def test_accept_privacy_popup_visible(main_page):
    main_page.expect_to_be_visible(main_page.popup())


def test_desktop_buttons_visible(main_page):
    main_page.expect_to_be_visible(main_page.desktop_buttons())


def test_accept_button_visible(main_page):
    main_page.expect_to_be_visible(main_page.accept_button())


def test_accept_privacy_popup_closed(main_page):
    close_popup_if_visible(main_page)
    main_page.expect_not_to_be_visible(main_page.popup_text())
    main_page.expect_not_to_be_visible(main_page.desktop_buttons())
    main_page.expect_not_to_be_visible(main_page.accept_button())


def test_user_menu_to_be_visible(main_page):
    main_page.expect_to_be_visible(main_page.user_menu())


def test_register_link_to_be_visible(main_page):
    close_popup_if_visible(main_page)
    main_page.hover(main_page.user_menu())
    main_page.expect_to_be_visible(main_page.register_link())
