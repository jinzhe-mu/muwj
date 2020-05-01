# 定义一个类Park
class Park:
    flower1 = "玫瑰、月季、荷花、桃花、菊花..."  # 实例化变量
    animal2 = "狮子、老虎、猴子、丹顶鹤、孔雀..."

    def flower(self):  # 定义一个flower方法
        print("公园有各种各样的花朵", self.flower1)  # 在方法中调用变量self.flower1并打印

    def animal(self):  # 定义一个animal方法
        print("公园有各种各样的动物", self.animal2)  # 在方法中调用变量self.animal2并打印

park=Park()  # 实例化类
park.animal()  #调用animal方法
park.flower()  #调用flower方法