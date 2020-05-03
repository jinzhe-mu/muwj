##出现了异常进行异常捕获，当不知道异常时候，可以直接用except： 不加具体异常进行捕获
while True:
    try:
        num1 = int(input("输入一个除数"))
        num2 = int(input("输入一个被除数"))
        print(num1/num2)
        break
    except ZeroDivisionError:
        print("被除数不能为零")

    except ValueError:
        print("请输入数值型整数")

    except:
        print("输入数字异常")

    # else:
    #     print("没有发生异常")

    # finally:
    #     print("发没有发生异常都执行")

#抛出异常：
print("抛出异常：")
x = 10
if x > 5:
    raise Exception("这是一个抛出的异常")


#自定义异常：
print("自定义异常：")
class MyException(Exception):
    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2

raise MyException ("value1", "value2")