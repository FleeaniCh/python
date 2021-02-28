"""
    时间处理
"""
import time

# 1.获取当前时间戳(从1970年1月1日到现在经过的秒数)
print(time.time())  # 1608817711.6334562

# 2.时间元组
# 时间戳 --> 时间元组
print(time.localtime(1608817711.6334562))
# 通过元组的操作获取时间
tuple_time = time.localtime()
# for item in tuple_time:
#     print(item)
print(tuple_time[1])

# 通过类的操作获取时间
print(type(tuple_time))
# print(time.struct_time)
print(tuple_time.tm_year)

# 时间元组 --> 时间戳
print(time.mktime(tuple_time))

# 3.时间元组 --> str
str_time01 = time.strftime("%y/%m/%d %H:%M:%S",tuple_time)
print(str_time01)

# str --> 时间元组
print(time.strptime(str_time01,"%y/%m/%d %H:%M:%S"))