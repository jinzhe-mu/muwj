"""
场景：
    测试方法后销毁清除数据的要如何进行？范围是模块的级别的。类似setupClass
解决：
    通过在同一个模块中加入yield关键字，yield是调用第一次返回结果，第一次执行它下面的语句返回
步骤：
    在@pytest.fixture(scope=module)
在登录的方法中加yield，之后加销毁清除的步骤注意，这种方式没有返回值，如果希望返回使用addfinalizer
"""
import pytest

# 作用域：module是在模块之前执行，模块之后执行
@pytest.fixture(scope="module")
def open():
    print("打开浏览器")
    yield

    print("执行teardown!")
    print("最后关闭浏览器")

def test_search1(open):
    print("test_search1")
    raise NameError

def test_search2(open):
    print("test_search2")
    pass

def test_search3(open):
    print("test_search3")
    pass

if __name__=='__main__':
    pytest.main()

