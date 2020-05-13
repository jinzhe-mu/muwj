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

class TestDemo2():
    def test_one2(self):
        print("开始执行 test_one2 方法")
        x = 'this'
        assert 'h' in x

    def test_two2(self):
        print("开始执行 test_two2 方法")
        x = 'hello'
        assert 'e' in x

if __name__ == '__main__':
    # 两种写法二选一
    # pytest.main("-v -x TestDemo1")
    # pytest.main(['-v', '-s', 'TestDemo1'])
    # 最后这个需要切换右上角执行变量，参考：https://home.testing-studio.com/t/topic/1173
    # 可以指定要执行的类
    pytest.main(['-v', '-s', 'testpytest_demo1.py::TestDemo1'])


