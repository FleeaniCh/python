"""
    模块
"""
'''
import os
import sys
# base_path = os.path.abspath(os.path.dirname(os.getcwd()))
base_path = os.path.abspath(os.getcwd())
print(base_path)
sys.path.append(base_path)
'''
# import module01
# 导入方式1
# 本质：使用变量名关联模块地址
# import module01  # 只执行一次
#
# module01.fun01()
# my02 = module01.MyClass02()
# my02.fun02()

import module01 as m01  # 只执行一次

m01.fun01()
my02 = m01.MyClass02()
my02.fun02()

# 导入方式2
# 本质：将指定的成员导入到当前模块作用域中
# 注意：导入进来的成员不要和当前模块成员名称相同【可使用as别名】
from module01 import MyClass02
from module01 import fun01

# def fun01():# 就近原则
#     print("当前模块fun01")

fun01()
MyClass02().fun02()

# 导入方式3
# 将指定模块的所有成员导入奥当前作用域中
from module01 import *
fun01()
my02 = MyClass02()
my02.fun02()
