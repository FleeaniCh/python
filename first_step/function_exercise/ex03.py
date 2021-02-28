"""
    练习1：
    在ListHelper中增加通用的求和方法
    案例1：计算敌人列表中所有敌人的总血量
    案例2：计算敌人列表中所有敌人的总攻击力
    案例3：计算敌人列表中所有敌人的总防御力
"""
from common.list_helper import *
class Enemy:
    def __init__(self, name, atk, defense, hp):
        self.name = name
        self.atk = atk
        self.defense = defense
        self.hp = hp

    def __str__(self):
        return "敌人信息：%s, %d, %d, %d" % (self.name, self.atk, self.defense, self.hp)

list_enemy = [
    Enemy("灭霸", 50, 100, 1000),
    Enemy("成昆", 4, 11, 0),
    Enemy("罗拉", 24, 9, 0),
    Enemy("星云", 20, 8, 45),
]

# def get_sum(list_target, func_handle):
#     sum = 0
#     for item in list_target:
#         sum += func_handle(item)
#     return sum

# def get_sum01(list_target):
#     sum = 0
#     for item in list_target:
#         sum += condition01(item)
#     return sum

# def condition01(item):
#     return item.atk
# print(get_sum(list_enemy,condition01))

print(ListHelper.sum(list_enemy, lambda item:item.atk))


