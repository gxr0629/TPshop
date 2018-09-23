from base.base_driver import web_driver
from page.page import Page


class TestLogin:
    def setup(self):
        self.driver = web_driver()
        self.page = Page(self.driver)

    def test_login(self):
        self.page.home.click_mine()
        self.page.mine.click_signup_login()
