from base.base_driver import web_driver
from page.page import Page
import time


class TestLogin:
    def setup(self):
        self.driver = web_driver()
        self.page = Page(self.driver)

    def test_login(self):
        self.page.home.click_mine()
        self.page.mine.click_signup_login()
        self.page.sign_up_and_login.input_phone("18503080305")
        self.page.sign_up_and_login.input_password("123456")
        self.page.sign_up_and_login.click_login()
        time.sleep(1)
        assert self.page.sign_up_and_login.is_toast_exit("登录成功")
