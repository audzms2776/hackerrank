#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    m_dict = dict()
    cnt = 0
    true_arr = [x+1 for x in range(len(q))]
    
    for x in q:
        m_dict[x] = 2
    
    while True:
        for i in range(len(q) - 1):
            curr_item = q[i]
            next_item = q[i+1]
            
            if curr_item > next_item:
                if m_dict[curr_item] == 0:
                    return "Too chaotic"
                
                q[i] = next_item
                q[i+1] = curr_item
                m_dict[curr_item] -= 1
                cnt += 1
            
            # print(q)
            if q == true_arr:
                return cnt
        
        

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())
        
        q = list(map(int, input().rstrip().split()))

        print(minimumBribes(q))
