from pages.base_page import BasePage


class CartPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self._page_title = "Koszyk"

    @property
    def page_title(self):
        return self._page_title

    def product_box(self):
        return self.find_by_page_locator('[data-ta="product-box"]')

    def product_name(self):
        return self.find_by_locator(
            self.product_box(), '[data-ta="product-title"]'
        )

    def product_price(self):
        return self.find_by_locator(
            self.product_box(), '[data-ta="product-main-price"]'
        )

    def quantity_box(self):
        return self.find_by_page_locator('[data-ta="quantity-box"]')

    def quantity_box_value(self):
        return self.find_by_locator(self.quantity_box(), "input")

    def quantity_box_remove_button(self):
        return self.find_by_locator(
            self.quantity_box(), '[data-ta="quantity-remove"]'
        )

    def empty_cart_section_title(self):
        return self.find_by_page_locator('[data-ta="empty-cart-section"]')
