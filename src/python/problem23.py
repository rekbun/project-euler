import math

def divisorSum(inp):
	divSum=1
	divSum+=sum(div+(inp/div) for div in range(2,int(math.sqrt(inp)+1)) if(inp%div==0)) 
	if((int(math.sqrt(inp)) * int(math.sqrt(inp)))==inp):
		divSum-=int(math.sqrt(inp));

	return divSum

adiv=set()
ans=0
for i in range(1,28124):
	flag=False
	if(divisorSum(i)>i):
		adiv.add(i)
	for num in range(1,i):
		if((num in adiv) and ((i-num) in adiv)):
			flag=True
			break
	if(flag==False):
		ans+=i
print ans

