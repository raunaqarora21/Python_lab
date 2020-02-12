a=int(input())
x=a
l=97+a
b=[]
for i in range(1,a):
    print((2*x-2)*('-'),end='')
    y=a
    #print(y,end='')
    z=0
    for  j in range(1,i+1):
        
        print(chr(96+y-z)+'-',end='')
        z=z+1
        
        r=0
    for k in range(1,i):
        print(chr(l+r)+'-',end='')
        r+=1
    l-=1
    if i!=a:
        print((2*(x-1)-1)*('-'),end='')
    x=x-1
    print()
for i in range(a):
    b.append(chr(96+a-i))
for i in range(1,a):
    b.append(chr(97+i))
print(*b,sep='-')
    

x=1
l=99

for i in range(a-1,0,-1):
    print((2*x)*('-'),end='')
    y=a
    #print(y,end='')
    z=0
    for  j in range(1,i+1):
        
        print(chr(96+y-z)+'-',end='')
        z=z+1
        
        r=0
    for k in range(1,i):
        print(chr(l+r)+'-',end='')
        r+=1
    l+=1
    if i!=a:
        print((2*x-1)*('-'),end='')
    x=x+1
    print()
