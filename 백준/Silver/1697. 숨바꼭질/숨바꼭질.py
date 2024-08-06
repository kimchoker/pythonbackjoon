from collections import deque
import sys

def bfs(sullae, domangga):
    # 술래보다 왼쪽에 있으면 무조건 걸어가야 함
    if sullae >= domangga:
        return sullae - domangga

    # 문제에서의 제한이 10만이므로 최대치를 10만으로 설정
    max = 100000

    # 방문을 확인할 방문 배열
    visited = [False] * (max + 1)

    # 술래의 현재 위치, 시간
    queue = deque([(sullae, 0)])

    while queue:
        current, time = queue.popleft()

        if current == domangga:
            return time

        # 이동할 수 있는 종류
        directions = [current - 1, current + 1, current * 2]

        for dx in directions:
            if 0 <= dx <= max and not visited[dx]:
                visited[dx] = True
                queue.append((dx, time + 1))


subin, ybrother = map(int, sys.stdin.readline().strip().split())

print(bfs(subin, ybrother))