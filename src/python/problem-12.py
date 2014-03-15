#!/usr/bin/env python

import math  

s=50
cnt=1;
limit=501

while(True):
	ss=s*(s+1)/2;
	cnt=1
	for i in range(1,int(math.sqrt(ss)+1)):
		if(ss%i==0):
			cnt+=2
		if(i*i==ss):
			cnt-=1
	s+=1;
	
	if(cnt>500):
		print ss
		break


			
