def gcd(a,b):
    if (a < b):
        q,w,e = gcd(b,a)
        return (q,e,w)
    else:
        if (b == 0):
            return (a,1,0)
        else:
            x,y,z = gcd(b,a%b)
            return (x,z,y-z*(a//b))
