def RLe(data):
    RL_table = []
    i = 0
    while i < len(data):
        t = data[i]
        j = i + 1
        while ((j < len(data)) and (data[j] == t)):
            j = j + 1
        RL_table.append([t, j-i])
        i = j
    idx, count= RLe_refine_result(RL_table)
    return [idx, count]

def RLe_decompress(result):
    sdata = ""
    for i in range(len(result)):
        l = result[i]
        sdata = sdata + l[0] * l[1]
    return sdata

def RLe_refine_result(result):
    length = len(result)
    list_idx = []
    list_count = []
    for i in range(length):
        d = result[i]
        list_idx.append(d[0])
        list_count.append(d[1])
    return list_idx, list_count