from _collections import deque
import sys

case_count = int(input())

base_case = deque()
results = []

for i in range(case_count):
    base_case.append(sys.stdin.readline().strip().split(' '))

for i in range(len(base_case) - 1, -1, -1):
    case = ''
    
    while base_case[i]:
        case += base_case[i].pop() + ' '
    case = case.strip()
    results.append(f"Case #{i + 1}: {case}")

results.sort()
for result in results:
    print(result)