"""
改造录制的用例：
第一次改造：修改定位方式，将自动生成的相对定位方式修改为绝对定位方式，修改为可阅读的，可维护的定位方式
"""

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy

class TestContact:
    def setup(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "mumu0"
        caps["appPackage"] = "com.tencent.base_api"
        caps["appActivity"] = "launch.WwMainActivity"
        caps["noReset"] = "True"

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(120)

    def teardown(self):
        self.driver.quit()

    def test_addcontact(self):
        # 点击通讯录
        el1 = self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']")
        el1.click()

        #  点击添加成员
        el2 = self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                  'new UiScrollable(new UiSelector().scrollable(true)\
                                  .instance(0)).scrollIntoView(new UiSelector().\
                                  text("添加成员".instance(0));')  # 进行滚动查找“添加成员”
        el2.click()
        #  点击手动输入添加
        el3 = self.driver.find_element(MobileBy.XPATH, "//*[@text='手动输入添加']")
        # 或者使用contains（查找包含后面的内容）
        el3.click()
        #  输入名字
        #  //*[contains(@text,'姓名')]/..//*[contains(@class,'EditText')] 或者用此种定位方式（姓名节点兄弟节点包含可编辑的选项）
        el4 = self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'姓名')]/..//*[@text='必填']")
        el4.send_keys("a2")
        #  选择性别
        gender = '女'
        #  点击性别
        el5 = self.driver.find_element(MobileBy.XPATH, "//*[@text='男']")
        el5.click()
        #  选择性别
        self.driver.find_element(MobileBy.XPATH, f"//*[@text='{gender}']").click()
        #  填写手机号
        #  查找到包含手机的框并且class属性为可编辑的
        el7 = self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'手机')and contains(@class,'EditText')]")
        el7.send_keys("13500000002")
        #  点击保存
        el8 = self.driver.find_element(MobileBy.XPATH, "//*[@text='保存']")
        el8.click()
        print(self.driver.page_source)
        self.driver.find_element(MobileBy.XPATH, "[//*@text='添加成员']")