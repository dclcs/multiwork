import struct
import json
import huffman

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
        print("=======================")
        print(byte)
        integer = int(byte, 2)
        print(integer)
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


def divedE(data):
    list_bytes = []
    size = len(data) / 8
    i = 0
    while i < size:
        list_bytes.append(data[i * 8: i * 8 + 8])
        i = i + 1
    return list_bytes

def refine_lists(raw):
    lists = []
    for i in raw:
        if i not in lists:
            lists.append(i)
    return sorted(lists)


def LWZ(list_bytes, dicts):
    p = ""
    result = []
    last = 256
    for c in list_bytes:
        pc = p + c
        if pc in dicts:
            p = pc
        else:
            result.append(dicts[p])
            dicts[pc] = str(last)
            last += 1
            p = c
    return result, dicts


def get_key(dict, value):
    return [k for k, v in dict.items() if v == value]

def generate_code(result):
    b_result = []
    i = 0
    code = ""
    while i < len(result):
        b_result.append(bin(result[i])[2:])
        temp = bin(result[i])[2:]
        code += temp
        i = i + 1
    return code


def decode(code, dict):
    first_code = code[0:8]
    last = 256
    print(first_code)
    raw = []
    raw.append(dict[first_code])
    sub_code = code[8:]
    print(sub_code)
    pW = first_code
    size = len(sub_code)
    i = 0
    P = ""
    C = ""
    step = 8
    while i < 1000:
        print("第%d步============",i)
        cW = sub_code[i: i + 8]
        print("cW:", cW)
        f_cW = sub_code[i: i + 16]
        print("f_cW:", f_cW)
        if f_cW in dict:
            print("cW 变成 f_cW")
            cW = f_cW
            step = 16
        print("step:", step)
        print("pW:", pW)
        if cW in dict:
            print("1")
            raw.append(dict[cW])
            P = pW[0:8]
            C = cW[0:8]
            print("P:", P)
            print("C:", C)
            dict[P+C] = last
            print(P+C, dict[P+C])
            last += 1
        else:
            print("2")
            P = pW[0:8]
            C = pW[0:8]
            dict[P+C] = last
            last += 1
            raw.append(dict[P+C])

        print("raw:",raw)
        pW = cW
        i = i + step
    return raw, dict


with open("origin_compression.txt", 'r') as f:
    s_data = f.read()


# print(s_data)
# print(type(s_data))
# print(len(s_data))
list_bytes = divedE(s_data)
# print(len(list_bytes))
refine_list = refine_lists(list_bytes)
# print(len(list_bytes))
dicts = dict(zip(refine_list, [str(i) for i in range(len(list_bytes))]))
# print(dicts)
result, dicts = LWZ(list_bytes, dicts)
print(result)
with open("result_test.dat", "w") as f:
    for i in result:
        f.write(str(i))
print("list_bytes",len(list_bytes))
print("result:", len(result))

size = len(result)
huf_dict = {}
for key in result:
    huf_dict[key] = huf_dict.get(key, 0) + 1
print(huf_dict)
codebook = []
for key, value in huf_dict.items():
    codebook.append((key, value))
print(codebook)
huff = huffman.codebook(codebook)
print(huff)
i = 0
code = ""
while i < size:
    temp = huff[result[i]]
    code += temp
    i += 1
print(len(code))
# lists = getIntegerList(code)
# transtoFile(lists, "decode.dat")
# print(len(code))
# code = generate_code(result)
# print(code)
# print(len(code) / 8)
# print(divedE(code))
# print(dicts)
# print(len(s_data))
# print(max(result))
# lists = getIntegerList(code)
# transtoFile(lists, "result.dat")
# print(bin(26506))
#
# with open("1.json", "w+") as f:
#     f.write(json.dumps(dicts)+'\n')
# decode_dict = dict(zip(refine_list, [i for i in range(len(list_bytes))]))
# raw, a= decode(code, decode_dict)
# print("raw:", raw)
# print("result:",result)
# print(raw == result)
# print(len(a))
# print(len(dicts))
# size = len(raw)
# print(a)
# print(size)
# i = 0
# print(raw)
# str1 = ""
# while i < size:
#     temp = get_key(a, raw[i])
#     print(temp[0])
#     str1 += temp[0]
#     i += 1
# print(temp)
# print("raw:", raw)
# print("result:", result)


