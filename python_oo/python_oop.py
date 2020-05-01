class Turtle:
    #  类变量，静态变量
    legs = 4
    mouth = 1
    eye = 2

    #  类中的函数,方法
    def bite(self):
        print("乌龟咬人")
    def clime(self):
        print("爬走")

print(Turtle.legs)
print(Turtle.bite)  # 直接调用类属性

turtle = Turtle()  # 类的实例化
turtle.bite()  # 调用实例对象中的属性
turtle.clime()
turtle.mouth


class QiaoFeng:
    height = 180
    face = "handsome"

    def fight_xlsbz(self):
        print("降龙十八掌")
qiaofeng = QiaoFeng()
qiaofeng.height
qiaofeng.fight_xlsbz()