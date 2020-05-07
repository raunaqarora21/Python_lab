
with open("Voting Machine.txt",'r') as f:
    data=f.readlines()
    

    
    voter_id=[]
    candidate_id=[]
    for i in data:
        a,b=list(map(int,i.split(',')))
        if a not in voter_id:
            voter_id.append(a)
            candidate_id.append(b)
        else:
            print('Fraud')

        
    print("Top 3 candidates:")

    c=[]

    for i in candidate_id:
        if i not in c:
            c.append(i)
      
    c.sort(key=lambda x:candidate_id.count(x),reverse=True)
    

    for i in range(3):
            print(c[i])

            
        
        

    
   


    
    
        
        
        
