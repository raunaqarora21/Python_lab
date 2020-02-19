a=tuple(eval(input()))
s=()
for i in a:
	if i not in s:
		if a.count(i) > 1:
			s+=(i,)

	
print(s)
