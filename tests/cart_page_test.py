import allure
import pytest

PRODUCTS_NAMES = ["iphone 16 pro", "harry potter"]


@allure.step("Search and open product page")
def search_and_open_product(main_page, search_page, product):
    main_page.expect_to_be_visible(main_page.search_input())
    main_page.fill(main_page.search_input(), product)
    main_page.expect_to_have_value(main_page.search_input(), product)

    main_page.expect_to_be_visible(main_page.search_dropdown_related_products_list())
    main_page.expect_to_have_text(
        main_page.search_dropdown_related_products_list_1st_value(), product
    )

    main_page.click(main_page.search_button())
    search_page.expect_to_be_visible(search_page.search_list())

    product_name_locator = search_page.search_list_1st_item_name()
    product_price_locator = search_page.search_list_1st_item_price()
    search_page.expect_to_contain_text_ignore_case(product_name_locator, product)

    product_name_text = product_name_locator.text_content()
    product_price_text = product_price_locator.text_content()

    search_page.click(search_page.search_list_1st_item_link())

    return product_name_text, product_price_text


@allure.step("Add product to cart and verify")
def add_product_to_cart(product_page, product_name_text, product_price_text):
    product_page.expect_to_be_visible(product_page.price_main_container())
    product_page.expect_to_have_text(product_page.product_name(), product_name_text)
    product_page.expect_to_have_text(product_page.product_price(), product_price_text)

    product_page.expect_to_be_visible(product_page.add_to_cart_button())
    product_page.click(product_page.add_to_cart_button())

    product_page.expect_to_be_visible(product_page.added_to_cart_window())
    product_page.expect_to_have_text(product_page.product_name(), product_name_text)
    product_page.expect_to_be_visible(
        product_page.added_to_cart_window_go_to_cart_button()
    )
    product_page.expect_to_be_visible(
        product_page.added_to_cart_window_continue_shopping_button()
    )

    product_page.click(product_page.added_to_cart_window_go_to_cart_button())


@allure.step("Verify and remove product from cart")
def verify_and_remove_from_cart(cart_page, product_name_text, product_price_text):
    cart_page.expect_to_have_title(cart_page.page_title)

    cart_page.expect_to_be_visible(cart_page.product_box())
    cart_page.expect_to_have_text(cart_page.product_name(), product_name_text)
    cart_page.expect_to_have_text(cart_page.product_price(), product_price_text)

    cart_page.expect_to_have_attribute(cart_page.quantity_box_value(), "value", "1")
    cart_page.expect_to_be_visible(cart_page.quantity_box_remove_button())

    cart_page.click(cart_page.quantity_box_remove_button())

    cart_page.expect_not_to_be_visible(cart_page.quantity_box())
    cart_page.expect_to_contain_text(
        cart_page.empty_cart_section_title(), "Twój koszyk jest pusty"
    )


@pytest.mark.parametrize("product", PRODUCTS_NAMES)
@allure.step("Add product to Cart and remove from Cart")
def test_add_and_remove_product_from_cart(
    main_page, search_page, product_page, cart_page, product
):
    product_name, product_price = search_and_open_product(
        main_page, search_page, product
    )
    add_product_to_cart(product_page, product_name, product_price)
    verify_and_remove_from_cart(cart_page, product_name, product_price)
