import pytest

from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage
from Config.Config import TestData
from Tests.test_base import BaseTest

@pytest.mark.testLogin
class Test_login(BaseTest):
    def test_login(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        #self.loginPage.do_login(TestData.USER_NAME)
        #This method should return the object of nect landing page as we will be going to Home so  will provide its object
        return HomePage(self.driver)