"""
猜数字游戏计算机出1~100之间的随机数由人来猜
计算机根据人猜的数字分别
给出提示大一点\小一点\猜对了
"""
"""
导入第三方random库，使computer_number在1到100取随机的整数
"""
import random
computer_number = random.randint(1,100)
while True:
    person_number = int(input("请输入一个数字"))
    if person_number>computer_number:
        print("小一点")
    elif person_number<computer_number:
        print("大一点")
    else:
        print("猜对了")
        break
