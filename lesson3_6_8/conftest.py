import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options



def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='ru',
                     help='Choose the language, like en - English')


@pytest.fixture(scope='function')
def browser(request):
    chosen_language = request.config.getoption('language')
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': chosen_language})
    browser = webdriver.Chrome(options=options)
    yield browser
    time.sleep(5)
    browser.quit()

