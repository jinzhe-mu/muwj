"""
模块的改造：
1、加入模块的改造：将类houyi与类角色通用两个文件夹的文件管理
2、加入异常改造：当平均的时候，抛出一个异常
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


