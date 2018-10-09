import allure

import Page

from Base.base import Base


class PageLogin(Base):
    #点击我
    @allure.step("点击我")
    def page_click_me(self):
        self.base_XPATH(Page.me_btn).click()
    #点已有账号去登录
    @allure.step("点击有账号去登录")
    def page_click_info(self):
        self.base_XPATH(Page.user).click()
    #输入账号
    @allure.step("输入账号")
    def page_input_user(self,username):
        self.base_input(Page.user_name,username)
    #输入密码
    @allure.step("输入密码")
    def page_input_pwd(self,password):
        self.base_input(Page.user_pwd,password)
    # 点击登录按钮
    @allure.step("点击登录按钮")
    def page_click_login_btn(self):
        self.base_click(Page.login_btn)

    #点击设置按钮
    @allure.step("点击设置按钮")
    def page_click_setting(self):
        self.base_click(Page.setting_btn)
    # 消息推送》修改密码
    @allure.step("滑动：消息推送》修改密码")
    def page_drag_and_drop(self):
        el1=self.base_XPATH(Page.msg_send)
        el2=self.base_XPATH(Page.update_pwd)
        self.base_drag_and_drop(el1,el2)
    # 点击退出
    @allure.step("点击退出")
    def page_click_exit(self):
        self.base_XPATH(Page.exit_btn).click()
    # 点击确认退出
    @allure.step("点击确认退出")
    def page_click_exit_ok(self):
        self.base_XPATH(Page.exit_ok).click()
    # 登录步骤大封装：
    def page_login(self,username,password):
        # 点击我
        self.page_click_me()
        # 点已有账号去登录
        self.page_click_info()
        # 输入账号
        self.page_input_user(username)
        # 输入密码
        self.page_input_pwd(password)
        # 点击登录按钮
        self.page_click_login_btn()
    #退出登录步骤封装
    def page_login_logout(self):
        # 点击设置按钮
        self.page_click_setting()
        # 消息推送》修改密码
        self.page_drag_and_drop()
        # 点击退出
        self.page_click_exit()
        # 点击确认退出
        self.page_click_exit_ok()
    #获取昵称方法
    @allure.step("获取昵称方法")
    def page_get_nickname(self):
        return self.base_get_test(Page.me_nickname)