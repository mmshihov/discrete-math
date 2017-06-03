import math

sdx=25
sdy=40

dx1=1
dx2=0.5
dx3=1.5
dx4=1

dx = dx1+dx2+dx3+dx4

dy1=2
dy2=1
dy3=1
dy4=1
dy5=2

dy = dy1+dy2+dy3+dy4+dy5

ents=[]
ents[0:0]=[[0, (dy1+dy2+dy3+dy4+dy5)*sdy/dy]]
ents[1:1]=[[0, (dy2+dy3+dy4+dy5)*sdy/dy]]
ents[2:2]=[[(dx1+dx2)*sdx/dx, (dy3+dy4+dy5)*sdy/dy]]
ents[3:3]=[[(dx1+dx2+dx3)*sdx/dx, (dy3+dy4+dy5)*sdy/dy]]
ents[4:4]=[[(dx1+dx2+dx3+dx4)*sdx/dx, (dy2+dy3+dy4+dy5)*sdy/dy]]
ents[5:5]=[[(dx1+dx2+dx3+dx4)*sdx/dx, (dy4+dy5)*sdy/dy]]
ents[6:6]=[[(dx1)*sdx/dx, (dy5)*sdy/dy]]
ents[7:7]=[[(dx1+dx2)*sdx/dx, 0]]


for i in range(6):
    ents[i+8:i+8] = [[-(ents[2+i])[0],(ents[2+i])[1]]]

links=[
    [0,1],
    [12,6],
    [13,7],
    [0,4],[0,10],
    [4,5],[10,11],
    [4,3],[10,9],
    [5,3],[11,9],
    [2,3],[8,9],
    [1,2],[1,8],
    [2,6],[8,12],
    [5,7],[11,13],
    [6,7],[12,13],
]    
    
def getV(x,y,lbl,ref):
    return "({0:4.2f},{1:4.2f})".format(x,y) + '*+[o][F-]{' + lbl + '}="' + ref + '"'
    
def getP(ref1,ref2):
    return '"' + ref1 + '" \\ar @{-} "' + ref2 + '"'
    
print('{\\shorthandoff{"}')    
print('    \\begin{xy}')    

for i in range(len(ents)):
    print("        \\POS " + getV((ents[i])[0],(ents[i])[1],chr(ord("a")+i),"l{0}".format(i)))
    
for link in links:
    print("        \\POS " + getP("l{0}".format(link[0]), "l{0}".format(link[1])))
    
print('    \\end{xy}')
print('\\shorthandon{"}}')    
    