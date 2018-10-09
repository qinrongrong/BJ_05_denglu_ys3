import os, sys

sys.path.append(os.getcwd())
from Base.read_yaml import ReadYaml
import allure
import pytest
from Page.page_login import PageLogin
from Base.get_driver import get_driver


def get_data():
    datas = ReadYaml("login.yaml").read_yaml()
    print(datas)
    arrs = []
    for data in datas.values():
        arrs.append((data.get("username"), data.get("password"), data.get("expect"), data.get("toast_expect")))
    return arrs


class TestLogin():
    def setup_class(self):
        self.login = PageLogin(get_driver())
        self.login.page_click_me()
        self.login.page_click_info()

    def teardown_class(self):
        self.login.driver.quit()

    @pytest.mark.parametrize("username,password,expect,toast_expect", get_data())
    def test_login(self, username, password, expect, toast_expect):
        if expect:
            try:
                self.login.page_input_user(username)
                self.login.page_input_pwd(password)
                self.login.page_click_login_btn()
                assert expect in self.login.page_get_nickname()
                allure.attach("登录状态：","登陆成功")
                self.login.page_login_logout()
                self.login.page_click_me()
                self.login.page_click_info()
            except:
                #     截图
                self.login.base_getImage()
                with open("./Image/faild.png", "rb") as f:
                    allure.attach("失败描述", f.read(), allure.attach_type.PNG)
                raise
        else:
            try:
                self.login.page_input_user(username)
                self.login.page_input_pwd(password)
                self.login.page_click_login_btn()
                assert toast_expect in self.login.base_get_toast(toast_expect)
                allure.attach("登录状态：", "逆向断言成功")
            except:
                # 截图
                self.login.base_getImage()
                with open("./Image/faild.png", "rb") as f:
                    allure.attach("失败描述", f.read(), allure.attach_type.PNG)
                raise
