# 客户端代码
class Employee:
   pass


class EmployeeManager:
    def __init__(self):
        self.__employees = []

    def add_employee(self, employee):
        self.__employees.append(employee)

    def __iter__(self):
        return EmployeeIterator(self.__employees)


class EmployeeIterator:
    def __init__(self,target):
        self.__target = target
        self.__index = 0

    def __next__(self):
        if self.__index > len(self.__target)-1:
            raise StopIteration
        tmp = self.__target[self.__index]
        self.__index += 1
        return tmp


# --------------测试代码----------------
em = EmployeeManager()
em.add_employee(Employee())
em.add_employee(Employee())
em.add_employee(Employee())

"""
# 原理
em_iterator = em.__iter__()
while True:
    try:
        item = em_iterator.__next__()
        print(item)
    except StopIteration:
        break
"""
for item in em:
    print(item)


