
n=int(input())
for i in range(1,n+1):
    
    a=int(input())
    b=input().split()
    x=0
    y=a-1
    x1=0
    y1=a-1
    flag=0
    flag1=0
    m=max(b)
    #print(m)
    if m != b[0] or m != b[a-1]:
        print('No')
        break
    else:
        while(b[x]>=b[y]):
            flag+=1
            x+=1
            y-=1
            #print(flag)
        while(b[y1]>=b[x1]):
            flag1+=1
            x1+=1
            y1-=1
            #print(flag1)
        if a%2==0:
            d=a//2
            if flag == d or flag1 == d:
                print("Yes")
            else:
                print('No')
        elif a%2!=0:
            d=(a+1)//2
            if flag == d or flag1 == d:
                print('Yes')
            else:
                print('No')
        
