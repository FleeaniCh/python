"""
    在ListHelper中新增以下功能：
        1.获取最小值
        2.降序排列
        3.根据指定条件删除元素
            案例：在敌人列表中，删除所有死人
            案例：在敌人列表中，删除攻击力小于50的所有敌人
            案例：在敌人列表中，删除防御力大于100的所有敌人
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
    Enemy("成昆", 4, 11, 1),
    Enemy("罗拉", 24, 9, 0),
    Enemy("星云", 20, 8, 45),
]

"""
def remove():
    # 使用正向索引倒序删除
    for i in range(len(list_enemy)-1,-1,-1):
        if list_enemy[i].hp == 0:
            del list_enemy[i]

remove()
for item in list_enemy:
    print(item)
"""

ListHelper.order_by_desc(list_enemy,lambda item:item.hp)
for item in list_enemy:
    print(item)


print("----------------删除指定元素-----------------")
ListHelper.delete_all(list_enemy, lambda item: item.hp == 0)
for item in list_enemy:
    print(item)