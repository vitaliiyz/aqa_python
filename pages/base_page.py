from playwright.sync_api import expect


class BasePage:
    def __init__(self, page):
        self._url = None
        self._page = page
        self._expect = expect

    @property
    def url(self):
        return self._url

    def open_page(self):
        self._page.goto(self._url)

    def find_by_locator(self, locator):
        return self._page.locator(locator)

    def find_by_text(self, text):
        return self._page.get_by_text(text)

    def expect_to_be_visible(self, element):
        self._expect(element).to_be_visible()

    def expect_not_to_be_visible(self, element):
        self._expect(element).not_to_be_visible()

    def click(self, element):
        element.click()

    def hover(self, element):
        element.hover()
