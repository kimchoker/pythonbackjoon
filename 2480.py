# or 연산자가 ||가 아닌 or임..
# 세미콜론 쓰지말기
# max(a, b)


a, b, c = map(int, input().split())

# 세 수가 모두 같은 경우
if a == b == c:
    print(10000 + a * 1000)

# 두 수가 같은 경우
elif a == b or b == c or a == c:
    # 같은 수를 찾아 줌
    if a == b:
        same = a
    elif b == c:
        same = b
    elif a == c:
        same = c
    print(1000 + (same * 100))
else:
    print(max(a, b, c) * 100)
