class Drawing:  # 创建房子类
    area = 100  # 类变量面积
    style = "North"  # 类变量风格
    __style2 = "China Style"  # 定义一个私有属性，私有变量

    def sleep(self):  # 定义房子的公共功能sleep
        print(self.__style2)  #  私有变量可以在方法中进行调用
        print("房子可以用来睡觉")  # 打印

    def cook(self):  # 定义房子的公共功能cook
        print("房子还可以用来做饭") #  打印

    def __sleepat_room(self):  # 定义房子的私有属性sleepat_room
        print("我在厕所")  # 打印
        self.sleep()  # 调用sleep方法

my_house = Drawing()  # 实例化 Drawing 对象

my_house._Drawing__sleepat_room()
#  通过name重写的方法就可以调用到私有属性，但是不建议这样使用
#  可以在类里面的方法去调用

my_house.sleep()  # 调用公共变量sleep方法打印房子特性
my_house._Drawing__style2

# 上下虽然实例化的是同一个类，但是概念上是不一样的

bob_house = Drawing()  # 实例化
bob_house.sleep()
