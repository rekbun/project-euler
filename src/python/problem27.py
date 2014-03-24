#!/usr/bin/env python

import math

def isPrime(inp):
	if(inp<0):
		return False	
	for i in range(2,int(math.sqrt(inp))+1):
		if(inp%i==0):
			return False
	return True 


def isPrime2(inp):
	if(inp==2 or inp==3):
		return True
	if(inp==1 or inp%2==0 or inp%3==0):
		return False
	if(inp<9):
		return True	
	mf=1
	f=5
	while(f*f<=inp):
		if(inp%f==0 or inp%(f+2)==0):
			return False
		f+=6
	return True


ret=0
ans=0
for a in range(-999,1000):
	for b in range(-999,1000):
		n=0
		while(True):
			if(isPrime(n*n+a*n+b)):
				n+=1
			else:
				break
		if(n>ret):
			ret=n
			ans=a*b			
	
print ans 
