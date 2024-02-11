
def person_lister(f):
    def inner(people):
        final = []
        for count in range(len(people)):
            people[count][2] = int(people[count][2])
        result = sorted(people, key=lambda x: x[2])
        for res in result:
            final.append(f(res))
        return final
    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]


if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')
