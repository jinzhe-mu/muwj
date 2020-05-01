"""
代码优化--继承
1、使用传参的方式传入hp和血量
2、第二个角色，他叫后裔，后裔继承了角色的hp和power。并多了护甲属性。
3、重新定义另外一个defanse方法：
  final_hp = hp+defanse-enemy_power
  enemy_final_hp = enemy_hp-power
  两个ho进行对比，血量神域多的人获胜
"""
class Game:  # 定义一个父类Game
    def __init__(self, hp=1000, power=200):  # 初始化实例变量类
        self.hp = hp  # 实例变量
        self.power = power  # 实例变量

    def fight(self, enemy_hp, enemy_power):  # 定义一个fight方法，传入值
        final_hp = self.hp - enemy_power  # 剩余血量=初始血量-敌人攻击力
        enemy_final_hp = enemy_hp - self.power  # 敌人的剩余血量=初始血量-攻击力
        while final_hp != enemy_final_hp:  # 当两个值不相等的时候
            if final_hp > enemy_final_hp:  # 我的值大于敌人的值
                print("我赢了")  # 打印我赢了
                break  # 中断
            else:  # 否则
                print("敌人赢了")  # 打印敌人赢了
                break  # 中断


class Houyi(Game):
    def __init__(self):
        super().__init__()
        self.defanse = 100

    def defanse1(self, enemy_hp, enemy_power):
        final_hp = self.hp + self.defanse - enemy_power
        enemy_final_hp = enemy_hp - self.power
        if final_hp > enemy_final_hp:  # 我的值大于敌人的值
            print("后裔赢了")  # 打印我赢了

        elif final_hp < enemy_final_hp:  # 否则
            print("敌人2赢了")  # 打印敌人赢了

        else:
            print("打成了平手")



houyi = Houyi()   # 实例化类并给init传值
houyi.defanse1(1000, 300)   # 调用fight方法并传入值