"""
    练习2：
    在ListHelper中增加通用的筛选方法
    案例1：获取敌人列表中所有敌人的名称
    案例2：获取敌人列表中所有敌人的攻击力
    案例3：获取敌人列表中所有敌人的名称和血量
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

# def filtering():
#     list_result = []
#     for item in list_enemy:
#         list_result.append(fucn_handle(item))
#     return list_result
#
# def fucn_handle(item):
#     return item.name,item.hp
#
# print(filtering())

re = ListHelper.select(list_enemy, lambda item: (item.name, item.atk))  # 生成器
for item in re:
    print(item)
