"""
场景：
    测试离不开数据，为了数据灵活，一般数据都是通过参数传递
解决：
    fixture通过固定参数request传递
步骤：
    在fixture中增加@pytest.fixture(params=[1,2,3,'linda'])在方法参数写request
"""
import pytest

# 将open方法自动运用到每一条测试用例上
@pytest.fixture(params=[1, 2, 3, 'linda'])
def test_data(request):
    return request.param

def test_one(test_data):
    print('/ntest data: %s' % test_data)


if __name__=='__main__':
    pytest.main()
