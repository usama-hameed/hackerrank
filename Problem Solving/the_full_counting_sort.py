
def countSort(arr):
    final = ''
    half = len(arr) // 2

    for i in range(half):
        arr[i][-1] = '-'

    sorted_arr =sorted(arr, key=lambda x: int(x[0]))

    for sort in sorted_arr:
        final += sort[-1] + ' '

    return final


if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(input().rstrip().split())

    countSort(arr)
