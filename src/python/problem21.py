
def f(inp):
	n1=sum(x for x in range(1,inp/2+1) if(inp%x==0))
	n2=sum(x for x in range(1,n1/2+1) if(n1%x==0))
	if(n2==inp and n1!=n2):
		return True
	return False
	

n1=sum([i for i in range(1,10000) if(f(i))]);
print n1
