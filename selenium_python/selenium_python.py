from selenium import  webdriver

class SeleniumPython:


    def __init__(self):
        pass

    def go_baidu(self):
        """
        1、打开百度
        2、输入搜索词
        3、点击搜索
        将原始定位和输入的数据使用Excel管理
        :return:
        """
        # 实例化driver
        driver = webdriver