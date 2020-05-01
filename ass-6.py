n=int(input())
l=list(map(int,input().split()))


x=0
while(x<(n-1)):
     if l[x]<l[x+1]:
         l.remove(l[x])
         n-=1
         
     else:
         x+=1

y=0
while(y<(n-1)):
    if l[y]<l[y+1]:
         l.remove(l[y])
         n-=1
        
    else:
         y+=1

if len(l)>1:
     
     if l[-1]<l[-2]:
         l.remove(l[-1])

print(len(l))
