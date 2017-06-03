import math

r1=10
r2=20
r3=25
r4=35

def getV(r,n,refs,lbls,dx,dy):
    x=r*math.sin(2*math.pi/len(refs)*n)+dx
    y=r*math.cos(2*math.pi/len(refs)*n)+dy
    return "({0:4.2f},{1:4.2f})".format(x,y) + '*++[o][F-]{' + lbls[n] + '}="' + refs[n] + '"'
    
def getVr(r,n,refs,lbls,dx,dy):
    x=r*math.sin(math.pi+2*math.pi/len(refs)*n)+dx
    y=r*math.cos(math.pi+2*math.pi/len(refs)*n)+dy
    return "({0:4.2f},{1:4.2f})".format(x,y) + '*++[o][F-]{' + lbls[n] + '}="' + refs[n] + '"'
    
lbls=['','','','','']

refs1=['a1','b1','c1','d1','e1']
refs2=['a2','b2','c2','d2','e2']
refs3=['a3','b3','c3','d3','e3']
refs4=['a4','b4','c4','d4','e4']


icnt1  =[[1,2],[2,3],[3,4],[4,5],[5,1]]
icnt4  =[[1,2],[2,3],[3,4],[4,5],[5,1]]

icnt1_2=[[1,1],[2,2],[3,3],[4,4],[5,5]]
icnt3_4=[[1,1],[2,2],[3,3],[4,4],[5,5]]

icnt2_3 =[
    [1,4],
    [2,5],
    [3,1],
    [4,2],
    [5,3],
    [1,3],
    [2,4],
    [3,5],
    [4,1],
    [5,2],
]


for i in range(len(refs1)):
    print('\\POS ' + getVr(r1,i,refs1,lbls,0,0))
for i in range(len(refs2)):
    print('\\POS ' + getVr(r2,i,refs2,lbls,0,0))
    
for i in range(len(refs3)):
    print('\\POS ' + getV(r3,i,refs3,lbls,0,0))
for i in range(len(refs4)):
    print('\\POS ' + getV(r4,i,refs4,lbls,0,0))

for p in icnt1:
    print('\\POS"' + refs1[p[0]-1] + '" \\ar @{-} "' + refs1[p[1]-1] + '"')
    
for p in icnt4:
    print('\\POS"' + refs4[p[0]-1] + '" \\ar @{-} "' + refs4[p[1]-1] + '"')
    
for p in icnt1_2:
    print('\\POS"' + refs1[p[0]-1] + '" \\ar @{-} "' + refs2[p[1]-1] + '"')
    
for p in icnt3_4:
    print('\\POS"' + refs3[p[0]-1] + '" \\ar @{-} "' + refs4[p[1]-1] + '"')
    
for p in icnt2_3:
    print('\\POS"' + refs2[p[0]-1] + '" \\ar @{-} "' + refs3[p[1]-1] + '"')
