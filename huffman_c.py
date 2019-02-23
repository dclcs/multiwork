import huffman
from utils.functions import *
data = read_from_origin()
sdata,_ = split_data(data)
count_ = {}
for i in range(len(sdata)):
    if sdata[i] not in count_:
        count_[sdata[i]] = 1
    else:
        count_[sdata[i]] = count_[sdata[i]] + 1

codebook_ = convert_to_codebook(count_)

print(codebook_)

dic = huffman.codebook(codebook_)

str_ = ""

for i in range(len(sdata)):
    str_ = str_ + dic[sdata[i]]
print(len(str_))
print(str_)
f = open("huffman.txt","w+")
f.write(str_)