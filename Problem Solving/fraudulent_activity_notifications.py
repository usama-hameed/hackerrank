#!/bin/python3

import math
import os
import random
import re
import sys


def calculate_median(expenditure):
    expenditure.sort()
    if len(expenditure) % 2 != 0:
        return (expenditure[len(expenditure) // 2]) * 2

    else:
        mid = (len(expenditure) // 2)
        return (expenditure[mid-1] + expenditure[mid]) / 2


def activityNotifications(expenditure, d):
    first = 0
    total_notifications = 0
    while d < len(expenditure):
        median = calculate_median(expenditure[first:d])
        if median <= expenditure[d] and d < len(expenditure) -1:
            total_notifications += 1
        first += 1
        d += 1
    return total_notifications


if __name__ == '__main__':

    result = activityNotifications([1, 2 ,3 ,4 ,4], 4)

    print(result)
