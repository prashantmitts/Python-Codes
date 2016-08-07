def quicksort(l):
    if (len(l) <= 2):
        l.sort()
        return l
    else:
        i = 1
        j = 1
        k = len(l)-1
        c = 1
        while (c < len(l)):
            if (l[i] > l[0]):
                l[k],l[i] = l[i],l[k]
                k -= 1
            else:
                l[j],l[i] = l[i],l[j]
                j += 1
                i += 1
            c += 1
        print(l)
        return(quicksort(l[1:j]) + [l[0]] +quicksort(l[j:]))
    
        
