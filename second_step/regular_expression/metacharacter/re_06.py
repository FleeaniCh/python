"""
    匹配字符集之外的任意一个字符    ^
"""
import re
print(re.findall('[^_#0-9a-z]',"Port-18"))