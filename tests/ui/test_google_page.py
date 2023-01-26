def test_google_search__text_input__text_from_input_in_results(t):
    t.step.page.google_search.open()
    t.step.page.google_search.search_text(t.data.google_text_to_search)

    search_result = t.step.page.google_results.get_text_after_search()
    t.step.check.equality(t.data.google_text_to_search, search_result)
