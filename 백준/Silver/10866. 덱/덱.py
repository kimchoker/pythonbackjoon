from _collections import deque
import sys

command_count = int(input())
command = [sys.stdin.readline().strip().split(" ") for _ in range(command_count)]

deque = deque()

for i in range(len(command)):
    current = command[i]
    if current[0] == 'push_front':
        deque.appendleft(current[1])
    elif current[0] == 'push_back':
        deque.append(current[1])
    elif current[0] == 'pop_front':
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[0])
            deque.popleft()
    elif current[0] == 'pop_back':
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[-1])
            deque.pop()
    elif current[0] == 'size':
        print(len(deque))
    elif current[0] == 'empty':
        if len(deque) == 0:
            print(1)
        else:
            print(0)
    elif current[0] == 'front':
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[0])
    elif current[0] == 'back':
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[-1])