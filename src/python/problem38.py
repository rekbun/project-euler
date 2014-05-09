

def find(n):
	num=0
	for i in range(1,3):
		num=num*100000+n*i
	ansb=num
	c = set()
	while(num>0):
	 	if( num%10 in c or num%10<=0):
			return False
		c.add(num%10)
		num=num/10
	
	print ansb
	return True 	


for i in range(9876,9123,-1):
	if find(i):
		break

