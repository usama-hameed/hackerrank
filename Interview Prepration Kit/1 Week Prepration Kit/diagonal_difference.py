#!/bin/python3

import math
import os
import random
import re
import sys


def diagonalDifference(arr):

    first_sum = 0
    sec_sum = 0
    start_index = 0
    end_index = len(arr) - 1
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i == j:
                first_sum += arr[i][j]
            if i == start_index and j == end_index:
                sec_sum += arr[i][j]
                start_index += 1
                end_index -= 1
    return abs(first_sum - sec_sum)

'''
00 01 02
10 11 12
20 21 22
-> [n-i-1]
'''
if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)
    print(result)
    # fptr.write(str(result) + '\n')
    #
    # fptr.close()
