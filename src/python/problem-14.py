#!/usr/bin/env python


number=1000000;
list=[True for i in range(0,number)];

cnt=0;
n=number;
i=number-1;
max=0
ret=0;
while(i>0):
	n=i
	cnt=0
	while(n>1):
		if(n%2==0):
			n=n/2
		else:
			n=3*n+1
		cnt+=1
	if(cnt>max):
		max=cnt
		ret=i
	i-=1;

print ret,max
		
