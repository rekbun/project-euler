#!/usr/bin/env python
def check(a,b,c,s):
	ss=set()
	num=str(a)+str(b)+str(c)
	for i in list(num):
		if(int(i) in ss):
			return False
		else:
			ss.add(int(i))
	if(ss.issuperset(s) and 0 not in ss):
		return True
	return False

ans=0
s= set()
for x in range(1,10):
	s.add(x)

output=set()
for i in range(1,99):
	a=1
	while(a<=9876):
		if(a*i not in output and check(a,i,a*i,s)):
			ans+=a*i
			output.add(a*i)
		a+=1
print ans			
