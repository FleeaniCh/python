"""
    获取进程PID号
"""
import os
from time import sleep

pid = os.fork()

if pid < 0:
    print("Error")
elif pid == 0:
    sleep(1)
    print("Child PID:",os.getpid()) # 子进程
    print("Get parent PID:",os.getppid())   # 父进程
else:
    print("Get child PID:",pid) # 子进程
    print("Parent PID:",os.getppid())
