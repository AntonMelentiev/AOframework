import pytest


def test_python_search__text_input__text_from_input_in_results(test):
    txt_to_search = test.test_data.python_text_to_search

    test.page.python.open()
    test.page.python.search_text(txt_to_search)
    result = test.page.python.get_text_after_search()

    test.check.equality(txt_to_search, result)


def test_python_page__text_input__first_result_link_correct(test):
    txt_to_search = "builtin"
    expected_link = "https://docs.python.org/3/library/builtins.html?highlight=builtin#module-builtins"

    test.page.python.open()
    test.page.python.search_text(txt_to_search)
    first_link = test.page.python.get_first_search_result()

    test.check.equality(first_link, expected_link)


@pytest.mark.parametrize(
    "txt_to_search, expected_results_num",
    [
        ("builtin", 69),
        ("adsfadsfdasfasdf", 0),
    ],
)
def test_python_page__text_input__number_of_results_correspond_to_text(step, txt_to_search, expected_results_num):
    step.page.python.open()
    step.page.python.search_text(txt_to_search)
    number_of_results = step.page.python.get_number_of_results()

    step.check.equality(number_of_results, expected_results_num)
