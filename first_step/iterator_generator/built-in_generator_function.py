"""
    练习1：定义生成器函数my_enumerate，实现下列现象：
                将元素·与索引合成一个元组
"""
list01 = [3, 4, 55, 6, 7]


# for index, element in enumerate(list01):
#     print(index, element)

def my_enumerate(iterable_target):
    # for i in range(len(iterable_target)):
    #     yield (i, iterable_target[i])
    index = 0
    for item in iterable_target:
        yield index, item
        index += 1


re = my_enumerate(list01)
for item in re:
    print(item)

"""
    练习2：定义生成器函数my_zip，实现下列现象：
                将多个列表的每个元素合并成一个元组
"""
list02 = ["孙悟空", "猪八戒", "唐僧", "沙僧"]
list03 = [101, 102, 103, 104]

# for item in zip(list02, list03):
#     print(item)

def my_zip(iterable01, iterable02):
    for i in range(min(len(iterable01), len(iterable02))):
        yield iterable01[i], iterable02[i]

# re = my_zip(list02, list03)
# for item in re:
#     print(item)

def my_zip_01(*args):
    # 跟星号元组形参第一个参数的长度生成索引len(args[0])
    for i in range(len(args[0])):
        list_result = []
        for item in args:
            list_result.append(item[i])
        yield tuple(list_result)


re01 = my_zip_01(list02,list03)
for item in re01:
    print(item)



