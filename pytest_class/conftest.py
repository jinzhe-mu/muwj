"""
当需要公共调用的代码块时，可以共享一个代码块
放在conftest文件中
调用此方法的文件就可以不用导入这个方法，可以自动到同级目录下寻找这个包进行使用
conftest.py配置需要注意：
* conftest文件名是不能换的
* conftest.py与运行的用例要在同一个package下，并且有__int__.py文件
* 不需要inport导入conftest.py，pytest用例会自动查找
* 全局的配置和前期工作都可以写在这里，放在某个包下，就是这个包数据共享的地方
"""

import pytest

# 不带参数的fixture默认参数为 scope=function
@pytest.fixture()
def login():
    print("这是个登录方法")

def pytest_configure(config):
    marker_list = ["search", "login"]  # 标签名集合
    for markers in marker_list:
        config.addinivalue_line(
            "markers", markers
        )