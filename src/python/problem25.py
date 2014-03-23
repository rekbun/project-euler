



prev=1
cnt=2
next=1
while(len(str(next))<1000):
	prev,next=next,next+prev
	cnt+=1

print(cnt)
