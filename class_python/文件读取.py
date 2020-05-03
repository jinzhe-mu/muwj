# f = open('MM2.py', 'rt')  # 打开文件
# # print(f.read())  # 读取文件
#
# print(f.readable())  # True表示文件是可读的
# # print(f.readline())  #  读取第一行，括号里面填数字代表读取第一行第几位
# # print(f.readline())  # 读取了第二行
# # print(f.readline())  # 读取了第三行
# print(f.readlines())  # 读取所有内容已列表的形式返回，并且在每一项内容后面加换行符\n
# f.close()

# 此方法可以不写close自动关闭，建议使用with方法
with open('MM2.py', 'rt')as f:
    # print(f.readlines())
    while True:
        line = f.readline()
        if line:
            print(line)  # print会自带一个回车
        else:
            break

