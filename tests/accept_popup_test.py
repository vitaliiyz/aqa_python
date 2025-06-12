from playwright.sync_api import Page, expect


def open_page(page: Page, page_name):
    page.goto(page_name)


def test_accept_privacy_popup(page: Page):
    open_page(page, "https://www.empik.com/")
    popup = page.locator("[class*=\"CookiesConsentsBannerRodoHelper\"]")
    popup_text = popup.get_by_text("Prywatność Użytkownika")
    desktop_buttons_el = popup.locator("[class*=\"buttonsDesktop\"]")
    accept_button = desktop_buttons_el.locator("[data-ta=\"cookie-btn-accept-all\"]")

    expect(popup_text).to_be_visible()
    expect(desktop_buttons_el).to_be_visible()
    expect(accept_button).to_be_visible()

    accept_button.click()

    expect(popup_text).not_to_be_visible()
    expect(desktop_buttons_el).not_to_be_visible()
    expect(accept_button).not_to_be_visible()

    login_button = page.locator("[class=\"empikNav__userText ta-login-link\"]")
    expect(login_button).to_be_visible()
    login_button.hover()

    register_link = page.get_by_text("Załóż je")

    expect(register_link).to_be_visible()
