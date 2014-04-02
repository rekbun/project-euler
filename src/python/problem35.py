



def isPrime(n):
	if(n==2 or n==3 or n==5 or n==7):
		return True
	if(n<=9):
		return False
	if(n%2==0 or n%3==0):
		return False
	x=5
	while(x*x<=n):
		if(n%x==0):
			return False
		if(n%(x+2)==0):
			return False
		x+=6
	return True


def isAllPrime(n):
	ln=len(str(n))
	f=ln-1

	while(ln>0):
		if(not isPrime(n)):
			return False
		n=(10**f)*(n%10)+n/10
		ln-=1
	return True
def cal(n):
	cnt=0
	for i in range(1,n):
		if(isAllPrime(i)):
			cnt+=1
	return cnt


print cal(1000000)
				
