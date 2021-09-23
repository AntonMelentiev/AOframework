def test_google_search__text_input__text_from_input_in_results(test):
    txt_to_search = test.test_data.get_google_text_to_search()

    test.page.google.open()
    test.page.google.search_text(txt_to_search)
    result = test.page.google.get_text_after_search()

    test.check.equality(txt_to_search, result)
