#!/usr/bin/env python
i=0
sum=0
last=1
cur=2
while cur<4000000:
	if(cur%2==0):
		sum+=cur
	temp=last
	last=cur
	cur=temp+cur

print sum	 
	
