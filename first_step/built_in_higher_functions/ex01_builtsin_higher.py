"""
    练习：
    1.([1,1,1],[2,2],[3,3,3,3])
        获取元组，长度最大的列表
    2.根据敌人列表，获取所有敌人的姓名与血量与攻击力
    3.在敌人列表中，获取攻击力大于100的所有活人
    4.根据防御力对敌人列表进行降序排列
"""
tuple01 = ([1, 1, 1], [2, 2], [3, 3, 3, 3])
# 练习1
re01 = max(tuple01, key=lambda item: len(item))
print(re01)


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

print("-----------------------练习2-------------------------")
for item in map(lambda item: (item.name, item.hp, item.atk), list_enemy):
    print(item)

print("-----------------------练习3-------------------------")
for item in filter(lambda item: item.hp > 0, list_enemy):
    print(item)

print("-----------------------练习4-------------------------")
re02 = sorted(list_enemy, key=lambda item: item.defense, reverse=True)
for item in re02:
    print(item)
