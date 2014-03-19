#!/usr/bin/env 

def facto(n):
	fact= (reduce(lambda x,y:x*y, range(1,n+1)))
	fact =str(fact)
	return sum(int(fact[i]) for i in range(0,len(fact)))  

print facto(100)
