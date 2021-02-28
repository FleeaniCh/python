import re

s = "任凯：renkai@7net.cc"

print(re.findall('\w+@\w+\.cc',s))
