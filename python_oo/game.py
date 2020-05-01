"""
1、使用面向对象的实现一个回合制格斗游戏
2、使用面向对象的继承改造游戏
一个回合制游戏，每个游戏都有hp和power，hp代表血量，power代表攻击力，
hp的初始值为1000，power的初始值为200.
定义一个fight方法：
   final_hp = hp-enemy_power
   enemy_final_hp = enemy_hp-power
两个hp进行对比，血量剩余的人获胜
"""
class Game:  # 定义一个父类Game
    def __init__(self, hp, power):  # 初始化实例变量类
        self.hp = hp  # 实例变量
        self.power = power  # 实例变量

class get_game(Game):   # 定义一个子类get_game，继承父类Game
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
        print("打成平手了")

game = get_game(1000,200)   # 实例化类并给init传值
game.fight(1000, 200)   # 调用fight方法并传入值