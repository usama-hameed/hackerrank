import re

'''
aaadaa
aa
'''


def find_index(str, sub_str):
    final = []
    for index, values in enumerate(str):
        if index + len(sub_str) <= len(str):
            if str[index: index + len(sub_str)] == sub_str:
                final.append((index, index + len(sub_str)-1))
    return final


str = input()
sub_str = input()

result = find_index(str, sub_str)
if not result:
    print((-1, -1))
for res in result:
    print(res)
