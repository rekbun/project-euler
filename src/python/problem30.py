


def sumPower5(inp):
	s=0
	s=sum([int(a)**5 for a in list(str(inp))])
	if(inp==s):
		return True
	return False

ans=0
for i in range(100,999999):
	if(sumPower5(i)):
		ans+=i

print ans		
