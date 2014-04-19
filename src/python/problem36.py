




def isPalin(n,b):
	x=n
	cnt=0
	while(x>0):
		x=x/b
		cnt+=1
	x=0
	num=0
	while(num<cnt/2):
		x=x*b+n%b
		n=n/b
		num+=1

	if(cnt%2!=0):
		n=n/b	
	if(n==x):
		return True
	return False

sum=0
for i in range(1,1000000):
	if(isPalin(i,10) and isPalin(i,2)):
		sum+=i

print sum
