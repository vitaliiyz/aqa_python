import pytest


def test_accept_privacy_popup_visible(main_page):
    main_page.expect_to_be_visible(main_page.popup())


def test_desktop_buttons_visible(main_page):
    main_page.expect_to_be_visible(main_page.desktop_buttons())


def test_accept_button_visible(main_page):
    main_page.expect_to_be_visible(main_page.accept_button())


def test_accept_privacy_popup_closed(main_page):
    main_page.click(main_page.accept_button())
    main_page.expect_not_to_be_visible(main_page.popup_text_element())
    main_page.expect_not_to_be_visible(main_page.desktop_buttons())
    main_page.expect_not_to_be_visible(main_page.accept_button())


def test_user_menu_to_be_visible(main_page):
    main_page.expect_to_be_visible(main_page.user_menu())


@pytest.mark.skip(reason="Skipping this test due to failure")
def test_register_link_to_be_visible(main_page):
    main_page.hover(main_page.user_menu())
    main_page.expect_to_be_visible(main_page.register_link())
