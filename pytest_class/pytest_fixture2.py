"""
场景：
    不想原测试方法有任何改动，或全部都自动实现自动应用，没特例，
    也都不需要返回值时可以选择自动应用
解决：
    使用fixture中参数autouse=True
步骤：
    在方法上面加@pytest.fixture(autouse=True)
    在测试方法上加@pytest.mark.usefixtures("start")
"""
import pytest

# 将open方法自动运用到每一条测试用例上  
@pytest.fixture(autouse=True)
def open():
    print("打开浏览器")
    yield

    print("执行teardown!")
    print("最后关闭浏览器")

def test_search1():
    print("test_search1")
    raise NameError
    pass

def test_search2():
    print("test_search2")
    pass

def test_search3():
    print("test_search3")
    pass

if __name__=='__main__':
    pytest.main()
