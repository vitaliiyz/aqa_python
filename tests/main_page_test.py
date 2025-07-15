import allure


@allure.step("Verify cookie popup is hidden")
def test_accept_privacy_popup_closed(main_page):
    main_page.expect_not_to_be_visible(main_page.popup_text_element())
    main_page.expect_not_to_be_visible(main_page.desktop_buttons())
    main_page.expect_not_to_be_visible(main_page.accept_button())


@allure.step("Verify User Menu is visible")
def test_user_menu_to_be_visible(main_page):
    main_page.expect_to_be_visible(main_page.user_menu())


@allure.step("Verify Register Link is visible")
def test_register_link_to_be_visible(main_page):
    main_page.hover(main_page.user_menu())
    main_page.expect_to_be_visible(main_page.register_link())
