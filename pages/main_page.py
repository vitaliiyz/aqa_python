from pages.base_page import BasePage


class MainPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self._url = "https://www.empik.com/"

    def popup(self):
        return self.find_by_page_locator('[class*="CookiesConsentsBannerRodoHelper"]')

    def popup_text_element(self):
        return self.find_by_text("Prywatność Użytkownika")

    def desktop_buttons(self):
        return self.find_by_page_locator('[class*="buttonsDesktop"]')

    def accept_button(self):
        return self.find_by_page_locator(
            '//div[contains(@class, "buttonsDesktop")]/button[@data-ta="cookie-btn-accept-all"]'
        )

    def user_menu(self):
        return self.find_by_page_locator('[class="empikNav__userLink userMenu"]')

    def register_link(self):
        return self.find_by_page_locator('[title="Zarejestruj się"]')

    def search_input(self):
        return self.find_by_page_locator('[type="search"]')

    def search_dropdown_related_products_list(self):
        return self.find_by_page_locator('[class="css-26b661"]')

    def search_dropdown_related_products_list_1st_value(self):
        return self.find_by_locator(self.search_dropdown_related_products_list(), "i").first

    def search_button(self):
        return self.find_by_page_locator('//div[@class="main-search__container"]//button[@type="submit"]')
