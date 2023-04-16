# Task:
# https://www.hackerrank.com/challenges/itertools-combinations/problem?isFullScreen=true

# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations
l1 = list(input().split())
s, k = l1[0], int(l1[1])
s1 = ''.join(sorted(s))
for i in range(1, k+1):
    l1= list((combinations(s1, i)))
    l1.sort()
    for item in l1:
        print(''.join(item))
    res += l1

