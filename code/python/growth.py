#рост функций
import math
ns=[1,2,4,5,10,20,40,60,80,100]

print("\\begin{tabular}{||r||r|r|r|r|r|r|}")
print("\\hline\hline")
print("$n$ & $\\log_2n$ & $n$ & $n\\log_2n$ & $n^2$ & $n^3$ & $2^n$\\\\ \\hline\\hline")

for n in ns:

    c1=math.log(n,2)
    c2=n
    c3=n*c1
    c4=n*n
    c5=n*n*n
    c6=2**n
    
    print("{0:3d} & {1:4.2f} & {2:3d} & {3:7.2f} & {4:5d} & {5:7d} & {6:33d}\\\\".format(n,c1,c2,c3,c4,c5,c6))
    
print("\\hline")
print("\\end{tabular}")
    