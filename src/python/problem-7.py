#!/usr/bin/env python 

import math

def isPrime(inp):
	for i in range(2,int(math.sqrt(inp))+1):
		if(inp%i==0):
			return False

	return True

ret=2;
cnt=0;
while True:
	if(isPrime(ret)):
		cnt+=1
	if(cnt==10001):
		print ret
		break

	ret+=1

	
