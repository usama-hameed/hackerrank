import os


def timeConversion(s):
    actual_time = s.split(":")
    if actual_time[-1][2:] == 'PM':
        if actual_time[0] != '12':

            actual_time[0] = str(int(actual_time[0]) + 12)
    elif actual_time[0] == '12':
        actual_time[0] = '00'

    return ':'.join(actual_time).replace('PM', '').replace('AM', '')


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    #
    # s = input()

    result = timeConversion('07:05:45PM')
    print(result)
    # fptr.write(result + '\n')
    #
    # fptr.close()
