#!/usr/bin/env python
import math
num=input();
lastPrime=0;
for i in range(2,int(math.sqrt(num))+1):
	while(num%i==0):
		num=num/i;
		lastPrime=i;

print lastPrime		
