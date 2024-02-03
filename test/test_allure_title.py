import pytest
import allure


@allure.title("some title for test")
def test_with_title():
    pass

@allure.title("test title with params {param}")
@pytest.mark.parametrize("param", ["first", "second"])
def test_with_dynamic_title(param):
    pass

