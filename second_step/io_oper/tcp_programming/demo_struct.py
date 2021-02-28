import struct

st = struct.Struct('i4sf')
data = st.pack(1, b'lily', 1.65)
print(data)

data1 = st.unpack(data)
print(data1)

data2 = struct.pack('i4sf',1,b'lily',1.65)
print(data2)

data3 = struct.unpack('i4sf',data2)
print(data3)
