from selenium.webdriver.common.by import By

"""
    以下为：百年奥莱APP登录数据
"""
# 点击我
me_btn = '我'
# 点击已有账户，去登录
user = '已有账号'
# 输入用户名
user_name = By.ID, "com.yunmall.lc:id/logon_account_textview"
# 输入密码
user_pwd = By.ID, "com.yunmall.lc:id/logon_password_textview"
# 点击登录按钮
login_btn = By.ID, "com.yunmall.lc:id/logon_button"
# 点击设置按钮
setting_btn = By.ID, "com.yunmall.lc:id/ymtitlebar_left_btn_image"
"""消息推送  -->  滑到--->修改密码"""
# 消息推送
msg_send ='消息推送'
# 修改密码
update_pwd ='修改密码'
# 点击退出按钮
exit_btn = '退出'
# 点击确认按钮
exit_ok = '确认'
# 昵称
me_nickname = By.ID, "com.yunmall.lc:id/tv_user_nikename"
"""
    以下为：百年奥莱地址数据
"""
# 点击地址管理
# address_manage = By.ID, "com.yunmall.lc:id/setting_address_manage"
address_manage ="地址管理"
# 点击新增地址
address_new_btn = By.ID, "com.yunmall.lc:id/address_add_new_btn"
# 点击收件人文本框
address_receipt_name = By.ID, "com.yunmall.lc:id/address_receipt_name"
# 点击电话文本框
address_add_phone = By.ID, "com.yunmall.lc:id/address_add_phone"
# 点击地区文本框
address_area = By.ID, "com.yunmall.lc:id/address_province"
# 点击详细地址文本框
address_detail_addr_info = By.ID, "com.yunmall.lc:id/address_detail_addr_info"
# 点击邮箱文本框
address_post_code = By.ID, "com.yunmall.lc:id/address_post_code"
# 点击默认地址单选框
address_default = By.ID, "com.yunmall.lc:id/address_default"
# 点击保存
address_save = By.ID, "com.yunmall.lc:id/button_send"
# 获取收件人和电话
address_receipt_and_phone=By.ID,"com.yunmall.lc:id/receipt_name"
"""地址修改数据"""
#获取编辑
address_edit_btn="编辑"
#获取修改
address_xiugai_btn="修改"
#点击保存
address_baocun="保存"
#确认删除
address_delete_ok=By.ID,"com.yunmall.lc:id/ymdialog_left_button"