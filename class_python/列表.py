"""一、列表
定义：
   1、python中可以通过组合一些值得到多种符合数据类型。
   2、列表是其中最常用的数据结构。
   3、列表通过方括号括起、逗号分隔的一组值得到。
   4、一个列表可以包含不同类型的元素，但通常使用时各个元素类型相同
列表的特性：
   1、list.append(x):在列表的末尾添加一个元素。相当于a[len(a):]=[x]
   2、list.insert(i,x):在给定的位置插入一个元素。第一个参数是要插入的元素的索引，
   以a.insert(0,x)插入列表头部，a.insert(len(a),x)等同于a.append(x).
   3、list.remove(x):移除列表中第一个值为x的元素。如果没有这样的元素，则抛出ValueError异常。
   4、list.pop([i]):删除列表中给定的元素并返回它。如果没有给定位置，a.pop()将会删除并返回列表中的最后一个元素。
   5、list.sort(key=None,reverse=False):对列表中的元素进行排序（参数可用于自定义排序，解释请参见sorted（）。
   6、list.reverse():反转列表中的元素
   7、list.clear()删除列表中所有的元素。相当于del a[:].
   8、list.estend(iterable)：使用可迭代对象中的所有元素来扩展列表。相当于a[len(a)]=iterable。
   9、list.index(x[,start[,end]])
   10、返回列表中第一个值为x的元素的从零的零开始的索引。如果没有这样的元素将会抛出ValueError异常
   11、可选参数start和end是切片符号，用于将搜索限制为列表的特定子序列。返回的索引是相对于整个序列的开始计算的，而不是start参数。
   12、list.count(x):返回元素x在列表中出现的次数。
   13、list.copy():返回列表的一个浅拷贝。相当于a[:].
   注意：
       insert,remove或者sort方法，只修改列表，没有答应出返回值——它们返回默认None.
       这是python中所有可变数据结构的设计原则。
       并非搜优数据或可以拍下或比较（字符串和数字等）
列表推导式：
    1、概念：列表推导式提供了一个更简单的穿件列表的方法。常见的用法是把某种操作应用于序列或可迭代对象的每个元素上，然后使用其结果来穿件爱你列表，
    或者通过满足某些特定条件元素来创建子序列。
    2、练习：如果我们想生成一个平方列表，比如[1,4,9...]，使用for循环应该怎么写，使用列表生成式又应该怎么写呢？
"""


list_hogwars=[1, 2, 3]
print("1、list.append(x):在列表的末尾添加一个元素。相当于a[len(a):]=[x]")
list_hogwars.append(0)  # 在列表末尾添加一个0元素
list_hogwars.append(8)
list_hogwars.append(6)
print(list_hogwars)

print("2、list.insert(i,x):在给定的位置插入一个元素。第一个参数是要插入的元素的索引，以a.insert(0,x)插入列表头部，a.insert(len(a),x)等同于a.append(x).")
list_hogwars.insert(1, 0)  # 在索引为1的地方插入一个0元素
print(list_hogwars)

print("3、list.remove(x):移除列表中第一个值为x的元素。如果没有这样的元素，则抛出")
list_hogwars.remove(0)  # 把列表中第一个为0的元素删除
print(list_hogwars)
# list_hogwars.remove(9)  # 列表中没有9这个元素，会抛出异常
# print(list_hogwars)

print("4、list.pop([i]):删除列表中给定的元素并返回它。如果没有给定位置，a.pop()")
y = list_hogwars.pop(1)  # 删除索引为1的元素,并可以把删除的值返回给y
print(list_hogwars)
print(y)

print("5、list.sort(key=None,reverse=False):对列表中的元素进行排序（参数可用")
list_hogwars.sort()  # 升序排序列表
print(list_hogwars)
list_hogwars.sort(reverse=True)  # 降序排序列表
print(list_hogwars)

print("6、list.reverse():反转列表中的元素")
list_hogwars.reverse()  # 反转列表中的元素
print(list_hogwars)

print("列表推导式：")
"""
2、练习：如果我们想生成一个平方列表，比如[1,4,9...]，使用for循环应该怎么写，使用列表生成式又应该怎么写呢？
"""
list_square = []
for i in list_hogwars:
    list_square.append(i**2)  # 求平方
print(list_square)
### 用列表推导式实现
list_square2 = []
list_square2 = [i**2 for i in list_hogwars]
print(list_square2)

#加入if语句
list_square3 = []
for i in list_hogwars:
    if i!=1:
        list_square3.append(i**2)
print(list_square3)
### 用列表推导式实现
list_square4 = []
list_square4 = [i**2 for i in list_hogwars if i!=1]
print(list_square4)

# 嵌套循环
list_square5= []
for i in range(1, 4):  # 取从索引1开始到索引4的数字
    for j in range(1, 4):
        list_square5.append(i*j)
print(list_square5)
#用列表推导式实现
list_square6 = [i*j for i in range(1, 4) for j in range(1, 4)]
print(list_square6)