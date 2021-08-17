from lib2to3.pgen2 import driver

import pytest

from Pages.LoginPage import LoginPage
from Tests.test_base import BaseTest
from Config.Config import TestData
from Pages.HomePage import HomePage
@pytest.mark.testLogin

class Test_Home(BaseTest):
    def test_home_page_title(self):
        self.loginPage = LoginPage(self.driver)
        homePage = self.loginPage.do_login(TestData.USER_NAME,TestData.PASSWORD)
        title = homePage.get_home_page_title(TestData.HOME_PAGE_TITLE)
        assert title == TestData.HOME_PAGE_TITLE

    def test_home_header(self):
        self.loginPage = LoginPage(self.driver)
        homePage = self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        header = homePage.get_header_value()
        assert header == TestData.HEADER_VALUE


    def test_setting_icon_exist(self):
        self.loginPage = LoginPage(self.driver)
        homePage = self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        assert homePage.is_setting_icon_exist()

