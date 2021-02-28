"""
    ?   匹配前面的字符出现0次或1次
"""
import re
print(re.findall('-?[0-9]+',"167 -28,29 -8"))

print(re.findall('[^ ]+',"Port-9 Error #404# %@STD"))