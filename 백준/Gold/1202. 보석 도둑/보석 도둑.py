import sys
import heapq

# 입력 받기
jewel_count, carrier_count = map(int, sys.stdin.readline().strip().split())

jewels = []
carriers = []

# 보석 정보 입력
for _ in range(jewel_count):
    weight, value = map(int, sys.stdin.readline().strip().split())
    jewels.append([weight, value])

# 가방 정보 입력
for _ in range(carrier_count):
    carriers.append(int(sys.stdin.readline().strip()))

# 보석을 가치 기준으로 내림차순 정렬
jewels.sort()
# 가방을 용량 기준으로 오름차순 정렬
carriers.sort()

# 최대 힙을 사용하기 위해 보석의 가격을 음수로 변환
max_heap = []
total_value = 0
j = 0

# 각 가방의 용량에 대해 처리
for capacity in carriers:
    # 현재 가방의 용량에 맞는 모든 보석을 최대 힙에 추가
    while jewels and jewels[j][0] <= capacity:
        heapq.heappush(max_heap, -jewels[j][1])  # 가격을 음수로 변환하여 힙에 추가
        heapq.heappop(jewels)
    # 힙에서 가장 높은 가격의 보석을 선택
    if max_heap:
        total_value -= heapq.heappop(max_heap)  # 꺼낼 때 다시 양수로 변환

print(total_value)
