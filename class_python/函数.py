"""函数的定义
1、函数代码块以def关键词开头，后面函数标识符名称和圆括号()。
2、任何传入参数和自变量必须放在圆括号中间，圆括号之间可以用于定义函数。
3、函数的第一行语句可以选择性地使用文文档字符串——用于存放函数说明。
4、函数内容以冒号起始，并且缩进。
5、return[表达式]结束函数，选择性地返回一个值给调用方，。不带表达式的reture相当于返回None
"""
print("函数的定义")
def method(a):  # 定义一个函数名
    """
    （文档字符串）
    :param a:
    :return:
    """
    print(a)
    return a+2  # 返回的值传给了method(a)
    # return
    # 当return后面没有更值或表达式的时候，会return一个None
print(method(1))  # 如果函数内有参数，且我们在调用的过程中，函数必须要传参，不然会报错

"""默认参数：
1、调用函数时，如果没有传递参数，则会使用默认参数
2、默认参数在定义函数的时候定义
3、默认值之后执行一次，这条规则在默认值为可变对象时很重要
"""
print("默认参数")
def method1(b, c=[]):
    c.append(b)
    return c

print(method1(1))
print(method1(2))  # 输出结果过[1,2]，即默认值c=[]只能被执行一次

"""函数的参数
关键字参数：
 1、kwarg=value形式，在调用函数时添加
 2、在函数调用/定义中，关键字参数必须跟随在位置参数的后面
 3、当存在一个心形式为**name的一个形参时，它会就收一个字典
 4、形式为*name，接收一个包含除了与已有形参列表以外的位置参数的 元组 的形参
"""
print("关键字参数1")
def method2(b, c):
    print(b)
    print(c)
    # return b

method2(c=1, b=2)  # 这样定义可以不注意参数传递的顺序
method2(3, c=4)  #关键字参数一定要在默认参数的后面

print("关键字参数2")
def method3(**a):  # 定义字典
    print(a.keys())

method3(a=1, b=2, c=3)  # 传递字典

print("关键字参数3")
def method4(*a):  # 元组传参
    print(a[0])
    print(a[1])
    print(a[2])
    print(a[3])

method4(4,3,6,7)  # 传递以后元组参数

"""
1、特殊参数：
   *：仅限关键字参数，在【仅限关键字】形参前放置一个*
2、解包参数列表
   ①*用来解包元组
   ②**用来解包字典
"""
print("关键字参数4.1、仅限关键字传参")
def method4(*,a):  # 元组传参
    print(a)

method4(a=4)  # 传递以后元组参数

print("关键字参数4.2、解包元组")
print(list(range(3, 6)))  # 列表从3开始到第6位
list_a = (3, 9)
print(list(range(*list_a)))  # 解包

print("关键字参数4.2、解包字典")
def method5(a, b, c):
    print(a)
    print(b)
    print(c)

dic1={"a":2, "b":2, "c":3}  # 定义一个字典
method5(**dic1)  # 进行字典解包

"""Lambda表达式：
1、可以用lambda关键字来创建一个小的匿名函数。
2、关键字为lambda
3、lambda的主体是一个表达式，而不是一个代码块。仅仅能在lambda表达式中封装有限的逻辑进去。
"""
print("关键字参数5、Lambda表达式")
y = lambda x, y, z : x+y+z

print(y(2, 3, 4))