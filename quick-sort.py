##quick sort
def quicksort(l):
    if (len(l) <= 1):
        return l
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
        return (quicksort(a) + [piv] + quicksort(b))
