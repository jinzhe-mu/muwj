import os

from selenium import webdriver
import time
import json
from selenium.webdriver.common.by import By


class TestCookie:  # 定义一个类
    def setup(self):  # 进行初始化
        self.driver = webdriver.Chrome()  # 浏览器进行实例化，使用webdriverd的Chrome方法打开Google浏览器
        self.driver.get("https://work.weixin.qq.com/")  # 获取企业微信的url

    def test_get_cookie(self):  # 定义一个方法
        """
        获取cookie
        :return:
        """
        time.sleep(20)  # 直接等待20秒,进行扫码登录
        cookie = self.driver.get_cookies()  # 获取浏览器的cookie
        with open("cookie.json", "w") as f:
            #  将获取到的cookie存入到一个json文件中
            json.dump(obj=cookie, fp=f)

    def test_cookie_login(self):
        # 获取cookie.json文件的内容
        cookies = json.load(open("./cookie.json"))
        # 循环cookies列表，将所有cookies添加到浏览器中
        for cookie in cookies:
            # 遍历列表发现有expiry,直接移除
            if "expiry" in cookie:
                cookie.pop("expiry")  # 传入key值
            # 添加一个cookies
            self.driver.add_cookie(cookie)
        time.sleep(2)  # 直接等待2秒
        # 获取企业微信通讯录的url
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
        time.sleep(2)  # 直接等待2秒
        # 定位到导入通讯录按钮并点击
        self.driver.find_element(By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(2)").click()
        time.sleep(2)  # 直接等待2秒
        # 获取上传ID并点击
        # dir 获取的就是当前文件的绝对路径
        dir = os.path.dirname(__file__)
        # 上传文件，上传文件可以使用send_keys。前提元素的标签必须为input。
        # send_keys里面放的文件，必须是绝对路径
        time.sleep(2)  # 直接等待2秒
        #  获取上传文件按钮位置并进行导入
        self.driver.find_element(By.ID, "js_upload_file_input").send_keys(dir+"/data1.xls")
        # 取出系统内部已导入的文件的名称
        ele_name = self.driver.find_element(By.ID, "upload_file_name").text
        # 断言上传文件的名称
        assert ele_name == "data1.xls"


