list01 = [3, "54", True, 4556, 6, "76", 1.6, False, 3.5]

# 生成器函数
def find01():
    for item in list01:
        if type(item) == int:
            yield item


re01 = find01()  # <generator object find01 at 0x0000000002154570>
for item in re01:
    print(item)

# 生成器表达式
# 此时没有计算，更没有结果
print("-------生成器表达式--------")
re02 = (item for item in list01 if type(item) == int)
# print(re02)  # <generator object <genexpr> at 0x00000000027645E8>
# 循环一次,计算一次,返回一次
for item in re02:
    print(item)

# 列表推导式
# 此时已完成所有计算，得到所有结果
print("--------列表推导式-----------")
re03 = [item for item in list01 if type(item) == int]
for item in re03:
    print(item)

# 1.获取列表中所有字符串
# 2.获取列表中所有小数
# 要求：分别使用生成器函数，生成器表达式，列表表达式实现
def get_str(iterable_target):
    for item in iterable_target:
        if type(item) == str:
            yield item

print("----------------字符串----------------")
re04 = get_str(list01)
for item in re04:
    print(item)

print("------------生成器表达式------------")
re05 = (item for item in list01 if type(item)==str)
for item in re05:
    print(item)

print("-------------列表表达式----------------")
re05 = [item for item in list01 if type(item)==str]
print(re05)

