import allure
from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class SignUpAndLoginPage(BaseAction):
    phone_button = By.ID, "com.tpshop.malls:id/edit_phone_num"
    password_button = By.ID, "com.tpshop.malls:id/edit_password"
    login_button = By.ID, "com.tpshop.malls:id/btn_login"

    def input_phone(self, text):
        self.send_keys(self.phone_button, text)

    def input_password(self, text):
        self.send_keys(self.password_button, text)

    def click_login(self):
        self.click(self.login_button)
