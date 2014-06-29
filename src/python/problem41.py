from itertools import *

def getPandigitalList(length):
	num=''
	for i in range(1,length+1):
		num+=str(i)		
	return (''.join(each) for each in list(permutations(num,length)))


def isPrime(n):
	if n==2 or n==3 or n==5 or n==7:
		return True
	if n%2==0 or n%3==0 or n%5==0:
		return False
	k=5
	while k*k<=n:
		if n%k==0 or n%(k+2)==0:
			return False;
		k+=6
	return True

lastPrime=123
def checkAll():
	lastPrime=123
	for i in range(9,1,-1):
		for (n,p) in enumerate(getPandigitalList(i)):
			if isPrime(int(p)) and int(p)>lastPrime:
				lastPrime=int(p)
				
	if lastPrime!=123:
		return lastPrime


print checkAll()					
