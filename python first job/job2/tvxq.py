class Tvxq:  # 创建类Tvxq
    number = 5  # 实例化变量
    __name = "Tong Vfang Shin Ki"  # 定义一个私有属性，私有变量

    def voice(self):  # 定义一个voice方法
        print("name is", self.__name)  # 在方法中调用私有变量
        print("singing is hero and Micky")  # 调用此方法时打印内容

    def dance(self):  # 定义一个dance方法
        print("dancing is U-Know and Xiah ")  # 调用此方法时打印内容

    def rapper(self):  # 定义一个Rapper方法
        print("Max is the rapper")  # 调用此方法时打印内容

tvxq = Tvxq()  # 实例化类Tvxq
tvxq.voice()  # 调用voice方法
tvxq.rapper()  # 调用rapper方法
