##count-inversions in an array
def merge(l1,l2):
    if (l1 == []):
        return (l2,0)
    elif (l2 == []):
        return (l1,0)
    else:
        if (l1[0] <= l2[0]):
            c1,c2 = merge(l1[1:],l2)
            return ([l1[0]] + c1,c2)
        else:
            c1,c2 = merge(l1,l2[1:])
            return ([l2[0]]+c1,c2 + len(l1))
def countInversions(l):
    if (len(l) <= 1):
        return (l,0)
    else:
        n = len(l)
        a1,a2 = countInversions(l[:n//2])
        b1,b2 = countInversions(l[n//2:])
        c1,c2 = merge(a1,b1)
        return (c1,c2+b2+a2)
