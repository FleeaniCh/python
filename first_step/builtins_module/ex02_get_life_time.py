# 根据生日，计算活了多少天
import time


def get_life_time(year, month, day):
    # 元组 -- > 时间戳
    birth_timestamp = time.mktime(time.strptime("%d-%d-%d" % (year, month, day), "%Y-%m-%d"))
    life_day = (time.time() - birth_timestamp) / 3600 // 24  # 计算活了多少天
    return int(life_day)


re = get_life_time(1993, 7, 2)
print(re)
