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

# 内部直接修改列表，使用时无需通过返回值获取数据
# ListHelper.order_by(list_enemy,lambda item:item.hp)
# for item in list_enemy:
#     print(item)


# 内部返回新列表，使用时必须获取返回值
re = sorted(list_enemy, key=lambda item: item.hp)  # 升序
for item in re:
    print(item)

re = sorted(list_enemy, key=lambda item: item.hp, reverse=True)  # 降序
for item in re:
    print(item)
