# 练习1：从列表[4,5,566,7,8,10]中选出所有的偶数
# 结果存入另外一个列表中
# 使用生成器实现
list01 = [4, 5, 566, 7, 8, 10]


def get_even_01():
    even_list = []
    for item in list01:
        if item % 2 == 0:
            even_list.append(item)
    return even_list


# print(get_even_01())

def get_even_02():
    for item in list01:
        if item % 2 == 0:
            yield item


for item in get_even_02():
    print(item)
