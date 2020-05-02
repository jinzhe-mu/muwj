"""
需要传入敌人的hp，power，进行一回合制对打，打完之后，比较双方血量。血多的一方获胜。
加入模块化改造
"""

from python_first_job.job3.xuzhu import Xuzhu  # 引入python_first_job.job3.xuzhu包里的Xuzhu类

class Fight(Xuzhu):  # 定义一个子类Fight继承Xuzhu父类属性

    def fight1(self, xuzhu_hp, xuzhu_power):  # 定义一个fight方法，传入值

        while True:  # 一直执行此循环直到循环被中断
            self.hp = self.hp - xuzhu_power  # 每次循环使self.hp动态变化
            xuzhu_hp = xuzhu_hp - self.power  # 每次循环使xuzhu_hp动态变化
            print("tonglao hp=", self.hp)  # 打印此次循环tonglao的hp
            print("xuzhu hp=", xuzhu_hp)  # 打印此次循环xuzhu的hp

            if xuzhu_hp <= 0 and xuzhu_hp < self.hp:  # 当xuzhu的hp小于等于零且虚竹的hp小于童姥的hp时执行
                print("童姥：哈哈哈哈哈哈哈，我岂是你们能够随便挑战的")  # 打印内容
                break  # 执行此操作后就中断while循环

            elif self.hp <= 0 and xuzhu_hp > self.hp:  # 当童姥的hp小于等于零时执行
                print("虚竹：童姥施主稍安勿躁，平僧失礼了")  # 打印内容
                break  # 执行此操作后就中断while循环

            else:  # 不满足以上时执行
                print("两败俱伤下次再战")  # 打印内容
                break  # 执行此操作后就中断while循环



fight = Fight(100, 200)  # 实例化Fight类，并给Tonglao类的init传值
fight.see_people("name")  # 调用see_people方法
fight.read()  # 调用read方法
fight.fight_zms()  # 调用fight_zms方法
fight.fight1(50, 400)  # 调用fight1方法并赋值

