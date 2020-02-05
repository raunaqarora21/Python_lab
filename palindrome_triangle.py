
  
for i in range(1,int(input())+1): #More than 2 lines will result in 0 score. Do not leave a blank line also
    for j in range(1,i+1):
                if i>=j:
                    print(j,end='')
    while((i-1)>0):
            
            print((i-1),end='')
            i-=1
    print()
    
