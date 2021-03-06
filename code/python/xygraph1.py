import math

r1=15
r2=7

def getV(r,n,refs,lbls,dx,dy):
    x=r*math.sin(2*math.pi/len(refs)*n)+dx
    y=r*math.cos(2*math.pi/len(refs)*n)+dy
    return "({0:4.2f},{1:4.2f})".format(x,y) + '*+[o][F-]{' + lbls[n] + '}="' + refs[n] + '"'
    
lbls1=['a','b','c','d','e']
lbls2=['f','g','h','i','j']

refs1=['a1','b1','c1','d1','e1']
refs2=['a2','b2','c2','d2','e2']

icnt1 =[[1,2],[2,3],[3,4],[4,5],[5,1]]
icnt2 =[[1,2],[2,3],[3,4],[4,5],[5,1]]
icnt23=[[1,1],[2,2],[3,3],[4,4],[5,5]]

for i in range(len(refs1)):
    print('\\POS ' + getV(r1,i,refs1,lbls1,0,0))

for i in range(len(refs2)):
    print('\\POS ' + getV(r2,i,refs2,lbls2,0,0))
    
for p in icnt1:
    print('\\POS"' + refs1[p[0]-1] + '" \\ar @{-} "' + refs1[p[1]-1] + '"')
    
for p in icnt2:
    print('\\POS"' + refs2[p[0]-1] + '" \\ar @{-} "' + refs2[p[1]-1] + '"')
    
for p in icnt23:
    print('\\POS"' + refs1[p[0]-1] + '" \\ar @{-} "' + refs2[p[1]-1] + '"')
