from pages.base_page import BasePage
from config import BASE_URL


class MainPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self._url = BASE_URL

    def go_to(self):
        self._page.goto(self._url)

    def popup(self):
        return self.find_by_locator('[class*="CookiesConsentsBannerRodoHelper"]')

    def popup_text_element(self):
        return self.find_by_text("Prywatność Użytkownika")

    def desktop_buttons(self):
        return self.find_by_locator('[class*="buttonsDesktop"]')

    def accept_button(self):
        return self.find_by_locator(
            '//div[contains(@class, "buttonsDesktop")]/button[@data-ta="cookie-btn-accept-all"]'
        )

    def user_menu(self):
        return self.find_by_locator('[class="empikNav__userLink userMenu"]')

    def register_link(self):
        return self.find_by_locator('[title="Zarejestruj się"]')