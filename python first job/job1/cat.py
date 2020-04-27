"""
作业1
用类和面向对象的思想，“描述”生活中任意接触到的东西（比如动物、小说里面的人物，不做限制，随意发挥），数量为5个
"""
#  定义一个Cat的类
class Cat:
    colour = "white"
    age = 3

    def vioce(self):
        print("喵喵喵~~~")

    def function1(self):
        print("抓老鼠")

my_cat = Cat()
my_cat.vioce()
my_cat.function1()