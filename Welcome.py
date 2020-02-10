a=input().split()
c,d=a
n=eval(c)
m=eval(d)
k=(n-1)//2
x=(m-3)//6
y=1
z=0
for i in range(k):
    print(x*('---')+y*('.|.')+z*('.|.')+x*('---'),end='')
    x-=1
    y+=1
    z+=1
    print()
i = (m-7)//2
print(i*('-')+'WELCOME'+i*('-'),end='')
print()
x=1
y=k
z=k-1
for i in range(k):
    print(x*('---')+y*('.|.')+z*('.|.')+x*('---'),end='')
    x+=1
    y-=1
    z-=1
    print()
    
    
