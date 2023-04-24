# Task:
# https://www.hackerrank.com/challenges/no-idea/problem?isFullScreen=true

# Enter your code here. Read input from STDIN. Print output to STDOUT
l1 = list(input().split())
n, m = int(l1[0]), int(l1[1])
l1 = list(input().split())  # numbers for check
l2 = list(input().split())
set1 = set(l2)  # 1st set
l2 = list(input().split())
set2 = set(l2) # 2nd set
result = 0
for item in l1:
    if item in set1:
        result +=1
    elif item in set2:
        result -=1
print(result) 