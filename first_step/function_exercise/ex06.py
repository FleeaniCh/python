"""
    在list_helper.py中增加通用的升序排列方法
    案例1：将敌人列表按照攻击力进行升序排列
    案例2：将敌人列表按照防御力进行升序排列
    案例3：将敌人列表按照血量进行升序排列
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

"""
def sort():
    for i in range(0, len(list_enemy) - 1):
        for j in range(i + 1, len(list_enemy)):
            if list_enemy[i].atk > list_enemy[j].atk:
                list_enemy[i], list_enemy[j] = list_enemy[j], list_enemy[i]

sort()
for item in list_enemy:
    print(item)
"""
ListHelper.order_by(list_enemy, lambda item:item.atk)
for item in list_enemy:
    print(item)

