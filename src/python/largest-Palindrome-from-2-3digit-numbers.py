#!/usr/bin/env python

def check(string):
	i=0
	j=len(string)-1
	while(i<j):
		if(string[i]!=string[j]):
			return None
		i=i+1
		j=j-1	
	return True


def largestPalindrome():
	largest=0;
	for n1 in range(999,100,-1):
		for n2 in range(999,100,-1):
			ans=n1*n2
			if(check(str(ans))!=None and ans>largest):
				largest=ans

	return largest


print largestPalindrome()

