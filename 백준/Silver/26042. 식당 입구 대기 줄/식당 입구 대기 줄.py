from collections import deque
import sys

history = int(input())

line = deque()
max_length = 0
last = 100001
for i in range(history):
    origin = sys.stdin.readline().strip()

    if origin[0] == '1':
        command = list(map(int, origin.split()))
        line.append(command[1])
        if len(line) > max_length:
            max_length = len(line)
            last = line[-1]
        elif len(line) == max_length:
            if line[-1] < last:
                last = line[-1]

    elif origin[0] == '2' and line:
        line.popleft()

print(f'{max_length} {last}')