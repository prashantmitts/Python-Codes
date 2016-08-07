##program to fing the median
def findmedian(l,n):
    if (len(l) <= 1):
        return l[0]
    else:
        piv = l[0]
        l = l[1:]
        a = []
        b = []
        i = 0
        while (i < len(l)):
            if (l[i] <= piv):
                a += [l[i]]
            else:
                b += [l[i]]
            i += 1
        if (len(a) == n):
            return piv
        elif (len(a) > n):
            return findmedian(a,n)
        else:
            return findmedian(b,n-len(a)-1)
