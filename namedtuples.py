# collections.namedtuple()
# https://www.hackerrank.com/challenges/py-collections-namedtuple/problem?isFullScreen=true

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple
n = int(input())
l1 = input().split()
fields = ','.join(l1)
students = namedtuple(l1[0],fields)
tot_marks = 0
for i in range(n):
    a, b, c, d = map(str, input().split())
    s1 = students(a, b, c, d)
    tot_marks += int(s1.MARKS)
print(tot_marks/n)    
    

