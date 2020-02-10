a=int(input())
b=[]
c=bin(a)
d=len(c)

#print(c)
for i in range(a+1):
    c=bin(i)
    e=len(c)
    print((d-e)*(' ')+str(c)[2:],end='')
    print()
