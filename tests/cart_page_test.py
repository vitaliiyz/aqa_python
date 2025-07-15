import allure
import pytest

from tests.conftest import search_page

PRODUCTS_NAMES = [
    "iphone 16 pro",
    "playstation 5",
    "harry potter"
]


@pytest.mark.parametrize('product', PRODUCTS_NAMES)
@allure.step("Add product to Cart and remove from Cart")
def test_add_and_remove_product_from_cart(main_page, search_page, product_page, cart_page, product):
def test_add_and_remove_product_from_cart(main_page, search_page, product_page, cart_page, product):
    allure.step("Pre-test setup: Close any visible popups")
    close_popup_if_visible(main_page.page) # Assuming close_popup_if_visible needs the page object

    with allure.step(f"Search for product: '{product}'"):
        main_page.search_for_product(product) # Using the new helper method

    with allure.step("Verify search results and navigate to product page"):
        search_page.expect_to_be_visible(search_page.search_list())
        
        product_name_locator = search_page.search_list_1st_item_name()
        product_price_locator = search_page.search_list_1st_item_price()

        search_page.expect_to_contain_text_ignore_case(product_name_locator, product)
        
        product_name_text = product_name_locator.text_content()
        product_price_text = product_price_locator.text_content()

        search_page.click(search_page.search_list_1st_item_link())

    with allure.step("Verify product details on product page and add to cart"):
        product_page.expect_to_be_visible(product_page.price_main_container())
        product_page.expect_to_have_text(product_page.product_name(), product_name_text)
        product_page.expect_to_have_text(product_page.product_price(), product_price_text)

        product_page.click(product_page.add_to_cart_button()) # Implicitly waits for visibility

        product_page.expect_to_be_visible(product_page.added_to_cart_window())
        product_page.expect_to_have_text(product_page.product_name(), product_name_text) # Re-check name in popup
        
        product_page.click(product_page.added_to_cart_window_go_to_cart_button())

    with allure.step("Verify product in cart"):
        cart_page.expect_to_have_title(cart_page.page_title)
        
        cart_page.expect_to_be_visible(cart_page.product_box())
        cart_page.expect_to_have_text(cart_page.product_name(), product_name_text)
        cart_page.expect_to_have_text(cart_page.product_price(), product_price_text)
        
        cart_page.expect_to_have_attribute(cart_page.quantity_box_value(), "value", "1")
        
    with allure.step("Remove product from cart and verify empty cart"):
        cart_page.click(cart_page.quantity_box_remove_button()) # Implicitly waits for visibility

        cart_page.expect_not_to_be_visible(cart_page.quantity_box())
        cart_page.expect_to_be_visible(cart_page.empty_cart_section())
        cart_page.expect_to_have_text(cart_page.empty_cart_section_title(), cart_page.EMPTY_CART_TITLE)
