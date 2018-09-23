from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class MinePage(BaseAction):
    signup_login_button = By.XPATH, "//*[@text='登录/注册']"

    def click_signup_login(self):
        self.click(self.signup_login_button)
