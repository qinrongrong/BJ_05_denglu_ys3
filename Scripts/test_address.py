import os,sys
sys.path.append(os.getcwd())
import allure
import pytest
from Base.read_yaml import ReadYaml
from Page.page_in import PageIn
from Base.get_driver import get_driver

def get_data(text_type):
    datas = ReadYaml("address.yaml").read_yaml()
    arrs = []
    if text_type == "add":
        for data in datas.get("add_address").values():
            arrs.append((data.get("name"), data.get("phone"), data.get("sheng"), data.get("shi"), data.get("qu"),
                         data.get("address"), data.get("youbian")))
        return arrs
    elif text_type == "update":
        for data in datas.get("update_address").values():
            arrs.append((data.get("name"), data.get("phone"), data.get("sheng"), data.get("shi"), data.get("qu"),
                         data.get("address"), data.get("youbian"), data.get("toast")))
        return arrs
class TestAddress02():
    def setup_class(self):
        self.page=PageIn(get_driver())
        self.page.page_get_login().page_login("13805489414","123456")
        #点击设置
        self.page.page_get_login().page_click_setting()
        #点击地址管理
        self.address=self.page.page_get_setting()
        self.address.page_address_manage()
    def teardown_class(self):
        self.page.driver.quit()
    """新增"""
    @pytest.mark.run(order=1)
    @pytest.mark.parametrize("name,phone,sheng,shi,qu,address,youbian", get_data("add"))
    def test02_address(self,name,phone,sheng,shi,qu,address,youbian):
        addr=self.address
        #点击新增地址
        addr.page_new_address()
        #输入收件人
        addr.page_receipt_name(name)
        #输入手机号
        addr.page_add_phone(phone)
        #选择所在区域
        addr.page_address_area(sheng,shi,qu)
        #输入详细地址
        addr.page_detail_addr_info(address)
        #输入邮编
        addr.page_address_post_code(youbian)
        #设置默认地址
        addr.page_address_default()
        #点击保存
        addr.page_address_save()
    #断言，是否新增成功
        try:
            # print("获取新增地址联系人电话",addr.page_get_recipit_and_phone())
            # assert name in addr.page_get_recipit_and_phone()
            """第二种实现断言方法：所有收件和电话"""
            #组装字符串
            name_phone=name+"  "+phone
            assert name_phone in addr.page_get_elements_text()
        except:
            self.login.base_getImage()
            with open("./Image/faild.png", "rb") as f:
                allure.attach("失败描述", f.read(), allure.attach_type.PNG)
            raise
    """更新地址"""
    @pytest.mark.run(order=2)
    @pytest.mark.parametrize("name,phone,sheng,shi,qu,address,youbian,toast",get_data("update"))
    def test_update_address(self,name,phone,sheng,shi,qu,address,youbian,toast):
        addr = self.address
        #点击编辑
        self.address.page_click_edit_btn()
        #点击修改
        self.address.page_click_xiugai()
        #点击信息
        #输入收件人
        addr.page_receipt_name(name)
        #输入手机号
        addr.page_add_phone(phone)
        #选择所在区域
        addr.page_address_area(sheng,shi,qu)
        #输入详细地址
        addr.page_detail_addr_info(address)
        addr.page_address_post_code(youbian)
        #点击保存
        addr.page_click_baocun_btn()
        try:
            name_phone=name+"  "+phone
            assert name_phone in addr.page_get_elements_text()
            #第二种toast
            assert toast in self.address.base_get_toast(toast)
        except:
            self.login.base_getImage()
            with open("./Image/faild.png", "rb") as f:
                allure.attach("失败描述", f.read(), allure.attach_type.PNG)
            raise

    """"删除"""
    @pytest.mark.run(order=3)
    def test_delete_address(self):
        #删除操作
        self.address.page_delete_address()
        #断言
        try:
            assert self.address.page_is_delete_ok()
        except:
            self.login.base_getImage()
            with open("./Image/faild.png", "rb") as f:
                allure.attach("失败描述", f.read(), allure.attach_type.PNG)
            raise






