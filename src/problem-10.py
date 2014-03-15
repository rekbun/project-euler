#!/usr/bin/env python



inp=map(lambda a:1,range(0,2000001))

inp[0]=0;
inp[1]=0;
inp[2]=0;

for i in range(2,len(inp),2):
	inp[i]=0

cnt=3
sum=2
while(cnt<len(inp)):
	#print cnt
	if(inp[cnt]==1):
		sum+=cnt
		for i in range(2*cnt,len(inp),cnt):
			inp[i]=0

	cnt+=2	

print sum

	



