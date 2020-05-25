"""复用浏览器
前置条件1：关闭所有google浏览器
前置条件2：找到Chrome的启动路径
右键点击Google浏览器图标–>点击属性–>点击快捷方式–>复制目标里面\chrome.exe前的所有内容
前置条件3：配置环境变量(PATH)
前置条件4：在cmd中执行chrome --remote-debugging-port=9222（执行成功的结果是打开google浏览器输入http://localhost:9222/ 成功即可）
"""

from selenium import webdriver  # 导入webdriver
#  小写的chrome
from selenium.webdriver.chrome.options import Options

class TestLogin:  # 定义一个类
    def test_debug_login(self):  # 定义一个方法
        option = Options()  # 实例化Options类
        option.debugger_address = "localhost:9222"  # 调用debugger_address，将url"localhost:9222"赋值给类中的属性debugger_address
        driver = webdriver.Chrome(options=option)  # 浏览器进行实例化，使用webdriverd的Chrome方法打开Google浏览器，并打开传入参数中的url
        driver.get("https://work.weixin.qq.com/wework_admin/frame")  # 打开浏览器中的企业微信地址