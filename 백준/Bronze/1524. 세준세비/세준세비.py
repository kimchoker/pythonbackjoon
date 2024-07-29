import sys

# 입력 개수를 받음
case_count = int(input().strip())

for i in range(case_count):
    # n과 m을 받음
    while True:
        line = sys.stdin.readline().strip()
        if line:
            n, m = map(int, line.split())
            break

    # 세준과 세비의 리스트를 받음
    sejun = list(map(int, sys.stdin.readline().strip().split()))
    sebi = list(map(int, sys.stdin.readline().strip().split()))
    sejun.sort(reverse=True)
    sebi.sort(reverse=True)

    while sejun and sebi:
        if sejun[-1] < sebi[-1]:
            sejun.pop()
        elif sejun[-1] > sebi[-1]:
            sebi.pop()
        else:
            sebi.pop()

    if sejun:
        print('S')
    elif sebi:
        print('B')
    else:
        print('C')