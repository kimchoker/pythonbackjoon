import sys
import itertools

case_count = int(input())

closet = {}

for i in range(case_count):
    each_case_count = int(input())

    for o in range(each_case_count):
        value, key = sys.stdin.readline().strip().split(' ')
        if key in closet:
            closet[key].append(value)
        else:
            closet[key] = [value]

    options = list(closet.values())
    print(options)
    permutations = []
    for length in range(1, len(options) + 1):
        perms = list(itertools.permutations(options, length))
        permutations.extend(perms)
    for perm in permutations:
        print(perm)

    closet.clear()


    #
    # permutations = []
    # for select in selection:
    #     perm = list(itertools.permutations(selection))
    #     permutations.extend(perm)
    #
    # for perm in permutations:
    #     print(perm)
    #
    # closet.clear()

