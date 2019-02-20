# -*- coding: utf-8 -*-
from functions import *


LZ77_WIN_SIZE = 8   #   8个码子 
MAX_BIT = max_bit(LZ77_WIN_SIZE)
data = read_from_origin()
# data = "0001001111010011100000110010001111000010111000110011001100010011110100111000001100100011110000101110001100110011"
print("data length :", len(data))
sdata = split_data(data) 
win = ["None" for i in range(LZ77_WIN_SIZE)]
NUM_DICTS = init_convert_dic(LZ77_WIN_SIZE)

# cwin = sdata[s_idx : s_idx + LZ77_WIN_SIZE] 
def get_table(win,start):
    '''
        在滑动窗口中，寻找与第一个码子相同的索引的列表
    '''
    # len = LZ77_WIN_SIZE
    s = 0
    ll = []
    while s <= LZ77_WIN_SIZE - 1:
        if win[s] == start:
          ll.append(s)
        s = s + 1
    return ll  

def compare_win(cwin, win, s_idx):
    # print("win:",win)
    # print("cwin:",cwin)
    #   匹配cwin和win的最大匹配串
    #   并且返回窗口的其实位置，长度，和未匹配串
    start = cwin[0]
    s_pos = 0
    if start not in win:
        win[0:LZ77_WIN_SIZE - 1] = win[1:]
        win[LZ77_WIN_SIZE - 1] = start
        s_idx = s_idx + 1
        flag = False
        return start,s_idx,flag
    else:
        opos = LZ77_WIN_SIZE - 1
        idx_table = get_table(win, start)
        # print("in win")
        while opos >= 0:
            search = cwin[:opos]
            # print(idx_table)
            for ii in idx_table:
                if search == win[ii:ii + opos]:
                    s_idx = opos + 1 + s_idx
                    i = ii
                    l = opos
                    # print(len(cwin))
                    # print(opos)
                    c = cwin[opos]
                    search.append(cwin[opos])
                    # print(search)
                    win[0:LZ77_WIN_SIZE - opos - 1] = win[opos + 1 :]
                    win[LZ77_WIN_SIZE - opos - 1:] = search
                    return start, [s_idx, ii, opos, c], True
            opos = opos - 1


def LZ77_decompress(data):
    
    _length = len(data)
    de_data = ""
    for i in range(_length):
        # print("#Epoch ", str(i))
        # print("Data is ", data[i])   
        # print("WIN is ", win)
        length = len(data[i])           
        if length == 8:
            de_data = de_data + data[i]
            win[0 : LZ77_WIN_SIZE - 1] = win[1:]
            win[LZ77_WIN_SIZE - 1] = data[i]
        else:
            # print(MAX_BIT)
            ii = de_convert_num(NUM_DICTS,data[i][0:MAX_BIT])
            ll = de_convert_num(NUM_DICTS,data[i][MAX_BIT:2 * MAX_BIT])
            da = data[i][2 * MAX_BIT :]
            # print("ii is ", ii)
            # print("ll is ", ll)
            rr = ""
            for idx in range(ll):
                rr = rr + win[ii + idx]
            rr = rr + data[i][2 * MAX_BIT:]
            # print(rr)
            de_data = de_data + rr
    return de_data

def LZ77_compress(data):
    length = len(data)
    compress_data = []
    s_idx = 0   # 记录处理原始数据的位置
    while s_idx <= length - 1:
        # print("### epoch idx:",s_idx)
        if LZ77_WIN_SIZE - 1 - s_idx <= 0:
            cwin = sdata[s_idx:]
        else:
            cwin = sdata[s_idx : s_idx + LZ77_WIN_SIZE + 1] 
        # compress_data.append(compare_win(cwin, win, s_idx))
        ch, pos, flag = compare_win(cwin, win, s_idx)
        if flag == False:
            s_idx = pos
            compress_data.append(ch)
        else:
            s_idx = pos[0]
            i = NUM_DICTS[pos[1]]
            l = NUM_DICTS[pos[2]]
            compress_data.append(i + l + pos[3])
        if len(win) != LZ77_WIN_SIZE:
            exit()
    return compress_data

# print(cwin)
compress_ = LZ77_compress(sdata)
print(compress_)
win = ["None" for i in range(LZ77_WIN_SIZE)]
pdata = LZ77_decompress(compress_)
print(pdata==data)
print(len(pdata))
print(len(data))
# print(pdata)
# print(compress_)
# print(compress_)
temp = ""
i = 0
while i < len(compress_):
    temp = temp + compress_[i]
    i = i + 1
# print(len(temp)/8)
with open("compress_data.txt", "w") as f:
    f.write(temp)
with open("p_data.txt", "w") as f:
    f.write(pdata)
# print(temp)