import sys
sys.setrecursionlimit(10000000)

def dfs(square, visited, height, width, y, x):
    if visited[y][x]:
        return
    if square[y][x] == 1:
        return

    visited[y][x] = True

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dy, dx in directions:
        ny, nx = y + dy, x + dx
        if 0 <= ny < height and 0 <= nx < width and square[ny][nx] == 0:
            dfs(square, visited, height, width, ny, nx)


height, width = map(int, sys.stdin.readline().strip().split())
square = [list(map(int, sys.stdin.readline().strip())) for _ in range(height)]
visited = [[False] * width for _ in range(height)]
result = 'NO'

for w in range(width):
    if True in visited[height - 1]:
        result = 'YES'
        break
    if square[0][w] == 0:
        dfs(square, visited, height, width, 0, w)


print(result)