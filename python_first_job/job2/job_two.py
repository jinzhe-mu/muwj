"""
作业2
用类和面向对象的思想，“描述”生活中任意接触到的东西（比如动物、小说里面的人物，不做限制，随意发挥），数量为5个
"""
###一、
#  定义一个Cat的类
class Cat:
    colour = "白色"
    age = "三岁"

    def vioce(self):
        print("喵喵喵~~~")

    def function1(self):
        print("抓老鼠")

my_cat = Cat()
print("我家的猫是", my_cat.colour, my_cat.age)
my_cat.vioce()
my_cat.function1()

###二、
# 创建类Tvxq
class Tvxq:
    number = 5  # 实例化变量
    __name = "Tong Vfang Shin Ki"  # 定义一个私有属性，私有变量

    def voice(self):  # 定义一个voice方法
        print("name is", self.__name)  # 在方法中调用私有变量__name
        print("singing is hero and Micky")  # 调用此方法时打印内容

    def dance(self):  # 定义一个dance方法
        print("dancing is U-Know and Xiah ")  # 调用此方法时打印内容

    def rapper(self):  # 定义一个Rapper方法
        print("Max is the rapper")  # 调用此方法时打印内容

tvxq = Tvxq()  # 实例化类Tvxq
tvxq.voice()  # 调用voice方法
tvxq.rapper()  # 调用rapper方法

###三、
#定义一个类Flower
class Flower:
    flower_name1 = "玫瑰"  # 实例化变量
    flower_name2 = "月季"
    flower_name3 = "尤加利"

    def dislike1(self):  # 定义一个dislike1方法
        print("但她不喜欢", self.flower_name3)  # 在方法中调用变量flower_name3

    def dislike2(self):  # 定义一个dislike2方法
        print("但她不喜欢", self.flower_name1)  # 在方法中调用变量flower_name1

    def xiao_mei(self):  # 定义一个xiao_mei方法
        print("小魅喜欢", self.flower_name1)  # 在方法中调用变量flower_name1
        self.dislike1()  # 调用dislike1方法

    def mu(self):  # 定义一个mu方法
        print("沐喜欢", self.flower_name2)  # 在方法中调用变量flower_name2
        self.dislike2()  # 调用dislike2方法

flower=Flower()  # 实例化类Flower
flower.xiao_mei()  # 调用xiao_mei方法
flower.mu()  # 调用mu方法

###四、
# 创建类Interest
class Interest:
    curriculum1 = "舞蹈课"  # 实例化变量
    curriculum2 = "英语课"
    curriculum3 = "体育课"

    def class_one(self):  # 定义一个class_one方法
        print("周四一班有", self.curriculum2, "没有", self.curriculum1)  # 在方法中调用变量curriculum1\curriculum2

    def class_two(self):  # 定义一个class_two方法
        print("周四二班有", self.curriculum1, "没有", self.curriculum3)  # 在方法中调用变量curriculum1\curriculum3

interest = Interest()  # 实例化类
interest.class_one()  # 调用class_one方法

xiao_ming = Interest()  # 实例化类
print("小明是二班的")  #  打印实例化类的特征
xiao_ming.class_two()  # 调用class_two方法


###五、
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