# numpy Zeros and Ones
# Task: https://www.hackerrank.com/challenges/np-zeros-and-ones/problem?isFullScreen=true


import numpy

tuple1 = tuple(map(int, input().split()))
# tuple1 contains different numbers of args for numpy.zeros (!)
arr2 = numpy.zeros((tuple1), dtype = numpy.int)
print(arr2)
arr2 = numpy.ones((tuple1), dtype = numpy.int)
print(arr2)