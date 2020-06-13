# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy

class TestSendMassage:
    def setup(self):
        caps = {}
        caps["platformName"] = "android"  # 测试设备类型
        caps["deviceName"] = "mumu0"  # 测试设备名
        caps["appPackage"] = "com.tencent.base_api"  # 初始登录APP
        caps["appActivity"] = "launch.WwMainActivity"  # 初始登录界面
        caps["noReset"] = "True"  # 不清空登录信息

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)  # 打开APP
        self.driver.implicitly_wait(120)  # 隐式等待

    def teardown(self):
        #  关闭应用回收资源
        self.driver.quit()

    @pytest.mark.parametrize("name , news", [
        ('a1', '测试code1'),
        ('a2', '测试code2'),
        ('a3', '测试code3'),
        ('a4', '测试code4'),
    ])
    def test_sendmassage(self, name, news):
        #  点击“通讯录”
        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        #  点击查找放大镜
        self.driver.find_element(MobileBy.ID, "com.tencent.base_api:id/gw1").click()
        #  搜索框输入查找内容“a1”
        el4 = self.driver.find_element(MobileBy.XPATH, "//*[@text='搜索']")
        el4.send_keys(name)
        #  点击查找出的成员
        self.driver.find_element(MobileBy.ID, "com.tencent.base_api:id/d37").click()
        #  点击发送消息按钮
        self.driver.find_element(MobileBy.XPATH, "//*[@text='发消息']").click()
        #  发送消息宽内输入要发送的内容
        el8 = self.driver.find_element(MobileBy.ID, "com.tencent.base_api:id/dxy")
        el8.send_keys(news)
        #  点击发送按钮
        self.driver.find_element(MobileBy.XPATH, "//*[@text='发送']").click()
        #  点击返回按钮退出发送消息界面
        self.driver.find_element(MobileBy.ID, "com.tencent.base_api:id/gvg").click()





