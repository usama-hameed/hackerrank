
def superReducedString(s):
    first_ptr = 0
    second_ptr = 1

    while second_ptr < len(s):
        if s[first_ptr] == s[second_ptr]:
            if first_ptr == 0:
                s = s[second_ptr+1:]
            else:
                s = s[0:first_ptr] + s[second_ptr+1:]

            first_ptr = 0
            second_ptr = 1
        else:
            first_ptr += 1
            second_ptr += 1
        if not s:
            return 'Empty String'
    return s


if __name__ == '__main__':

    s = input()

    result = superReducedString(s)

    print(result)
