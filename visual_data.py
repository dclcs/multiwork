import struct
import json
import huffman
import matplotlib.pyplot as plt
import numpy as np
import matplotlib

matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['axes.unicode_minus'] = False


def getIntegerList(t_data):
    folds = []
    ys = len(t_data) % 8
    if ys != 0:
        t_data += "0" * ys
    size = len(t_data)
    num_folds = int(size / 8)
    i = 0
    # # index_split = np.array_split(np.arange(size),indices_or_sections=num_folds)
    while i < num_folds:
        byte = t_data[i * 8: i * 8 + 8]

        integer = int(byte, 2)
        folds.append(integer)
        i = i + 1
    return folds


def transtoFile(folds, name):
    size = len(folds)
    with open(name, "wb+") as f:
        i = 0
        while i < size:
            wb = struct.pack('B', folds[i])
            f.write(wb)
            i = i + 1


with open("origin_compression.txt", 'r') as f:
    s_data = f.read()

data = np.random.randn(10000)
# print(s_data)
i_data = getIntegerList(s_data)

print(i_data)
print("i_data 的长度：",len(i_data))
# print(list(set(i_data)))
r = []
for i in range(len(i_data)):
    if i_data[i] not in r:
        r.append(i_data[i])
print(r)
print("r 的长度：", len(r))
counts = [0] * 256
for i in range(len(i_data)):
    counts[i_data[i]] = counts[i_data[i]] + 1
print(counts)
print("counts 的长度：", len(counts))

l = np.arange(0, 256)
plt.barh(l, counts, fc='b')
plt.xlabel("0-256")
plt.ylabel("次数")
plt.savefig('visual_data.png')
plt.show()