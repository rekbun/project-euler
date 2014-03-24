


def spiralSum(ms):
	s=1
	cnt=2
	r=1
	while(r<ms*ms):
		i=0
		while(i<4):
			r+=cnt
			s+=r
			i+=1
			
		cnt+=2
	print s


spiralSum(1001)


