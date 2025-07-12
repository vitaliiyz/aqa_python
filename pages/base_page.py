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

    def find_by_page_locator(self, locator):
        return self._page.locator(locator)

    def find_by_locator(self, base, locator):
        return base.locator(locator)

    def find_by_text(self, text):
        return self._page.get_by_text(text)

    def get_by_role(self, role):
        return self._page.get_by_role(role)

    def expect_to_be_visible(self, element):
        self._expect(element).to_be_visible()

    def expect_to_have_value(self, element, value):
        self._expect(element).to_have_value(value)

    def expect_to_have_text(self, element, text_value):
        self._expect(element).to_have_text(text_value)

    def expect_to_have_attribute(self, element, attr_name, attr_value):
        self._expect(element).to_have_attribute(attr_name, attr_value)

    def expect_to_contain_text_ignore_case(self, element, expected_text):
        self._expect(element).to_contain_text(expected_text, ignore_case=True)

    def expect_to_have_title(self, value):
        self._expect(self._page).to_have_title(value)

    def wait_for_element_visible(self, element, timeout=None):
        timeout = timeout if timeout is not None else 5000
        element.wait_for(state="visible", timeout=timeout)

    def expect_not_to_be_visible(self, element):
        self._expect(element).not_to_be_visible()

    def click(self, element):
        element.click()

    def hover(self, element):
        element.hover()

    def fill(self, element, value):
        element.fill(value)
