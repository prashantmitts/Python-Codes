import time
def eratosthenes(n):
    multiples = {}
    l = []
    for i in range(2, n+1):
        if ~(i in multiples):
            l += [i]
            for j in range(i*i, n+1, i):
                multiples[j] = 1
    return l
start = time.time()
primes = eratosthenes(1000000)
print(time.time() - start)

