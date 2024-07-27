import sys
import heapq

# 입력받을 줄의 수
how_many_spots = int(input())

# 최대 힙을 구현하기 위한 변수
gift_bag = []

for _ in range(how_many_spots):
    line = list(map(int, sys.stdin.readline().split()))
    a = line[0]
    
    if a == 0:
        if not gift_bag:
            print(-1)
        else:
            # 가장 큰 값을 꺼내서 출력
            gifted = -heapq.heappop(gift_bag)
            print(gifted)
    else:
        # 선물 충전
        for value in line[1:]:
            heapq.heappush(gift_bag, -value)
