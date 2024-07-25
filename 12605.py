from _collections import deque
import sys

case_count = int(input())

base_case = deque()
results = []

for i in range(case_count):
    base_case.append(sys.stdin.readline().strip().split(' '))

for i in range(len(base_case) - 1, -1, -1):
    case = ''
    # 파이썬에서 빈 리스트가 False, 비어 있지 않은 리스트는 True 로 평가되는 성질을 이용
    # 리스트가 비면 while 문 종료
    while base_case[i]:
        case += base_case[i].pop() + ' '
    case = case.strip()
    results.append(f"Case #{i + 1}: {case}")

results.sort()

for result in results:
    print(result)