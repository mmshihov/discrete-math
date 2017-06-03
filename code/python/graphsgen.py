import math

def getV(r,n,refs,lbls,dx,dy):
    x=r*math.sin(2*math.pi/len(refs)*n)+dx
    y=r*math.cos(2*math.pi/len(refs)*n)+dy
    return "({0:4.2f},{1:4.2f})".format(x,y) + '*+[o][F-]{' + lbls[n] + '}="' + refs[n] + '"'
    
lbls1=['1','2','3','4','5','6','7']
lbls2=['a','b','c','d','e','f','g']

refs1=['a1','b1','c1','d1','e1','f1','g1']
refs2=['a2','b2','c2','d2','e2','f2','g2']

icnt1=[[1,2],[1,3],[1,6],[1,7],[2,7],[2,3],[2,4],[3,4],[3,5],[4,5],[4,6],[5,6],[5,7],[6,7]]
icnt2=[[1,2],[1,4],[2,3],[2,5],[3,4],[3,6],[4,5],[4,7],[5,6],[5,1],[6,7],[6,2],[7,1],[7,3]]

for i in range(len(refs1)):
    print('\\POS ' + getV(15,i,refs1,lbls1,0,0))

for i in range(len(refs2)):
    print('\\POS ' + getV(15,i,refs2,lbls2,40,0))
    
for p in icnt1:
    print('\\POS"' + refs1[p[0]-1] + '" \\ar @{-} "' + refs1[p[1]-1] + '"')
    
for p in icnt2:
    print('\\POS"' + refs2[p[0]-1] + '" \\ar @{-} "' + refs2[p[1]-1] + '"')
