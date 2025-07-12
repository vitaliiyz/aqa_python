from pages.base_page import BasePage


class SearchPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    def search_list(self):
        return self.find_by_page_locator(
            '//div[contains(@class, "search-list search-with-info")][@data-box-type="product"]')

    def search_list_1st_item(self):
        return self.find_by_locator(self.search_list(), 'xpath=//div[@itemprop="item"]').first

    def search_list_1st_item_link(self):
        return self.find_by_locator(self.search_list_1st_item(), '[class="seoTitle"]')

    def search_list_1st_item_name(self):
        return self.find_by_locator(self.search_list_1st_item_link(), 'strong')

    def search_list_1st_item_price(self):
        return self.find_by_locator(self.search_list_1st_item(), 'xpath=//div[@itemprop="price"]')
