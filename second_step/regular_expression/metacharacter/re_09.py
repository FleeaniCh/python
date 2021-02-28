"""
    *   匹配前面的字符出现0次或多次
"""
import re

print(re.findall('wo*',"wooooooooooo~~w!")) # o 重复0次或多次

print(re.findall('[a-zA-Z]*',"How are you?"))
print(re.findall('[0-9]*',"I'm 18"))

print(re.findall('[A-Z][a-z]*',"How are you? Fine Jame"))
