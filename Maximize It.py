# Task (itertools): https://www.hackerrank.com/challenges/maximize-it/problem?isFullScreen=true

from itertools import product

k, m = tuple(map(int, input().split()))
list1 = []
lens = []
res = -1
for i in range(k):  # forming lists
    list2 = list(map(int, input().split()))
    lens.append(list2[0])
    list2 = list(list2[1:])
    if list1 == []:
        list1 = [list2]
    else:
        list1.append(list2)

for part in product(*list1):  # use itetools.product
    list2 = list(part)
    x = sum(list(map(lambda a: a**2, list2)))
    if (x % m) > res:  # check for new result
        res = (x % m)

print(res)
