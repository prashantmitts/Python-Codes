def search(l,i):
    if(len(l) == 1):
        if(l[0] == i):
            return 0
        else:
            return -1
    x = len(l)//2
    if(l[x] == i):
        return x
    if(l[x] > i):
        return search(l[:x],i)
    k = search(l[x:],i)
    if(k != -1):
        return x + k
    else:
        return -1
