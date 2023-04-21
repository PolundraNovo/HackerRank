# Date and Time
# Task: https://www.hackerrank.com/challenges/python-time-delta/problem?isFullScreen=true
#
#!/bin/python3

import math
import os
import random
import re
import sys
from datetime import datetime, timedelta

# Complete the time_delta function below.
def time_delta(t1, t2):
    print('====================')
#    print(t1.strip()[4:-6])
#    print(t2.strip()[4:-6])
    time1 = datetime.strptime(t1.strip()[4:-6],"%d %b %Y %H:%M:%S")
    time2 = datetime.strptime(t2.strip()[4:-6],"%d %b %Y %H:%M:%S")
    delta1 = int((time1 - time2).total_seconds())
    print(' point1 ', time1, time2)
    print(delta1)
    hours = int(t1.strip()[-5:][:3]) - int(t2.strip()[-5:][:3])
    min0 = int(t1.strip()[-5]+t1.strip()[-2:]) - int(t2.strip()[-5]+t2.strip()[-2:])
    print(t1.strip()[-5:][:3], t1.strip()[-2:])
    print(t2.strip()[-5:][:3], t2.strip()[-2:])
    print(hours, min0)
    delta2 = hours * 3600 + min0 * 60  # need to subtract
    delta1 -= delta2
    print(delta2)
    return str(abs(delta1))
    
    
if __name__ == '__main__':
    First = True
    t1, t2 = '',''
    with open('data1.txt') as f:
        for line in f:
#            print('----------------')
            if len(line) > 10:
#                print(line)
                if First:
                    t1 = line
                else:
                    t2 = line
                    print('----------------')
#                    print(t1)
#                    print(t2)
                    delta = time_delta(t1, t2)
                    print(delta)
                First = not First

#    fptr = open(os.environ['OUTPUT_PATH'], 'w')
#
#    t = int(input())
#
#    for t_itr in range(t):
#        t1 = input()
#
#        t2 = input()
#
#        delta = time_delta(t1, t2)
#
#        fptr.write(delta + '\n')
#
#    fptr.close()
