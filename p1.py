l1=[1,3,4,2]
l2=[1,4,9,5]
l3=[i for i in l1 if i not in l2]
l4=[i for i in l2 if i not in l1]
a=l3+l4
print(a)



