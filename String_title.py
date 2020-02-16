

s = input().split()
b=[]
#print(s)
for i in range(len(s)):
    if ord(s[i][0]) >=48 and ord(s[i][0])<=57:
        b.append(s[i])
        #print(s[i])
    else:
        b.append(s[i].title())

for i in range(len(b)):
    print(b[i],end=' ')



        



