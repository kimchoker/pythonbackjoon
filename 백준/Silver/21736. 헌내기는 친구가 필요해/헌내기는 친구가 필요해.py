import sys
sys.setrecursionlimit(10**6)


def dfs(campus, visited, y, x, height, width, count):
    # 범위를 벗어난 경우
    if x < 0 or x >= width or y < 0 or y >= height:
        return
    # 이미 방문한 경우
    if visited[y][x]:
        return
    # 만난 블록이 P인 경우
    elif campus[y][x] == 'P':
        count[0] += 1
    # X를 만난 경우
    elif campus[y][x] == 'X':
        return

    # 방문 표시
    visited[y][x] = True

    nx = x + 1
    ny = y + 1
    px = x - 1
    py = y - 1

    # 오른쪽
    if nx < width and campus[y][x + 1] != 'X':
        dfs(campus, visited, y, x + 1, height, width, count)
    # 왼쪽
    if px >= 0 and campus[y][x - 1] != 'X':
        dfs(campus, visited, y, x - 1, height, width, count)
    # 위(범위 오류나는지 확인)
    if py >= 0 and campus[y - 1][x] != 'X':
        dfs(campus, visited, y - 1, x, height, width, count)
    # 아래
    if ny < height and campus[y + 1][x] != 'X':
        dfs(campus, visited, y + 1, x, height, width, count)


height, width = map(int, sys.stdin.readline().strip().split())
visited = [[False] * width for _ in range(height)]
campus = [list(sys.stdin.readline().strip()) for _ in range(height)]
count = [0]
start_x = start_y = -1

for h in range(height):
    for w in range(width):
        if campus[h][w] == 'I':
            start_x, start_y = w, h
            break

if start_x != -1 and start_y != -1:
    dfs(campus, visited, start_y, start_x, height, width, count)

if count[0] == 0:
    print('TT')
else:
    print(count[0])
