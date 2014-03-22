def perm(inp):
	perm=reduce(lambda x,y:x*y,range(1,10))
	ans='';
	numSet=range(0,10)
	last=9;
	while(inp>0):
		d=1
		while(d*perm<inp):
			d+=1
		ans+=str(numSet[d-1])
		inp=inp-(d-1)*perm
		if(last==0):
			break
		perm/=last
		del numSet[d-1]
		last-=1
		
	print ans

perm(1000000)
