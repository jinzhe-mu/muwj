import pytest
import yaml


from testing.calc import Calc



class TestCalc():
    def setup_class(sefl):
        sefl.calc = Calc()
        print("setup_class")

    def teardown_class(self):
        print("teardown_class")

    @pytest.mark.parametrize('a, b, expect', yaml.safe_load(open("data.yaml")))
    def test_add_1(self, a, b, expect):
        result = self.calc.add(a, b)
        print(f"result={a}+{b}={result}")
        assert result == expect

    @pytest.mark.parametrize('a, b, expect', yaml.safe_load(open("data1.yaml")))
    def test_div(self, a, b, expect):
        result = self.calc.div(a, b)
        print(f"result={a}/{b}={result}")
        assert result == expect


if __name__ == '__main__':
    pytest.main(['-v', '-s', 'TestCalc'])