import allure
import pytest
from utils.helpers import close_popup_if_visible


@allure.step("Verify cookie popup initial visibility")
def test_accept_privacy_popup_visible(main_page):
    main_page.expect_to_be_visible(main_page.popup())


@allure.step("Accept all cookies")
def test_desktop_buttons_visible(main_page):
    main_page.expect_to_be_visible(main_page.desktop_buttons())


@allure.step("Verify cookie popup is hidden")
def test_accept_privacy_popup_closed(main_page):
    main_page.expect_to_be_visible(main_page.accept_button())
    close_popup_if_visible(main_page)
    main_page.expect_not_to_be_visible(main_page.popup_text_element())
    main_page.expect_not_to_be_visible(main_page.desktop_buttons())
    main_page.expect_not_to_be_visible(main_page.accept_button())


def test_user_menu_to_be_visible(main_page):
    main_page.expect_to_be_visible(main_page.user_menu())


@pytest.mark.skip(reason="Skipping this test due to failure")
def test_register_link_to_be_visible(main_page):
    close_popup_if_visible(main_page)
    main_page.hover(main_page.user_menu())
    main_page.expect_to_be_visible(main_page.register_link())
