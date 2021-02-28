"""
    练习1：定义敌人类（姓名，攻击力，防御力，血量）
    创建敌人列表，使用ListHelper实现以下功能
    (1)查找姓名是“灭霸”的敌人
    (2)查找攻击力大于10的所有敌人
    (3)查找活的敌人数量
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
re01 = ListHelper.find_single(list_enemy,lambda item:item.name == "灭霸")
print(re01)

# 查找攻击力大于10的敌人
for item in ListHelper.find_all(list_enemy,lambda item:item.atk>10):
    print(item)

result = ListHelper.get_count(list_enemy,lambda item:item.hp>0)
print(result)

"""
    练习2：在ListHelper中增加判断是否存在某个对象的方法
    案例1：判断敌人列表中是否存在“成昆”
    案例2：判断敌人列表中是否存在攻击力小于5或者防御力小于10的敌人
"""

# def is_exist():
#     for item in list_enemy:
#         if item.name == "成昆":
#             return True
#     return False

re02 = ListHelper.is_exist(list_enemy,lambda item:item.name=="成昆")
print(re02)

re03 = ListHelper.is_exist(list_enemy,lambda item:item.atk<2 or item.defense<3)
print(re03)