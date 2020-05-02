###1、类型提示
# def excute_date(a):  # 处理一个列表
#     b = a
#     b.sort()  # 调用排序
#     print(b)
#
# excute_date([9, 8, 7, 5, 0, 4])
"""1、类型提示:
①提前给变量一个数据类型，然后可以直接调用此数据类型的方法
②没有实际作用
"""
# def excute_date(a:list):  # 处理一个列表
#     a.sort()  # 调用类型提醒：提醒使用sort
#     print(a)
# excute_date([9, 4, 7, 5, 0, 4])

###2、三目运算
# def fight(self ):
#     print("后裔赢了") if self.houyi_hp > self.enemy_final_hp else print("敌人2赢了")
#     # if为真执行前面输出，否则执行后面输出，不允许多重分支，只能两个分支

###3、列表推导式
"""
给一个整数数组nums，请你返回其中位数为 偶数 的数字的个数
列表推导式使用：
   1、要有for循环
   2、要有append
转换方式：
1、先新建一个空列表 
2、把循环判断循环语句塞进去
3、把append里面的内容放到最前面
"""
nums = [12, 345, 2, 6, 7896]
list1 = []
# for i in nums:
#     if len(str(i)) % 2 == 0:   # 用str做强制类型转换,取数组里面位数为偶数的数字
#         list1.append(i)   # 将此数字传给数组list1
# print(list1)
# print(len(list1))  # 输出此列表的长度
# 将上面5行代码（列表推导式）转换为下面的2行
print([i for i in nums if len(str(i)) % 2 == 0])
print(len([i for i in nums if len(str(i)) % 2 == 0]))