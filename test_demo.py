from pytest import mark

from selenium import webdriver


@mark.demo
def test_func_ok():
    browser = webdriver.Chrome()
    browser.get('www.google.es')
    assert True

