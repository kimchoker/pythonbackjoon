import sys
sys.setrecursionlimit(10000)


def dfs(map, visited, width, height, y, x):
    if visited[y][x]:
        return

    visited[y][x] = True

    if map[y][x] == 0:
        return


    # 상
    if y - 1 >= 0 and map[y - 1][x] == 1:
        dfs(map, visited, width, height, y - 1, x)
    # 하
    if y + 1 < height and map[y + 1][x] == 1:
        dfs(map, visited, width, height, y + 1, x)
    # 좌
    if x - 1 >= 0 and map[y][x - 1] == 1:
        dfs(map, visited, width, height, y, x - 1)
    # 우
    if x + 1 < width and map[y][x + 1] == 1:
        dfs(map, visited, width, height, y, x + 1)
    # 좌상
    if x - 1 >= 0 and y - 1 >= 0 and map[y - 1][x - 1] == 1:
        dfs(map, visited, width, height, y - 1, x - 1)
    # 우상
    if x + 1 < width and y - 1 >= 0 and map[y - 1][x + 1] == 1:
        dfs(map, visited, width, height, y - 1, x + 1)
    # 좌하
    if x - 1 >= 0 and y + 1 < height and map[y + 1][x - 1] == 1:
        dfs(map, visited, width, height, y + 1, x - 1)
    # 우하
    if x + 1 < width and y + 1 < height and map[y + 1][x + 1] == 1:
        dfs(map, visited, width, height, y + 1, x + 1)


while True:
    width, height = map(int, sys.stdin.readline().strip().split())
    if width == 0 and height == 0:
        break

    mapped = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(height)]
    visited = [[False] * width for _ in range(height)]

    count = 0

    for h in range(height):
        for w in range(width):
            if mapped[h][w] == 1 and not visited[h][w]:
                dfs(mapped, visited, width, height, h, w)
                count += 1

    print(count)
