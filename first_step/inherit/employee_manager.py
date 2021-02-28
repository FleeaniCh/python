"""
    定义员工管理器
                1.管理所有员工
                2.计算所有员工工资

    员工：
                程序员：底薪+项目分红
                销售：底薪+提成(销售额*0.05)
                软件测试...
                ......
    要求：增加新岗位，员工管理器不变
"""


# 客户端代码
class EmployeeManager:
    def __init__(self):
        self.__employees = []

    def add_employee(self, employee):
        if isinstance(employee, Employee):
            self.__employees.append(employee)
        else:
            raise ValueError()

    def get_total_salary(self):
        total_salary = 0
        for item in self.__employees:
            # 调用的是抽象的员工类
            # 多态
            total_salary += item.caculate_salary()  # 具体事务的抽象
        return total_salary


class Employee:
    def __init__(self, basic_salary):
        self.basic_salary = basic_salary

    def caculate_salary(self):
        return self.basic_salary


class Programmer(Employee):
    def __init__(self, basic_salary, bonus):
        # self.basic_salary = basic_salary
        super().__init__(basic_salary)
        self.bonus = bonus

    def caculate_salary(self):
        # return self.basic_salary + self.bonus
        return super().caculate_salary() + self.bonus  # 扩展重写


class Salesman(Employee):
    def __init__(self, basic_salary, sales):
        # self.basic_salary = basic_salary
        super().__init__(basic_salary)
        self.sales = sales

    def caculate_salary(self):
        return self.basic_salary + self.sales * 0.05


# 测试
em = EmployeeManager()
p01 = Programmer(10000, 6000)
s01 = Salesman(2000, 100000)
em.add_employee(p01)
em.add_employee(s01)
re = em.get_total_salary()
print(re)
