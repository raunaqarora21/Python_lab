s=list(input())
#print(len(s))
s.append('@')
#print(s)
b=[]
str=""
for i in range(len(s)):
    
    if ord (s[i]) >=48 and ord(s[i]) <=57 or s[i] == '-':
        str+=s[i]
    else:
        b.append(str)
        str=""
        
for i in range(len(b)):
    print(b[i],end=' ')
        
