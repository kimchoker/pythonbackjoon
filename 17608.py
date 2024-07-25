from collections import deque
import sys
num_count = int(input())

stack = deque()

for _ in range(num_count):
    stick = int(sys.stdin.readline().strip())
    stack.append(stick)

count = 0
reference = 0

# 스택을 오른쪽에서 왼쪽으로 순회
for _ in range(num_count):
    # 스택에서 막대기 하나를 꺼냄
    height = stack.pop()
    if height > reference:
        reference = height
        count += 1

print(count)