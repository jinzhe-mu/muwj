###冒泡排序每一行加注释说明

list_mu = [3,6,7,3,9,3,70,45,43,56]
for i in range(len(list_mu)-1):    #进行i-1次循环比较，i为list_mu的长度
    for j in range(len(list_mu)-i-1): #j代表列表里的第j位索引,进行j-1次循环
        print(f"i={i}")        #当循环第i次的时候执行情况
        if list_mu[j]>list_mu[j+1]: #判断列表索引第j和j+1位的大小，当列表索引数值[j]大于[j+1]时执行
            print(f"j={j}需要进行交换")    #输出第j位需要交换的索引值
            list_mu[j], list_mu[j + 1] = list_mu[j + 1], list_mu[j]#当索引值[j]>[j+1]时交换两个值
        else:
            print("没有交换") # 当索引值[j]<=[j+1]时不交换两个值
print(list_mu)