"""二、元组
1、元组使用()进行定义
2、tuple、list、range都是序列数据类型。
3、元组是不可变的，可以通过解包、索引来访问
"""
print("1、元组使用()进行定义")
tuple_hogwarts = (1, 2, 3)  # 两种定义的方式
tuple_hogwarts1 = 4, 5, 6
print("tuple_hogwarts：", tuple_hogwarts)  # 打印元组的数据
print(type(tuple_hogwarts))  # 打印数据类型
print("tuple_hogwarts1：", tuple_hogwarts1)
print(type(tuple_hogwarts1))

"""
元组的不可变特性
"""
print("元组的不可变特性")
#列表的特性
list_hogwarts = [1, 2, 3]
list_hogwarts[0] = 4  #修改列表索引为0的元素
print(list_hogwarts)
#元组的特性
# tuple_hogwarts2 = (1, 2, 3)
# tuple_hogwarts2[0] = 4  # 因为元组的不可变特性，会报错
# print(tuple_hogwarts2)

"""
元组可嵌套列表
"""
a = [4, 5, 6]
tuple_hogwarts3 = [1, 2, a]
print(id(tuple_hogwarts3))
tuple_hogwarts3[2][0] = 9
print(tuple_hogwarts3)
print(id(tuple_hogwarts3))
# 元组的不可变特性针对变量指针地址不可变，a相当于一个指针地址，对a列表内部数据进行修改不影响a的指针地址

"""
元组的内置函数
"""
print("元组的内置函数")
a = (3, 4, 5, "b", "b")
print(a.count("a"))  # a在元组中出现的次数
print(a.count("b"))  # b在元组中出现的次数
print(a.index(5))  # 求元素5在元组中的索引
print(a.index("b"))  # 有重复的元素以第一个索引位置为主




