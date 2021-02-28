"""
    在不改变原有功能调用与定义的情况下，
    为其增加新功能
"""
import time


def execution_time(func):
    """计算指定程序执行时间"""
    def wrapper(*args, **kwargs):
        # 记录调用前的时间
        start_time = time.time()
        result = func(*args, **kwargs)
        # 记录调用后时间
        exec_time = time.time() - start_time
        print("执行时间：", exec_time)
        return result

    return wrapper


@execution_time
def fun01():
    time.sleep(2)  # 睡眠2s，用于模拟程序执行过程
    print("fun01执行完毕喽")


@execution_time
def fun02(a):
    time.sleep(1)
    print("fun02执行完毕喽，参数是：", a)


fun01()
fun02(100)
