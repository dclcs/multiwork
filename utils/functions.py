import numpy as np
import struct

def read_from_origin(name="origin_compression.txt"):
    with open(name, 'r') as f:
        source = f.read()
    return source

def split_data(data):
    folds = []
    ys = len(data) % 8
    if ys != 0:
        ys = 8 - ys
        #  如果不能被8除则后续补零
        data += "0" * ys
    size = len(data)
    num_folds = int(size / 8)
    i = 0
    index_split = np.array_split(np.arange(size),indices_or_sections=num_folds)
    for i in index_split:
        cell = data[i[0]:i[-1] + 1]
        folds.append(cell)
    return folds,ys

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

def init_convert_dic(std=64, type="LZ77"):
    dicts = {}
    for i in range(std):
        if type == 'LZW':
            # dicts[i] = convert_num(i, std)
            dicts[convert_num(i, std)] = i
        if type == 'LZW_d':
            dicts[bin(i)[2:]] = convert_num(i, std)
        else:
            dicts[i] = convert_num(i, std)
    return dicts
    
def de_convert_num(num_dic, value):
    dic_list = list(num_dic.values())

    return dic_list.index(value)

# dicts = init_convert_dic(8)
# dic_list = list(dicts.values())
# print(dic_list.index("000"))
# print(type(dicts.values()))

def add_(list_):
    r = ""
    for i in range(len(list_)):
        r = r + list_[i]
    return r

def generate_result(str_b):
    scode,_ = split_data(str_b)
    size = len(scode)
    
    with open('result.txt', 'wb+') as f:
        i = 0
        while i < size:
            wb = struct.pack('B', int(scode[i],2))
            f.write(wb)
            i = i + 1
    print("...result.txt")

def convert_to_codebook(dics):
    keys = list(dics.keys())
    values = list(dics.values())
    codebook = []
    for i in range(len(dics)):
        codebook.append((str(keys[i]), values[i]))
    return codebook

