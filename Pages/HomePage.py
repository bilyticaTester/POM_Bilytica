from lib2to3.pgen2 import driver

from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By
class HomePage(BasePage):
    #HEADER = (By.CSS_SELECTOR,"em.HomeHome")
    #HEADER = (By.ID,"LiHome")
    #HEADER = (By.XPATH,"//*[@id='LiHome']/a/em")
    HEADER = (By.ID,"EditProfile")
    SETTING_ICON = (By.ID,"userlogo")

    def __init__(self,driver):
        super().__init__(driver)

    def get_home_page_title(self, title):
        return self.get_title(title)

    def is_setting_icon_exist(self):
        return self.is_visible(self.SETTING_ICON)

    def get_header_value(self):
        if self.is_visible(self.HEADER):
            return self.get_element_text(self.HEADER)

