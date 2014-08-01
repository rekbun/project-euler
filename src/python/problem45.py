__author__ = 'rakesh.singh'
from sets import Set;
import math;


def findTriangle(n):
    return n*(n+1)/2;



def findPentagonal(n):
    return n*(3*n-1)/2;



def findHexagonal(n):
    return n*(2*n-1);





t={};
ts=Set();
p={};
ps=Set();
h={};
hs=Set();

for i in range(1,1000000):
    t[findTriangle(i)]=i
    ts.add(findTriangle(i));

for i in range(1,100000):
    p[findPentagonal(i)]=i;
    ps.add(findPentagonal(i));

for i in range(1,300000):
    h[findHexagonal(i)]=i;
    hs.add(findHexagonal(i));

res=ts&ps&hs;
print res

if not len(res) is 0:
    print res
    print t[res.pop()]
    res=res.pop();







