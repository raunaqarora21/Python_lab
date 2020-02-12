a=int(input())
z=str(a)
f=len(z)

b=[]
c=bin(a)
h=oct(a)
j=len(h)
d=len(c)
#f=len(a)
m=len(hex(a))


#print(c)
for i in range(1,a+1):
    c=bin(i)
    e=len(c)
    g=len(str(i))
    k=oct(i)
    l=len(k)
    n=hex(i)
    o=len(n)
    print((f-g)*(' ')+str(i)+('  '),end='')
    print((j-l)*(' ')+str(k)[2:]+('  '),end='')
    print((m-o)*(' ')+str.upper(n)[2:]+('  '),end='')
    print((d-e)*(' ')+str(c)[2:],end='')
    
    print()
