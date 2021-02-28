"""
    yield -- > 生成器
"""


def my_range(stop_value):
    number = 0
    while number < stop_value:
        yield number
        number += 1


my01 = my_range(10)
print(type(my01))  # <class 'generator'>

for item in my01:
    print(item)
