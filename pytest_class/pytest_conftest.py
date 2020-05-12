"""
场景：
    你与其他测试工程师合作一起开发时，公共模块要在不同文件中，要在大家都访问到的地方
解决：
    conftest.py这个文件进行数据共享，并且他可以放在不同的位置骑着不同的范围共享作用
执行：
    系统执行到参数login是先总本文件中查找是否有这个名字的变量，之后再 conftest.py中找是否有
步骤：
    将登陆模块带@pytest.fixture写在conftest.py
"""
import pytest

# @pytest.fixture()
# def login():
#     print("这是个登录方法")
"""
可作为公共调用的代码块
放在conftest文件中
调用此方法的文件就可以不用导入这个方法，可以自动到同级目录下寻找这个包进行使用
"""

def test_case1(login):
    print("test_case1需要登录")
    pass

def test_case2():
    print("test_case2不需要登录")
    pass

def test_case3(login):
    print("test_case3需要登录")
    pass

if __name__=='__main__':
    pytest.main()

"""结果：
pytest_fixture.py::test_case1 这是个登录方法
PASSED                                     [ 33%]test_case1需要登录

pytest_fixture.py::test_case2 PASSED                                     [ 66%]test_case2不需要登录

pytest_fixture.py::test_case3 这是个登录方法
PASSED                                     [100%]test_case3需要登录
"""