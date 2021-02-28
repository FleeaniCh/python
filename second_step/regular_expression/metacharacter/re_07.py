"""
    ^   匹配目标字符串的开头位置
"""
import re
print(re.findall('^Jame',"Jame,hello"))
print(re.findall('^Jame',"Hi,Jame"))