







nums=set()
nums.add(1)
nums.add(2)
nums.add(5)
nums.add(10)
nums.add(20)
nums.add(50)
nums.add(100)
nums.add(200)


dp=[0 for i in range(1,202)]
dp[0]=1
for i in nums:
	for j in range(201):
		if(dp[j]>0 and i+j<201):
			dp[j+i]=dp[i+j]+dp[j]

print dp[200]

	

