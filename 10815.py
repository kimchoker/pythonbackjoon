import sys

sCount = int(sys.stdin.readline())
card_set = set(map(int, sys.stdin.readline().split()))

fCount = int(sys.stdin.readline())
check_list = list(map(int, sys.stdin.readline().split()))

isExist = []

for i in range(0, len(check_list)):
    if check_list[i] in card_set:
        isExist.append(1)
    else:
        isExist.append(0)

print(" ".join(map(str, isExist)))