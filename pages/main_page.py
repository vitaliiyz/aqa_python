from .base_page import BasePage

popup_locator = '[class*="CookiesConsentsBannerRodoHelper"]'
popup_text = "Prywatność Użytkownika"
desktop_buttons_locator = '[class*="buttonsDesktop"]'
accept_button_locator = (
    '//div[contains(@class, "buttonsDesktop")]/button[@data-ta="cookie-btn-accept-all"]'
)
user_menu_locator = '[class="empikNav__userLink userMenu"]'
# register_link_text = "Załóż je"
register_link_locator = '[title="Zarejestruj się"]'


class MainPage(BasePage):
    def __init__(self, page, expect):
        super().__init__(page, expect)
        self._url = "https://www.empik.com/"

    def popup(self):
        print(popup_locator)
        return self.find_by_locator(popup_locator)

    def popup_text(self):
        return self.find_by_text(popup_text)

    def desktop_buttons(self):
        return self.find_by_locator(desktop_buttons_locator)

    def accept_button(self):
        return self.find_by_locator(accept_button_locator)

    def user_menu(self):
        return self.find_by_locator(user_menu_locator)

    def register_link(self):
        # return self.find_by_text(register_link_text)
        return self.find_by_locator(register_link_locator)
