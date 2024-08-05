import sys
from collections import deque


def dfs(square, visit, max_height, max_width, y, x):
    stack = deque([(y, x)])
    # 상하좌우
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while stack:  # 변경: 스택을 사용하여 DFS 반복문 실행

        y, x = stack.pop()
        if visit[y][x]:
            continue
        visit[y][x] = True

        for dy, dx in directions:
            ny, nx = y + dy, x + dx
            if 0 <= ny < max_height and 0 <= nx < max_width and not visit[ny][nx] and square[ny][nx] == 255:
                stack.append((ny, nx))  # 변경: 스택에 새로운 좌표 추가


# 높이와 너비 받기
origin_height, origin_width = map(int, sys.stdin.readline().strip().split())

origin = []
# 요소 3개가 점 하나의 값이므로
size = 3

for h in range(origin_height):
    # 들어오는 한 줄 데이터
    data = sys.stdin.readline().strip().split()
    # 3개의 요소를 하나의 점으로(배열로) 묶어서 저장 ex) [[a, b, c], [d, e, f]...]
    origin.append([list(map(int, data[i:i + size])) for i in range(0, len(data), size)])

# 경계값
reference = int(sys.stdin.readline().strip())
# 경계값을 기준으로 만들어줄 새 배열
converted = [[] for _ in range(origin_height)]

# 경계값에 따라 새 배열 만들기
for h in range(origin_height):
    for w in range(origin_width):
        # 점 배열 안의 값의 평균이 경계값보다 크거나 같으면
        # 나눗셈 기호 오류 안나나 확인 필요할 듯
        if sum(origin[h][w]) / 3 >= reference:
            converted[h].append(255)
        else:
            converted[h].append(0)

# 배열이 바뀌었으므로 너비와 높이도 업데이트
height = len(converted)
width = len(converted[0])

# 방문 확인 배열
visited = [[False] * width for _ in range(height)]

# 물건의 갯수를 세어 줄 카운트
count = 0

# 기준 길이 잡을 때 주의
for h in range(height):
    for w in range(width):
        if converted[h][w] == 255 and not visited[h][w]:
            dfs(converted, visited, height, width, h, w)
            count += 1

print(count)