#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    result = 0
    level = 0
    
    for i in s:
        if level == -1 and i == 'U':
            level += 1
            result += 1
        elif i == 'U':
            level += 1
        else:
            level -= 1
    
    return result
        
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
