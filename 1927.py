import sys
import heapq

command_count = int(input())
commands = [sys.stdin.readline().strip() for _ in range(command_count)]
minHeap = []

for i in range(command_count):
    current = int(commands[i])

    if current > 0:
        heapq.heappush(minHeap, current)
    elif current == 0 and len(minHeap) == 0:
        print(0)
    else:
        min_num = heapq.heappop(minHeap)
        print(min_num)
