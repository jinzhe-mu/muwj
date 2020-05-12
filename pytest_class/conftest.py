"""
当需要公共调用的代码块时，可以共享一个代码块
放在conftest文件中
调用此方法的文件就可以不用导入这个方法，可以自动到同级目录下寻找这个包进行使用
"""

import pytest

@pytest.fixture()
def login():
    print("这是个登录方法")

def pytest_configure(config):
    marker_list = ["search", "login"]  # 标签名集合
    for markers in marker_list:
        config.addinivalue_line(
            "markers", markers
        )