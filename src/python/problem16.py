#!/usr/bin/env python


def pow(m,n):
	res=1
	while(n>0):
		res=res*m
		n-=1
	return str(res)	

res=pow(2,1000)

res=str(reduce((lambda x,y:x*y),[2 for i in range(0,1000)]))
print sum(int(res[i]) for i in range(0,len(res)))




