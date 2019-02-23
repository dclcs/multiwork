from utils.functions import *
from utils.RLe import *
data = read_from_origin(name="LWZ_result.txt")
# data = read_from_origin()

result = RLe(data)
item = result[0]
count = result[1]
import huffman
# dic = init_convert_dic(max(count) + 1)
# print(max(count))
# compress_data =""
# for i in range(len(item)):
#     compress_data = compress_data + item[i] + dic[count[i]]
# print(len(compress_data))
# print(len(data))
def refine_count(count_0):
    dic_count_0 = {}
    for ite in count_0:
        if ite not in dic_count_0:
            dic_count_0[ite] = 1
        else:
            dic_count_0[ite] += 1
    return dic_count_0
def convert_to_codebook(dics):
    keys = list(dics.keys())
    values = list(dics.values())
    codebook = []
    for i in range(len(dics)):
        codebook.append((str(keys[i]), values[i]))
    return codebook
start = item[0]
count_0 = []
_count_0 = 0
count_1 = []
_count_1 = 0
for i in range(len(item)):
    if item[i] == '0':
        count_0.append(count[i])
        _count_0 = _count_0 + 1
    elif item[i] == '1':
        count_1.append(count[i])
        _count_1 = _count_1 + 1


dic_count_0 = refine_count(count_0)
dic_count_1 = refine_count(count_1)

codebook_0 = convert_to_codebook(dic_count_0)
codebook_1 = convert_to_codebook(dic_count_1)
# print(codebook_1)
r_0 = huffman.codebook(codebook_0)
r_1 = huffman.codebook(codebook_1)
# print(r_0)
str_0 = ""
for i in range(len(count_0)):
    str_0 = str_0 + r_0[str(count_0[i])]
str_1 = ""
for i in range(len(count_1)):
    str_1 = str_1 + r_1[str(count_1[i])]

# print(len(str_0))
# print(len(str_1))
# f = open("Re_str_0.txt", "w+")
# f.write(str_0)
# f = open("Re_str_1.txt","w+")
# f.write(str_1)
# f = open("Re_str.txt",'w+')
# f.write(str_0+str_1)
if start == '0':
    str_ = str_0 + str_1
elif start == '1':
    str_ = str_1 + str_0
s_0 = len(str_0)
s_1 = len(str_1)
if s_0 > s_1:
    comp = "0"
    diff = s_0 - s_1
else:
    comp = "1"
    diff = s_1 - s_0
diff = bin(diff)[2:]
prefix = start + comp + diff

f = open(".dict","w+")
f.write(str(r_1))
f.write(str(r_0))

generate_result(prefix+str_)