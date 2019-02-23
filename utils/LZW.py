from utils.functions import *
import struct
def LWZ(list_bytes, dicts):
    p = ""
    result = []
    last = 256
    for i in range(len(list_bytes)):
        c = list_bytes[i]
        pc = p + c
        if pc in dicts:
            p = pc
        else:
            result.append(dicts[p])
            dicts[pc] = last
            last += 1
            p = c
    result.append(dicts[p])
    return result, dicts

def LWZ_decompress(compress_data, dicts):
    length = len(compress_data)
    result = []
    last = 256
    for i in range(length):
        
        cW = compress_data[i]
        if i == 0:
            pW = cW
            result.append(dicts[cW])
        else:
            if cW in dicts:
                result.append(dicts[cW])
                P = dicts[pW]
                C = dicts[cW][0:8]
                dicts[last] = P + C
                last = last + 1
            else:
                P = dicts[pW]
                C = dicts[pW][0:8]
                dicts[last] = P + C
                last = last + 1
                result.append(P+C)
            pW = cW
    return result

def convert_to_byte(result):
    b_result = []
    i = 0
    code = ""
    while i < len(result):
        b_result.append(bin(result[i])[2:])
        i = i + 1
    return b_result
def convert_to_str(result):
    byte = convert_to_byte(result)
    str_b = add_(byte)
    return str_b

def convert_to_(result):
    byte = convert_to_byte(result)
    str_b = add_(byte)
    scode = split_data(str_b)
    size = len(scode)
    with open('lzz_result.txt', 'wba+') as f:
        i = 0
        while i < size:
            wb = struct.pack('B', int(scode[i],2))
            f.write(wb)
            i = i + 1
    print("...lzz_result.txt")
    