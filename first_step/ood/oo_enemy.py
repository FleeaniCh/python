class Enemy:
    def __init__(self, name, hp, atk, defense):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.defense = defense

    def print_self_info(self):
        print(self.name, self.hp, self.atk, self.defense)


list01 = [
    Enemy("玄冥二老", 86, 120, 58),
    Enemy("成昆", 0, 100, 4),
    Enemy("谢逊", 120, 130, 60),
    Enemy("灭霸", 5000, 13099, 690),
]


def find01():
    for item in list01:
        if item.name == "灭霸":
            return item


e01 = find01()
if e01:
    e01.print_self_info()
else:
    print("没找到")


def find02():
    list_result = []
    for item in list01:
        if item.hp == 0:
            list_result.append(item)
    return list_result


re02 = find02()
for item in re02:
    item.print_self_info()


def caculate():
    sum_atk = 0
    for item in list01:
        sum_atk += item.atk
    return sum_atk / len(list01)

print(caculate())


def delete01():
    for i in range(len(list01)-1,-1,-1):
        if list01[i].defense < 10:
            del list01[i]

delete01()
for item in list01:
    item.print_self_info()

def set01():
    for item in list01:
        item.atk += 50


set01()
for item in list01:
    print(item.atk)