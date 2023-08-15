import pytest
from selenium import webdriver


@pytest.fixture()
def user():
    options = webdriver.ChromeOptions()
    options.add_argument('start-maximized')
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()
