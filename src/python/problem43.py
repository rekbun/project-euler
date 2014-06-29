from itertools import *


def getPandigitalNumber(length):
    inp=''
    for num in range(0, length):
        inp+=str(num)
    return (''.join(each) for each in list(permutations(inp, length)))

lis=getPandigitalNumber(10)
li=[2,3,5,7,11,13,17]
sum=0
for (n,p) in enumerate(lis):
    for j in range(1,8):
        if int(p[j:j+3])%li[j-1]!=0:
            break;
        else:
            if j==7:
                sum+=int(p)

print sum