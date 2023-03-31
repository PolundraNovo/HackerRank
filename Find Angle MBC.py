# Find Angle MBC
# https://www.hackerrank.com/challenges/find-angle/problem?isFullScreen=true

from math import atan2, degrees 
x = int(input())
y = int(input())
res = degrees(atan2(x, y))
deg = u'\xb0'
print(str(round(res))+deg)