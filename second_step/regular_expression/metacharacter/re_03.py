"""
    匹配其中之一      |
"""
import re

print(re.findall('http|https', 'https://www.7net.cc'))
print(re.findall('com|cn', 'https://www.7net.com.cn'))
