"""
    模块相关概念
"""
import os
from module01 import *

fun01()
# 隐藏成员，不能通过from模块import x形式导入
_fun02()

# 隐藏成员，可以通过其他方式导入
from module01 import *

MyClass.fun03()
_fun02()

# 可以通过该属性，查看文档注释
print(__doc__)

# 返回当前文件/模块的绝对路径
print(__file__)
print(os.path.dirname(__file__))

# 主模块叫做：__main__
# 非主模块叫做：真名
# print(__name__)
# 作用1：测试代码，只能从当前模块运行才执行（不是主模块不执行——测试代码）
# 作用2：限制只能从当前模块才执行（只有是主模块才执行——主模块代码）
# 使用
if __name__ == '__main__':
    pass
