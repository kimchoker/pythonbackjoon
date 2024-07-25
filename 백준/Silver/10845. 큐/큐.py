import sys
from collections import deque

command_count = int(input())
command = [sys.stdin.readline().strip().split(" ") for _ in range(command_count)]

queue = deque()

for i in range(command_count):
    current = command[i]
    if current[0] == 'push':
        queue.append(current[1])
    elif current[0] == 'pop':
        if len(queue) != 0:
            pop = queue.popleft()
            print(pop)
        else:
            print(-1)
    elif current[0] == 'size':
        print(len(queue))
    elif current[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif current[0] == 'front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif current[0] == 'back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])
