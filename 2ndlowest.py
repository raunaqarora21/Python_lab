n=[]
s=[]
k=[]
if __name__ == '__main__':
    num=int(input())
    for _ in range(num):
        name = input()
        score = float(input())
        n.append(name)
        s.append(score)
b=[[i,j] for i in n for j in s]
#print(b)
c=b[0:((num**2)+1):(num+1)]
m=min(s)
#print(m)
def myfun(i):
    return i[1]
c.sort(key=myfun)
print(c)
#a=c[1]
#print(a)

for i in range(num):
            if c[i][1]!= m:
                f=i
                break
k=c[f][1]
#print(c[f])
d=[]
for i in c:
    if i[1] == k:
            d.append(i[0])
#print(d)
d.sort()
#print(d)
for i in range(len(d)):
        print(d[i])
                    
                    
