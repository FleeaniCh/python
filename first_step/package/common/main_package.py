import sys
# 如果不在pycharm中运行当前模块，则导包失败
# 将项目根目录加入path中，导包才会成功
sys.path.append(r"E:\03-Python_Note\home\tarena\myproject\package ")

print(
    sys.path)  # ['E:\\03-Python_Note\\home\\tarena\\first_step\\package\\common', 'E:\\03-Python_Note\\home\\tarena', 'E:\\03-Python_Note\\home\\tarena\\data\\day03', 'E:\\03-Python_Note\\home\\tarena\\interfacetest', 'E:\\03-Python_Note\\home\\tarena\\first_step\\use_modules', 'E:\\03-Python_Note\\home\\tarena\\first_step\\double_list_helper', 'E:\\03-Python_Note\\home\\tarena\\first_step\\student_manage_system', 'E:\\03-Python_Note\\home\\tarena\\first_step\\package', 'C:\\Python\\Python37\\python37.zip', 'C:\\Python\\Python37\\DLLs', 'C:\\Python\\Python37\\lib', 'C:\\Python\\Python37', 'C:\\Python\\Python37\\lib\\site-packages', 'D:\\Program Files\\JetBrains\\PyCharm 2018.1.4\\helpers\\pycharm_matplotlib_backend']
