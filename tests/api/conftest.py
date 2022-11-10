import pytest

from framework import T


@pytest.fixture
def t():
    t_object = T(driver=None)

    yield t_object
