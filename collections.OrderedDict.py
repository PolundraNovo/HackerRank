# Task:
# https://www.hackerrank.com/challenges/py-collections-ordereddict/problem?isFullScreen=true

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict
n = int(input())
mydict = OrderedDict()
for i in range(n):
    l1 = list(input().split())
    s, k = ' '.join(l1[:-1]), int(l1[-1])
    good = mydict.get(s)
    if good:
        mydict[s]=k + good  # add to existing item
    else:
        mydict[s]=k  # new item
#print(mydict) 
goods = (mydict.items())
for key, value in goods:
    print(key, value)