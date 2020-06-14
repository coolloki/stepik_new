import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


class TestRegistration(unittest.TestCase):
    def test_reg1(self):
        link = 'http://suninjuly.github.io/registration1.html'
        browser = webdriver.Chrome()
        browser.get(link)
        first_name = browser.find_element(By.CSS_SELECTOR, '.first_block .first')
        first_name.send_keys('Ivan')
        last_name = browser.find_element(By.CSS_SELECTOR, '.first_block .second')
        last_name.send_keys('Shmidt')
        email = browser.find_element(By.CSS_SELECTOR, '.first_block .third')
        email.send_keys('i.shmidt@gmailk.com')
        button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
        button.click()
        rigth_answer = 'Congratulations! You have successfully registered!'
        answer = WebDriverWait(browser, 5).until(EC.text_to_be_present_in_element((By.TAG_NAME, 'h1'), rigth_answer))
        self.assertIsNotNone(answer, 'Test not pass')
        browser.quit()

    def test_reg2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)
        first_name = browser.find_element(By.CSS_SELECTOR, '.first_block .first')
        first_name.send_keys('Ivan')
        last_name = browser.find_element(By.CSS_SELECTOR, '.first_block .second')
        last_name.send_keys('Shmidt')
        email = browser.find_element(By.CSS_SELECTOR, '.first_block .third')
        email.send_keys('i.shmidt@gmailk.com')
        button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
        button.click()
        rigth_answer = 'Congratulations! You have successfully registered!'
        answer = WebDriverWait(browser, 5).until(EC.text_to_be_present_in_element((By.TAG_NAME, 'h1'), rigth_answer))
        self.assertIsNotNone(answer, 'Test not pass')
        browser.quit()


if __name__ == "__main__":
    unittest.main()
