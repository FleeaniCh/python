"""
    空洞文件
"""
f = open('test.py','wb')

f.write(b'start')
f.seek(1024*1024,2) # 从结尾向后移动1MB
f.write(b'end')

f.close()