import time

def fib(n):
    i=0
    f0=0
    f1=1
    while i < n:
        i += 1
        t = f1
        f1 += f0
        f0 = t
    return f0
    
for n in range(1000):
    start = time.clock()
    r = fib(n)
    end = time.clock()
    print("fib({0})={1}, time={2}".format(n, r, end-start))
    
