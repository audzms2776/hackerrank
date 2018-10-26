#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    cnt = 0
    idx = 0
    
    while True:
        if idx + 2 == len(c):
            cnt += 1
            break
        elif idx + 1 >= len(c):
            break
        
        next1 = c[idx + 1]
        next2 = c[idx + 2]
        
        if next1 == 1:
            idx += 2
        elif next2 == 1:
            idx += 1
        else:
            idx += 2
        
        cnt += 1
        
    return cnt 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
