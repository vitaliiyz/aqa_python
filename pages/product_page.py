from pages.base_page import BasePage


class ProductPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    def price_main_container(self):
        return self.find_by_page_locator('[data-ta-section="priceMainContainer"]')

    def product_name(self):
        return self.find_by_page_locator('xpath=//div[@data-ta-section="ProductMainInfoDesktop"]//h1')

    def product_price(self):
        return self.find_by_locator(self.price_main_container(), '[data-ta="price"]')

    def add_to_cart_button(self):
        return self.find_by_locator(self.price_main_container(), '[data-ta="add-to-cart-btn"]')

    def added_to_cart_window(self):
        return self.find_by_page_locator('[data-ta-section="DrawerDesktop"]')

    def added_to_cart_window_product_name(self):
        return self.find_by_locator(self.added_to_cart_window(), 'h4')

    def added_to_cart_window_go_to_cart_button(self):
        return self.find_by_locator(self.added_to_cart_window(), '[data-ta="go-to-cart"]')

    def added_to_cart_window_continue_shopping_button(self):
        return self.find_by_locator(self.added_to_cart_window(), '[data-ta="close-drawer"]')
