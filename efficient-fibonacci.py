##efficient fibonacci calculation
##using the matrix multiplication

Q = [[0,1],[1,1]]
I = [[1,0],[0,1]]

def mul(q1,q2):
    k1 = ((q1[0])[0])*((q2[0])[0]) + ((q1[0])[1])*((q2[1])[0])
    k2 = ((q1[0])[0])*((q2[0])[1]) + ((q1[0])[1])*((q2[1])[1])
    k3 = ((q1[1])[0])*((q2[0])[0]) + ((q1[1])[1])*((q2[1])[0])
    k4 = ((q1[1])[0])*((q2[0])[1]) + ((q1[1])[1])*((q2[1])[1])
    return ([[k1,k2],[k3,k4]])

def add(q1,q2):
    k1 = (q1[0])[0] + (q2[0])[0]
    k2 = (q1[0])[1] + (q2[0])[1]
    k3 = (q1[1])[0] + (q2[1])[0]
    k4 = (q1[1])[1] + (q2[1])[1]
    return ([[k1,k2],[k3,k4]])
    
def fib(n):
    if (n == 1):
        return Q
    else:
        if (n%2 == 0):
            k = fib(n//2)
            return mul(k,k)
        else:
            k = fib(n//2)
            return mul(mul(k,k),Q)


def fibonacci(n):
    if (n == 0):
        return 1
    else:
        return (fib(n)[0])[1]
