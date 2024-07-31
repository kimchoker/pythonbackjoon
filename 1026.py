import sys

# 입력 부분
count = int(sys.stdin.readline().strip())
A = list(map(int, sys.stdin.readline().strip().split(' ')))
B = list(map(int, sys.stdin.readline().strip().split(' ')))

# list 에서 popleft() 사용했을 때 생기는 성능 저하를 방지하기 위해
# 작은 수 정렬이 필요한 A는 역순으로 정렬
A.sort(reverse=True)
B.sort()
sumAB = 0

# 카운트 만큼 돌면서
for i in range(count):
    # sum 값은 A의 가장 작은 값 곱하기 B의 가장 큰 값
    sumAB += min(A) * max(B)
    # A도 역순정렬 되어있기 때문에 pop 으로 처리 가능
    # B는 애초에 가장 큰 수를 pop 하는 것이기 때문에 pop
    A.pop()
    B.pop()

print(sumAB)