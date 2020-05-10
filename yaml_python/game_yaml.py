"""
游戏规则：
设定一个回合制2人对打游戏。
每个人物都有hp，power，skill
hp代表血量，power代表攻击力，
每三个回合可以使用一次skill，skill将攻击力翻倍
"""
import yaml

class Game:  # 定义一个类Game
    def __init__(self):  # 初始化实例变量类
        infor = yaml.safe_load(open("game.yaml"))  # 将yaml文件内容导入赋值给infor
        print(infor)
        default = infor["default"]  # 将default的值赋值给default
        self.first = default[0]  # 取出default第一位的值
        self.second = default[1]  # 取出default第二位的值
        print("第一位选手:", self.first, "第二位选手：", self.second)
        # 第一个人物
        self.first_hp = infor[self.first]["hp"]  # 根据default第一位的值取出对应hp
        self.first_power = infor[self.first]["power"]  # 根据default第一位的值取出对应power
        self.first_skill = infor[self.first]["skill"]  # 根据default第一位的值取出对应skill
        print(self.first, "hp:", self.first_hp, "power:", self.first_power, "skill:", self.first_skill)

        # 第二个人物
        self.second_hp = infor[self.second]["hp"]  # 根据default二位的值取出对应hp
        self.second_power = infor[self.second]["power"]  # 根据default第二位的值取出对应power
        self.second_skill = infor[self.second]["skill"]  # 根据default第二位的值取出对应skill
        print(self.second, "hp:", self.second_hp, "power:", self.second_power, "skill:", self.second_skill)

    def fight(self):  # 定义一个fight方法
        frequency = 0

        while True:  # 当两个值不相等的时候
            print(self.first, self.first_hp)
            print(self.second, self.second_hp)
            frequency += 1
            if frequency % 3 == 1:
                self.first_hp = self.first_hp - self.second_power * self.second_skill  # self.first剩余血量=self.first初始血量-self.second攻击力*skill将攻击力翻倍值
                self.second_hp = self.second_hp - self.first_power * self.first_skill  # self.second的剩余血量=self.second初始血量-攻击力*skill将攻击力翻倍值
            else:
                self.first_hp = self.first_hp - self.second_power   # self.first剩余血量=self.first初始血量-self.second攻击力
                self.second_hp = self.second_hp - self.first_power   # self.second剩余血量=self.second初始血量-self.first攻击力
            if self.first_hp <= 0:  # self.first的hp小于等于0
                print("{}赢了".format(self.second))  # 打印self.second赢了
                break  # 中断
            elif self.second_hp <= 0:  # # self.second的hp小于等于0
                print("{}赢了".format(self.first))  # 打印self.first赢了
                break  # 中断


if __name__ == '__main__':
    game = Game()   # 实例化类并给init传值
    game.fight()

