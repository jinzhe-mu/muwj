"""三、集合
1、集合是由不重复元素组合的无序的集
2、它的基本用法包括成员检测和消除重复元素
3、可以使用{}或者set（）函数创建集合
4、要创建一个空集合只能用set（）而不能用{}
"""
print("定义集合")
a = {1}
b = set()
print(len(b))
print(type(a))
print(type(b))

print("集合的内置函数")
a = {1, 2, 3}
b = {3, 4, 5}
print(a.union(b))  # 求两个集合的并集
print(a.intersection(b))  # 求两个集合的交集
print(a.difference(b))  # 求集合a存在但集合b没的元素

print("集合内添加元素")
a.add("a")  # 加双引号后所有元素默认加在集合后面
a.add(8)
# a.add("a")
print(a)
# 求出字符串内去重之后的集合
print({i for i in "dyfshjhdfuggfhfaa"})

c = "dhhhhhssssurgjgkjglh"
print(set(c))  # 求出字符串c中去重之后的集合










