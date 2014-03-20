f=open('../names.txt','r')

try:
	lines=''
	for line in f:
		lines+=line
	lines=lines.split(',')
	lines.sort()
	ans=0;
	for i in range(0,len(lines)):
		ln=0
		for j in (list(str(lines[i])[1:-1])):
			ln=ln+(ord(j)-ord('A'))+1
		ans=ans+ln*(i+1)
	print ans
finally:
	f.close()
