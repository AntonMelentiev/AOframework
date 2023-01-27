import pytest


def test_python_search__text_input__text_from_input_in_results(t):
    t.step.page.python_documentation.open()
    t.step.page.python_documentation.search_text(t.data.python_text_to_search)

    actual_search_value = t.step.page.python_search.elements.SEARCH_INPUT.value
    t.step.check.equality(t.data.python_text_to_search, actual_search_value)


def test_python_page__text_input__first_result_link_correct(t):
    expected_link = "https://docs.python.org/3/library/builtins.html?highlight=builtin#module-builtins"

    t.step.page.python_documentation.open()
    t.step.page.python_documentation.search_text(t.data.python_text_to_search)

    first_link = t.step.page.python_search.get_first_search_result().LINK.url
    t.step.check.equality(first_link, expected_link)


@pytest.mark.parametrize(
    argnames=["txt_to_search", "expected_results_num"],
    argvalues=[
        ("builtin", 80),
        ("adsfadsfdasfasdf", 0),
    ],
    ids=["search builtin", "search abstract text"],
)
def test_python_page__text_input__number_of_results_correspond_to_text(t, txt_to_search, expected_results_num):
    t.step.page.python_documentation.open()
    t.step.page.python_documentation.search_text(txt_to_search)

    number_of_results = t.step.page.python_search.get_number_of_results()
    t.step.check.equality(number_of_results, expected_results_num)
