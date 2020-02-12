s = input()
f1=0
f2=0
f3=0
f4=0
f5=0
for i in s:
        if i.isalnum() == True:
             print ('True')
             f1=1
             break
if f1 == 0:
    print('False')
for i in s:
        if i.isalpha() == True :
            print ('True')
            f2=1
            break
if f2 == 0:
    print('False')
for i in s:
        if i.isdigit() == True :
            print ('True')
            f3=1
            break
if f3 == 0:
    print('False')

for i in s:
        if i.islower() == True :
            print ('True')
            f4=1
            break
if f4 == 0:
    print('False')

for i in s:
        if i.isupper() == True :
            print ('True')
            f5=1
            break
if f5 == 0:
    print('False')    
