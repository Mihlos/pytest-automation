from pytest import fixture

from selenium import webdriver


@fixture(scope='function')
def chrome_browser():
    browser = webdriver.Chrome(
      'home/miguel/.local/chromedriver')
    yield browser

    # Con yield se sigue ejecutando código, al contrario de con return
    print('Este print se ve.')
