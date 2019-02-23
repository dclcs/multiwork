import struct
import numpy as np
from utils.functions import *
from utils.LZW import  *
import huffman


data = read_from_origin(name="sniff_lzw.txt")
print(len(data))
sdata,diff = split_data(data)
print(sdata)
dicts = init_convert_dic(std=256, type="LZW")

result, dicts = LWZ(sdata, dicts)
rs_str = convert_to_str(result)

len_r = []
len_st = ""
for i in range(len(result)):
    s = bin(result[i])[2:]
    t = len(s)
    len_r.append(t)
    len_st = len_st + bin(result[i])[2:]
print(len(rs_str))
