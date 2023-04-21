# Deque operations
# Task - https://www.hackerrank.com/challenges/py-collections-deque/problem?isFullScreen=true

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque
n = int(input())
d = deque()
for i in range(n):
    command = input()
#    print(command)    
    if command[-1].isdigit():
        param = (command.split()[-1])
#        print(param)
    if command.startswith("appendleft"):
       d.appendleft(param) 
    elif command.startswith("append"):
        d.append(param)
    elif command.startswith("popleft"):
        x = d.popleft()
    elif command.startswith("pop"):
        x = d.pop()
    elif command.startswith("clear"):
        d.clear()
    elif command.startswith("extendleft"):
        d.extendleft(param)
    elif command.startswith("extend"):
        d.extend(param)
    elif command.startswith("remove"):
        d.remove(param)
    elif command.startswith("reverse"):
        d.reverse()
    elif command.startswith("rotate"):
        d.rotate(param)
#print(d)   
print(" ".join(d))

