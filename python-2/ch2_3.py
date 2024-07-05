def mod_position(arr, s):
    lst = []
    for i in range(len(arr)):
        if (i+1)%(int(s)) == 0:
            lst.append(arr[i])
    return lst