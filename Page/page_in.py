from Page.page_address import PageAddress
from Page.page_login import PageLogin
class PageIn():
    def __init__(self,driver):
        self.driver=driver
    def page_get_login(self):
        return PageLogin(self.driver)
    def page_get_setting(self):
        return PageAddress(self.driver)