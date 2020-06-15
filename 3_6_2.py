import time
import math
import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome()
    browser.implicitly_wait(20)
    yield browser
    browser.quit()


@pytest.mark.parametrize('sublink', ['895', '896', '897', '898', '899', '903', '904', '905'])
def test_get_answer_in_optional_feedback(browser, sublink):
    link = f"https://stepik.org/lesson/236{sublink}/step/1"
    browser.get(link)
    answer_field = browser.find_element_by_class_name('ember-text-area')
    answer = math.log(int(time.time()))
    answer_field.send_keys(str(answer))
    send_button = browser.find_element_by_class_name('submit-submission')
    send_button.click()
    smart_hint = browser.find_element_by_class_name('smart-hints__hint')
    message = smart_hint.text
    assert message == 'Correct!', f"expected 'Correct!', got {message}"





