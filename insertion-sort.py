def insert(l,x):
    if (l == []):
        return [x]
    else:
        k = l[0]
        if (k < x):
            return [k] + insert(l[1:],x)
        else:
            return [x] + l
def insort(l):
    if (len(l) <= 1):
        return l
    else:
        return insert(insort(l[1:]),l[0])
