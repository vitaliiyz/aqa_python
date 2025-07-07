import time

import allure
import pytest

from tests.conftest import search_page
from utils.helpers import close_popup_if_visible

PRODUCTS_NAMES = [
    "iphone 16 pro",
    "playstation 5",
    "harry potter"
]


@pytest.mark.parametrize('product', PRODUCTS_NAMES)
@allure.step("Add product to Cart and remove from Cart")
def test_add_and_remove_product_from_cart(main_page, search_page, product_page, cart_page, product):
    # If the Search Input is visible
    main_page.expect_to_be_visible(main_page.search_input())

    # Fill the data to the search input
    main_page.fill(main_page.search_input(), product)

    # Check the filled value
    main_page.expect_to_have_value(main_page.search_input(), product)

    # Dropdown with related to search products is disabled
    main_page.expect_to_be_visible(main_page.search_dropdown_related_products_list())

    # Check the 1st dropdown value
    main_page.expect_to_have_text(main_page.search_dropdown_related_products_list_1st_value(), product)

    # Click Search button
    main_page.click(main_page.search_button())

    # Check if there Search List
    search_page.expect_to_be_visible(search_page.search_list())

    # Check if the 1st Product Link Title Attribute contains Searched Value and save Product Name and Product Price
    product_name_locator = search_page.search_list_1st_item_name()
    product_price_locator = search_page.search_list_1st_item_price()
    search_page.expect_to_contain_text_ignore_case(product_name_locator, product)
    product_name_text = product_name_locator.text_content()
    product_price_text = product_price_locator.text_content()

    # Click on the 1st Product Page Link
    search_page.click(search_page.search_list_1st_item_link())

    # Check Price Container is visible
    product_page.expect_to_be_visible(product_page.price_main_container())

    # Compare Product Name and Price to Search List on Search Page
    product_page.expect_to_have_text(product_page.product_name(), product_name_text)
    product_page.expect_to_have_text(product_page.product_price(), product_price_text)

    # Check Add To Cart button is visible and click
    product_page.expect_to_be_visible(product_page.add_to_cart_button())
    product_page.click(product_page.add_to_cart_button())

    # Check Added To Cart window and buttons are visible and name of the added product is correct
    product_page.expect_to_be_visible(product_page.added_to_cart_window())
    product_page.expect_to_have_text(product_page.product_name(), product_name_text)
    product_page.expect_to_be_visible(product_page.added_to_cart_window_go_to_cart_button())
    product_page.expect_to_be_visible(product_page.added_to_cart_window_continue_shopping_button())

    # Click Go To Cart button
    product_page.click(product_page.added_to_cart_window_go_to_cart_button())

    # Check if Page Title is Koszyk
    cart_page.expect_to_have_title(cart_page.page_title)

    # Check if Product Box, Product Name and Price are visible; Product Name and Price are correct
    cart_page.expect_to_be_visible(cart_page.product_box())
    cart_page.expect_to_be_visible(cart_page.product_name())
    cart_page.expect_to_be_visible(cart_page.product_price())
    cart_page.expect_to_have_text(cart_page.product_name(), product_name_text)
    cart_page.expect_to_have_text(cart_page.product_price(), product_price_text)

    # Check if Quantity Box, Quantity Remove Button and Quantity Box value are visible
    cart_page.expect_to_be_visible(cart_page.quantity_box())
    cart_page.expect_to_have_attribute(cart_page.quantity_box_value(), "value", "1")
    cart_page.expect_to_be_visible(cart_page.quantity_box_remove_button())

    # Click Quantity Remove Button
    cart_page.click(cart_page.quantity_box_remove_button())

    # Check if Quantity Box is not visible
    cart_page.expect_not_to_be_visible(cart_page.quantity_box())

    # Check if Empty Cart Section is visible and Title equals to Twój koszyk jest pusty
    cart_page.expect_to_be_visible(cart_page.empty_cart_section())
    cart_page.expect_to_have_text(cart_page.empty_cart_section_title(), 'Twój koszyk jest pusty')
