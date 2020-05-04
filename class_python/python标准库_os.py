"""
可以到python.org=>Docs=>Library Reference中去查找相应的库的使用方法
可以用ctrl+F去查找
"""
print("os模块：")
import os

os.mkdir("testdir")  # 在点前目录下穿件一个文件
print(os.listdir("./"))  # 列出当前目录下有哪些文件和目录，以列表的形式返回（和ls相同）
os.removedirs("testdir")  #  移除"testdir"文件
print(os.getcwd())  # 打印出当前的绝对路径
#还有很多其他功能，可以自己研究


print(os.path.exists("testdir"))  # 判断当前目录下存不存在"testdir"文件
if not os.path.exists("testdir"):  # 判断当前目录下是否存在"testdir"文件，如果不存在
    os.mkdir("testdir")  # 创建"testdir"文件
if not os.path.exists("testdir/test.txt"):  # 判断testdir目录下是否存在test.txt文件，如果不存在
    f = open("testdir/test.txt", "w")  # 创建test.txt，并给与写的权限
    f.write("hello, os using")  # 在文件中写入内容
    f.close()  # 关闭文件写的权限






