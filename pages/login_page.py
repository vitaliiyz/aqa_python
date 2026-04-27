from pages.base_page import BasePage


class LoginPage(BasePage):
    """Login page object for handling login operations."""

    def __init__(self, page):
        """Initialize the login page."""
        super().__init__(page)
        self._page_title = "Logowanie - EMPIK"

    @property
    def page_title(self):
        return self._page_title

    def main_form(self):
        return self.find_by_page_locator('xpath=//main/div[1]')

    def register_link(self):
        return self.find_by_locator(self.main_form(), 'xpath=./div[1]/p/a')

    def login_form(self):
        return self.find_by_locator(self.main_form(), 'xpath=./div[2]/form')

    def do_not_have_account_link(self):
        return self.find_by_locator(self.login_form(), 'xpath=./div[2]/button[1]')

    def email_input(self):
        return self.find_by_locator(self.login_form(), 'xpath=./div[1]/div[1]//input')

    def email_input_label(self):
        return self.find_by_locator(self.login_form(), 'xpath=./div[1]/div[1]//label')

    def pwd_input(self):
        return self.find_by_locator(self.login_form(), 'xpath=./div[1]/div[2]//input')

    def pwd_input_label(self):
        return self.find_by_locator(self.login_form(), 'xpath=./div[1]/div[2]//label')

    def login_button(self):
        return self.find_by_locator(self.login_form(), 'xpath=./div[2]/button[2]')

    def login_button_text(self):
        return self.find_by_locator(self.login_button(), 'xpath=./span[@data-testid="button-text"]')

    def email_is_mandatory_helper(self):
        return self.find_by_locator(self.login_form(), 'xpath=./div[1]/div[1]/p')

    def pwd_is_mandatory_helper(self):
        return self.find_by_locator(self.login_form(), 'xpath=./div[1]/div[2]/p')
