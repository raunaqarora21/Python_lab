a=input().split(',')

b=[]
c=[]
d=[]
#b=[b.append(i) for i in a if i not in b]
#print(b)
for i in a:
    if i not in b:
        b.append(i)
#print(b)
for i in  range(len(b)):
        c.append(a.count(b[i]))
#print(c)
m=max(c)
for i in range(len(b)):
   
    if m == c[i]:
        d.append(b[i])
d.sort()
#for i in range(len(d)):
    print(d[0])
    
