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

def max_bit(num):
    return len(bin(num)[2:]) - 1

def convert_num(num,std=64):
    std_len = max_bit(std)
    _bin = bin(num)[2:]
    if len(_bin) < std_len:
        _diff = std_len - len(_bin)
        diff = "0" * _diff
        _bin = diff + _bin
    return _bin
    # print(bin(num))
def init_convert_dic(std=64):
    dicts = {}
    for i in range(std):
        # dicts.update(i=convert_num(i, std))
        dicts[i] = convert_num(i, std)
    return dicts
    
def de_convert_num(num_dic, value):
    dic_list = list(num_dic.values())

    return dic_list.index(value)

# dicts = init_convert_dic(8)
# dic_list = list(dicts.values())
# print(dic_list.index("000"))
# print(type(dicts.values()))