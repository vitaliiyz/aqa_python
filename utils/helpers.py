def close_popup_if_visible(main_page):
    """Close privacy/cookie popup if it's visible on the page."""
    popup = main_page.popup()
    try:
        main_page.wait_for_element_visible(element=popup, timeout=3000)
        if popup.is_visible():
            main_page.click(main_page.accept_button())
    except Exception:
        # Popup not found or not visible - this is expected behavior
        pass
