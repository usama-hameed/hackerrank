def wrapper(f):
    def fun(l):
        first = []
        for i in l:
            first.append(int(i))
        first.sort()
        for index, value in enumerate(first):
            value = str(value)
            if len(value) <= 10:
                new_str = '+91 ' + value[0:5] + ' ' + value[5:]
            else:
                new_str = '+' + value[0:2] + ' ' + value[2:7] + ' ' + value[7:]
            first[index] = new_str
        return f(first)
    return fun

'''
3
09191919191
9100256236
+919593621456
'''
@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')


if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l)