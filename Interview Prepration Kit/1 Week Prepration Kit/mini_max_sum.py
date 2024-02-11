def miniMaxSum(arr):
    arr.sort()
    min_sum = 0
    max_sum = 0
    for i in range(0, len(arr)-1):
        min_sum += arr[i]

    for i in range(len(arr)-1, 0, -1):
        max_sum += arr[i]

    return min_sum, max_sum


if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))
    min, max = miniMaxSum(arr)
    print(min, max)
