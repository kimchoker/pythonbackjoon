import sys
sys.setrecursionlimit(10000)


def dfs(map, visited, width, height, y, x):
    # 이미 방문했으면 리턴
    if visited[y][x]:
        return

    # 방문했으므로 True
    visited[y][x] = True

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
    # 조건이 0 0이 들어오기 전까지 계속되므로
    if width == 0 and height == 0:
        break

    # map 이라는 변수 이름이 충돌을 일으켜서 mapped 로 바꿔줌
    mapped = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(height)]
    visited = [[False] * width for _ in range(height)]

    count = 0

    # 지도에서 1인 경우에만 dfs 를 실행하고 카운트를 올려 줌
    for h in range(height):
        for w in range(width):
            if mapped[h][w] == 1 and not visited[h][w]:
                dfs(mapped, visited, width, height, h, w)
                count += 1

    print(count)
