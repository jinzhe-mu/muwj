"""
可以到python.org=>Docs=>Library Reference中去查找相应的库的使用方法
可以用ctrl+F去查找
"""

import time
# print("time模块：")
# print(time.time())  # 从纪元（1970.01.01 00：00：00）开始到现在的秒数（时间戳）
#
# print(time.asctime())  # 西方格式的标准，周几+几月+几号+几点+哪年
# print(time.localtime())  # 元组的形式返回
# print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

###获取两天前的时间
# now_timestamo = time.time()  # 获取当前的时间
# two_day_before = now_timestamo - 60*60*24*2  # 用当前时间-48小时
# print(time.localtime(two_day_before))  # 转换成元组形式
# print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(two_day_before)))


###获取三天后的时间
now_timestamo = time.time()  # 获取当前的时间
three_day_after = now_timestamo + 60*60*24*3  # 用当前时间-48小时
print(time.localtime(three_day_after))  # 转换成元组形式
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(three_day_after)))


