"""
    {m,n}       匹配前面的字符出现m-n次
"""
import re

print(re.findall('[1-9][0-9]{5,10}', "qq: 2316231830"))
