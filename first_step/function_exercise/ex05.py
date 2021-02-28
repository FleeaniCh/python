"""
    练习3：
    在ListHelper中增加通用的获取最大值方法
    案例1：获取敌人列表中攻击力最大的敌人
    案例2：获取敌人列表中防御力最大的敌人
    案例3：获取敌人列表中血量最高的敌人
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
def max():
    max_value = list_enemy[0]
    for i in range(1,len(list_enemy)):
        if max_value.atk < list_enemy[i].atk:
            max_value = list_enemy[i]
    return max_value

def max01():
    max_value = list_enemy[0]
    for i in range(1,len(list_enemy)):
        if max_value.defense < list_enemy[i].defense:
            max_value = list_enemy[i]
    return max_value

def get_max():
    max_value = list_enemy[0]
    for i in range(1,len(list_enemy)):
        if max_value.atk < list_enemy[i].atk:
            max_value = list_enemy[i]
    return max_value

print(max())
"""
re = ListHelper.get_max(list_enemy,lambda item:item.hp)
print(re)


