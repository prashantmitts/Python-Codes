def selsort(l):
    if (len(l) <= 1):
        return l
    else:
        k = min(l)
        l.remove(k)
        return [k] + selsort(l)
