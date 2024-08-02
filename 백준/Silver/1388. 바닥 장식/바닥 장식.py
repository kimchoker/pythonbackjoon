import sys


# 바닥 장식, 방문 체크용 배열, y 좌표, x 좌표, 최대 높이, 최대 너비
def dfs(ground, visited, y, x, height, width):
    # dfs 로 방문했으므로 True
    visited[y][x] = True

    # | 인 경우
    if ground[y][x] == '|':
        # 유효값 이내이고(높이를 벗어나지 않고) y로 이어지는 값이 | 이면
        if y + 1 < height and ground[y + 1][x] == '|':
            # 다음 값을 기준으로 다시 dfs 호출
            dfs(ground, visited, y + 1, x, height, width)
            # | 가 아닌 경우 return
        else:
            return

    elif ground[y][x] == '-':
        # 유효값 이내이고(너비를 벗어나지 않고) y로 이어지는 값이 - 이면
        if x + 1 < width and ground[y][x + 1] == '-':
            dfs(ground, visited, y, x + 1, height, width)
        else:
            return


# 높이와 너비
height, width = map(int, sys.stdin.readline().strip().split())

# 바닥 장식
ground = [list(sys.stdin.readline().strip()) for _ in range(height)]
# 방문했었는지 확인할 높이와 너비가 ground 와 같은 False로 채워진 배열
visited = [[False for _ in range(width)] for _ in range(height)]
# 바닥에 필요한 판의 개수를 구해줄 카운트
count = 0

# height 를 순회
for y in range(height):
    # width 를 순회
    for x in range(width):
        # 방문하지 않은 곳이면 dfs 실행
        if not visited[y][x]:
            dfs(ground, visited, y, x, height, width)
            count += 1

print(count)
