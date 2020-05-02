#定义一个类Flower
class Flower:
    flower_name1 = "玫瑰"  # 实例化变量
    flower_name2 = "月季"
    flower_name3 = "尤加利"

    def dislike1(self):  # 定义一个dislike1方法
        print("但她不喜欢", self.flower_name3)  # 在方法中调用变量flower_name3

    def dislike2(self):  # 定义一个dislike2方法
        print("但她不喜欢", self.flower_name1)  # 在方法中调用变量flower_name1

    def xiao_mei(self):  # 定义一个xiao_mei方法
        print("小魅喜欢", self.flower_name1)  # 在方法中调用变量flower_name1
        self.dislike1()  # 调用dislike1方法

    def mu(self):  # 定义一个mu方法
        print("沐喜欢", self.flower_name2)  # 在方法中调用变量flower_name2
        self.dislike2()  # 调用dislike2方法

flower=Flower()
flower.xiao_mei()
flower.mu()