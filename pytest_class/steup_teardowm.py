import pytest

# 模块级别的，在执行整个py文件前会先调用setup_module，优先级最高
def setup_module():
    print("这是个 setup_module 方法（模块级别）")

# 模块级别的，在py文件所有模块执行结束之后调用teardown_module，最后执行
def teardown_module():
    print("这是个 teardown_module 方法（模块级别）")

# 函数级别的，类外面的，在类外面的方法执行之前执行setup_function
def setup_function():
    print("这是个 setup_funftion 方法（函数级别）")

# 函数级别的，外面的方法执行完之后执行teardown_function
def teardown_function():
    print("这是个 teardown_function 方法（函数级别）")

def test_login():
    print("这是一个外部的函数")

class TestDemo():

# 类级别，在类执行之前执行setup_class
    def setup_class(self):
        print("这是个 steup_class 方法（类级别）")

 # 在类执行完之后执行teardown_class
    def teardown_class(self):
        print("这是个 teardown_class 方法（类级别）")

# 方法级别，执行类里面的每个方法之前都要执行一次，优先级比tetup高
    def setup_method(self):
        print("这是个setup_method 方法（方法级别）")

# 执行类里面的每个方法之后都要执行一次，在teardown之后执行
    def teardown_method(self):
        print("这是个 teardown_method 方法（方法级别）")

#类里面的，运用在调用方法的前后，即：执行类里面的每个方法之前都要执行一次，优先级比tetup_mothod低
    def setup(self):
        print("这是个setup 方法")

# 执行类里面的每个方法之后都要执行一次，在teardown_method之后前执行
    def teardown(self):
        print("这是个teardown 方法")

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

if __name__=='__main__':
    pytest.main("-v -s")

"""执行结果顺序：
steup_teardowm.py::test_login 这是个 setup_module 方法（模块级别）
这是个 setup_funftion 方法（函数级别）
PASSED                                     [ 25%]这是一个外部的函数
这是个 teardown_function 方法（函数级别）

steup_teardowm.py::TestDemo::test_one 这是个 steup_class 方法（类级别）
这是个setup_method 方法（方法级别）
这是个setup 方法
PASSED                             [ 50%]开始执行 test_one 方法
这是个teardown 方法
这是个 teardown_method 方法（方法级别）

steup_teardowm.py::TestDemo::test_two 这是个setup_method 方法（方法级别）
这是个setup 方法
PASSED                             [ 75%]开始执行 test_two 方法
这是个teardown 方法
这是个 teardown_method 方法（方法级别）

steup_teardowm.py::TestDemo::test_three 这是个setup_method 方法（方法级别）
这是个setup 方法
PASSED                           [100%]开始执行 test_three 方法
这是个teardown 方法
这是个 teardown_method 方法（方法级别）
这是个 teardown_class 方法（类级别）
这是个 teardown_module 方法（模块级别）
"""