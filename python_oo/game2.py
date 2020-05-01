"""
改造----不建议，代码可读性差
虽然减少了代码量，但是尽量不要这样改造。
子类和父类要尽量解耦，子类的逻辑不要写在父类
"""
class Game:  # 定义一个父类Game
    def __init__(self, hp=1000, power=200, enemy_hp=1000, enemy_power=300, defanse=100):  # 初始化实例变量类
        self.hp = hp  # 实例变量
        self.power = power  # 实例变量
        self.final_hp = self.hp - enemy_power  # 剩余血量=初始血量-敌人攻击力
        self.enemy_final_hp = enemy_hp - self.power  # 敌人的剩余血量=初始血量-攻击力
        self.houyi_hp = self.hp + defanse - enemy_power

    def fight(self):  # 定义一个fight方法，传入值
            if self.houyi_hp > self.enemy_final_hp:  # 我的值大于敌人的值
                print("后裔赢了")  # 打印我赢了

            elif self.houyi_hp< self.enemy_final_hp:  # 否则
                print("敌人2赢了")  # 打印敌人赢了

            else:  # 当打成平手时抛出异常
                raise Exception("no peace,keep fighting")



class Houyi(Game):
    # def __init__(self):
    #     super().__init__()
    #     self.defanse = 100
    pass





houyi = Houyi()   # 实例化类并给init传值
houyi.fight()   # 调用fight方法并传入值