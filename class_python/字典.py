"""四、字典
1、字典是用【关键字】为索引
2、关键字可以是任意不可变类型，通常是字符串或数字。如果一个元组只包含字符串、数字或元组，那么这个元组页可以用作关键字。
"""
print("定义字典")
muwj_dict = {"a": 1, "b": 2}  # 两种字典的定义方式
muwj_dict2 = dict(a=1, b=2)
print("muwj_dict:", muwj_dict)
print(type(muwj_dict))
print("muwj_dict2:", muwj_dict2)
print(type(muwj_dict2))

print("字典常用可以调用的内置函数")
print(muwj_dict.keys())  # 找出字典的key值（key值不可变）
print(muwj_dict.values())  # 找出字典的values值
print(muwj_dict.pop("a"))  # 输入key值，会把values值返回，并把为a的键值对删除
print(muwj_dict)

print(muwj_dict2.popitem())  # 返回被删除的键值对
print(muwj_dict2)  # 删除掉上面执行的键值对后，还剩余的元素

a = {}
b = a.fromkeys([2, 3, 4], "a")  # 分别把列表里面的元素作为key值作为键值建立一个列表,把a作为所有key值的values值
print(b)


print("字典推导式")
print({i: i * 2 for i in range(1, 3)})  # 定义一个字典推导式

