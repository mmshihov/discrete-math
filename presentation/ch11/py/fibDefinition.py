import time

def fib(n):
    if n == 0: 
        return 0
    if n == 1: 
        return 1
    return fib(n-1) + fib(n-2)
    
for n in range(1000):
    start = time.clock()
    r = fib(n)
    end = time.clock()
    print("fib({0})={1}, time={2}".format(n, r, end-start))
    
