import time

from Pages.BasePage import BasePage
from Config.Config import TestData
from selenium.webdriver.common.by import By

from Pages.HomePage import HomePage


class LoginPage(BasePage):
    # Below we are initializing the locators we define in the Base class
    EMAIL = (By.ID, "txtEmail")
    PASSWORD = (By.ID, "txtPassword")
    LOGIN_BUTTON = (By.ID, "btnLogin")

    def __init__(self, driver):
        #becasue of Super constructor we will be able to access constructor of BasePage inside the constructor of LoginPage
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    # this function will be doing the login by using the loctors and function defined in he Base class
    def do_login(self,username, password):
    #def do_login(self, username):
        # here do_send_keys_requires ID and text so Login will provide the ID but text will be provided in the testLoginPage when called
        self.do_send_keys(self.EMAIL, username)
        self.do_click(self.LOGIN_BUTTON)

        time.sleep(3)
        self.do_send_keys(self.PASSWORD,password)
        self.do_click(self.LOGIN_BUTTON)


        return HomePage(self.driver)
