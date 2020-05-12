import pytest

def test_a():
    print("test_a")

class TestDemo1():
    def test_one(self):
        print("开始执行 test_one 方法")
        x = 'this'
        assert 'h' in x

    def test_two(self):
        print("开始执行 test_two 方法")
        x = 'hello'
        assert 'e' in x

    def test_three(self):
        print("开始执行 test_three 方法")
        a = 'hello'
        b = 'hello world'
        assert a in b

if __name__ == '__main__':
    # 两种写法二选一
    pytest.main("-v -x TestDemo1")
    pytest.main(['-v', '-x', 'TestDemo1'])
    # 执行所有测试用例，在main里面不加参数

