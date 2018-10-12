import Page
from Base.base import Base

"""地址封装"""
class PageAddress(Base):
    def page_address_manage(self):
        self.base_xpath_click(Page.address_manage)
    # 点击新增地址
    def page_new_address(self):
        self.base_click(Page.address_new_btn)
     # 输入收件人
    def page_receipt_name(self,name):
        self.base_input(Page.address_receipt_name,name)
    #输入电话号
    def page_add_phone(self, telphone):
        self.base_input(Page.address_add_phone,telphone)
    def page_address_area(self, sheng,shi,qu):
        #点击所在地区
        self.base_click(Page.address_area)
        # 点击所在省
        self.base_xpath_click(sheng)
        # 点击所在市
        self.base_xpath_click(shi)
        # 点击所在区
        self.base_xpath_click(qu)
    # 输入详细地址
    def page_detail_addr_info(self,address):
        self.base_input(Page.address_detail_addr_info,address)
    # 设置默认地址
    def page_address_default(self):
        self.base_click(Page.address_default)
    # 点击保存
    def page_address_save(self):
        self.base_click(Page.address_save)
    # 输入邮编
    def page_address_post_code(self,postcode):
        self.base_input(Page.address_post_code,postcode)
    #获取收件人和电话
    def page_get_recipit_and_phone(self):
        return self.base_get_test(Page.address_receipt_and_phone)
    #获取一组元素的文本
    def page_get_elements_text(self):
        #获取地址列表（收件人+电话）所有元素
        elements=self.base_find_elements(Page.address_receipt_and_phone)
        #返回每个元素的文本
        return [i.text for i in elements]
    #点击编辑
    def page_click_edit_btn(self):
        self.base_xpath_click(Page.address_edit_btn)
    #点击保存
    def page_click_baocun_btn(self):
        self.base_xpath_click(Page.address_baocun)
    #点击修改
    def page_click_xiugai(self):
        elements=self.base_XPATHS(Page.address_xiugai_btn)
        #点击第一个修改
        self.base_click_elements(elements)
    #删除地址
    def page_delete_address(self,text="删除"):
        eles=self.base_find_elements(Page.address_receipt_and_phone)
        for i in range(len(eles)):
            # 点击编辑
            self.page_click_edit_btn()
            elements=self.base_XPATHS(text)
            self.base_click_elements(elements)
            self.base_click(Page.address_delete_ok)
    #确认是否删除
    def page_is_delete_ok(self):
        try:
            self.base_find_elements(Page.address_receipt_and_phone,timeout=3)
            return False
        except:
            return True





