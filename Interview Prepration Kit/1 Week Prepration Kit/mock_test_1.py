def findMedian(arr):
    arr.sort()
    if len(arr) % 2 != 0:
        mid = len(arr) // 2
    else:
        mid = len(arr) // 2

        mid = (mid + (mid - 1)) // 2

    return arr[mid]


print(findMedian([1, 2, 3, 4, 5, 6]))
