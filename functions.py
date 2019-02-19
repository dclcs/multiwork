import numpy as np


def read_from_origin():
    with open("origin_compression.txt", 'r') as f:
        source = f.read()
    return source

def split_data(data):
    folds = []
    ys = len(data) % 8
    if ys != 0:
        #  如果不能被8除则后续补零
        data += "0" * ys
        print("补充的0的个数:",ys)
    size = len(data)
    num_folds = int(size / 8)
    i = 0
    index_split = np.array_split(np.arange(size),indices_or_sections=num_folds)
    for i in index_split:
        cell = data[i[0]:i[-1] + 1]
        folds.append(cell)
    return folds