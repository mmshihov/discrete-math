import time

def fib(n):
    if n == 0:
        return 0
    (f1, f0) = fibFast(n)
    return f1
    
def fibFast(n):
    if n == 1:
        return (1, 0)
    if n % 2 == 0:
        m = n/2
        (fm1, fm0) = fibFast(m)
        fm1sqr = fm1*fm1
        return (fm1sqr + 2*fm1*fm0, fm1sqr + fm0*fm0)
    else:
        m=(n-1)/2
        (fm1, fm0) = fibFast(m)
        fm1sqr = fm1*fm1
        fn1 = fm1sqr + 2*fm1*fm0
        fn0 = fm1sqr + fm0*fm0
        return (fn0 + fn1, fn1)
        
for n in range(1000):
    start = time.clock()
    r = fib(n)
    end = time.clock()
    print("fib({0})={1}, time={2}".format(n, r, end-start))
    
