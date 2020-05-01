"""
要实现可以一直对打到一方血量小于等于0
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


class Houyi(Game):  # 定义一个子类变量继承Game父类属性
    def __init__(self):  # 初始化实例变量类
        super().__init__()  # 继承父类的init属性
        self.defanse = 100  # 实例变量

    def defanse1(self, enemy_hp, enemy_power):  # 定义一个defanse1方法，传入值

        while True:  # 一直执行此循环直到循环被中断
            self.hp = self.hp + self.defanse - enemy_power  # hp一直动态变化中
            enemy_hp = enemy_hp - self.power  # enemy_hp一直动态变化中
            print("我的", self.hp)  # 打印此次循环我的hp
            print("敌人", enemy_hp)  # 打印此次循环敌人的hp
            if enemy_hp <= 0:  # 当敌人的hp小于等于零是执行
                print("后裔赢了")  # 打印我赢了
                break  # 执行此操作后就中断while循环

            elif self.hp <= 0:  # 当我的hp小于等于零是执行
                print("敌人2赢了")  # 打印敌人2赢了
                break  # 执行此操作后就中断while循环



houyi = Houyi()   # 实例化类并给init传值
houyi.defanse1(1000, 300)   # 调用fight方法并传入值