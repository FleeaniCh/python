"""
    测试通用模块  List_helper
"""
from common.list_helper import *

class SkillData:
    def __init__(self, id, name, atk_ratio, duration):
        self.id = id
        self.name = name
        self.atk_ratio = atk_ratio
        self.duration = duration

    def __str__(self):
        return "技能数据有：%d  %s  %d  %d" % (self.id, self.name, self.atk_ratio, self.duration)

list_skill = [
    SkillData(101, "乾坤大挪移", 5, 10),
    SkillData(102, "降龙十八掌", 8, 5),
    SkillData(103, "葵花宝典", 10, 2),
]

# 练习：在list_helper.py中，定义通用的查找满足条件的单个对象
# 案例：查找名称是“葵花宝典”的技能
#           查找编号是101的技能
#           查找持续时间大于0的技能（只取其一）
# 要求：使用lambda实现
"""
def condition04(item):
    return item.name == "葵花宝典"

def condition05(item):
    return item.id == 101

def condition06(item):
    return item.duration > 0

# def find_single():
#     for item in list_skill:
#         if condition06(item):
#             return item
#
# re = find_single()
# print(re)
re02 = ListHelper.find_single(list_skill, condition04)
print(re02)
"""
re01 = ListHelper.find_single(list_skill,lambda item:item.name == "葵花宝典")
print(re01)

re02 = ListHelper.find_single(list_skill,lambda item:item.id == 101)
print(re02)

re03 = ListHelper.find_single(list_skill,lambda item:item.duration > 0)
print(re03)

# 需求1：计算技能列表中技能名称大于4个字的所有技能数量
# 需求2：计算技能列表中技能持续时间小于等于5的技能数量
"""
def get_count(func_condition):
    count_value = 0
    for item in list_skill:
        if func_condition(item):
            count_value += 1
    return count_value
"""
re04 = ListHelper.get_count(list_skill,lambda item:len(item.name)>4)
print(re04)

re05 = ListHelper.get_count(list_skill,lambda item:item.duration<=5)
print(re05)


