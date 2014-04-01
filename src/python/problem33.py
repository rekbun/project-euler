



def find():
	n=1
	d=1
	for a in range(1,10):
		for b in range(1,10):
			for c in range(1,10):
				if(c*(10*a+b)==a*(10*b+c)):
					n*=a
					d*=c

	return n,d

def gcd(a,b):
	if(a==0 or b==0):
		return a
	if(a<b):
		return gcd(b,a)
	return gcd(b,a%b)

a,b=find()
print b/gcd(a,b)

				

