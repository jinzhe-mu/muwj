"""
作业3
定义一个天山童姥类 ，类名为TongLao，属性有血量，武力值（通过传入的参数得到）。TongLao类里面有2个方法，
see_people方法，需要传入一个name参数，如果传入”WYZ”（无崖子），则打印，“师弟！！！！”，
如果传入“李秋水”，打印“呸，贱人”，
如果传入“丁春秋”，打印“叛徒！我杀了你”
fight_zms方法（天山折梅手），调用天山折梅手方法会将自己的武力值提升10倍，血量缩减2倍。
"""
class Tonglao:  # 定义一个Tonglao类

    def __init__(self, hp, power):  # 初始化实例变量类
        self.hp = hp  # 实例变量
        self.power = power  # 实例变量

    def see_people(self, name):  # 定义一个fight方法，传入值
        print("请在WYX、李秋水、丁春秋中选择一人")  # 打印内容
        while True:  # 一直执行此循环直到循环被中断
            self.name = input("请输入名字")  # 屏幕录入内容
            if self.name == "WYX":  # 当录入内容是WYX时执行
                print("师弟！！！！")  # 打印内容
                print("快来助我一臂之力！！！！")  # 打印内容
                break  # 执行此操作后就中断while循环

            elif self.name == "李秋水":  # 当录入内容是李秋水时执行
                print("呸，贱人")
                print("等我给你好看！！！")
                break  # 执行此操作后就中断while循环

            elif self.name == "丁春秋":  # 当录入内容是丁春秋时执行
                print("叛徒！我杀了你")  # 打印内容
                print("去死吧~~~")  # 打印内容
                break  # 执行此操作后就中断while循环

            else:
                print("请在WYX、李秋水、丁春秋中选择一人")  # 打印内容且不中断循环继续执行


    def fight_zms(self):  # 定义一个fight_zms方法
        self.hp = self.hp / 2  # 童姥血量血量缩减2倍
        self.power = self.power * 10  # 童姥武力值提升10倍
        print("童姥武力值UP 10倍,血量dump 2倍")  # 打印内容
        print("hp=", self.hp, "power=", self.power)  # 打印当前操作后的self.hp、self.power值


