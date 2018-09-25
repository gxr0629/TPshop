from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class BaseAction:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, location, timeout=10, poll=1.0):
        by, value = location
        wait = WebDriverWait(self.driver, timeout, poll)
        return wait.until(lambda x: x.find_element(by, value))

    def find_elements(self, location, timeout=10, poll=1):
        by, value = location
        wait = WebDriverWait(self.driver, timeout, poll)
        return wait.until(lambda x: x.find_elements(by, value))

    def click(self, location):
        self.find_element(location).click()

    def send_keys(self, location, text):
        self.find_element(location).send_keys(text)

    def find_toast(self, key_word):
        location = By.XPATH, "//*[contains(@text,'" + key_word + "')]"
        return self.find_element(location, timeout=5, poll=0.1).text

    def is_toast_exit(self, key_word):
        try:
            self.find_toast(key_word)
            return True
        except Exception:
            return False
