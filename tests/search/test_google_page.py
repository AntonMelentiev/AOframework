def test_google_search__text_input__text_from_input_in_results(step):
    txt_to_search = "Selenium"

    step.page.google.open()
    step.page.google.search_text(txt_to_search)
    result = step.page.google.get_text_after_search()

    step.check.equality(txt_to_search, result)
