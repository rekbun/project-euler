





dic=set()
for i in range(2,101):
	for j in range(2,101):
		if(pow(i,j) in dic):
			continue
		else:
			dic.add(pow(i,j))

print len(dic)	
