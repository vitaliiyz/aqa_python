def close_popup_if_visible(main_page):
    popup = main_page.popup()
    if popup.is_visible():
        main_page.click(main_page.accept_button())
