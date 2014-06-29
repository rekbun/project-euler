import numpy as np
import math
f=open('words.txt','r')
cnt=0
str=f.readline()
sep=str.split(',')

i=0
while i<len(sep):
    sum=int(np.frombuffer(sep[i],"uint8").sum() -(ord('A')-1)*(len(sep[i])-2))-68
    if int(math.sqrt(sum*2))*(int(math.sqrt(sum*2))+1)==(sum*2) and sum!=0:
        cnt+=1
        print sep[i],sum
    i+=1

print cnt,i




