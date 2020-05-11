"""
需要传入敌人的hp，power，进行一回合制对打，打完之后，比较双方血量。血多的一方获胜。
加入模块化改造
"""

from yaml_python.game_tlbb.xuzhu import Xuzhu  # 引入python_first_job.job3.xuzhu包里的Xuzhu类

class Fight(Xuzhu):  # 定义一个子类Fight继承Xuzhu父类属性

    def fight1(self):  # 定义一个fight方法，传入值

        frequency = 0

        while True:  # 当两个值不相等的时候
            print(self.first, self.first_hp)
            print(self.second, self.second_hp)
            frequency += 1
            if frequency % 3 == 1:
                self.first_hp = self.first_hp - self.second_power * self.second_skill  # self.first剩余血量=self.first初始血量-self.second攻击力*skill将攻击力翻倍值
                self.second_hp = self.second_hp - self.first_power * self.first_skill  # self.second的剩余血量=self.second初始血量-攻击力*skill将攻击力翻倍值
            else:
                self.first_hp = self.first_hp - self.second_power  # self.first剩余血量=self.first初始血量-self.second攻击力
                self.second_hp = self.second_hp - self.first_power  # self.second剩余血量=self.second初始血量-self.first攻击力
            if self.first_hp <= 0:  # self.first的hp小于等于0
                print("{}赢了".format(self.second))  # 打印self.second赢了
                break  # 中断
            elif self.second_hp <= 0:  # # self.second的hp小于等于0
                print("{}赢了".format(self.first))  # 打印self.first赢了
                break  # 中断


fight = Fight()  # 实例化Fight类，并给Tonglao类的init传值
fight.see_people()  # 调用see_people方法
fight.read()  # 调用read方法
fight.fight1()  # 调用fight1方法并赋值

