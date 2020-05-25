import pytest  # 导入pytest包
import yaml  # 导入yaml包


from testing.calc import Calc  # 导入testing包下的calc.py文件中的Calc类


class TestCalc():  # 定义测试类
    def setup_class(sefl):  # 定义steup_class 方法（类级别）
        sefl.calc = Calc()  # 实例化Calc类
        print("setup_class")

    def teardown_class(self):  # 定义teardown_class 方法（类级别）
        print("teardown_class")

    @pytest.mark.parametrize('a, b, expect', yaml.safe_load(open("data.yaml")))  # 从data.yaml文件中传入列表值赋值给a, b, expect，供test_add_1方法调用
    def test_add_1(self, a, b, expect):  # 定义测试方法，传入a，b，expect数值
        result = self.calc.add(a, b)  # 调用calc.add方法进行计算并赋值给result
        print(f"result={a}+{b}={result}")  # 打印内容
        assert result == expect  # 断言result 等于 expect

    @pytest.mark.parametrize('a, b, expect', yaml.safe_load(open("data1.yaml")))  # 从data1.yaml文件中传入列表值赋值给a, b, expect，供test_div方法调用
    def test_div(self, a, b, expect):  # 定义测试方法，传入a，b，expect数值
        result = self.calc.div(a, b)  # 调用calc.add方法进行计算并赋值给result
        print(f"result={a}/{b}={result}")  # 打印内容
        assert result == expect  # 断言result 等于 expect


if __name__ == '__main__':  # 定义main函数
    pytest.main(['-v', '-s', 'TestCalc'])   # 运行当前测试文件