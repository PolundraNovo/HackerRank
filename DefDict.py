from collections import defaultdict
l1 = input().split()
n, m = int(l1[0]), int(l1[1])
d = defaultdict(list)

for i in range(n):   # add words from Group A into our defaultdict
    word = input()
    d[word].append(i+1)

for i in range(m):    # search words from Group B in our defaultdict
    word = input()
    x = d.get(word)
    if x == None:
        print(-1)
    else:
        res = ''
        for item in x:
            res = res +  str(item) + ' '
        print(res)    
