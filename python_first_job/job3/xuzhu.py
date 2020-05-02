"""
定义一个XuZhu类，继承于童姥。虚竹宅心仁厚不想打架。所以虚竹只有一个read（念经）的方法。
每次调用都会打印“罪过罪过”
"""

from python_first_job.job3.tonglao import Tonglao  # 引入python_first_job.job3.tonglao包里的Tonglao类

class Xuzhu(Tonglao):  # 定义一个子类Xuzhu继承Tonglao父类属性

    def read(self):  # 定义一个read方法
        print("xuzhu:罪过罪过")  # 打印内容
        print("施主手下留情，万物皆有灵性，不可杀生~")  # 打印内容

