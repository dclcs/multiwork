import struct
import numpy as np
from utils.functions import *
from utils.LZW import  *

def LWZ_(name="origin_compression.txt"):
    data = read_from_origin(name=name)

    sdata,diff = split_data(data)

    dicts = init_convert_dic(std=256, type="LZW")

    result, dicts = LWZ(sdata, dicts)


    # print(result)


    rs_str = convert_to_str(result)
    print(len(rs_str))
    dicts = init_convert_dic(std=256)

    de_compress = LWZ_decompress(result, dicts)

    ddata = add_(de_compress)


    if ddata == (data + diff * "0"):
        print("name" + " decompress success")
        if diff != 0:
            print("diff : ", diff)
    else:
        print(len(ddata))
        print(len(data))

    return rs_str
# result_0 = LWZ_("Re_str_0.txt")
# result_1 = LWZ_("Re_str_1.txt")
result_2 = LWZ_()
# result_3 =LWZ_("Re_str.txt")
# print(len(result_0) + len(result_1))
# print(len(result_2))
# print(len(result_3))
f = open("LWZ_result.txt","w+")
f.write(result_2)
data = read_from_origin()
