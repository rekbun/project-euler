#!/usr/bin/env python
from functools import reduce
num=20
n= reduce((lambda x,y: x*y),range(2*num,num,-1))
d= reduce((lambda x,y:x*y),range(num,0,-1))

print n/d
