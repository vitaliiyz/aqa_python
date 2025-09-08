from pages.base_page import BasePage
from config import BASE_URL


class MainPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self._url = BASE_URL

    def go_to(self):
        self._page.goto(self._url)

    def popup(self):
        return self.find_by_page_locator('[class*="CookiesConsentsBannerRodo"][class*="container"]')

    def popup_text_element(self):
        return self.find_by_text("Prywatność Użytkownika")

    def desktop_buttons(self):
        return self.find_by_page_locator('[class*="buttonsDesktop"]')

    def accept_button(self):
        return self.find_by_page_locator(
            '[class*="InfoPage-module_buttonsDesktop"] [data-ta="cookie-btn-accept-all"]'
        )

    def user_menu(self):
        return self.find_by_page_locator('.empikNav__userLink.userMenu')

    def register_link(self):
        return self.find_by_page_locator('[title="Zarejestruj się"]')

    def search_input(self):
        return self.find_by_page_locator('[type="search"]')

    def search_dropdown_related_products_list(self):
        return self.find_by_page_locator('.css-26b661')

    def search_dropdown_related_products_list_1st_value(self):
        return self.find_by_locator(self.search_dropdown_related_products_list(), "i").first

    def search_button(self):
        return self.find_by_page_locator('//div[@class="main-search__container"]//button[@type="submit"]')
