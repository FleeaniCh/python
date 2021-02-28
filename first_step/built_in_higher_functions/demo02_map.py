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

# 2.获取所有敌人的信息
# for item in ListHelper.select(list_enemy,lambda item:item.name):
#     print(item)

re = map(lambda item:item.name,list_enemy)
# print(re)#<map object at 0x0000000001E73160>
for item in re:
    print(item)