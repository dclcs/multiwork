import struct
import numpy as np
from utils.functions import *
from utils.LZW import  *
import huffman
MAX_BIT = 12

def get_max_str(s_pos, t,dicts):
    i = MAX_BIT
    while i >= 0:
        # print("## Epoch :", i)
        pstr = t[s_pos : s_pos + i]
        # print("pstr is ", pstr)
        # if pstr.startswith('0') == True:
        #     return [False]
        # print(pstr.startswith('0'))
        if pstr in dicts: 
                        
            # print("#in,", int(pstr, 2))
            return [True, pstr, len(pstr)]
        i = i - 1  
    return [False]
    
def dec_(rs_str):
    print("decompress length", len(rs_str))
    MAX_BIT = 12
    flag = MAX_BIT
    dicts = init_convert_dic(std=256, type="LZW_d")

    i = 0
    while i < len(rs_str):
        r_ = get_max_str(i, rs_str, dicts)
        print(r_)
        
        i = i + r_[2]
        
    pass

data = read_from_origin(name="huffman.txt")

sdata,diff = split_data(data)

dicts = init_convert_dic(std=256, type="LZW")

result, dicts = LWZ(sdata, dicts)


# print(result)
rs_str = convert_to_str(result)

dicts_d = init_convert_dic(std=256)

de_compress = LWZ_decompress(result, dicts_d)

ddata = add_(de_compress)


if ddata == (data + diff * "0"):
    print("name" + " decompress success")
    if diff != 0:
        print("diff : ", diff)
else:
    print(len(ddata))
    print(len(data))

print(len(rs_str))
# print(result)
# print(15 * len(result))
# print(len(data))
count_result = {}
for i in range(len(result)):
    if result[i] not in count_result:
        count_result[result[i]] = 1
    else:
        count_result[result[i]] = count_result[result[i]] + 1

codebook = convert_to_codebook(count_result)

huf_dic = huffman.codebook(codebook)

str_ = ""


print(max(result))
for i in  range(len(result)):
    str_ = str_ + huf_dic[str(result[i])]
print(len(str_))
# generate_result(str_)
# f = open("t_result_1.txt","w+")
# f.write(str_)
# print(len(data))
# result_0 = LWZ_("Re_str_0.txt")
# result_1 = LWZ_("Re_str_1.txt")
# result_3 =LWZ_("Re_str.txt")
# print(len(result_0) + len(result_1))
# print(len(result_2))
# print(len(result_3))
# f = open("LWZ_result.txt","w+")
# f.write(result_2)
# data = read_from_origin()
# # v = list(dicts.values())
# l = {}
# for i in result:
#     if i not in l:
#         l[i] = 1
#     else:
#         l[i] = l[i] + 1
# print(l)
# print(result)
# # print(len(result))
# len_r = []
# len_st = ""
# sniff = ""
# sniff_0 = []
# for i in range(len(result)):
#     s = bin(result[i])[2:]
#     t = len(s)
#     t_ = ""
#     if t == 1:
#         t_ = "1"
        
#     else:
#         t_ = "1" + "0" * (t - 1)
#     sniff = sniff + t_
#     len_r.append(t)
#     sniff_0.append(t-1)
#     len_st = len_st + bin(result[i])[2:]

# print(len_r)
# print(sum(len_r[:2]))
# print(len(rs_str))
# print(len(sniff))
# f = open("sniff_lzw.txt","w+")
# f.write(sniff+rs_str)
# print(max(sniff_0))
# generate_result(sniff+rs_str)
# print(max(len_r))
# print(len(rs_str))
# # print(len(len_st))
# # print(len(data))
# # f = open("st.txt","w+")
# # f.write(len_st)
# # length = len(rs_str)

# count_len = {}
# for i in range(len(len_r)):
#     if len_r[i] not in count_len:
#         count_len[len_r[i]] = 1
#     else:
#         count_len[len_r[i]] = count_len[len_r[i]] + 1
# len_code_book = convert_to_codebook(count_len)
# huffman_code = huffman.codebook(len_code_book)
# print(len_code_book)
# print(huffman_code)
# str_len = ""
# for i in range(len(len_r)):
#     str_len = str_len + huffman_code[str(len_r[i])]
# print(len(str_len))
# f = open("st.txt","w+")
# f.write(str_len)



