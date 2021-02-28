class Student:
    def __init__(self, name, age, score, sex):
        # 创建实例变量
        self.name = name
        self.age = age
        self.score = score
        self.sex = sex

    def print_self_info(self):
        # 读取实例变量
        print("学生的姓名是%s，年龄是%d，分数为%.1f，性别为%s" %
              (self.name, self.age, self.score, self.sex))

list01 = [
    Student("赵敏", 28, 100, "女"),
    Student("苏大强", 68, 72, "男"),
    Student("明玉", 30, 95, "女"),
    Student("无忌", 29, 70, "男"),
    Student("张三丰", 130, 96, "男"),
]

def find01():
    """
        按name查找一个
    """
    for item in list01:
        if item.name == "苏大强":
            return item
    # 如果没有找到，则返回空。而函数返回值默认就是空，所以可以不写
    # return None

# stu = find01()
# print(stu.name, stu.age)

def find02():
    """
        按sex查找多个
    """
    result = []
    for item in list01:
        if item.sex == "女":
            result.append(item)
    return result

# stu = find02()
# for item in stu:
#     print(item.name,item.sex)

def find03():
    count = 0
    for item in list01:
        if item.age >= 30:
            count += 1
    return count


# print(find03())


def set01():
    """
        所有学生成绩归零
    """
    for item in list01:
        item.score = 0


# set01()
# for stu in list01:
#     stu.print_self_info()

def find05():
    """
        获取list01中所有学生的名字
    """
    names = []
    for item in list01:
        names.append(item.name)
    return names

# print(find05())


def find06():
    """
        在list01中查找年龄最大的学生对象
    """
    max_obj = list01[0]
    for index in range(1, len(list01)):
        if max_obj.age < list01[index].age:
            max_obj = list01[index]
    return max_obj

stu = find06()
stu.print_self_info()