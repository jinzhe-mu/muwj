from decimal import Decimal  # 导入Decimal


class Calc:  # 定义类

    def add(self, a, b):  # 定义方法，传入a，b两个数值
        return float(Decimal(str(a)) + Decimal(str(b)))  # 计算a+b的值并返回，强制转化十进制的浮点型数据

    def div(self, a, b):  # 定义方法，传入a，b两个数值
        return a / b  # 计算a/b的值并返回

