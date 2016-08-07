def merge(l1,l2):
    if (l1 == []):
        return l2
    elif (l2 == []):
        return l1
    else:
        k1 = l1[0]
        k2 = l2[0]
        if (k1 < k2):
            return [k1] + merge(l1[1:],l2)
        else:
            return [k2] + merge(l1,l2[1:])
def mergesort(l):
    n = len(l)
    if (n <= 1):
        return l
    else:
        return merge(mergesort(l[:n//2]),mergesort(l[n//2:]))
