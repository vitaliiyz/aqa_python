from pages.base_page import BasePage
from config import BASE_URL


class MainPage(BasePage):
    """Main page object for the Empik.com website."""

    def __init__(self, page):
        """Initialize the main page with base URL."""
        super().__init__(page)
        self._url = BASE_URL

    def popup(self):
        return self.find_by_page_locator(
            '[class*="CookiesConsentsBannerRodo-module_containerInfo"]'
        )

    def popup_text_element(self):
        return self.find_by_text("Prywatność Użytkownika")

    def desktop_buttons(self):
        return self.find_by_page_locator('[class*="buttonsDesktop"]')

    def accept_button(self):
        return self.find_by_page_locator(
            '[class*="InfoPage-module_buttonsDesktop"] '
            '[data-ta="cookie-btn-accept-all"]'
        )

    # def user_menu(self):
    #     return self.find_by_page_locator(".empikNav__userLink.userMenu")

    def login_button(self):
        return self.find_by_page_locator('xpath=//header//a[contains(@title, "Zaloguj")]')

    def register_link(self):
        return self.find_by_page_locator('[title="Zarejestruj się"]')

    def search_input(self):
        return self.find_by_page_locator('xpath=//header//input[@type="search"]')

    def search_dropdown_related_products_list(self):
        return self.find_by_page_locator('[class*="phrasesList"]')

    def search_dropdown_related_products_list_1st_value(self):
        return self.find_by_locator(
            self.search_dropdown_related_products_list(), "i"
        ).first

    def search_button(self):
        return self.find_by_page_locator(
            '//header//div[contains(@class, "searchContainer")]//button[@type="submit"]'
        )
