"""
    +   匹配前面的字符出现1次或多次
"""
import re
print(re.findall('[A-Z][a-z]+',"How are you? Fine, Thank you"))