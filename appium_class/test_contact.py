# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
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
        # el1 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.RelativeLayout[2]/android.widget.TextView")
        # el1 = driver.find_element_by_xpath("//*[@text='通讯录']")
        el1 = self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']")
        el1.click()

        #  点击添加成员
        #el2 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.ListView/android.widget.RelativeLayout[3]/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.TextView")
        # el2 = driver.find_element_by_xpath("//*[@text='添加成员']")
        # el2 = driver.find_element(MobileBy.XPATH, "//*[@text='添加成员']")  # 只能在当前页面进行查找，需要滚动查找
        # el2 = self.driver.find_element(MobileBy.XPATH, "//*[@text='添加成员']")
        el2 = self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                  'new UiScrollable(new UiSelector().scrollable(true)\
                                  .instance(0)).scrollIntoView(new UiSelector().\
                                  text("添加成员".instance(0));')  # 进行滚动查找“添加成员”
        el2.click()

        #  点击手动输入添加
        # el3 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.RelativeLayout[2]/android.widget.LinearLayout/android.widget.TextView[1]")
        # el3 = driver.find_element_by_xpath("//*[@text='手动输入添加']")  # //*[contains(@text,'输入添加')]
        # 或者使用contains（查找包含后面的内容）
        el3 = self.driver.find_element(MobileBy.XPATH, "//*[@text='手动输入添加']")
        el3.click()

        #  输入名字
        # el4 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout[1]/android.widget.RelativeLayout/android.widget.EditText")
        # el4 = driver.find_element_by_xpath("//*[contains(@text,'姓名')]/..//*[@text='必填']")  # 查找到姓名节点下的兄弟节点text为必填的选项
        #  //*[contains(@text,'姓名')]/..//*[contains(@class,'EditText')] 或者用此种定位方式（姓名节点兄弟节点包含可编辑的选项）
        el4 = self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'姓名')]/..//*[@text='必填']")
        el4.send_keys("a2")

        #  选择性别
        gender = '女'
        #  点击性别
        # el5 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout[2]/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.TextView")
        # el5 = driver.find_element_by_xpath("//*[@text='男']")  # 因为默认性别为男，直接查找此元素进行点击
        el5 = self.driver.find_element(MobileBy.XPATH, "//*[@text='男']")
        el5.click()

        #  选择性别
        # if gender == '女'
        #     # el6 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ListView/android.widget.RelativeLayout[2]/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.TextView")
        #     driver.find_element_by_xpath("//*[@text='女']").click()
        #
        # else:
        #     driver.find_element_by_xpath("//*[@text='男']").click()
        # driver.find_element_by_xpath(f"//*[@text='{gender}']").click()
        self.driver.find_element(MobileBy.XPATH, f"//*[@text='{gender}']").click()

        #  填写手机号
        # el7 = driver.find_element_by_id("com.tencent.base_api:id/er6")
        # el7 = self.driver.find_element_by_xpath("//*[contains(@text,'手机')and contains(@class,'EditText')]")
        #  查找到包含手机的框并且class属性为可编辑的
        el7 = self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'手机')and contains(@class,'EditText')]")
        el7.send_keys("13500000002")

        #  点击保存
        # el8 = driver.find_element_by_id("com.tencent.base_api:id/gvy")
        # el8 = driver.find_element_by_xpath("//*[@text='保存']")
        el8 = self.driver.find_element(MobileBy.XPATH, "//*[@text='保存']")
        el8.click()

        print(self.driver.page_source)
        self.driver.find_element(MobileBy.XPATH, "[//*@text='添加成员']")

