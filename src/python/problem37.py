
def isPrime(n):
	if(n==2 or n==3 or n==5 or n==7):
		return True
	if(n%2==0 or n%3==0):
		return False
	if(n<=9):
		return False
	itr=5
	while(itr*itr<=n):
		if(n%itr==0):
			return False
		if(n%(itr+2)==0):
			return False
		itr+=6
	return True


def checkTrunctablePrime(n):
	lr=n
	cnt=1
	while(lr>0):
		if(not isPrime(lr)):
			return False
		lr=lr/10
		cnt*=10
	rl=n
	cnt=cnt/10
	while(rl>0):
		if(not isPrime(rl)):
			return False
		rl=rl%(cnt)
		cnt=cnt/10
	return True

cnt=0
n=11
sum=0
while(cnt<11):
	if(checkTrunctablePrime(n)):
		cnt+=1
		sum+=n
	if(checkTrunctablePrime(n+2) and cnt<11):
		cnt+=1
		sum+=n+2
	n+=6
print sum
