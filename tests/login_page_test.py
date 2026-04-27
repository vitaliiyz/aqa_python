import allure


@allure.step("Verify and click on Login button")
def verify_and_click_on_login_button(main_page, login_page):
    main_page.expect_to_be_visible(main_page.login_button())
    main_page.click(main_page.login_button())
    login_page.expect_to_be_visible(login_page.register_link())


@allure.step("Verify register and I dont have account link")
def verify_register_and_no_account_link(login_page):
    login_page.expect_to_be_visible(login_page.register_link())
    login_page.expect_to_have_text(login_page.register_link(), "Załóż nowe")

    login_page.expect_to_be_visible(login_page.do_not_have_account_link())
    login_page.expect_to_have_text(login_page.do_not_have_account_link(), "Nie pamiętam hasła")


@allure.step("Verify email and password inputs, login button")
def verify_email_and_password_inputs(login_page):
    login_page.expect_to_be_visible(login_page.email_input())
    login_page.expect_to_have_text(login_page.email_input_label(), "Adres e-mail*")

    login_page.expect_to_be_visible(login_page.pwd_input())
    login_page.expect_to_have_text(login_page.pwd_input_label(), "Hasło*")

    login_page.expect_to_be_visible(login_page.login_button())
    login_page.expect_to_have_text(login_page.login_button_text(), "Zaloguj")


@allure.step("Verify that email and password are required")
def verify_required_inputs(login_page):
    login_page.expect_not_to_be_visible(login_page.email_is_mandatory_helper())
    login_page.expect_not_to_be_visible(login_page.pwd_is_mandatory_helper())

    login_page.click(login_page.login_button())
    login_page.expect_to_be_visible(login_page.email_is_mandatory_helper())
    login_page.expect_to_be_visible(login_page.pwd_is_mandatory_helper())
    login_page.expect_to_have_text(login_page.email_is_mandatory_helper(), "Wprowadź adres e-mail")
    login_page.expect_to_have_text(login_page.pwd_is_mandatory_helper(), "Hasło jest wymagane")


@allure.step("Login test")
def test_login(main_page, login_page):
    verify_and_click_on_login_button(main_page, login_page)
    verify_register_and_no_account_link(login_page)
    verify_email_and_password_inputs(login_page)
    verify_required_inputs(login_page)
