"""
    fork1.py
"""
import os
from time import sleep

print("====================")
a = 1

# 创建子进程
pid = os.fork()

if pid < 0:
    print("Create process failed")
#  子进程
elif pid == 0:
    print("The new process")
    print("a= ", a)
    a = 10000

# 父进程
else:
    sleep(1)
    print("The old process")
    print("a= ", a)

print("All a->", a)

"""
The new process
a=  1
All a-> 10000
The old process
a=  1
All a-> 1

"""
