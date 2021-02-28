"""
    匹配字符集   []
"""
import re
print(re.findall('[aeiou]','hello world'))

print(re.findall('[_#0-9a-z]','port#1998'))