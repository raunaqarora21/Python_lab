m=list(map(int,input().split(',')))
n=list(map(int,input().split(',')))
l=[]
def bitwise_And(x):
    global m
    global n
    if x == len(m):
        return l
    else:
        l.append(m[x]&n[x])
        bitwise_And(x+1)
r=bitwise_And(0)
print(l)
