"""
    定义函数，根据年月日返回星期数
"""
import time


def get_week_day(year, month, day):
    tuple_time = time.strptime("%d-%d-%d" % (year, month, day), "%Y-%m-%d")  # 注意时间元组中的format
    week_day_dict = {
        "0": "星期一",
        "1": "星期二",
        "2": "星期三",
        "3": "星期四",
        "4": "星期五",
        "5": "星期六",
        "6": "星期日"
    }
    week_day = week_day_dict[str(tuple_time[6])]
    return week_day


re = get_week_day(2020, 12, 28)
print(re)
