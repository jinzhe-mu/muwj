# 创建类Interest
class Interest:
    curriculum1 = "舞蹈课"  # 实例化变量
    curriculum2 = "英语课"
    curriculum3 = "体育课"

    def class_one(self):  # 定义一个class_one方法
        print("周四一班有", self.curriculum2, "没有", self.curriculum1)  # 在方法中调用变量curriculum1\curriculum2

    def class_two(self):  # 定义一个class_two方法
        print("周四二班有", self.curriculum1, "没有", self.curriculum3)  # 在方法中调用变量curriculum1\curriculum3

interest = Interest()  # 实例化类
interest.class_one()  # 调用class_one方法

xiao_ming = Interest()  # 实例化类
print("小明是二班的")  #  打印实例化类的特征
xiao_ming.class_two()  # 调用class_two方法