from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class Base():
    def __init__(self, driver):
        self.driver = driver

    def base_find_element(self, loc, timeout=30, poll_frequency=0.5):
        return WebDriverWait(self.driver, timeout, poll_frequency).until(lambda x: x.find_element(*loc))
    def base_find_elements(self, loc, timeout=30, poll_frequency=0.5):
        return WebDriverWait(self.driver, timeout, poll_frequency).until(lambda x: x.find_elements(*loc))
    # 点击
    def base_click(self, loc):
        self.base_find_element(loc).click()

    # 输入
    def base_input(self, loc, text):
        el=self.base_find_element(loc)
        el.clear()
        el.send_keys(text)

    # 截图
    def base_getImage(self):
        Path = "./Image/faild.png"
        self.driver.get_screenshot_as_file(Path)

    # 获取toast
    def base_get_toast(self, message):

        return self.base_XPATH(message).text

    # self.base_find_element((By.XPATH,"//*[contains(@text,'"+message+"')]"))
    # xpath文本模糊封装
    def base_XPATH(self, text):
        # text传入要查找的文本
        loc = By.XPATH, "//*[contains(@text,'"+text+"')]"
        return self.base_find_element(loc)

    # 滑动封装
    def base_drag_and_drop(self, el1, el2):
        self.driver.drag_and_drop(el1, el2)
    # 获取文本的方法
    def base_get_test(self,loc):
        return self.base_find_element(loc).text

    #点击文本的元素
    def base_xpath_click(self,text):
        self.base_XPATH(text).click()
    #封装传入文本查找多元素的方法
    def base_XPATHS(self, text):
        # text传入要查找的文本
        loc = By.XPATH, "//*[contains(@text,'"+text+"')]"
        return self.base_find_elements(loc)
    #通过下标点击元素方法（base_find_elements得到的是多元素的列表）
    def base_click_elements(self,elements,num=0):
        elements[num].click()

