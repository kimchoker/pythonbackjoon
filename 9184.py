# 메모이제이션 구현을 위한 메모 딕셔너리 초기화
memo = {}


def w(a, b, c):
    # 메모 딕셔너리에 이미 존재하는 값이라면 존재하는 값을 리턴
    if (a, b, c) in memo:
        return memo[(a, b, c)]

    # 조건대로 세 수 모두가 0보다 작거나 같으면 1 리턴
    if a <= 0 or b <= 0 or c <= 0:
        return 1

    # 세 수가 모두 20보다 큰 경우 w(20, 20, 20) 리턴
    if a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)

    # a < b < c 인 경우 조건에 따른 값 리턴
    if a < b < c:
        memo[(a, b, c)] = w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c)

    # 어느것에도 해당하지 않는 경우 조건에 따른 값 리턴
    else:
        memo[(a, b, c)] = w(a - 1, b, c) + w(a - 1, b - 1, c) + w(a - 1, b, c - 1) - w(a - 1, b - 1, c - 1)

    return memo[(a, b, c)]


results = []

# -1 -1 -1이 입력될 때 까지 입력받기
while True:
    a, b, c = map(int, input().split())
    if a == -1 and b == -1 and c == -1:
        break

    results.append((a, b, c, w(a, b, c)))

for a, b, c, result in results:
    print(f"w({a}, {b}, {c}) = {result}")
