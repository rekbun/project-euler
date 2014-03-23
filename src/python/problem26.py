



def genCycle(inp):
	nums={}
	digiNum=1
	while(digiNum<inp):
		digiNum*=10
	cnt=0;
	while(True):
		digi=digiNum/inp
		cnt+=1
		if(digiNum%inp==0):
			return 0
		if(digiNum%inp in nums):
			break
		
		nums[digiNum%inp]=cnt
		digiNum=digiNum%inp
		digiNum*=10
	return cnt-nums[digiNum%inp]

num=1
maxNum=0
for i in range(1,1000):
	ret=genCycle(i)
	if(ret>num):
		num=ret
		maxNum=i		

print maxNum 
