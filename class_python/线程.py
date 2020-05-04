import _thread
import logging  # 加入日志模块
from time import sleep, ctime
logging.basicConfig(level=logging.INFO)  # 日志级别为logging.INFO的都会被输出
import threading

# def loop0():
#     logging.info("start loop0 at " + ctime())
#     sleep(4)
#     logging.info("end loop0 at " + ctime())
#
# def loop1():
#     logging.info("start loop1 at " + ctime())
#     sleep(2)
#     logging.info("end loop1 at " + ctime())
#
# def loop2():
#     logging.info("start loop2 at " + ctime())
#     sleep(3)
#     logging.info("end loop2 at " + ctime())
#
# def main():
#     logging.info("start all at " + ctime())
#     loop0()
#     loop1()
#     loop2()
#     logging.info("end all at " + ctime())
#
# if __name__=='__main__':
#     main()


"""
对以上线程进行多线程优化
"""
# def main():
#     logging.info("start all at " + ctime())
#     _thread.start_new_thread(loop0, ())  # 三个线程会被同时执行
#     _thread.start_new_thread(loop1, ())
#     _thread.start_new_thread(loop2, ())
#     sleep(3)
#     # 主线程如果不加延时，当主线程执行完成后退出，所有的子线程会被强行终止退出，不能守住线程
#     logging.info("end all at " + ctime())
#
# if __name__=='__main__':
#     main()

"""
二次优化:加入锁的概念，让子线程结束后主线程才能结束
"""
# loops = [2, 4]
#
# def loop(nloop, nsec, lock):
#     logging.info("start loop" + str(nloop) + " at " + ctime())
#     sleep(nsec)
#     logging.info("end loop" + str(nloop) + " at " + ctime())
#     lock.release()
#
# def main():
#     logging.info("start all at " + ctime())
#     locks = []  # 声明一个锁
#     nloops = range(len(loops))  # 设置loops的长度
#     for i in nloops:  # 取出nloops的每一个值
#         lock = _thread.allocate_lock()  # 声明一个新的锁
#         lock.acquire()  # 加锁操作
#         locks.append(lock)  # 将所有的锁加入
# ###加锁和子线程要分开（即：上面的for循环和下面的for循环要分开），为防止在下一个加锁操作没完成的时候，子线程已经处理完成，直接解锁操作，就退出了主线程
#     for i in nloops:
#         _thread.start_new_thread(loop, (i, loops[i], locks[i]))  # 开启线程
#     for i in nloops:
#         while locks[i].locked(): pass
#     logging.info("end all at " + ctime())
#
# main()

"""
用threading代替_thread
"""
# loops = [2, 4]
#
#
# def loop(nloop, nsec):
#     logging.info("start loop" + str(nloop) + " at " + ctime())
#     sleep(nsec)
#     logging.info("end loop" + str(nloop) + " at " + ctime())
#
# def main():
#     logging.info("start all at " + ctime())
#     threads = []
#     nloops = range(len(loops))  # 设置loops的长度
#     for i in nloops:
#        t = threading.Thread(target=loop, args=(i, loops[i]))  # 开启线程
#        threads.append(t)
#     for i in nloops:
#         threads[i].start()
#     for i in nloops:
#         threads[i].join()
#     logging.info("end all at " + ctime())
#
# if __name__=='__main__':
#     main()


"""
用threading代替_thread
"""
loops = [2, 4]
class MyThread(threading.Thread):
    def __init__(self, func, args, name=''):
        threading.Thread.__init__(self)
        self.func = func
        self.args = args
        self.name = name

    def run(self):
        self.func(*self.args)


def loop(nloop, nsec):
    logging.info("start loop" + str(nloop) + " at " + ctime())
    sleep(nsec)
    logging.info("end loop" + str(nloop) + " at " + ctime())

def main():
    logging.info("start all at " + ctime())
    threads = []
    nloops = range(len(loops))  # 设置loops的长度
    for i in nloops:
       t = MyThread(loop, (i, loops[i]),loop.__name__)  # 开启线程
       threads.append(t)
    for i in nloops:
        threads[i].start()
    for i in nloops:
        threads[i].join()
    logging.info("end all at " + ctime())

if __name__=='__main__':
    main()


"""
进阶学习：
原语
①锁
②信号量
"""