#!/bin/python3

import os


def lonelyinteger(a):
    count_dict = {}

    for num in a:
        if num not in count_dict:
            count_dict[num] = 1
        else:
            count_dict[num] += 1

    for i in a:
        if count_dict[i] == 1:
            return i


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)
    # print(result)
    fptr.write(str(result) + '\n')

    fptr.close()
