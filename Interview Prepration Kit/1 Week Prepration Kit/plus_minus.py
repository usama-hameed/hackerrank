def plusMinus(arr):
    pos_numbers = 0
    neg_numbers = 0
    zeros = 0

    for i in arr:
        if i < 0:
            neg_numbers += 1
        elif i > 0:
            pos_numbers += 1
        else:
            zeros += 1
    return pos_numbers/len(arr), neg_numbers/len(arr), zeros/len(arr)


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    pos, neg, zero = plusMinus(arr)
    print("{:.6f}".format(pos))
    print("{:.6f}".format(neg))
    print("{:.6f}".format(zero))
