"""场景：
--用例1需要先登录
--用例2不需要登录
--用例3需要登录
这种场景无法用setup与teardown实现
用法：
    在方法前面加@pytest.fixture()
步骤：
    导入pytest
    在登录的函数上面加@pytest.fixture()
    在要使用的测试方法中传入（登录函数名称），就先登录
    不传入的就不登录直接咨询测试方法
"""
import pytest

@pytest.fixture()
def login():
    print("这是个登录方法")



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