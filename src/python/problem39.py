def f(n):
	cnt=0
	for a in range(1,n-3):
		for b in range(a,n-3):
			c =n-a-b
			if(c>b):
				if((a*a+b*b)==c*c):
					cnt+=1
	return cnt

ans=0
num=0
for i in range(1000,100,-1):
	val= f(i)
	if(val>ans):
		ans=val
		num=i
print num		
