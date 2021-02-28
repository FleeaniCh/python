# 练习1：使用迭代器原理遍历元组
# ("铁扇公主","铁锤公主","扳手王子")
tuple01 = ("铁扇公主", "铁锤公主", "扳手王子")
tuple01_iteration = tuple01.__iter__()
while True:
    try:
        key = tuple01_iteration.__next__()
        print(key)
    except StopIteration:
        break


# 练习2：不使用for，获取字典所有数据
# {"铁扇公主":101,"铁锤公主":102,"扳手王子":103}
dict01 = {"铁扇公主":101,"铁锤公主":102,"扳手王子":103}
dict01_iteration = dict01.__iter__()
while True:
    try:
        key = dict01_iteration.__next__()#默认获取key
        print(key,dict01[key])
    except StopIteration:
        break

