# Task: https://www.hackerrank.com/challenges/piling-up/problem?isFullScreen=true

# Enter your code here. Read input from STDIN. Print output to STDOUT
t = int(input())
for i in range(t):  # loop on test cases
    n = input()
    Last_Block = 99999999999
    Blocks = input().split() # list of blocks
    Yes = True
    while len(Blocks) > 0:
        if max(int(Blocks[0]), int(Blocks[-1])) > Last_Block:
            Yes = False
            break
        if int(Blocks[0]) > int(Blocks[-1]):
            Last_Block = int(Blocks[0])
            Blocks.pop(0)    
        else:    
            Last_Block = int(Blocks[-1])
            Blocks.pop(-1)    
    if Yes:
        print('Yes')
    else:
        print('No')    