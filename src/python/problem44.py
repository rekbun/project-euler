limit = 100000


from subprocess import call
from datetime import date,time,datetime,timedelta




def getPantagonalList():
    n = 0
    array = set()
    while n < limit:
        array.add((3 * n * (3 * n - 1)))
        n += 1
    return array


d = limit


def checkAll():
    d = limit
    list = getPantagonalList()
    # print list
    for e in list:
        for j in list:
            if j - e in list and j + e in list:
                if abs(j - e) < d:
                    d = abs(j - e)

    print d


checkAll()
print "done"