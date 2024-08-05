import sys
from collections import deque


def dfs(square, visit, max_height, max_width, start_y, start_x):
    stack = deque([(start_y, start_x)])
    size = 0
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while stack:
        y, x = stack.pop()

        if visit[y][x]:
            continue
        visit[y][x] = True
        size += 1

        for dy, dx in directions:
            ny, nx = y + dy, x + dx
            if 0 <= ny < max_height and 0 <= nx < max_width and square[ny][nx] == 1 and not visit[ny][nx]:
                stack.append((ny, nx))

    return size


# 높이 너비 쓰레기의 개수를 받기
height, width, trash = map(int, sys.stdin.readline().strip().split())
# 쓰레기가 없는 깔끔한 복도를 일단 만들어주기
hallway = [[0] * width for _ in range(height)]
trash_size = []

# 복도에 쓰레기를 버리기
for _ in range(trash):
    y, x = map(int, sys.stdin.readline().strip().split())
    hallway[y - 1][x - 1] = 1

# 방문 배열
visited = [[False] * width for _ in range(height)]

for h in range(height):
    for w in range(width):
        if hallway[h][w] == 1 and not visited[h][w]:
            trash_size.append(dfs(hallway, visited, height, width, h, w))

print(max(trash_size) if trash_size else 0)