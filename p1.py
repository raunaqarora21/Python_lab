a=list()
while 1:
	item=input("Enter the item ")
	a.append(item)
	n=input("Do you want to continue Y/N ")
	if n.lower() == 'n':
		break
a.sort(reverse=True,key=max)

print(a[0])
