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


def condition01(item):
    return item.atk_ratio > 6

def condition02(item):
    return 4 <= item.duration <= 11

def condition03(item):
    return len(item.name) > 4 and item.duration < 6

generator01 = ListHelper.find_all(list_skill, condition01)
# for item in generator01:
#     print(item)


# 练习：在list_helper.py中，定义通用的查找满足条件的单个对象
# 案例：查找名称是“葵花宝典”的技能
#           查找编号是101的技能
#           查找持续时间大于0的技能（只取其一）
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
