"""
    程序入口
"""
from ui import StudentManagerView

# 限制只能从当前模块运行才执行
if __name__ == '__main__':
    view = StudentManagerView()
    view.main()
