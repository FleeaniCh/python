"""
    {n}     匹配前面的字符出现n次
"""
import re
print(re.findall('1[0-9]{10}',"renkai:17355641830 kk:173554108830"))
print(re.findall('张.{3}',"张测井号，张无忌"))
