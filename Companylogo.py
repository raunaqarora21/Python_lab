 a=input()
    b=[0]*26
    c=1
    for i in  a:
        b[ord(i)-97] +=1
    while c<=3:
        m=max(b)
        for i in range(26):
                if m == b[i]:
                    print('{} {}'.format(chr(i+97),m))
                    b[i]= 0
                    break
        c+=1
