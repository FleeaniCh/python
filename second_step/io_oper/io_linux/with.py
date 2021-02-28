"""
    with.py
    使用with语句打开文件
"""

with open('dict.txt') as f:
    data = f.read()
    print(data)

# with语句块结束 f对象被自动销毁