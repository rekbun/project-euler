#!/usr/bin/env python



num=map((lambda x:x),range(1,21));
ans=1;

print num
for i in range(2,20):
	cnt=0;
	for j in range(1,20):
		cur=0;
		while(num[j]%i==0):
			num[j]=num[j]/i;
			cur+=1;
			if(cur>cnt):
				cnt=cur;
			
	ans=ans*pow(i,cnt);

print ans;	

		
				
