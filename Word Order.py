# Task: https://www.hackerrank.com/challenges/word-order/problem?isFullScreen=true

Dict1 = {}
n = int(input())
for i in range(n):
    str1 = input()
    if Dict1.get(str1) == None:
        Dict1[str1] = 1
    else:
        Dict1[str1] += 1   
print(len(Dict1))
for item in Dict1:
    print(Dict1[item], end=' ')