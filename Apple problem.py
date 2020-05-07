#input--->-6,0,2,40



l=list(map(int,input().split(',')))


for i in range(len(l)):
    if l[i]>i:
        print('False')
        break
    else:
        if l[i] == i:
            print(i)
            break
else:
    print('False')
