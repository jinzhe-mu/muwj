"""
作业4
使用列表推导式写下面这个算法题
给定一个按非递减顺序排序的整数数组 A，返回每个数字的平方组成的新数组，要求也按非递减顺序排序。

示例 1：
输入：[-4,-1,0,3,10]
输出：[0,1,9,16,100]

示例 2：
输入：[-7,-3,2,3,11]
输出：[4,9,9,49,121]

提示：
1 <= A.length <= 10000
-10000 <= A[i] <= 10000
A 已按非递减顺序排序。
"""

A = [-4, -1, 0, 3, 10]  # 定义一个列表A
list1 = []  # 定义一个空列表list1

# for i in A:  # 判断当i在A列表里面
#     if len(A):  # 当A列表不为空时
#         list1.append(pow(i, 2))  # 对i求平方赋值给list1
# list1.sort()  # 让list1按照配递减排序
# print(list1)  # 打印list1
###  用列表推导式方式给list1赋值
list1 = [pow(i, 2) for i in A if len(A)]  # 判断当i在A列表里面，当A列表不为空时，对i求平方赋值给list1
list1.sort()  # 让list1按照配递减排序
print(list1)  # 打印list1

