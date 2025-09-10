def close_popup_if_visible(main_page):
    """Close privacy/cookie popup if it's visible on the page."""
    popup = main_page.popup()
    main_page.wait_for_element_visible(element=popup)
    if popup.is_visible():
        main_page.click(main_page.accept_button())
