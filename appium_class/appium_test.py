from appium import webdriver
desired_caps={}
desired_caps['platformName'] = 'Android'
# desired_caps['platformVersion'] = '6.0'
desired_caps['deviceName'] = '127.0.0.1:7555'
desired_caps['appPackage'] = 'com.tencent.base_api'
desired_caps['appActivity'] = 'launch.WwMainActivity'
desired_caps['noReset'] = 'True'
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

# driver.quit()