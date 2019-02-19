from functions import *




LZ77_WIN_SIZE = 32   #   8个码子

data = read_from_origin()

sdata = split_data(data)

# 

win = ["None" for i in range(LZ77_WIN_SIZE)]

# cwin = sdata[s_idx : s_idx + LZ77_WIN_SIZE] 

def get_table(win,start):
    # len = LZ77_WIN_SIZE
    s = 0
    ll = []
    while s <= LZ77_WIN_SIZE - 1:
        if win[s] == start:
          ll.append(s)
        s = s + 1
    return ll  

def convert(num):
    if num == 1:
        return "001"
    elif num == 2:
        return "010"
    elif num == 3:
        return "011"
    elif num == 4:
        return "100"
    elif num == 5:
        return "101"
    elif num == 6:
        return "110"
    elif num == 7:
        return "111"
    elif num == 0:
        return "000"

def convert_l(num):
    if num == 1:
        return "001"
    elif num == 2:
        return "010"
    elif num == 3:
        return "011"
    elif num == 4:
        return "100"
    elif num == 5:
        return "101"
    elif num == 6:
        return "110"
    elif num == 7:
        return "111"
    elif num == 8:
        return "000"

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

def LZ77_compress(data):
    length = len(data)
    compress_data = []
    s_idx = 0   # 记录处理原始数据的位置
    while s_idx <= length - 1:
        # print("### epoch idx:",s_idx)
        if LZ77_WIN_SIZE - 1 - s_idx < 0:
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
            # i = convert(pos[1])
            # l = convert_l(pos[2])
            i = str(pos[1])
            l = str(pos[2])
            compress_data.append(i + l + pos[3])
        # print("")
        # print("result,win:",win)
        if len(win) != LZ77_WIN_SIZE:
            exit()
        # print("compress_data:",compress_data)
    return compress_data

# print(cwin)
compress_ = LZ77_compress(sdata)
# print(win)
# print(compress_)
# s = compare_win(cwin,win)

print(len(compress_))
temp = ""
i = 0
while i < len(compress_):
    temp = temp + compress_[i]
    i = i + 1
print(len(temp))