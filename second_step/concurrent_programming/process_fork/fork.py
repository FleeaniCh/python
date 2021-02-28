"""
    fork.py 多进程
"""
import os

# 创建子进程
pid = os.fork() #仅Linux环境可调用fork()

if pid < 0:
    print("Create process failed")
#  子进程执行部分
elif pid == 0:
    print("The new process")
# 父进程执行部分
else:
    print("The old process")

# 父子进程都会执行
print("Fork test.py over")
