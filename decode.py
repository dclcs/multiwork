import struct
with open("result.dat", "rb") as f:
    data = f.read()


print(data)
print(len(data))
# print(str(data)[2:])
# print(type(data))
# a = b'\xfaw_'
# print(a)