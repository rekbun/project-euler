


def fact(n):
	if(n==0):
		return 1
	return reduce(lambda x,y:x*y,range(1,n+1))

ret=0
for i in range(10,2540161):
	sum=0
	init=i
	while(i>0):
		sum+=fact(i%10)
		i=i/10
	if(sum==init):
		ret+=init
print ret		
