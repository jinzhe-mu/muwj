"""
写一个Bicycle（自信车）类，有run(骑行)方法，
调用时显示骑行里程KM（骑行里程为传入的数字）；
再写一个电动自行车EBicycle，添加电池电量valume属性通过，
参数传入，同时有两个方法；
1、fill_charge(vol)用来充电，vol为电量
2、rum(km)方法用来骑行，没骑行10km消耗电量为1度，
但电量消耗近时调用Bicycle方法骑行，通过传入的骑行里程数，显示骑行结果
"""

class Bicycle: # 定义一个Bicycle类

    def run(self, km):  # 定义一个run方法,定义的同时传入一个km参数
        print("骑行的里程数为{}".format(km)) # 显示骑行里程

class EBicycle(Bicycle):  # EBicycle继承Bicycle类的属性
    def __init__(self, volume):  # 类在初始化
        self.valume = volume  # 实例变量

    def get_valume(self):
        print("当前电量为", self.valume)

    def fill_charge(self, vol):
        print("充电的电量为", self.vol)

    def run(self, km):
        e_miles = self.valume*10  # 电瓶车的最大里程
        miles = km - e_miles  # 假如电瓶有10度电，我们支持的最大里程数就是10*10=100
        if miles<=0:
            print("电瓶车骑了", km)
        else:
            ##因为子类中有一个rum，把父类的run覆盖掉了
            # self.run() 此调用的是子类的rum
            ##此调用的是父类的run
            print("电瓶车骑了", e_miles)
            super().run(miles)  # 应该传入的参数是除了电瓶车之外的里程数

# 在类的初始化的时候，给init中定义的参数传参(只给init传）
bike = EBicycle(10)
bike.run(120)