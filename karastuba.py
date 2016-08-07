import math
##karastuba multiplication
def mul(a,b):
    if ((a <= 10) or (b <= 10)):
        return (a*b)
    else:
        n1 = 10**((math.ceil(math.log10(a)))//2)
        n2 = 10**((math.ceil(math.log10(b)))//2)
        n = min(n1,n2)
        a1 = a//n
        a2 = a%n
        b1 = b//n
        b2 = b%n
        n1 = mul(a1,b1)
        n2 = mul(a2,b2)
        return (n1*n*n + (mul(a1+a2,b1+b2)- n1 - n2)*n + n2)
