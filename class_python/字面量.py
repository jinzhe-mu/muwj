"""
字面量差值方法：
1、格式化输出  %的用法
2、通过string.format()方法拼接
3、通过F-string拼接，一种字符串格式化机制
"""
print("1、格式化输出  %的用法")
name = 'Tom'
str1 = "my name is %s, my age is %d" % (name, 20)
print(str1)
print("pi = %.2f" % 3.1415926)  # 保留两位小数

print("2、通过string.format()方法拼接")
name1 = 'Tom'
name2 = 'Jerry'
print("字符串拼接:we are the {0} and {1},{0} is tom, {1} is jerry".format(name1, name2))  # 字符串拼接

listdata = [8, 2, 3, 4]
print("列表拼接:we are the {0} and {1}".format(*listdata))  # 列表拼接

dictdata = {"name": 'tom', "age": '5'}
print("字典拼接:my name is {name}, age is {age}".format(**dictdata))  # 字典拼接

print("3、通过F-string拼接，一种字符串格式化机制")
name3 = 'ERIC'
print(f'my name is {name3.lower()}')  # 输出名字并转化成小写
print(f'1+1 = {1+1}')  # 大括号{}中间不能加转义字符\




