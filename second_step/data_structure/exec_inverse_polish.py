"""
    逆波兰表达式(dc)
"""
from sstack import *
st = SStack()

while True:
    exp = input("dc\n")
    tmp = exp.split(' ')
    for i in tmp:
        if i not in ['+','-','*','/','p']:
            st.push(float(i))
        elif i == '+':
            y = st.pop()
            x = st.pop()
            st.push(x+y)
        elif i == '-':
            y = st.pop()
            x = st.pop()
            st.push(x-y)
        elif i == '*':
            y = st.pop()
            x = st.pop()
            st.push(x*y)
        elif i == '/':
            y = st.pop()
            x = st.pop()
            st.push(x/y)
        elif i == 'p':
            print(st.top())
