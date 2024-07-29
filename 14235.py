import sys
import heapq
# 입력받을 줄의 수
how_many_spots = int(input())

gift_bag = []

for _ in range(how_many_spots):
    visited = list(map(int, sys.stdin.readline().split()))
    command = visited[0]

    # 배열이 비었으면 false
    if command == 0 and not gift_bag:
        print(-1)
    elif command == 0:
        gifted = - heapq.heappop(gift_bag)
        print(gifted)
    else:
        for i in range(1, command + 1):
            heapq.heappush(gift_bag, - command)


import sys
import heapq
how_many_spots = int(input())

gift_bag = []

visited = [list(map(int, sys.stdin.readline().split())) for _ in range(how_many_spots)]
for place in visited:
    if place[0] == 0 and len(gift_bag) == 0:
        print(-1)
    elif place[0] == 0:
        gifted = - heapq.heappop(gift_bag)
        print(gifted)
    else:
        for i in range(1, place[0] + 1):
            heapq.heappush(gift_bag, - place[i])